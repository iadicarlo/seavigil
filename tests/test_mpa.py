"""Tests for the MPA point-in-polygon overlay.

These run offline against the bundled approximate sample polygons. They also pin
the shapely STRtree pair orientation: a point known to be inside the Galápagos
sample box must resolve to that MPA, which fails loudly if the (point, tree)
index order is ever swapped.
"""

from __future__ import annotations

import pandas as pd
import pytest
from shapely.geometry import Polygon

from seavigil import mpa


def _square_index(name: str = "Box") -> mpa.MPAIndex:
    # Unit square covering lon/lat in [0, 1].
    poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
    return mpa.MPAIndex([mpa.MPA(name=name, geometry=poly)])


def test_sample_geojson_loads():
    mpas = mpa.load_mpas()
    names = {m.name for m in mpas}
    assert len(mpas) >= 4
    assert "Galápagos Marine Reserve" in names
    assert all(m.approximate for m in mpas)  # the bundled sample is flagged approximate


def test_grade_severity_levels():
    assert mpa.grade_severity("Ia", "All")[0] == "high"
    assert mpa.grade_severity("II", None)[0] == "high"
    assert mpa.grade_severity("VI", "None")[0] == "low"
    assert mpa.grade_severity(None, None)[0] == "medium"


def test_sample_carries_protection_attrs():
    mpas = {m.name: m for m in mpa.load_mpas()}
    g = mpas["Galápagos Marine Reserve"]
    assert g.iucn_cat == "II" and g.no_take == "Part"
    assert g.version == "sample-approx-2024"
    assert mpas["Great Barrier Reef Marine Park"].iucn_cat == "VI"


def test_point_inside_and_outside_unit_square():
    idx = _square_index("Box")
    assigned = idx.assign([0.5, 5.0], [0.5, 5.0])
    names = idx.names(assigned)
    assert assigned[0] == 0 and names[0] == "Box"   # inside
    assert assigned[1] == -1 and names[1] is None    # outside


def test_orientation_real_sample_box():
    # A point clearly inside the Galápagos approximate box (lon -91, lat -0.5)
    # and one in the open Atlantic (lon 0, lat 0).
    idx = mpa.MPAIndex.from_geojson()
    names = idx.names(idx.assign([-91.0, 0.0], [-0.5, 0.0]))
    assert names[0] == "Galápagos Marine Reserve"
    assert names[1] is None


def test_lowest_index_wins_on_overlap():
    a = mpa.MPA(name="A", geometry=Polygon([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)]))
    b = mpa.MPA(name="B", geometry=Polygon([(1, 1), (3, 1), (3, 3), (1, 3), (1, 1)]))
    idx = mpa.MPAIndex([a, b])  # the point (1.5, 1.5) is inside both
    assigned = idx.assign([1.5], [1.5])
    assert idx.names(assigned)[0] == "A"  # lowest index wins, deterministically


def test_assign_positions_dataframe_helper():
    idx = _square_index("Box")
    df = pd.DataFrame({"lon": [0.5, 9.0], "lat": [0.5, 9.0]})
    mpa_idx, mpa_name = mpa.assign_positions(df, idx)
    assert mpa_idx.tolist() == [0, -1]
    assert mpa_name[0] == "Box" and mpa_name[1] is None


def test_empty_input_returns_empty():
    idx = _square_index()
    assert idx.assign([], []).tolist() == []


def test_mismatched_lengths_raise():
    idx = _square_index()
    with pytest.raises(ValueError):
        idx.assign([0.0, 1.0], [0.0])
