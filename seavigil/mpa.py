"""Assign AIS positions to Marine Protected Areas (MPAs) by point-in-polygon.

Loads MPA polygons from GeoJSON (the bundled approximate sample under data/mpa/,
or any WDPA GeoJSON export), builds a shapely ``STRtree`` spatial index, and labels
each (lon, lat) position with the MPA that contains it (or "outside").

CPU-only; depends only on ``shapely`` -- deliberately no GDAL / geopandas, to keep
the stack laptop-deployable.

The bundled sample (data/mpa/sample_mpas.geojson) uses APPROXIMATE bounding
polygons for a few large MPAs, for reproducible demos only. For real use, pass an
official WDPA polygon export to ``load_mpas()``.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import shapely
from shapely import STRtree
from shapely.geometry import shape
from shapely.geometry.base import BaseGeometry

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MPA_GEOJSON = ROOT / "data" / "mpa" / "sample_mpas.geojson"

# Property keys we look for, in priority order, when reading a GeoJSON feature.
_NAME_KEYS = ("name", "NAME", "ORIG_NAME", "WDPA_PID")
_WDPA_KEYS = ("wdpa_id", "WDPAID", "WDPA_PID")


@dataclass(frozen=True)
class MPA:
    """One protected area: a name plus a shapely geometry."""

    name: str
    geometry: BaseGeometry
    wdpa_id: str | None = None
    approximate: bool = False


def _first_prop(props: dict, keys: tuple[str, ...]) -> str | None:
    for k in keys:
        v = props.get(k)
        if v is not None and str(v) != "":
            return str(v)
    return None


def load_mpas(path: str | Path | None = None) -> list[MPA]:
    """Read a GeoJSON FeatureCollection into a list of ``MPA``.

    Recognises common WDPA property keys for the name and id. Features without a
    geometry are skipped. Raises if the file yields no usable MPA.
    """
    path = Path(path) if path is not None else DEFAULT_MPA_GEOJSON
    data = json.loads(path.read_text())
    features = data.get("features", []) if isinstance(data, dict) else []

    mpas: list[MPA] = []
    for feat in features:
        geom = feat.get("geometry")
        if not geom:
            continue
        props = feat.get("properties") or {}
        name = _first_prop(props, _NAME_KEYS) or f"MPA_{len(mpas)}"
        mpas.append(
            MPA(
                name=name,
                geometry=shape(geom),
                wdpa_id=_first_prop(props, _WDPA_KEYS),
                approximate=bool(props.get("approximate", False)),
            )
        )

    if not mpas:
        raise ValueError(f"no MPA features with geometry found in {path}")
    return mpas


class MPAIndex:
    """STRtree spatial index over MPA polygons for fast point-in-polygon."""

    def __init__(self, mpas: list[MPA]):
        if not mpas:
            raise ValueError("MPAIndex requires at least one MPA")
        self.mpas = list(mpas)
        self._geoms = np.array([m.geometry for m in self.mpas], dtype=object)
        self._tree = STRtree(self._geoms)
        self._names = np.array([m.name for m in self.mpas], dtype=object)

    @classmethod
    def from_geojson(cls, path: str | Path | None = None) -> "MPAIndex":
        return cls(load_mpas(path))

    def __len__(self) -> int:
        return len(self.mpas)

    def assign(self, lon, lat) -> np.ndarray:
        """Map each (lon, lat) to an MPA index, or -1 if outside every MPA.

        Returns a 1-D int64 array aligned to the (flattened) inputs. When a point
        falls in more than one polygon (overlapping MPAs are rare), the
        lowest-index MPA wins, deterministically.
        """
        lon = np.atleast_1d(np.asarray(lon, dtype="float64")).ravel()
        lat = np.atleast_1d(np.asarray(lat, dtype="float64")).ravel()
        if lon.shape != lat.shape:
            raise ValueError("lon and lat must have the same number of elements")

        out = np.full(lon.shape, -1, dtype="int64")
        if lon.size == 0:
            return out

        points = shapely.points(lon, lat)
        # STRtree.query with an array returns a (2, K) array of pairs:
        # row 0 = input (point) indices, row 1 = tree (MPA) indices, for every
        # pair where the MPA geometry intersects the point. "intersects" counts
        # boundary points as inside, which is the behaviour we want.
        point_idx, mpa_idx = self._tree.query(points, predicate="intersects")

        # Lowest MPA index wins: process pairs in ascending MPA order so the first
        # write per point is the smallest index, then keep only first writes.
        order = np.argsort(mpa_idx, kind="stable")
        for p, m in zip(point_idx[order], mpa_idx[order]):
            if out[p] == -1:
                out[p] = m
        return out

    def names(self, assigned: np.ndarray) -> np.ndarray:
        """Turn an array of MPA indices (from ``assign``) into MPA names / None."""
        assigned = np.asarray(assigned)
        res = np.full(assigned.shape, None, dtype=object)
        inside = assigned >= 0
        res[inside] = self._names[assigned[inside]]
        return res


def assign_positions(df, index: MPAIndex, *, lon_col: str = "lon", lat_col: str = "lat"):
    """Convenience: return (mpa_index_array, mpa_name_array) for a positions frame."""
    idx = index.assign(df[lon_col].to_numpy(), df[lat_col].to_numpy())
    return idx, index.names(idx)


if __name__ == "__main__":
    index = MPAIndex.from_geojson()
    print(f"loaded {len(index)} MPAs: {[m.name for m in index.mpas]}")
    # A point inside the Galápagos sample box and one in the open Atlantic.
    demo_idx = index.assign([-91.0, 0.0], [-0.5, 0.0])
    print("assignments:", index.names(demo_idx).tolist())
