#!/usr/bin/env python3
"""Detect vessels in a Sentinel-2 optical scene over an AOI: the free daytime complement to SAR.

A vessel is a bright anomaly on dark water. We read the near-infrared band (B08, where water is
near-black and a hull is bright), keep only the scene's own water class (SCL), morphologically close
the water so vessels (bright holes) count as sea, then erode a coastal buffer so the shoreline / surf
fringe and tile edge drop out. On that open water we flag pixels that are both (a) bright relative to
their 610 m neighbourhood (a high-pass that flattens broad sun glint) and (b) above an absolute
brightness floor, and that sit on genuinely dark deep water (a vessel offshore has a dark background;
a shallow bank does not). Connected blobs of vessel size become detections. No model or GPU.

Honest scope and reliable regime (measured on real CDSE scenes, 2026-06):
  - Cloud is the hard limit. Optical only sees vessels in clear daylight; the all-weather sensor is
    SAR. In testing, the priority offshore IUU zones (West Africa, SW Atlantic) were cloud-covered.
  - This threshold detector is trustworthy on DEEP OPEN WATER with an isolated fleet. Nearshore /
    archipelago / reef scenes over-trigger: shallow-bank NIR brightness, sun glint, small rocks, and
    a heavy presence of legal local boats (most without AIS) all read as "bright object on water".
    So a raw count here is NOT a dark-vessel count.
  - Intended role: TARGETED CONFIRMATION. Point it at a specific lead (a SAR detection or an AIS gap)
    in open water; a single bright object on dark water at the expected spot corroborates the lead
    with a second, independent sensor. For standalone wide-area optical, a trained detector (e.g. the
    Allen optical model) is the right tool, not a statistical threshold.

    AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... uv run python scripts/run_sentinel2_detection.py \
        --scene S2C_MSIL2A_..._.SAFE --bbox -78 -12.5 -77 -11.5 --out data/positions/s2_detections.csv
"""

from __future__ import annotations

import argparse
import math
import os
import re
import sys
from pathlib import Path

# PROJ/GDAL data dirs, in case the conda env is not activated (same fix as the SAR script).
for _var, _sub in (("PROJ_DATA", "proj"), ("PROJ_LIB", "proj"), ("GDAL_DATA", "gdal")):
    _cand = os.path.join(sys.prefix, "share", _sub)
    if os.path.isdir(_cand):
        os.environ.setdefault(_var, _cand)

PX_3857 = 2 * math.pi * 6378137 / 512 / (2 ** 13)   # ~9.55 m, a 10 m-ish grid
S3_ENDPOINT = "eodata.dataspace.copernicus.eu"


def _s3():
    import boto3
    from botocore.config import Config
    k = os.environ.get("AWS_ACCESS_KEY_ID") or os.environ.get("CDSE_S3_KEY")
    s = os.environ.get("AWS_SECRET_ACCESS_KEY") or os.environ.get("CDSE_S3_SECRET")
    if not (k and s):
        raise SystemExit("Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY (Copernicus S3 keys).")
    return boto3.client("s3", endpoint_url=f"https://{S3_ENDPOINT}", aws_access_key_id=k,
                        aws_secret_access_key=s, config=Config(s3={"addressing_style": "path"}),
                        region_name="default")


def _bands(s3, scene):
    """Resolve the B08/B03 (10 m) and SCL (20 m) JP2 keys inside the L2A .SAFE on S3."""
    m = re.search(r"_(\d{8})T", scene)
    d = m.group(1)
    prefix = f"Sentinel-2/MSI/L2A/{d[:4]}/{d[4:6]}/{d[6:8]}/{scene}/GRANULE/"
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket="eodata", Prefix=prefix):
        keys += [o["Key"] for o in page.get("Contents", [])]
    out = {}
    for k in keys:
        if k.endswith("_B08_10m.jp2"):
            out["nir"] = k
        elif k.endswith("_B03_10m.jp2"):
            out["green"] = k
        elif k.endswith("_SCL_20m.jp2"):
            out["scl"] = k
    miss = {"nir", "green", "scl"} - set(out)
    if miss:
        raise SystemExit(f"Could not find bands {miss} under {prefix}")
    return out


def _warp(s3_key, aoi, token_env):
    from osgeo import gdal
    gdal.DontUseExceptions()
    for kk, vv in token_env.items():
        gdal.SetConfigOption(kk, vv)
    w, s, e, n = aoi
    ds = gdal.Warp("", f"/vsis3/eodata/{s3_key}", format="MEM", dstSRS="EPSG:3857",
                   xRes=PX_3857, yRes=PX_3857, outputBounds=[w, s, e, n],
                   outputBoundsSRS="EPSG:4326", resampleAlg="near", multithread=True)
    if ds is None:
        raise SystemExit(f"warp failed for {s3_key}: {gdal.GetLastErrorMsg()}")
    return ds


def main() -> None:
    ap = argparse.ArgumentParser(description="Detect vessels in a Sentinel-2 scene over an AOI")
    ap.add_argument("--scene", required=True, help="Sentinel-2 L2A .SAFE scene name")
    ap.add_argument("--bbox", required=True, nargs=4, type=float, metavar=("W", "S", "E", "N"))
    ap.add_argument("--out", default="data/positions/s2_detections.csv")
    ap.add_argument("--k", type=float, default=9.0, help="brightness threshold (median + k*MAD)")
    ap.add_argument("--coast-buffer-px", type=int, default=15,
                    help="drop detections within this many 10 m pixels of shore/tile-edge (surf, glint)")
    ap.add_argument("--deep-water-frac", type=float, default=0.15,
                    help="only trust vessels whose local background is within this fraction of the water "
                         "median, i.e. genuinely dark deep water (rejects shallow-bank / reef brightness)")
    a = ap.parse_args()

    import numpy as np
    from osgeo import gdal
    s3 = _s3()
    bands = _bands(s3, a.scene)
    env = {"AWS_S3_ENDPOINT": S3_ENDPOINT, "AWS_VIRTUAL_HOSTING": "FALSE", "AWS_HTTPS": "YES",
           "AWS_ACCESS_KEY_ID": os.environ["AWS_ACCESS_KEY_ID"],
           "AWS_SECRET_ACCESS_KEY": os.environ["AWS_SECRET_ACCESS_KEY"]}
    print(f"scene {a.scene}\nAOI {a.bbox}")
    # Hold a reference to each warped MEM dataset until after the read (GDAL frees it otherwise).
    nir_ds = _warp(bands["nir"], a.bbox, env)
    green_ds = _warp(bands["green"], a.bbox, env)
    scl_ds = _warp(bands["scl"], a.bbox, env)
    nir = nir_ds.GetRasterBand(1).ReadAsArray().astype("float32")
    green = green_ds.GetRasterBand(1).ReadAsArray().astype("float32")
    scl = scl_ds.GetRasterBand(1).ReadAsArray()
    print(f"grid {nir.shape}")

    from scipy import ndimage as ndi
    cloud = np.isin(scl, [3, 8, 9, 10])             # shadow, cloud med/high, cirrus
    water = (scl == 6) & ~cloud                     # the scene's own water class (robust vs NDWI on turbid coast)
    if water.sum() < 500:
        print("almost no clear water in the AOI (cloud or land); no detections.")
        _write(a.out, [], a.scene)
        return

    # A vessel is a bright HOLE in the water mask: close the water (fill vessel-sized holes so vessels
    # count as sea), then erode a coastal buffer so the shoreline/surf fringe and tile edge drop out.
    sea = ndi.binary_closing(water, iterations=8)
    sea = ndi.binary_erosion(sea, iterations=a.coast_buffer_px)
    if sea.sum() < 500:
        print("no open water left after the coastal buffer; no detections.")
        _write(a.out, [], a.scene)
        return

    # Open water is near-uniform, so a global brightness cut trips on broad sun glint. A vessel is
    # instead bright RELATIVE TO ITS NEIGHBOURHOOD: subtract a 610 m local-mean background (a high-pass
    # that flattens glint gradients) and keep compact peaks. Require both that local contrast AND a
    # real absolute brightness, so neither broad glint nor a locally-bright dim ripple qualifies.
    bg = ndi.uniform_filter(nir, size=61)
    contrast = nir - bg
    wv = nir[water & sea]
    med = float(np.median(wv))
    cw = contrast[water & sea]
    cmad = float(np.median(np.abs(cw - np.median(cw)))) or 1.0
    con_cut = max(a.k * 1.4826 * cmad, 150.0)       # local-contrast cutoff (floored: water is too flat for MAD alone)
    abs_cut = med + 0.4 * med                        # absolute brightness floor: clearly above the water median
    deep = bg < med * (1.0 + a.deep_water_frac)      # background is dark deep water (not a bright shallow bank)
    mask = (contrast > con_cut) & (nir > abs_cut) & sea & deep
    print(f"water {100*water.mean():.0f}%  open-sea {100*sea.mean():.0f}%  deep-dark {100*(sea & deep).mean():.0f}%  "
          f"water-median {med:.0f}  contrast-cut {con_cut:.0f}  brightness-floor {abs_cut:.0f}")
    thresh = abs_cut

    from skimage.measure import label, regionprops
    lbl = label(mask)
    tr = gdal.Transformer(nir_ds, None, ["DST_SRS=WGS84"])
    rows = []
    for r in regionprops(lbl, intensity_image=nir):
        if not (4 <= r.area <= 150):                # vessel-sized blobs only (reject 1-3 px specks + clouds)
            continue
        cy, cx = r.centroid
        ok, p = tr.TransformPoint(0, float(cx), float(cy), 0)
        if not ok:
            continue
        score = min(1.0, (r.mean_intensity - med) / (thresh - med + 1e-6) * 0.5)
        rows.append({"lon": round(p[0], 5), "lat": round(p[1], 5),
                     "score": round(0.5 + 0.5 * min(score, 1.0), 3),
                     "pixels": int(r.area), "scene_id": a.scene.replace(".SAFE", "")})
    _write(a.out, rows, a.scene)
    print(f"{len(rows)} optical vessel detections -> {a.out}")
    print("Fold into a view with sar_detections_to_incidents.py (optical detections, same schema).")


def _write(out, rows, scene):
    import csv
    p = Path(out)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["lon", "lat", "score", "pixels", "scene_id"])
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
