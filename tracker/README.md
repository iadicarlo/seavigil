# SeaVigil live tracker

The always-on half of SeaVigil: one process streams live AIS into a database, a second serves
the real SeaVigil site with that live data wired in. No CDN, no cloud, no commercial data
vendor. This is the local proof of the live loop before it lifts onto a renewable-powered VPS
or a Raspberry Pi.

## What it is

`ingest.py` holds one aisstream WebSocket (free, community-sourced terrestrial AIS) and upserts
each vessel's latest position into `tracker.db` (SQLite, WAL mode). `server.py` serves the
actual `web/` site and adds one dynamic endpoint, `/live/positions.geojson`, rebuilt from that
database on each request. The site's live layer polls it every few seconds, so the rich page
(MPAs, EEZ, the Sentinel-1 SAR and Sentinel-2 optical dark-vessel layers, IUU flags, dossiers,
four languages) shows every broadcasting vessel moving in real time, beneath the incident flags.

This is the coastal real-time IDENTITY layer: vessels that broadcast AIS, where shore receivers
reach (strong near coasts, thin far offshore). Open-ocean presence and dark (non-broadcasting)
vessels are the separate Copernicus SAR / optical layer the site already carries. The two stack.

## Run it locally

Needs a free aisstream.io key in `AISSTREAM_KEY` (in `.env` at the repo root, gitignored).

```bash
tracker/run.sh            # starts ingest + server, opens http://localhost:8100
```

Or by hand, in two terminals:

```bash
# all watchlist areas (remote, so AIS-sparse), or a busy box that fills the map:
uv run --with websockets python tracker/ingest.py --bbox=-1.0,49.5,5.0,52.5   # English Channel

python3 tracker/server.py 8100                                                # the live SeaVigil site
```

Open http://localhost:8100. The live vessels are a teal layer under the incident flags; the
pill at the bottom shows how many are live. Click one for MMSI, name, flag, speed, and age.

## Pieces

- `ingest.py` continuous aisstream -> SQLite upsert (WAL, so the server reads while it writes).
  `--seconds N` stops after N seconds (0 = forever) for a supervised restart or a test. Pass a
  negative-longitude box with the equals form: `--bbox=-1.0,49.5,5.0,52.5`.
- `server.py` serves `web/` plus `/live/positions.geojson` (vessels seen in the last
  `TRACKER_WINDOW_MIN` minutes, default 60). Range support for PMTiles.
- `tracker.db` is regenerated and gitignored; never committed.

## Lifting to an always-on host

The two-process, one-database shape is deliberately production-like. On a renewable EU VPS or a
Raspberry Pi, `ingest.py` and `server.py` become two long-running services, SQLite swaps for
Postgres if it grows, and the same site sits behind a login for the private instance. Nothing
about the design changes.
