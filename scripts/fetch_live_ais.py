#!/usr/bin/env python3
"""Stream near-real-time AIS from aisstream.io into the seavigil `--positions` schema.

aisstream.io is a free global live AIS WebSocket (needs a free API key in AISSTREAM_KEY).
This subscribes to a bounding box, collects PositionReports for a while, and writes a CSV
the model can score (distance_from_shore/port are computed on load by seavigil.enrich).

Because a static site cannot hold a live socket, "near-real-time" means a scheduled job
runs this every N minutes for the monitored MPAs, then re-scores and republishes.

Setup:  export AISSTREAM_KEY=...   (kept in .env, gitignored)
Run:
  uv run --with websockets python scripts/fetch_live_ais.py \
      --bbox -24.5,142.5,-10.5,154.0 --seconds 60 --out data/positions/live_ais_real.csv
  uv run python -m seavigil.alert --positions data/positions/live_ais_real.csv \
      --mpa data/mpa/wdpa_marine_sample.geojson
"""

from __future__ import annotations

import argparse
import asyncio
import csv
import datetime as dt
import json
import os

ENDPOINT = "wss://stream.aisstream.io/v0/stream"
FIELDS = ["vessel_id", "timestamp", "lat", "lon", "speed", "course", "gear"]


def _epoch(s) -> int | None:
    if not s:
        return None
    try:  # aisstream time_utc looks like "2026-06-25 16:31:52.607 +0000 UTC"
        return int(dt.datetime.strptime(str(s)[:19], "%Y-%m-%d %H:%M:%S")
                   .replace(tzinfo=dt.timezone.utc).timestamp())
    except (ValueError, TypeError):
        return None


async def _stream(key: str, bbox, seconds: int, maxn: int) -> list[dict]:
    import websockets

    sub = {
        "APIKey": key,
        "BoundingBoxes": [[[bbox[0], bbox[1]], [bbox[2], bbox[3]]]],
        "FilterMessageTypes": ["PositionReport"],
    }
    rows: list[dict] = []
    async with websockets.connect(ENDPOINT, ping_interval=None, max_size=None) as ws:
        await ws.send(json.dumps(sub))
        try:
            async with asyncio.timeout(seconds):
                async for raw in ws:
                    m = json.loads(raw)
                    if m.get("MessageType") != "PositionReport":
                        continue
                    pr = m["Message"]["PositionReport"]
                    meta = m.get("MetaData", {})
                    lat, lon = pr.get("Latitude"), pr.get("Longitude")
                    ts = _epoch(meta.get("time_utc"))
                    if lat is None or lon is None or ts is None:
                        continue
                    rows.append({
                        "vessel_id": str(meta.get("MMSI", "")),
                        "timestamp": ts, "lat": lat, "lon": lon,
                        "speed": pr.get("Sog", 0.0), "course": pr.get("Cog", 0.0),
                        "gear": "unknown",
                    })
                    if len(rows) >= maxn:
                        break
        except (asyncio.TimeoutError, TimeoutError):
            pass
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description="Stream live AIS (aisstream.io) into --positions CSV")
    ap.add_argument("--bbox", required=True, help="lat_min,lon_min,lat_max,lon_max")
    ap.add_argument("--seconds", type=int, default=60)
    ap.add_argument("--max", type=int, default=20000)
    ap.add_argument("--out", default="data/positions/live_ais_real.csv")
    args = ap.parse_args()

    key = os.environ.get("AISSTREAM_KEY")
    if not key:
        raise SystemExit("AISSTREAM_KEY not set (free key at aisstream.io; keep it in .env)")
    bbox = [float(x) for x in args.bbox.split(",")]

    rows = asyncio.run(_stream(key, bbox, args.seconds, args.max))
    with open(args.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    vessels = len({r["vessel_id"] for r in rows})
    print(f"wrote {len(rows)} live AIS positions ({vessels} vessels) -> {args.out}")


if __name__ == "__main__":
    main()
