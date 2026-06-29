#!/usr/bin/env python3
"""SeaVigil own near-real-time event detection: going-dark and at-sea encounters computed from
OUR rolling AIS buffer, not consumed from GFW (whose published events lag 3 to 4 days).

Both detectors are coverage-aware, the same honesty rule as the SAR dark flag: an event is only
asserted where our own capture density supports it. We never infer "went dark" from a gap in our
own sampling; we require that we kept seeing the same patch of sea after the vessel vanished.

  going dark : a vessel last seen inside a watchlist area, silent for more than GAP_H hours, while
               we kept receiving OTHER vessels within COVER_NM of its last position afterwards.
  encounter  : two vessels within ENC_NM, both slow (< ENC_KN), co-located across at least MIN_HITS
               separate capture moments (a sustained rendezvous, not a single passing).

Honest scope: aisstream coverage is sparse offshore, so with the current hourly buffer these fire
rarely. They become reliable once AIS capture over the watchlist is continuous (a persistent
streaming worker), which is the real unlock. Until then SeaVigil keeps consuming GFW's
authoritative events, labelled with their 3 to 4 day lag.

    uv run python scripts/own_events.py --buffer data/positions/ais_buffer.csv --out results/own_events.json
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WATCHLIST = ROOT / "data" / "watchlist.json"
NM_M = 1852.0

GAP_H = 6.0        # silent for more than this many hours
COVER_NM = 10.0    # "we kept seeing the area" radius
COVER_HITS = 3     # at least this many other-vessel fixes after it vanished
ENC_NM = 0.5       # two vessels this close
ENC_KN = 1.0       # both slower than this
ENC_WIN_S = 1800   # capture moments bucketed to 30 min
MIN_HITS = 2       # co-located across at least this many buckets


def _haversine_nm(lon1, lat1, lon2, lat2) -> float:
    r1, r2 = math.radians(lat1), math.radians(lat2)
    dphi, dlmb = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(r1) * math.cos(r2) * math.sin(dlmb / 2) ** 2
    return (6371000.0 * 2 * math.asin(math.sqrt(a))) / NM_M


def _load(buffer_csv):
    rows = []
    with open(buffer_csv) as f:
        for a in csv.DictReader(f):
            try:
                rows.append({"id": a.get("vessel_id", ""), "ts": float(a["timestamp"]),
                             "lat": float(a["lat"]), "lon": float(a["lon"]),
                             "speed": float(a.get("speed") or 0)})
            except (KeyError, ValueError):
                continue
    return rows


def _areas(watchlist):
    return json.loads(Path(watchlist).read_text())["areas"]


def _area_of(lon, lat, areas):
    for ar in areas:
        w, s, e, n = ar["bbox"]
        if w <= lon <= e and s <= lat <= n:
            return ar["name"]
    return None


def going_dark(rows, areas):
    tmax = max(r["ts"] for r in rows)
    by_vessel = {}
    for r in rows:
        by_vessel.setdefault(r["id"], []).append(r)
    events = []
    for vid, fixes in by_vessel.items():
        if len(fixes) < 3:                       # need a real track, not a single ping
            continue
        fixes.sort(key=lambda r: r["ts"])
        last = fixes[-1]
        area = _area_of(last["lon"], last["lat"], areas)
        if not area or (tmax - last["ts"]) < GAP_H * 3600:
            continue
        # coverage: did we keep receiving OTHER vessels near its last spot after it went silent?
        cover = sum(1 for r in rows if r["id"] != vid and r["ts"] > last["ts"]
                    and _haversine_nm(last["lon"], last["lat"], r["lon"], r["lat"]) <= COVER_NM)
        if cover < COVER_HITS:
            continue                              # could be our own coverage gap, not dark
        events.append({"type": "ais_disabling", "vessel_id": vid, "area": area,
                       "lat": last["lat"], "lon": last["lon"], "last_seen_ts": last["ts"],
                       "silent_hours": round((tmax - last["ts"]) / 3600, 1),
                       "coverage_fixes_after": cover})
    return events


def encounters(rows):
    slow = [r for r in rows if r["speed"] < ENC_KN]
    buckets = {}
    for r in slow:
        buckets.setdefault(int(r["ts"] // ENC_WIN_S), []).append(r)
    pair_hits, pair_pos = {}, {}
    for _, group in buckets.items():
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                if a["id"] == b["id"]:
                    continue
                if _haversine_nm(a["lon"], a["lat"], b["lon"], b["lat"]) <= ENC_NM:
                    key = tuple(sorted((a["id"], b["id"])))
                    pair_hits[key] = pair_hits.get(key, 0) + 1
                    pair_pos[key] = ((a["lat"] + b["lat"]) / 2, (a["lon"] + b["lon"]) / 2)
    return [{"type": "encounter", "vessel_ids": list(k), "hits": h,
             "lat": pair_pos[k][0], "lon": pair_pos[k][1]}
            for k, h in pair_hits.items() if h >= MIN_HITS]


def main() -> None:
    ap = argparse.ArgumentParser(description="Detect our own going-dark + encounter events from the AIS buffer")
    ap.add_argument("--buffer", required=True)
    ap.add_argument("--watchlist", default=str(WATCHLIST))
    ap.add_argument("--out", default="results/own_events.json")
    a = ap.parse_args()

    rows = _load(a.buffer)
    if not rows:
        print("AIS buffer empty; no own-events this run.")
        return
    areas = _areas(a.watchlist)
    dark = going_dark(rows, areas)
    enc = encounters(rows)
    out = {"source": "seavigil_own_ais_buffer", "n_positions": len(rows),
           "n_vessels": len({r["id"] for r in rows}),
           "going_dark": dark, "encounters": enc,
           "note": "Coverage-aware events from our own AIS buffer (live, best-effort). Sparse "
                   "offshore until AIS capture is continuous; GFW events remain the authoritative "
                   "3-4 day source."}
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    Path(a.out).write_text(json.dumps(out, indent=1))
    print(f"own events: {len(dark)} going-dark, {len(enc)} encounters "
          f"from {out['n_positions']} positions / {out['n_vessels']} vessels -> {a.out}")


if __name__ == "__main__":
    main()
