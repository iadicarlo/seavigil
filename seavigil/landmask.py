"""Drop detections that fall on land.

A SAR or VIIRS vessel detector run over a coastal scene flags bright land features as false
"vessels". We remove any detection inside the Natural Earth land polygons. Coarse (110m) land is
enough to kill clearly-inland false positives while keeping near-shore and high-seas ocean
detections (verified: it drops inland Queensland but keeps the open Coral Sea and the Argentine
Blue Hole). If the land file is absent, nothing is dropped (no silent over-filtering).
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAND_GEOJSON = ROOT / "data" / "geo" / "ne_110m_land.geojson"


@lru_cache(maxsize=1)
def _index():
    from shapely import STRtree
    from shapely.geometry import shape
    data = json.loads(LAND_GEOJSON.read_text())
    geoms = [shape(f["geometry"]) for f in data["features"]]
    return STRtree(geoms), geoms


def is_land(lon, lat) -> bool:
    if lon is None or lat is None or not LAND_GEOJSON.exists():
        return False
    from shapely.geometry import Point
    tree, geoms = _index()
    p = Point(float(lon), float(lat))
    return any(geoms[i].contains(p) for i in tree.query(p))


def drop_land(dossiers: list) -> tuple[list, int]:
    """Return (water-only dossiers, number dropped)."""
    if not LAND_GEOJSON.exists():
        return dossiers, 0
    kept = [d for d in dossiers if not is_land(d.get("centroid_lon"), d.get("centroid_lat"))]
    return kept, len(dossiers) - len(kept)
