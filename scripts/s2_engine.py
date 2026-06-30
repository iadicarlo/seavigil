#!/usr/bin/env python3
"""SeaVigil Sentinel-2 optical engine: the optical analog of sar_engine.

For each watchlist area it (1) asks GFW where the foreign / distant-water fleet is densest, (2) finds a
recent low-cloud Sentinel-2 L1C scene over that hotspot, (3) runs the Ai2 trained optical detector on
it, and (4) folds the detections into the optical (?s2) view, cross-matched against GFW AIS for the
matched / dark split.

Honest scope: optical is cloud-limited, so most cycles a hotspot has no clear scene and the engine says
so (like the SAR engine reporting no new scenes). And the trained model is heavy (full-scene CPU
inference, a few minutes per scene), so this runs LOCALLY / on demand; CI automation needs a GPU runner.
The capability is the same one the SAR engine uses, pointed at the optical sensor.

  RSLP_PYTHON=/path/to/rslp-env/bin/python GFW_TOKEN=... \
  uv run python scripts/s2_engine.py --max-scenes 2 --max-cloud 25 --since-days 20
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))

from sar_engine import _gfw_ais_rows, _gfw_hotspot, _gfw_token  # noqa: E402

CATALOG = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products"
WATCHLIST = ROOT / "data" / "watchlist.json"
STATE = ROOT / "data" / "s2_state.json"


def _find_clear_s2(lon: float, lat: float, since_iso: str, max_cloud: float) -> str | None:
    """The most recent low-cloud Sentinel-2 L1C scene over a point, as a scene id (no .SAFE)."""
    poly = (f"POLYGON(({lon - 0.05} {lat - 0.05},{lon + 0.05} {lat - 0.05},"
            f"{lon + 0.05} {lat + 0.05},{lon - 0.05} {lat + 0.05},{lon - 0.05} {lat - 0.05}))")
    flt = (f"Collection/Name eq 'SENTINEL-2' and contains(Name,'MSIL1C') "
           f"and OData.CSC.Intersects(area=geography'SRID=4326;{poly}') "
           f"and ContentDate/Start gt {since_iso} "
           f"and Attributes/OData.CSC.DoubleAttribute/any(att:att/Name eq 'cloudCover' "
           f"and att/OData.CSC.DoubleAttribute/Value lt {max_cloud})")
    url = CATALOG + "?" + urllib.parse.urlencode(
        {"$filter": flt, "$orderby": "ContentDate/Start desc", "$top": "1", "$select": "Name"})
    req = urllib.request.Request(url, headers={"User-Agent": "SeaVigil/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        vals = json.load(r).get("value", [])
    return vals[0]["Name"].replace(".SAFE", "") if vals else None


def main() -> None:
    ap = argparse.ArgumentParser(description="SeaVigil Sentinel-2 optical hotspot engine")
    ap.add_argument("--rslp-python", default=None, help="rslearn venv python (else $RSLP_PYTHON)")
    ap.add_argument("--since-days", type=float, default=20.0)
    ap.add_argument("--max-cloud", type=float, default=25.0)
    ap.add_argument("--hotspot-days", type=int, default=14)
    ap.add_argument("--max-scenes", type=int, default=2)
    ap.add_argument("--accumulate-days", type=int, default=30)
    ap.add_argument("--discover-only", action="store_true", help="show hotspots + clear scenes, do not run the model")
    a = ap.parse_args()

    token = _gfw_token()
    areas = json.loads(WATCHLIST.read_text())["areas"]
    now = datetime.now(timezone.utc)
    since_iso = (now - timedelta(days=a.since_days)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    hs_range = f"{(now - timedelta(days=a.hotspot_days)):%Y-%m-%d},{(now - timedelta(days=1)):%Y-%m-%d}"

    # 1. for each area, find the GFW hotspot, then a clear S2 scene over it
    todo = []
    for area in areas:
        hs = _gfw_hotspot(area, token, hs_range)
        if not hs:
            continue
        scene = _find_clear_s2(hs["lon"], hs["lat"], since_iso, a.max_cloud)
        tag = ("foreign " + str(hs["flag"])) if hs["foreign"] else ("local " + str(hs["flag"]))
        if scene:
            todo.append({"area": area, "hotspot": hs, "scene": scene})
            print(f"  [{area['name']}] {tag} hotspot ({hs['lat']:.2f},{hs['lon']:.2f}) -> clear scene {scene[:46]}")
        else:
            print(f"  [{area['name']}] {tag} hotspot ({hs['lat']:.2f},{hs['lon']:.2f}) -> no clear S2 scene (cloud)")
    todo.sort(key=lambda t: (not t["hotspot"]["foreign"], -float(t["hotspot"].get("hours") or 0)))  # foreign first
    print(f"discovery: {len(todo)} hotspot(s) with a clear Sentinel-2 scene")
    if not todo:
        print("no clear optical scene over any hotspot this cycle (optical is cloud-limited).")
        return
    if a.discover_only:
        return

    # 2. run the trained model over each, collect detections + GFW AIS for the match
    work = Path(tempfile.mkdtemp(prefix="s2_engine_"))
    det_rows, header, ais_rows = [], None, []
    for info in todo[: a.max_scenes]:
        scene, hs, area = info["scene"], info["hotspot"], info["area"]
        per = work / "one.csv"
        cmd = [sys.executable, str(ROOT / "scripts" / "run_sentinel2_allen.py"),
               "--scene-id", scene, "--out", str(per)]
        env = {"RSLP_PYTHON": a.rslp_python} if a.rslp_python else None
        print(f"  detect {scene[:46]} (full-scene CPU; a few minutes) ...")
        import os
        run_env = dict(os.environ, **(env or {}))
        if subprocess.run(cmd, env=run_env).returncode != 0 or not per.exists():
            print(f"    optical detection failed for {scene}; skipping")
            continue
        with open(per) as f:
            rd = csv.reader(f)
            hdr = next(rd, None)
            header = header or hdr
            det_rows.extend(list(rd))
        m = __import__("re").search(r"_(\d{8})T", scene)
        if m:
            h = 0.25
            aoi = [hs["lon"] - h, hs["lat"] - h, hs["lon"] + h, hs["lat"] + h]
            gfw = _gfw_ais_rows(aoi, m.group(1), token)
            ts = int(now.timestamp())
            for i, rr in enumerate(gfw):
                ais_rows.append([f"gfw_{rr.get('flag')}_{i}", ts, rr["lat"], rr["lon"]])

    # 3. fold into the optical view (matched / dark) + accumulate
    if not (det_rows and header):
        print("no optical detections produced this cycle; ?s2 view left unchanged")
        return
    combined = work / "s2_predictions.csv"
    with open(combined, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(det_rows)
    cmd = [sys.executable, str(ROOT / "scripts" / "sar_detections_to_incidents.py"),
           "--detections", str(combined), "--source", "optical",
           "--accumulate-days", str(a.accumulate_days)]
    if ais_rows:
        ais_csv = work / "gfw_ais.csv"
        with open(ais_csv, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["vessel_id", "timestamp", "lat", "lon"])
            w.writerows(ais_rows)
        cmd += ["--ais", str(ais_csv)]
    print(f"publish: {len(det_rows)} optical detections, {len(ais_rows)} GFW AIS positions")
    subprocess.run(cmd, check=True)
    STATE.write_text(json.dumps({"last_run_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
                                 "scenes": [t["scene"] for t in todo[: a.max_scenes]]}, indent=1))


if __name__ == "__main__":
    main()
