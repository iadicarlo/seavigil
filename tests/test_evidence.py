"""Tests for the auditable evidence package (integrity hash + provenance)."""

from __future__ import annotations

from seavigil.evidence import (
    SCHEMA_VERSION,
    enrich_evidence,
    evidence_hash,
    provenance_for,
)


def test_hash_deterministic_and_tamper_sensitive():
    d = {"incident_id": "x", "type": "dark_vessel_sar",
         "centroid_lat": 1.0, "centroid_lon": 2.0, "severity": "high"}
    h = evidence_hash(d)
    assert len(h) == 64
    assert evidence_hash(dict(d)) == h          # deterministic
    tampered = {**d, "centroid_lat": 1.5}
    assert evidence_hash(tampered) != h          # any canonical change moves the hash


def test_enrich_stamps_schema_and_hash():
    ds = [{"incident_id": "a", "type": "ais_fishing_incident", "centroid_lat": 0, "centroid_lon": 0}]
    enrich_evidence(ds)
    assert ds[0]["evidence_schema"] == SCHEMA_VERSION
    assert len(ds[0]["evidence_hash"]) == 64


def test_provenance_includes_type_and_boundary_sources():
    prov = provenance_for("dark_vessel_sar")
    datasets = " ".join(s["dataset"] for s in prov)
    assert "SAR" in datasets and "WDPA" in datasets and "Economic Zones" in datasets
