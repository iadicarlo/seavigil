#!/usr/bin/env python3
"""SeaVigil live tracker: the write half. Continuous AIS ingest from aisstream.io into SQLite.

This is the always-on process. It holds one open WebSocket to aisstream (free,
community-sourced terrestrial AIS) and, on every PositionReport, upserts the vessel's
latest position into a local SQLite database. tracker/server.py reads that same database
to serve the live map, so the two run side by side and share one file.

This is the coastal real-time IDENTITY layer: vessels that broadcast AIS, where shore
receivers reach. Open-ocean presence and dark (non-broadcasting) vessels are a separate
layer, the Copernicus SAR / optical detectors; see tracker/README.md.

Honest scope: aisstream coverage is strong near coasts and thin far offshore. No silent
fallback: without AISSTREAM_KEY the process exits.

  export AISSTREAM_KEY=...            # free key at aisstream.io, kept in .env (gitignored)
  uv run --with websockets python tracker/ingest.py                  # all watchlist areas
  uv run --with websockets python tracker/ingest.py --bbox=-92.5,-2.0,-88.5,2.0   # one box

(Use --bbox=... with the equals sign: a leading minus in the longitude is otherwise read
as a flag.)
"""

from __future__ import annotations

import argparse
import asyncio
import datetime as dt
import json
import os
import sqlite3
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from seavigil import flags  # noqa: E402

ENDPOINT = "wss://stream.aisstream.io/v0/stream"
WATCHLIST = ROOT / "data" / "watchlist.json"
DB = Path(__file__).resolve().parent / "tracker.db"

# AIS ship-type code -> label, the same mapping the batch collector uses.
_TYPE = {30: "Fishing", 31: "Tug", 32: "Tug", 36: "Sailing", 37: "Pleasure craft",
         50: "Pilot", 51: "SAR", 52: "Tug", 53: "Port tender", 55: "Law enforcement"}


def _ship_type_label(code) -> str:
    try:
        c = int(code)
    except (TypeError, ValueError):
        return ""
    if c in _TYPE:
        return _TYPE[c]
    if 40 <= c <= 49:
        return "High-speed craft"
    if 60 <= c <= 69:
        return "Passenger"
    if 70 <= c <= 79:
        return "Cargo"
    if 80 <= c <= 89:
        return "Tanker"
    return "Other"


def _epoch(s) -> int | None:
    if not s:
        return None
    try:  # aisstream time_utc looks like "2026-06-25 16:31:52.607 +0000 UTC"
        return int(dt.datetime.strptime(str(s)[:19], "%Y-%m-%d %H:%M:%S")
                   .replace(tzinfo=dt.timezone.utc).timestamp())
    except (ValueError, TypeError):
        return None


def _iso2(mmsi: str) -> str:
    if not mmsi.isdigit():
        return ""
    try:
        iso2, _ = flags.from_mmsi(int(mmsi))
        return iso2 or ""
    except Exception:  # flag lookup is best-effort, never fatal to ingest
        return ""


def _connect(db_path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(str(db_path))
    con.execute("PRAGMA journal_mode=WAL")        # let the server read while we write
    con.execute("PRAGMA synchronous=NORMAL")
    con.execute("""
        CREATE TABLE IF NOT EXISTS vessels (
            mmsi TEXT PRIMARY KEY,
            lat REAL, lon REAL, ts INTEGER,
            speed REAL, course REAL,
            name TEXT, flag TEXT, ship_type TEXT, destination TEXT
        )
    """)
    con.execute("CREATE INDEX IF NOT EXISTS vessels_ts ON vessels(ts)")
    con.commit()
    return con


def _boxes(bbox: str | None) -> list:
    """aisstream wants boxes as [[lat_min, lon_min], [lat_max, lon_max]]."""
    if bbox:
        b = [float(x) for x in bbox.split(",")]   # lon_min,lat_min,lon_max,lat_max (GeoJSON order)
        return [[[b[1], b[0]], [b[3], b[2]]]]
    wl = json.loads(WATCHLIST.read_text())
    out = []
    for a in wl["areas"]:
        lon0, lat0, lon1, lat1 = a["bbox"]
        out.append([[lat0, lon0], [lat1, lon1]])
    return out


def _upsert(con: sqlite3.Connection, rows: list[tuple]) -> None:
    # Newest position per MMSI wins; identity fields keep their last known non-empty value.
    con.executemany("""
        INSERT INTO vessels (mmsi, lat, lon, ts, speed, course, name, flag, ship_type, destination)
        VALUES (?,?,?,?,?,?,?,?,?,?)
        ON CONFLICT(mmsi) DO UPDATE SET
            lat=excluded.lat, lon=excluded.lon, ts=excluded.ts,
            speed=excluded.speed, course=excluded.course,
            name=COALESCE(NULLIF(excluded.name,''), vessels.name),
            flag=COALESCE(NULLIF(excluded.flag,''), vessels.flag),
            ship_type=COALESCE(NULLIF(excluded.ship_type,''), vessels.ship_type),
            destination=COALESCE(NULLIF(excluded.destination,''), vessels.destination)
        WHERE excluded.ts >= vessels.ts
    """, rows)
    con.commit()


async def _run(key: str, boxes: list, prune_hours: float, heartbeat_s: float) -> None:
    import websockets

    con = _connect(DB)
    sub = {"APIKey": key, "BoundingBoxes": boxes,
           "FilterMessageTypes": ["PositionReport", "ShipStaticData"]}
    statics: dict[str, dict] = {}   # MMSI -> last seen name / destination / ship_type
    pending: list[tuple] = []       # buffered position rows, flushed in batches
    total = 0
    last_commit = last_beat = last_prune = time.time()

    while True:  # reconnect loop: a dropped socket is normal, never fatal
        try:
            async with websockets.connect(ENDPOINT, ping_interval=20, max_size=None) as ws:
                await ws.send(json.dumps(sub))
                print(f"connected; subscribed to {len(boxes)} box(es)")
                async for raw in ws:
                    m = json.loads(raw)
                    mt = m.get("MessageType")
                    meta = m.get("MetaData", {})
                    mmsi = meta.get("MMSI")
                    if mmsi is None:
                        continue
                    mmsi = str(mmsi)

                    if mt == "ShipStaticData":
                        sd = m["Message"]["ShipStaticData"]
                        st = {"name": (sd.get("Name") or meta.get("ShipName") or "").strip(),
                              "destination": (sd.get("Destination") or "").strip(),
                              "ship_type": _ship_type_label(sd.get("Type"))}
                        statics[mmsi] = st
                        con.execute(
                            "UPDATE vessels SET name=COALESCE(NULLIF(?,''),name), "
                            "destination=COALESCE(NULLIF(?,''),destination), "
                            "ship_type=COALESCE(NULLIF(?,''),ship_type) WHERE mmsi=?",
                            (st["name"], st["destination"], st["ship_type"], mmsi))
                        continue

                    if mt != "PositionReport":
                        continue
                    pr = m["Message"]["PositionReport"]
                    lat, lon = pr.get("Latitude"), pr.get("Longitude")
                    if lat is None or lon is None:
                        continue
                    ts = _epoch(meta.get("time_utc")) or int(time.time())
                    st = statics.get(mmsi, {})
                    pending.append((mmsi, lat, lon, ts, pr.get("Sog") or 0.0, pr.get("Cog") or 0.0,
                                    st.get("name", ""), _iso2(mmsi),
                                    st.get("ship_type", ""), st.get("destination", "")))
                    total += 1

                    now = time.time()
                    if len(pending) >= 50 or now - last_commit >= 2.0:
                        _upsert(con, pending)
                        pending.clear()
                        last_commit = now
                    if now - last_beat >= heartbeat_s:
                        live = con.execute("SELECT COUNT(*) FROM vessels WHERE ts>=?",
                                           (int(now) - 3600,)).fetchone()[0]
                        print(f"  {total} msgs in, {live} vessels live in the last hour")
                        last_beat = now
                    if now - last_prune >= 600:
                        con.execute("DELETE FROM vessels WHERE ts < ?",
                                    (int(now) - int(prune_hours * 3600),))
                        con.commit()
                        last_prune = now
        except KeyboardInterrupt:
            raise
        except Exception as e:  # noqa: BLE001 - any socket/parse error: flush, wait, reconnect
            if pending:
                _upsert(con, pending)
                pending.clear()
            print(f"  socket dropped ({type(e).__name__}: {e}); reconnecting in 5s")
            await asyncio.sleep(5)


def main() -> None:
    ap = argparse.ArgumentParser(description="Continuous aisstream -> SQLite for the live tracker")
    ap.add_argument("--bbox", help="lon_min,lat_min,lon_max,lat_max, e.g. --bbox=-1.0,49.5,5.0,52.5 "
                                   "(default: every watchlist area)")
    ap.add_argument("--prune-hours", type=float, default=6.0,
                    help="drop vessels not seen in this many hours")
    ap.add_argument("--heartbeat", type=float, default=15.0, help="seconds between status lines")
    ap.add_argument("--seconds", type=float, default=0.0,
                    help="stop after N seconds (0 = run forever; >0 suits a supervised restart or a test)")
    a = ap.parse_args()

    key = os.environ.get("AISSTREAM_KEY")
    if not key:
        raise SystemExit("AISSTREAM_KEY not set (free key at aisstream.io; keep it in .env, gitignored)")

    boxes = _boxes(a.bbox)
    print(f"live tracker ingest -> {DB}")

    async def _bounded() -> None:
        if a.seconds and a.seconds > 0:
            try:
                await asyncio.wait_for(_run(key, boxes, a.prune_hours, a.heartbeat), a.seconds)
            except (asyncio.TimeoutError, TimeoutError):
                print(f"\nbounded run: {a.seconds:.0f}s elapsed, stopping")
        else:
            await _run(key, boxes, a.prune_hours, a.heartbeat)

    try:
        asyncio.run(_bounded())
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()
