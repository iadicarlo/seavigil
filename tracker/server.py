#!/usr/bin/env python3
"""SeaVigil live server: serves the real SeaVigil site, made live.

This is the always-on read half of the live tracker. It serves the actual web/ site (the
rich map: MPAs, EEZ, the Sentinel-1 SAR and Sentinel-2 optical dark-vessel layers, IUU
flags, evidence dossiers, all four languages) and adds ONE dynamic endpoint,
/live/positions.geojson, rebuilt on each request from the SQLite database that
tracker/ingest.py keeps current. The site polls that endpoint and draws every broadcasting
vessel as a live layer beneath the incident flags, so the same rich page ticks in real time
instead of showing a committed snapshot.

PMTiles needs byte-range requests, so file responses honour Range (206 Partial Content).
On a static host (GitHub Pages) the endpoint is simply absent and the live layer stays empty;
everything else renders as before.

  python3 tracker/server.py 8100
  TRACKER_WINDOW_MIN=120 python3 tracker/server.py 8100
"""

from __future__ import annotations

import json
import os
import posixpath
import re
import sqlite3
import sys
import time
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WEB = ROOT / "web"
DB = HERE / "tracker.db"
LIVE_ENDPOINT = "/live/positions.geojson"
MAX_FEATURES = 8000   # backstop so a very busy window cannot produce a pathological payload


def _positions_geojson(window_min: float) -> bytes:
    """Every vessel seen in the last window_min minutes, as a GeoJSON FeatureCollection."""
    feats = []
    if DB.exists():
        con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
        try:
            now = int(time.time())
            cutoff = now - int(window_min * 60)
            cur = con.execute(
                "SELECT mmsi,lat,lon,ts,speed,course,name,flag,ship_type,destination "
                "FROM vessels WHERE ts>=? ORDER BY ts DESC LIMIT ?", (cutoff, MAX_FEATURES))
            for mmsi, lat, lon, ts, sog, cog, name, flag, stype, dest in cur:
                feats.append({
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [lon, lat]},
                    "properties": {
                        "mmsi": mmsi, "name": name or "", "flag": flag or "",
                        "speed": round(sog or 0.0, 1), "course": round(cog or 0.0),
                        "ship_type": stype or "", "destination": dest or "",
                        "age_min": round((now - ts) / 60.0, 1),
                    },
                })
        finally:
            con.close()
    body = {"type": "FeatureCollection", "generated": int(time.time()),
            "window_min": window_min, "features": feats}
    return json.dumps(body).encode()


class Handler(SimpleHTTPRequestHandler):
    window_min = 60.0

    def end_headers(self):  # noqa: N802 (stdlib casing)
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_GET(self):  # noqa: N802 (stdlib casing)
        if self.path.split("?", 1)[0] == LIVE_ENDPOINT:
            body = _positions_geojson(self.window_min)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()

    def translate_path(self, path: str) -> str:
        # The whole UI is the real web/ site; "/" is its index.
        clean = posixpath.normpath(unquote(path.split("?", 1)[0].split("#", 1)[0]))
        if clean in ("/", "/index.html", "."):
            return str(WEB / "index.html")
        rel = clean.lstrip("/")
        cand = (WEB / rel).resolve()
        if cand == WEB or WEB in cand.parents:   # contained within web/, no traversal
            return str(cand)
        return str(WEB / rel)  # outside web/: let the parent emit a clean 404

    def send_head(self):  # noqa: N802 - add Range support (PMTiles needs 206)
        rng = self.headers.get("Range")
        path = self.translate_path(self.path)
        if not rng or not os.path.isfile(path):
            return super().send_head()
        size = os.path.getsize(path)
        m = re.match(r"bytes=(\d*)-(\d*)", rng)
        if not m:
            return super().send_head()
        start = int(m.group(1)) if m.group(1) else 0
        end = int(m.group(2)) if m.group(2) else size - 1
        end = min(end, size - 1)
        if start > end:
            self.send_error(416, "Requested Range Not Satisfiable")
            return None
        length = end - start + 1
        f = open(path, "rb")  # noqa: SIM115 (caller closes)
        f.seek(start)
        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        self._range = (f, length)
        return f

    def copyfile(self, source, outputfile):
        rng = getattr(self, "_range", None)
        if rng is None:
            return super().copyfile(source, outputfile)
        f, length = rng
        remaining = length
        while remaining > 0:
            chunk = f.read(min(64 * 1024, remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            remaining -= len(chunk)


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8100
    Handler.window_min = float(os.environ.get("TRACKER_WINDOW_MIN", "60"))
    handler = partial(Handler, directory=str(WEB))
    print(f"SeaVigil live site on http://localhost:{port}  "
          f"(live layer {LIVE_ENDPOINT}, window {Handler.window_min:.0f} min, db {DB.name})")
    HTTPServer(("0.0.0.0", port), handler).serve_forever()


if __name__ == "__main__":
    main()
