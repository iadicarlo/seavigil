#!/usr/bin/env python3
"""Extract continuous fishing-vessel AIS tracks from a NOAA Marine Cadastre daily file.

NOAA AIS (marinecadastre.gov, US public domain) is identity-bearing (MMSI) and
continuous, which the curated GFW training labels are not. That is exactly what
SeaVigil needs to demonstrate the AIS behaviors that require real tracks: going dark
(AIS disabling) and at-sea encounters. This streams one whole-US daily file (it is
~1.5 GB unzipped, so we do NOT load it into memory), keeps fishing vessels inside a
bounding box, maps the columns onto the SeaVigil positions schema, and writes a CSV.

Run:
  uv run python scripts/fetch_noaa_ais.py --zip data/ais_raw/AIS_2024_07_01.zip \
      --out data/positions/noaa_tracks.csv
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seavigil import flags  # noqa: E402

# US West Coast / California Current: dense fishing and an offshore EEZ edge.
DEFAULT_BBOX = (-130.0, 32.0, -117.0, 43.0)  # minlon, minlat, maxlon, maxlat
OUT_FIELDS = ["vessel_id", "timestamp", "lat", "lon", "speed", "course",
              "gear", "ship_name", "flag", "ship_type"]


def _epoch(s: str) -> int | None:
    try:  # NOAA BaseDateTime looks like "2024-07-01T13:45:02"
        return int(dt.datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S")
                   .replace(tzinfo=dt.timezone.utc).timestamp())
    except (ValueError, TypeError):
        return None


def main() -> None:
    ap = argparse.ArgumentParser(description="NOAA Marine Cadastre AIS -> SeaVigil positions CSV")
    ap.add_argument("--zip", required=True)
    ap.add_argument("--bbox", default=None, help="minlon,minlat,maxlon,maxlat")
    ap.add_argument("--vessel-type", type=int, default=30, help="NOAA VesselType (30 = fishing)")
    ap.add_argument("--out", default="data/positions/noaa_tracks.csv")
    args = ap.parse_args()
    minlon, minlat, maxlon, maxlat = (
        tuple(float(x) for x in args.bbox.split(",")) if args.bbox else DEFAULT_BBOX)

    zf = zipfile.ZipFile(args.zip)
    member = next(n for n in zf.namelist() if n.lower().endswith(".csv"))
    n_in = n_kept = 0
    vessels: set = set()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with zf.open(member) as raw, io.TextIOWrapper(raw, encoding="utf-8", errors="replace") as fh, \
            open(out_path, "w", newline="") as out:
        reader = csv.reader(fh)
        header = next(reader)
        col = {name: i for i, name in enumerate(header)}
        need = ("MMSI", "BaseDateTime", "LAT", "LON", "SOG", "COG", "VesselName", "VesselType")
        idx = {k: col.get(k) for k in need}
        if any(v is None for v in idx.values()):
            raise SystemExit(f"unexpected NOAA header: {header}")

        w = csv.DictWriter(out, fieldnames=OUT_FIELDS)
        w.writeheader()
        for row in reader:
            n_in += 1
            try:
                vt = int(float(row[idx["VesselType"]])) if row[idx["VesselType"]] else -1
            except (ValueError, IndexError):
                continue
            if vt != args.vessel_type:
                continue
            try:
                lat = float(row[idx["LAT"]])
                lon = float(row[idx["LON"]])
            except (ValueError, IndexError):
                continue
            if not (minlat <= lat <= maxlat and minlon <= lon <= maxlon):
                continue
            ts = _epoch(row[idx["BaseDateTime"]])
            if ts is None:
                continue
            mmsi = row[idx["MMSI"]]
            iso2, _ = flags.from_mmsi(mmsi)
            try:
                speed = float(row[idx["SOG"]]) if row[idx["SOG"]] else 0.0
                course = float(row[idx["COG"]]) if row[idx["COG"]] else 0.0
            except ValueError:
                speed = course = 0.0
            w.writerow({
                "vessel_id": mmsi, "timestamp": ts, "lat": lat, "lon": lon,
                "speed": speed, "course": course, "gear": "unknown",
                "ship_name": (row[idx["VesselName"]] or "").strip(),
                "flag": iso2, "ship_type": "Fishing",
            })
            n_kept += 1
            vessels.add(mmsi)

    print(f"scanned {n_in:,} rows; kept {n_kept:,} fishing positions "
          f"({len(vessels):,} vessels) in bbox -> {out_path}")


if __name__ == "__main__":
    main()
