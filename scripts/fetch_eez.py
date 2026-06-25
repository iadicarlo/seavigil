#!/usr/bin/env python3
"""Fetch the showcase EEZ boundaries from Marine Regions (Flanders VLIZ).

Exclusive Economic Zones are the jurisdiction most IUU fishing actually violates
(a foreign vessel fishing in a coastal state's EEZ), so they are the reference layer
that turns SeaVigil from "MPA-only" into an IUU tool. Unlike WDPA, the Marine Regions
EEZ dataset is CC BY 4.0 (redistributable with attribution), so the simplified
boundaries can ship as plain GeoJSON.

Source:  Flanders Marine Institute (2024). Maritime Boundaries Geodatabase: Maritime
Boundaries and Exclusive Economic Zones (200NM), version 12. https://marineregions.org/
DOI 10.14284/632. License: CC BY 4.0.

Run:  uv run --with shapely python scripts/fetch_eez.py
"""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path

from shapely.geometry import mapping, shape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "web" / "data" / "eez.geojson"
WFS = "https://geo.vliz.be/geoserver/MarineRegions/wfs"
SIMPLIFY_DEG = 0.03  # ~3 km; EEZs are vast and smooth, this stays faithful and small
ATTRIBUTION = ("Flanders Marine Institute (2024), Maritime Boundaries Geodatabase: "
               "Exclusive Economic Zones (200NM), version 12, marineregions.org, "
               "DOI 10.14284/632. CC BY 4.0.")

# mrgid -> clean display name (confirmed against the EEZ layer).
TARGETS = {
    8403: "Galapagos EEZ (Ecuador)",
    8323: "Australia EEZ",
    8450: "Phoenix Islands EEZ (Kiribati)",
    8453: "Hawaii EEZ (United States)",
    21787: "Easter Island EEZ (Chile)",
}


def main() -> None:
    ids = ",".join(str(m) for m in TARGETS)
    params = (
        "service=WFS&version=2.0.0&request=GetFeature"
        "&typeNames=MarineRegions:eez&outputFormat=application/json"
        f"&cql_filter=mrgid%20IN%20({ids})"
    )
    url = f"{WFS}?{params}"
    print(f"fetching {len(TARGETS)} EEZ polygons ...")
    with urllib.request.urlopen(url, timeout=120) as r:  # noqa: S310 (trusted gov endpoint)
        data = json.loads(r.read())

    feats = []
    for f in data["features"]:
        p = f["properties"]
        mrgid = int(p["mrgid"])
        g = shape(f["geometry"]).simplify(SIMPLIFY_DEG, preserve_topology=True)
        if g.is_empty:
            continue
        feats.append({
            "type": "Feature",
            "geometry": mapping(g),
            "properties": {
                "name": TARGETS.get(mrgid, p.get("geoname")),
                "geoname": p.get("geoname"),
                "mrgid": mrgid,
                "sovereign": p.get("sovereign1"),
                "iso_sov": p.get("iso_sov1"),
                "territory": p.get("territory1"),
                "area_km2": p.get("area_km2"),
            },
        })
        print(f"  {TARGETS.get(mrgid):34} ok")

    fc = {"type": "FeatureCollection", "_attribution": ATTRIBUTION, "features": feats}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(fc))
    print(f"\nwrote {len(feats)} EEZ polygons -> {OUT}  ({OUT.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
