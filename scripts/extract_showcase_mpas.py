#!/usr/bin/env python3
"""Extract the showcase MPAs' real WDPA boundaries from the marine .gdb.

Replaces the crude bounding-box "rectangles" with the genuine, detailed polygons
(Great Barrier Reef keeps its four IUCN management zones so severity can reflect a
no-take area; Galapagos, Phoenix Islands, Papahanaumokuakea no-take monument and
Rapa Nui are taken as their reserve boundary). Geometries are simplified for the web.

WDPA/WD-OECM is UNEP-WCMC and IUCN (2026), Protected Planet, NON-COMMERCIAL. Only a
handful of named, simplified boundaries are produced here, with attribution carried in
the FeatureCollection. The .gdb and this output stay gitignored; the served map data
is derived from it.

Run (geopandas/pyogrio are not project deps; pull them just for this):
  uv run --with pyogrio --with geopandas python scripts/extract_showcase_mpas.py
"""

from __future__ import annotations

import json
from pathlib import Path

import geopandas as gpd

GDB = Path("/Users/Abdel042/Downloads/WDPA_WDOECM_Jun2026_Public_marine/"
           "WDPA_WDOECM_Jun2026_Public_marine.gdb")
LAYER = "WDPA_WDOECM_poly_Jun2026_marine"
OUT = Path(__file__).resolve().parent.parent / "data" / "mpa" / "wdpa_marine_showcase.geojson"
SIMPLIFY_DEG = 0.004  # ~440 m; keeps shape, drops the millions of coastal vertices
VERSION = "WDPA/WD-OECM Jun2026"
ATTRIBUTION = ("UNEP-WCMC and IUCN (2026), Protected Planet: The World Database on "
               "Protected Areas (WDPA) and WD-OECM, June 2026, Cambridge, UK. "
               "www.protectedplanet.net")

# One WHERE clause selecting every target record (read the global layer ONCE).
WHERE = ("SITE_PID = '11753' "
         "OR NAME = 'Great Barrier Reef' "
         "OR NAME LIKE 'Phoenix Islands%' "
         "OR (NAME LIKE 'Papahanaumokuakea%' AND IUCN_CAT = 'Ia') "
         "OR NAME = 'Rapa Nui'")


def _display_name(row) -> str | None:
    name = (row.get("NAME") or "").strip()
    if str(row.get("SITE_PID")) == "11753":
        return "Galapagos Marine Reserve"
    if name == "Great Barrier Reef":
        return "Great Barrier Reef Marine Park"
    if name.startswith("Phoenix Islands"):
        return "Phoenix Islands Protected Area"
    if name.startswith("Papahanaumokuakea") and (row.get("IUCN_CAT") or "").strip() == "Ia":
        return "Papahanaumokuakea Marine National Monument"
    if name == "Rapa Nui":
        return "Rapa Nui Marine Protected Area"
    return None


def _is_no_take(no_take, iucn) -> bool:
    nt = (no_take or "").strip().lower()
    return nt in ("all", "part") or (iucn or "").strip() == "Ia"


def main() -> None:
    g = gpd.read_file(GDB, layer=LAYER, where=WHERE)
    g = g.to_crs(4326)
    g["geometry"] = g.geometry.simplify(SIMPLIFY_DEG, preserve_topology=True)

    feats = []
    counts: dict = {}
    for _, r in g.iterrows():
        display = _display_name(r)
        geom = r.geometry
        if display is None or geom is None or geom.is_empty:
            continue
        iucn = r.get("IUCN_CAT")
        no_take = r.get("NO_TAKE")
        gj = json.loads(gpd.GeoSeries([geom], crs=4326).to_json())["features"][0]["geometry"]
        feats.append({
            "type": "Feature",
            "geometry": gj,
            "properties": {
                "name": display,
                "wdpa_name": r.get("NAME"),
                "WDPAID": str(r.get("SITE_PID") or r.get("SITE_ID") or ""),
                "IUCN_CAT": iucn,
                "NO_TAKE": no_take,
                "no_take": _is_no_take(no_take, iucn),
                "area_km2": round(float(r.get("REP_M_AREA") or 0), 1),
                "iso3": r.get("ISO3"),
                "approximate": False,
            },
        })
        counts[display] = counts.get(display, 0) + 1
    for name, n in counts.items():
        print(f"{name:46} -> {n} polygon(s)")

    fc = {"type": "FeatureCollection", "wdpa_version": VERSION,
          "_attribution": ATTRIBUTION, "features": feats}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(fc))
    size_kb = OUT.stat().st_size / 1024
    print(f"\nwrote {len(feats)} polygons -> {OUT}  ({size_kb:.0f} KB)")


if __name__ == "__main__":
    main()
