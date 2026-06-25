#!/usr/bin/env python3
"""Export WDPA marine protected-area polygons from Google Earth Engine to a GeoJSON
that seavigil.mpa.load_mpas / `--mpa` ingests directly.

The WDPA on GEE (WCMC/WDPA/current/polygons) is a server-side FeatureCollection - not a
plain file - so you filter + export it. This pulls polygons intersecting a bounding box,
filtered to marine areas, keeping the WDPAID/NAME/IUCN_CAT/NO_TAKE attributes SeaVigil
grades severity from, and stamps the snapshot version for reproducibility.

Setup (one-time):
    pip install earthengine-api
    earthengine authenticate          # opens a browser; uses YOUR Google / GEE account

Usage:
    python scripts/wdpa_from_gee.py --bbox -92.5,-1.7,-89.0,0.7 --out data/mpa/galapagos_wdpa.geojson
    uv run python -m seavigil.alert --mpa data/mpa/galapagos_wdpa.geojson --positions your_ais.csv

License: WDPA is UNEP-WCMC, NON-COMMERCIAL. Private/local analysis is fine; a PUBLIC web map
needs non-downloadable tiles + UNEP-WCMC permission (see docs/DEPLOY.md). Keep the
IUCN/UNEP-WCMC citation + a protectedplanet.net link visible. Use a dated snapshot
(WCMC/WDPA/YYYYMM/polygons) to pin the boundary version at incident time.

Not a package dependency (earthengine-api is heavy and auth is user-specific) - run standalone.
For large regions use ee Export.table.toDrive instead of getInfo().
"""

from __future__ import annotations

import argparse
import json
import sys

WDPA_CURRENT = "WCMC/WDPA/current/polygons"


def main() -> None:
    ap = argparse.ArgumentParser(description="Export WDPA marine polygons (GEE) to GeoJSON")
    ap.add_argument("--bbox", required=True, help="minlon,minlat,maxlon,maxlat")
    ap.add_argument("--out", required=True)
    ap.add_argument("--asset", default=WDPA_CURRENT,
                    help="GEE WDPA asset; use WCMC/WDPA/YYYYMM/polygons for a fixed snapshot")
    args = ap.parse_args()

    try:
        import ee
    except ImportError:
        sys.exit("earthengine-api not installed. Run: pip install earthengine-api "
                 "&& earthengine authenticate")

    ee.Initialize()
    minlon, minlat, maxlon, maxlat = (float(x) for x in args.bbox.split(","))
    region = ee.Geometry.Rectangle([minlon, minlat, maxlon, maxlat])
    fc = (ee.FeatureCollection(args.asset)
          .filterBounds(region)
          .filter(ee.Filter.inList("MARINE", ["1", "2", 1, 2])))

    n = fc.size().getInfo()
    if n > 5000:
        sys.exit(f"{n} features in bbox - too many for getInfo(); shrink the bbox "
                 "or use Export.table.toDrive.")

    gj = fc.getInfo()  # a GeoJSON FeatureCollection
    gj["wdpa_version"] = args.asset  # stamp the snapshot for reproducibility
    with open(args.out, "w") as f:
        json.dump(gj, f)
    print(f"wrote {n} WDPA features -> {args.out} "
          "(keys incl. WDPAID / NAME / IUCN_CAT / NO_TAKE)")


if __name__ == "__main__":
    main()
