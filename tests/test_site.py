"""Tests for the static-site GeoJSON builder."""

from __future__ import annotations

import json

from seavigil import site


def _ais(**kw):
    base = {
        "incident_id": "a", "type": "ais_fishing_incident", "mpa_name": "X",
        "time_start_utc": "t", "mean_fishing_proba": 0.8, "vessel_id": "v",
        "gear": "trawlers", "centroid_lat": 1.0, "centroid_lon": 2.0,
        "explanation": {"top_drivers": [{"feature": "speed", "mean_value": 1.0, "mean_shap": 0.2}]},
        "caveats": ["c1"],
    }
    base.update(kw)
    return base


def test_incidents_to_geojson_lonlat_and_why():
    sar = {
        "incident_id": "b", "type": "dark_vessel_sar", "mpa_name": "Y",
        "time_start_utc": "t2", "mean_fishing_proba": 0.9, "vessel_id": "(dark)",
        "gear": "SAR detection", "centroid_lat": 3.0, "centroid_lon": 4.0,
        "explanation": {"drivers": ["inside MPA: Y", "not broadcasting AIS (dark vessel)"]},
        "caveats": ["c2"],
    }
    gj = site.incidents_to_geojson([_ais(), sar])
    assert gj["type"] == "FeatureCollection" and len(gj["features"]) == 2

    f0 = gj["features"][0]
    assert f0["geometry"]["coordinates"] == [2.0, 1.0]  # [lon, lat]
    assert f0["properties"]["kind"] == "ais_fishing_incident"
    assert "speed" in f0["properties"]["why"]

    f1 = gj["features"][1]
    assert f1["properties"]["kind"] == "dark_vessel_sar"
    assert "inside MPA" in f1["properties"]["why"]


def test_summarize_counts_by_type_mpa_gear():
    sar = {"type": "dark_vessel_sar", "mpa_name": "Y", "gear": "SAR detection"}
    s = site.summarize([_ais(), _ais(mpa_name="Z"), sar])
    assert s["total"] == 3
    assert s["by_type"]["ais_fishing_incident"] == 2
    assert s["by_type"]["dark_vessel_sar"] == 1
    assert set(s["by_mpa"]) == {"X", "Z", "Y"}
    assert s["by_gear"]["trawlers"] == 2


def test_build_site_writes_all_files(tmp_path):
    inc = tmp_path / "incidents.json"
    inc.write_text(json.dumps([_ais(explanation=None)]))
    out = tmp_path / "data"

    # MPA boundaries are NOT written here (they ship as non-extractable vector tiles
    # under web/tiles/); build_site emits the incident data + summary only.
    res = site.build_site(inc, mpa_geojson=None, out_dir=out)
    assert res["n_records"] == 1
    for f in ("incidents.geojson", "tracks.geojson", "summary.json"):
        assert (out / f).exists()
    assert not (out / "mpas.geojson").exists()
    gj = json.loads((out / "incidents.geojson").read_text())
    assert gj["features"][0]["geometry"]["coordinates"] == [2.0, 1.0]
    assert json.loads((out / "summary.json").read_text())["total"] == 1
