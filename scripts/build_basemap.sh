#!/usr/bin/env bash
# Build the local dark vector basemap (web/tiles/basemap.pmtiles) so the map needs no
# CDN and runs fully offline. Source: Natural Earth 1:50m (public domain) land polygons
# and country boundary lines. Requires tippecanoe (brew install tippecanoe).
set -euo pipefail
cd "$(dirname "$0")/.."

NE=https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson
mkdir -p data/natural_earth web/tiles

curl -fsSL -o data/natural_earth/ne_50m_land.geojson "$NE/ne_50m_land.geojson"
curl -fsSL -o data/natural_earth/ne_50m_boundary_lines_land.geojson "$NE/ne_50m_admin_0_boundary_lines_land.geojson"

tippecanoe -o web/tiles/basemap.pmtiles -Z0 -z8 -P \
  --coalesce-densest-as-needed --simplification=4 --no-tile-size-limit \
  -L land:data/natural_earth/ne_50m_land.geojson \
  -L boundaries:data/natural_earth/ne_50m_boundary_lines_land.geojson \
  --force

echo "wrote web/tiles/basemap.pmtiles"
