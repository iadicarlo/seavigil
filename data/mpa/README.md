# MPA boundaries

`sample_mpas.geojson` holds **approximate** bounding polygons for a few large Marine
Protected Areas (Galápagos, Phoenix Islands / PIPA, Papahānaumokuākea, Great Barrier Reef).
They exist so the pipeline runs with **no extra download**, and they are flagged
`"approximate": true` in their properties.

**Do not use these boundaries for any real enforcement or analysis.** They are rectangular
approximations, not official limits.

For real use, export the official polygons from the
[World Database on Protected Areas (WDPA)](https://www.protectedplanet.net/) as GeoJSON and
pass the path to `seavigil.mpa.load_mpas(path)` (or `--mpa <path>` on the alert entrypoint).
The loader reads standard GeoJSON `FeatureCollection`s and recognises common WDPA property
keys (`NAME`, `WDPAID`, `WDPA_PID`).

This file is committed (small reference data); raw AIS data under `data/raw/` is not.

## Real boundaries from Protected Planet

Download a WDPA / WD-OECM File Geodatabase from protectedplanet.net and convert it:

```bash
uv run --with pyogrio --with geopandas python scripts/wdpa_gdb_to_geojson.py \
  --gdb path/to/WDPA_WDOECM_..._marine.gdb --name "Phoenix Islands,Papahanaumokuakea" \
  --out data/mpa/wdpa_marine_sample.geojson
uv run python -m seavigil.alert --mpa data/mpa/wdpa_marine_sample.geojson
```

The converted output (`data/mpa/wdpa_*.geojson`) is gitignored: WDPA/WD-OECM is non-commercial
and may not be redistributed as a downloadable map. Citation: UNEP-WCMC and IUCN (2026),
Protected Planet: WDPA and WD-OECM, June 2026, Cambridge, UK, www.protectedplanet.net.
