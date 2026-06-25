"""Tests for the behavioral detectors (AIS spoofing, going dark)."""

from __future__ import annotations

import pandas as pd

from seavigil import going_dark, spoofing


def test_spoofing_flags_teleporting_mmsi():
    # One MMSI alternating between two points 130+ nm apart every minute: impossible.
    t0 = 1_700_000_000
    rows = []
    for k in range(20):
        lat, lon = (35.0, -122.0) if k % 2 == 0 else (36.0, -120.0)
        rows.append({"vessel_id": "111", "timestamp": t0 + k * 60, "lat": lat, "lon": lon})
    dos = spoofing.build_spoofing_dossiers(pd.DataFrame(rows))
    assert len(dos) == 1
    assert dos[0]["type"] == "ais_spoofing"
    assert dos[0]["anomaly_count"] >= 3


def test_spoofing_ignores_normal_track():
    t0 = 1_700_000_000
    rows = [{"vessel_id": "222", "timestamp": t0 + k * 600, "lat": 35.0 + k * 0.01,
             "lon": -122.0 + k * 0.01} for k in range(20)]
    assert spoofing.build_spoofing_dossiers(pd.DataFrame(rows)) == []


def test_going_dark_flags_offshore_gap():
    t0 = 1_700_000_000
    rows = [{"vessel_id": "333", "timestamp": t0 + k * 1800, "lat": 40.0, "lon": -150.0,
             "speed": 5, "distance_from_shore": 200_000} for k in range(26)]  # dense, >50 nm
    rows.append({"vessel_id": "333", "timestamp": rows[-1]["timestamp"] + 14 * 3600,
                 "lat": 40.5, "lon": -150.5, "speed": 5, "distance_from_shore": 200_000})
    dos = going_dark.build_disabling_dossiers(pd.DataFrame(rows))
    assert len(dos) == 1
    assert dos[0]["type"] == "ais_disabling"
    assert dos[0]["gap_hours"] >= 12


def test_going_dark_ignores_nearshore_gap():
    t0 = 1_700_000_000
    rows = [{"vessel_id": "444", "timestamp": t0 + k * 1800, "lat": 40.0, "lon": -124.0,
             "speed": 5, "distance_from_shore": 5_000} for k in range(26)]  # < 50 nm offshore
    rows.append({"vessel_id": "444", "timestamp": rows[-1]["timestamp"] + 14 * 3600,
                 "lat": 40.1, "lon": -124.1, "speed": 5, "distance_from_shore": 5_000})
    assert going_dark.build_disabling_dossiers(pd.DataFrame(rows)) == []
