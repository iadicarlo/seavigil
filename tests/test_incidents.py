"""Tests for in-MPA fishing incident segmentation."""

from __future__ import annotations

import numpy as np
import pandas as pd

from seavigil import incidents


def _scored(rows: list[dict]) -> pd.DataFrame:
    """Build a scored frame; timestamp/datetime derived from a base epoch + minutes."""
    base = 1_350_000_000
    out = []
    for r in rows:
        ts = base + r["min"] * 60
        out.append(
            {
                "vessel_id": r["vessel_id"],
                "gear": r.get("gear", "trawlers"),
                "timestamp": float(ts),
                "datetime": pd.to_datetime(ts, unit="s", utc=True),
                "lat": r.get("lat", -0.5),
                "lon": r.get("lon", -91.0),
                "fishing_proba": r["proba"],
                "mpa_idx": r["mpa_idx"],
                "mpa_name": r.get("mpa_name", "Galápagos Marine Reserve"),
                "wdpa_id": r.get("wdpa_id", None),
            }
        )
    return pd.DataFrame(out)


def test_single_fishing_visit_is_one_incident():
    df = _scored(
        [
            {"vessel_id": "v1", "min": 0, "proba": 0.9, "mpa_idx": 0},
            {"vessel_id": "v1", "min": 10, "proba": 0.8, "mpa_idx": 0},
            {"vessel_id": "v1", "min": 20, "proba": 0.6, "mpa_idx": 0},
        ]
    )
    inc = incidents.build_incidents(df)
    assert len(inc) == 1
    assert inc[0].n_fishing_positions == 3
    assert inc[0].mpa_name == "Galápagos Marine Reserve"
    assert inc[0].vessel_id == "v1"
    assert 0.7 < inc[0].mean_fishing_proba < 0.8


def test_passing_through_without_fishing_is_no_incident():
    df = _scored(
        [
            {"vessel_id": "v2", "min": 0, "proba": 0.1, "mpa_idx": 0},
            {"vessel_id": "v2", "min": 5, "proba": 0.2, "mpa_idx": 0},
        ]
    )
    assert incidents.build_incidents(df) == []


def test_positions_outside_any_mpa_are_ignored():
    df = _scored(
        [
            {"vessel_id": "v3", "min": 0, "proba": 0.95, "mpa_idx": -1},
            {"vessel_id": "v3", "min": 5, "proba": 0.95, "mpa_idx": -1},
        ]
    )
    assert incidents.build_incidents(df) == []


def test_large_time_gap_splits_into_two_incidents():
    df = _scored(
        [
            {"vessel_id": "v4", "min": 0, "proba": 0.9, "mpa_idx": 0},
            {"vessel_id": "v4", "min": 30, "proba": 0.9, "mpa_idx": 0},
            # > 6 h later -> new visit
            {"vessel_id": "v4", "min": 30 + 7 * 60, "proba": 0.9, "mpa_idx": 0},
        ]
    )
    inc = incidents.build_incidents(df)
    assert len(inc) == 2
    assert {i.incident_id.endswith("_0000") for i in inc} == {True, False} or len(
        {i.incident_id for i in inc}
    ) == 2


def test_mpa_change_splits_incidents():
    df = _scored(
        [
            {"vessel_id": "v5", "min": 0, "proba": 0.9, "mpa_idx": 0, "mpa_name": "A"},
            {"vessel_id": "v5", "min": 10, "proba": 0.9, "mpa_idx": 1, "mpa_name": "B"},
        ]
    )
    inc = incidents.build_incidents(df)
    assert len(inc) == 2
    assert {i.mpa_name for i in inc} == {"A", "B"}


def test_n_positions_counts_nonfishing_within_visit():
    # One non-fishing dip in the middle of a visit -> still one incident,
    # n_positions=3 but n_fishing_positions=2.
    df = _scored(
        [
            {"vessel_id": "v6", "min": 0, "proba": 0.9, "mpa_idx": 0},
            {"vessel_id": "v6", "min": 10, "proba": 0.2, "mpa_idx": 0},
            {"vessel_id": "v6", "min": 20, "proba": 0.9, "mpa_idx": 0},
        ]
    )
    inc = incidents.build_incidents(df)
    assert len(inc) == 1
    assert inc[0].n_positions == 3
    assert inc[0].n_fishing_positions == 2


def test_fishing_ids_point_back_into_frame():
    df = _scored(
        [
            {"vessel_id": "v7", "min": 0, "proba": 0.9, "mpa_idx": 0},
            {"vessel_id": "v7", "min": 10, "proba": 0.1, "mpa_idx": 0},
        ]
    )
    inc = incidents.build_incidents(df)
    assert len(inc) == 1
    ids = inc[0].fishing_ids
    assert len(ids) == 1
    assert np.isclose(df.loc[ids[0], "fishing_proba"], 0.9)
