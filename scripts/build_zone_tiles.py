#!/usr/bin/env python3
"""Build non-extractable vector tiles for the global EEZ (Marine Regions).

EEZ is CC BY 4.0, but a full-resolution global GeoJSON (~285 polygons, 259 MB) is far
too heavy for the browser, so the global reference layer ships as web/tiles/eez.pmtiles.
tippecanoe reads and simplifies the GeoJSON itself (streaming, per-zoom Douglas-Peucker),
so we never parse the whole file into Python. The small per-region web/data/eez.geojson
stays as the offline jurisdiction-tagging source.

Run (after the global EEZ fetch):
  uv run python scripts/build_zone_tiles.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "eez" / "eez_global.geojson"
OUT = ROOT / "web" / "tiles" / "eez.pmtiles"


def main() -> None:
    if not SRC.exists():
        sys.exit(f"missing {SRC}; run the global EEZ fetch first")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([  # noqa: S603,S607
        "tippecanoe", "-o", str(OUT), "-l", "eez", "-Z0", "-z7", "-r1",
        "--simplification=10", "--no-tile-size-limit", "--no-feature-limit",
        "--coalesce-smallest-as-needed", "--drop-densest-as-needed",
        "-f", str(SRC),
    ], check=True)
    print(f"wrote global EEZ tiles -> {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
