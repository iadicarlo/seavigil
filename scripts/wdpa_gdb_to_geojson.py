#!/usr/bin/env python3
"""Convert a WDPA / WD-OECM File Geodatabase (.gdb) to a GeoJSON the --mpa loader accepts.

Filters by name pattern(s) or a bounding box, simplifies the (often huge) polygons, and
maps the Protected Planet schema (SITE_PID, NAME, IUCN_CAT, NO_TAKE) onto the property keys
seavigil.mpa expects, stamping the snapshot version for reproducibility.

WDPA/WD-OECM is UNEP-WCMC + IUCN, NON-COMMERCIAL, and may not be redistributed as a
downloadable web map. The output is gitignored: use it locally with --mpa, or convert to
non-extractable tiles (scripts/wdpa_to_pmtiles.sh) for a public map. Cite:
  UNEP-WCMC and IUCN (2026), Protected Planet: The World Database on Protected Areas (WDPA)
  and World Database on Other Effective Area-based Conservation Measures (WD-OECM), June 2026,
  Cambridge, UK: UNEP-WCMC and IUCN. www.protectedplanet.net

Run (geopandas/pyogrio are not project deps; pull them just for this):
  uv run --with pyogrio --with geopandas python scripts/wdpa_gdb_to_geojson.py \
      --gdb ~/Downloads/WDPA_WDOECM_Jun2026_Public_marine/WDPA_WDOECM_Jun2026_Public_marine.gdb \
      --name "Galapagos,Galapagos Marine Reserve,Phoenix Islands,Papahanaumokuakea,Great Barrier Reef" \
      --out data/mpa/wdpa_marine_sample.geojson
"""

from __future__ import annotations

import argparse
import json
import sys

DEFAULT_LAYER = "WDPA_WDOECM_poly_Jun2026_marine"
NAME_KEYS = ("NAME", "NAME_ENG")
ID_KEYS = ("SITE_PID", "SITE_ID", "WDPA_PID", "WDPAID")


def _first(row, keys, default=None):
    for k in keys:
        if k in row and row[k] not in (None, ""):
            return row[k]
    return default


def main() -> None:
    ap = argparse.ArgumentParser(description="WDPA/WD-OECM .gdb -> --mpa GeoJSON")
    ap.add_argument("--gdb", required=True)
    ap.add_argument("--layer", default=DEFAULT_LAYER)
    ap.add_argument("--name", default=None, help="comma-separated name patterns (LIKE %%pat%%)")
    ap.add_argument("--bbox", default=None, help="minlon,minlat,maxlon,maxlat")
    ap.add_argument("--out", required=True)
    ap.add_argument("--simplify", type=float, default=0.01, help="degrees (~1.1 km); 0 to disable")
    ap.add_argument("--version", default="WDPA/WD-OECM Jun2026")
    args = ap.parse_args()

    try:
        import geopandas as gpd
    except ImportError:
        sys.exit("run with: uv run --with pyogrio --with geopandas python scripts/wdpa_gdb_to_geojson.py ...")

    read_kwargs = {"layer": args.layer}
    if args.name:
        pats = [p.strip() for p in args.name.split(",") if p.strip()]
        read_kwargs["where"] = " OR ".join(f"NAME LIKE '%{p}%'" for p in pats)
    if args.bbox:
        minlon, minlat, maxlon, maxlat = (float(x) for x in args.bbox.split(","))
        read_kwargs["bbox"] = (minlon, minlat, maxlon, maxlat)

    g = gpd.read_file(args.gdb, **read_kwargs)
    if args.simplify > 0:
        g["geometry"] = g.geometry.simplify(args.simplify, preserve_topology=True)

    feats = []
    for _, row in g.iterrows():
        if row.geometry is None or row.geometry.is_empty:
            continue
        feats.append({
            "type": "Feature",
            "geometry": json.loads(gpd.GeoSeries([row.geometry]).to_json())["features"][0]["geometry"],
            "properties": {
                "name": _first(row, NAME_KEYS, "MPA"),
                "WDPAID": _first(row, ID_KEYS),
                "IUCN_CAT": row.get("IUCN_CAT"),
                "NO_TAKE": row.get("NO_TAKE"),
                "approximate": False,
            },
        })

    fc = {"type": "FeatureCollection", "wdpa_version": args.version,
          "_attribution": "UNEP-WCMC and IUCN (2026), Protected Planet: WDPA & WD-OECM, "
                          "June 2026, www.protectedplanet.net",
          "features": feats}
    with open(args.out, "w") as f:
        json.dump(fc, f)
    print(f"wrote {len(feats)} WDPA polygons -> {args.out}")
    for ft in feats:
        p = ft["properties"]
        print(f"  {str(p['name'])[:42]:42} | IUCN {p['IUCN_CAT']} | NO_TAKE {p['NO_TAKE']}")


if __name__ == "__main__":
    main()
