#!/usr/bin/env python3
"""Satellite-image chips for SeaVigil detections: the "see the boat" view.

For each recent detection in results/<source>/incidents.json, crop a true-color window from
the source Copernicus scene around the detection and save web/data/<source>/chips/<id>.png,
with an index.json mapping detection id -> {url, label, ts}. The dossier shows the chip, so a
dark vessel stops being a dot and becomes a picture, which is the difference between "a blip"
and "here is the boat, fishing, broadcasting nothing." Chips older than --keep-days, or whose
detection has aged out of the view, are pruned, so the gallery stays current and small.

Runs on the always-on box, where the CDSE S3 keys (CDSE_S3_KEY / CDSE_S3_SECRET) and the geo
deps (rasterio, boto3, pillow, numpy) live. Currently Sentinel-2 optical; Sentinel-1 SAR is in
radar geometry and needs GCP-based geocoding, a later add.

  CDSE_S3_KEY=... CDSE_S3_SECRET=... ~/geoenv/bin/python scripts/make_chips.py --source s2
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
S2_L1C = "Sentinel-2/MSI/L1C"


def _s2_bands(s3, scene: str) -> dict:
    """Locate the true-color image bands (B02/B03/B04) of an S2 L1C scene on CDSE S3."""
    y, m, d = scene[11:15], scene[15:17], scene[17:19]
    prefix = f"{S2_L1C}/{y}/{m}/{d}/{scene}.SAFE/"
    bands: dict = {}
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket="eodata", Prefix=prefix):
        for o in page.get("Contents", []):
            k = o["Key"]
            if "/IMG_DATA/" in k and k.endswith(".jp2"):
                for b in ("B02", "B03", "B04"):
                    if f"_{b}.jp2" in k:
                        bands[b] = k
    return bands


def _crop_rgb(bands: dict, lat: float, lon: float, half_m: float = 750.0, size: int = 256):
    """A size x size true-color crop centered on (lat, lon), read straight from CDSE via gdal."""
    import numpy as np
    import rasterio
    from rasterio.warp import transform as warp_transform
    from rasterio.windows import from_bounds

    def stretch(a):
        lo, hi = np.percentile(a, (2, 98))
        return np.clip((a - lo) / (hi - lo + 1e-6) * 255, 0, 255).astype("uint8")

    def band(key):
        with rasterio.open(f"/vsis3/eodata/{key}") as ds:
            xs, ys = warp_transform("EPSG:4326", ds.crs, [lon], [lat])
            win = from_bounds(xs[0] - half_m, ys[0] - half_m, xs[0] + half_m, ys[0] + half_m,
                              ds.transform)
            return ds.read(1, window=win, out_shape=(size, size), boundless=True, fill_value=0)

    return np.dstack([stretch(band(bands["B04"])), stretch(band(bands["B03"])),
                      stretch(band(bands["B02"]))])


def main() -> None:
    ap = argparse.ArgumentParser(description="Crop Copernicus image chips for SeaVigil detections")
    ap.add_argument("--source", default="s2", choices=["s2"], help="s2 optical (sar is a later add)")
    ap.add_argument("--keep-days", type=float, default=30.0, help="prune chips older than this")
    ap.add_argument("--max", type=int, default=60, help="cap chips generated per run")
    a = ap.parse_args()

    import boto3
    import numpy as np
    from PIL import Image

    key, sec = os.environ.get("CDSE_S3_KEY"), os.environ.get("CDSE_S3_SECRET")
    if not (key and sec):
        raise SystemExit("CDSE_S3_KEY / CDSE_S3_SECRET not set (needed to read Copernicus scenes)")
    os.environ.update({"AWS_S3_ENDPOINT": "eodata.dataspace.copernicus.eu",
                       "AWS_ACCESS_KEY_ID": key, "AWS_SECRET_ACCESS_KEY": sec,
                       "AWS_VIRTUAL_HOSTING": "FALSE", "AWS_HTTPS": "YES"})
    s3 = boto3.client("s3", endpoint_url="https://eodata.dataspace.copernicus.eu",
                      aws_access_key_id=key, aws_secret_access_key=sec)

    inc_path = ROOT / "results" / a.source / "incidents.json"
    chips_dir = ROOT / "web" / "data" / a.source / "chips"
    chips_dir.mkdir(parents=True, exist_ok=True)
    index_path = chips_dir / "index.json"
    index = json.loads(index_path.read_text()) if index_path.exists() else {}

    dets = json.loads(inc_path.read_text()) if inc_path.exists() else []
    now = time.time()

    # Prune: drop chips that aged out (keep-days) or whose detection is gone from the view.
    cur_ids = {d.get("incident_id") for d in dets}
    for cid in list(index):
        ent = index[cid]
        aged = (now - ent.get("ts", now)) > a.keep_days * 86400
        if aged or cid not in cur_ids:
            (chips_dir / Path(ent["url"]).name).unlink(missing_ok=True)
            del index[cid]

    band_cache: dict = {}
    made = 0
    for d in dets:
        cid, scene = d.get("incident_id"), d.get("scene_id")
        lat, lon = d.get("centroid_lat"), d.get("centroid_lon")
        if not (cid and scene and lat is not None and lon is not None):
            continue
        if cid in index and (chips_dir / Path(index[cid]["url"]).name).exists():
            continue
        if made >= a.max:
            break
        try:
            if scene not in band_cache:
                band_cache[scene] = _s2_bands(s3, scene)
            bands = band_cache[scene]
            if not all(b in bands for b in ("B02", "B03", "B04")):
                print(f"  no RGB bands for {scene[:24]}; skipping {cid}")
                continue
            rgb = _crop_rgb(bands, float(lat), float(lon))
            if int(np.asarray(rgb).max()) == 0:
                print(f"  blank crop for {cid}; skipping")
                continue
            fname = f"{cid}.png"
            Image.fromarray(rgb).save(chips_dir / fname)
            y, m, dd = scene[11:15], scene[15:17], scene[17:19]
            index[cid] = {"url": f"./data/{a.source}/chips/{fname}",
                          "label": f"Sentinel-2 · {y}-{m}-{dd}", "ts": now}
            made += 1
            print(f"  chip {cid} <- {scene[:24]}")
        except Exception as e:  # noqa: BLE001 - one bad scene must not stop the rest
            print(f"  chip failed for {cid}: {type(e).__name__}: {e}")

    index_path.write_text(json.dumps(index, indent=0))
    print(f"{a.source}: {made} new chip(s), {len(index)} in the index")


if __name__ == "__main__":
    main()
