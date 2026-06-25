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
