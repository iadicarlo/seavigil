#!/usr/bin/env python3
"""SeaVigil dark-vessel engine: the GFW-hotspot playbook, automated.

For each priority area it (1) asks GFW where the foreign / distant-water fleet is densest right
now, (2) runs our Sentinel-1 detector on a scene over that hotspot, (3) cross-matches the detections
against GFW's AIS for that area and date (matched / dark / no-coverage), and (4) republishes ?sar.

This is the automated form of the Guinea proof: GFW AIS points us where to look and tells us which
detections are dark; our SAR sees everything, broadcasting and dark alike.

Honest scope: GFW fishing data lags a few days, so the engine targets scenes a few days old (where
GFW coverage exists) rather than sub-day NRT. A validated few-day dark flag beats an unverified
sub-day one.

Run (conda env for the detector; GFW_TOKEN + Copernicus S3 keys in the environment):
  GFW_TOKEN=... AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... \
  uv run python scripts/sar_engine.py --vds /path/to/vessel-detection-sentinels \
    --detect-python /path/to/vds-env/bin/python
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import subprocess
import sys
import tempfile
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
CATALOG = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products"
GFW_4WINGS = "https://gateway.api.globalfishingwatch.org/v3/4wings/report"
WATCHLIST = ROOT / "data" / "watchlist.json"
STATE = ROOT / "data" / "sar_state.json"


def _gfw_token(arg=None):
    tok = arg or os.environ.get("GFW_TOKEN", "")
    if not tok and (ROOT / ".env").exists():
        for line in (ROOT / ".env").read_text().splitlines():
            if line.startswith("GFW_TOKEN="):
                tok = line.split("=", 1)[1].strip().strip("'\"")
                break
    if not tok:
        raise SystemExit("GFW_TOKEN not set (needed to locate hotspots and match AIS).")
    return tok


def _gfw_report(bbox, date_range, token, group_by="FLAG", res="HIGH"):
    """GFW 4wings fishing-effort report over a bbox + date range; returns the per-cell rows."""
    w, s, e, n = bbox
    geom = {"type": "Polygon", "coordinates": [[[w, s], [e, s], [e, n], [w, n], [w, s]]]}
    qs = urllib.parse.urlencode({"spatial-resolution": res, "temporal-resolution": "ENTIRE",
        "group-by": group_by, "datasets[0]": "public-global-fishing-effort:latest",
        "date-range": date_range, "format": "JSON"})
    req = urllib.request.Request(GFW_4WINGS + "?" + qs, data=json.dumps({"geojson": geom}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "SeaVigil/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        d = json.load(r)
    e0 = (d.get("entries") or [None])[0]
    if isinstance(e0, list):
        return e0
    if isinstance(e0, dict):
        for v in e0.values():
            if isinstance(v, list):
                return v
    return []


def _gfw_hotspot(area, token, date_range):
    """The densest fishing cell in the area, preferring foreign flags (the IUU signal)."""
    try:
        rows = _gfw_report(area["bbox"], date_range, token)
    except Exception as ex:
        print(f"  [{area['name']}] GFW hotspot query failed: {ex}")
        return None
    if not rows:
        return None
    iso = area.get("iso3")
    foreign = [r for r in rows if r.get("flag") and r.get("flag") != iso]
    pool = foreign or rows
    best = max(pool, key=lambda r: r.get("hours", 0))
    return {"lat": best["lat"], "lon": best["lon"], "flag": best.get("flag"),
            "foreign": bool(foreign), "hours": best.get("hours", 0)}


def _gfw_ais_rows(aoi, ymd, token):
    """GFW AIS fishing positions in the AOI on the scene's date (the broadcasting fleet)."""
    d0 = datetime.strptime(ymd, "%Y%m%d")
    dr = f"{d0:%Y-%m-%d},{(d0 + timedelta(days=1)):%Y-%m-%d}"
    try:
        return _gfw_report(aoi, dr, token)
    except Exception as ex:
        print(f"  GFW AIS query failed: {ex}")
        return []


def _query_scenes(bbox, since_iso, before_iso, top=10):
    """Sentinel-1 IW GRDH (COG) scenes intersecting bbox, acquired in [since, before]."""
    w, s, e, n = bbox
    poly = f"POLYGON(({w} {s},{e} {s},{e} {n},{w} {n},{w} {s}))"
    flt = (f"Collection/Name eq 'SENTINEL-1' and contains(Name,'GRDH') and contains(Name,'COG') "
           f"and OData.CSC.Intersects(area=geography'SRID=4326;{poly}') "
           f"and ContentDate/Start gt {since_iso} and ContentDate/Start lt {before_iso}")
    url = CATALOG + "?" + urllib.parse.urlencode(
        {"$filter": flt, "$orderby": "ContentDate/Start desc", "$top": str(top),
         "$select": "Name,ContentDate"})
    req = urllib.request.Request(url, headers={"User-Agent": "SeaVigil/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = json.load(r)
    return [(v["Name"], v["ContentDate"]["Start"]) for v in data.get("value", [])]


def _scene_dt(start_iso):
    return datetime.fromisoformat(start_iso.replace("Z", "+00:00"))


def main() -> None:
    ap = argparse.ArgumentParser(description="SeaVigil GFW-hotspot dark-vessel engine")
    ap.add_argument("--vds", required=True, help="cloned allenai/vessel-detection-sentinels repo")
    ap.add_argument("--detect-python", default=sys.executable, help="conda env python (gdal+torch)")
    ap.add_argument("--gfw-token", default=None)
    ap.add_argument("--watchlist", default=str(WATCHLIST))
    ap.add_argument("--state", default=str(STATE))
    ap.add_argument("--since-days", type=float, default=10.0, help="oldest scene to consider")
    ap.add_argument("--lag-days", type=float, default=3.0, help="skip scenes newer than this (GFW lag)")
    ap.add_argument("--hotspot-days", type=int, default=14, help="GFW lookback to locate the fleet")
    ap.add_argument("--max-scenes", type=int, default=2, help="cap scenes per run (CPU bound)")
    ap.add_argument("--aoi-deg", type=float, default=0.5)
    ap.add_argument("--conf", type=float, default=0.7)
    ap.add_argument("--device", default="cpu", choices=["cpu", "cuda"])
    a = ap.parse_args()

    token = _gfw_token(a.gfw_token)
    areas = json.loads(Path(a.watchlist).read_text())["areas"]
    state = json.loads(Path(a.state).read_text()) if Path(a.state).exists() else {"processed": []}
    done = set(state.get("processed", []))
    now = datetime.now(timezone.utc)
    since_iso = (now - timedelta(days=a.since_days)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    before_iso = (now - timedelta(days=a.lag_days)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    hs_range = f"{(now - timedelta(days=a.hotspot_days)):%Y-%m-%d},{(now - timedelta(days=1)):%Y-%m-%d}"

    # 1. for each area, find the GFW fleet hotspot, then a scene over it
    todo = {}
    for area in areas:
        hs = _gfw_hotspot(area, token, hs_range)
        if not hs:
            continue
        pt = [hs["lon"] - 0.05, hs["lat"] - 0.05, hs["lon"] + 0.05, hs["lat"] + 0.05]
        try:
            scenes = _query_scenes(pt, since_iso, before_iso)
        except Exception as ex:
            print(f"  [{area['name']}] catalogue query failed: {ex}")
            continue
        for name, start in scenes:
            if name in done or name in todo:
                continue
            todo[name] = {"area": area, "hotspot": hs, "start": start}
            tag = ("foreign " + str(hs["flag"])) if hs["foreign"] else ("local " + str(hs["flag"]))
            print(f"  [{area['name']}] hotspot {tag} at ({hs['lat']:.2f},{hs['lon']:.2f}) "
                  f"-> {name[:40]} ({start[:10]})")
            break   # one scene per area per run
    print(f"discovery: {len(todo)} hotspot scene(s) across {len(areas)} areas")
    if not todo:
        print("no new hotspot scenes to process.")
        return

    # 2. detect at the hotspot + collect GFW AIS for the match
    work = Path(tempfile.mkdtemp(prefix="sar_engine_"))
    det_rows, det_header, processed, ais_rows = [], None, [], []
    for name, info in list(todo.items())[: a.max_scenes]:
        hs, area = info["hotspot"], info["area"]
        w0, s0, e0, n0 = area["bbox"]
        h = a.aoi_deg / 2
        aoi = [max(hs["lon"] - h, w0), max(hs["lat"] - h, s0),
               min(hs["lon"] + h, e0), min(hs["lat"] + h, n0)]
        per = work / "engine_one.csv"
        print(f"  detect {name}\n    aoi={[round(x, 2) for x in aoi]}")
        cmd = [a.detect_python, str(ROOT / "scripts" / "run_sentinel1_detection.py"),
               "--vds", a.vds, "--scene", name, "--bbox", *[str(x) for x in aoi],
               "--out", str(per), "--conf", str(a.conf), "--device", a.device]
        if subprocess.run(cmd).returncode != 0 or not per.exists():
            print(f"    detection failed for {name}; will retry next run")
            continue
        processed.append(name)
        with open(per) as f:
            rd = csv.reader(f)
            hdr = next(rd, None)
            if det_header is None:
                det_header = hdr
            det_rows.extend(list(rd))
        dt = _scene_dt(info["start"])
        ts = int(dt.timestamp())
        gfw = _gfw_ais_rows(aoi, dt.strftime("%Y%m%d"), token)
        for i, r in enumerate(gfw):
            ais_rows.append([f"gfw_{r.get('flag')}_{i}", ts, r["lat"], r["lon"]])
        print(f"    {len(gfw)} GFW AIS positions for the match")

    # 3 + 4. publish (the 3-way match runs against the GFW AIS) + record state
    if det_rows and det_header:
        combined = work / "engine_predictions.csv"
        with open(combined, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(det_header)
            w.writerows(det_rows)
        cmd = [sys.executable, str(ROOT / "scripts" / "sar_detections_to_incidents.py"),
               "--detections", str(combined)]
        if ais_rows:
            ais_csv = work / "engine_gfw_ais.csv"
            with open(ais_csv, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["vessel_id", "timestamp", "lat", "lon"])
                w.writerows(ais_rows)
            cmd += ["--ais", str(ais_csv)]
        print(f"publish: {len(det_rows)} detections, {len(ais_rows)} GFW AIS positions")
        subprocess.run(cmd, check=True)
    else:
        print("no detections produced this run; ?sar view left unchanged")

    state["processed"] = sorted(done | set(processed))[-2000:]
    state["last_run_utc"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    Path(a.state).write_text(json.dumps(state, indent=1))
    print(f"state: {len(processed)} scene(s) processed -> {a.state}")


if __name__ == "__main__":
    main()
