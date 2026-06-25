#!/usr/bin/env python3
"""Reconcile the showcase incidents with the real WDPA boundaries.

Two things happen here:
1. AIS incidents (2013-2014 labels, originally segmented against approximate boxes)
   are re-validated against the real WDPA polygons: an incident is kept only if its
   centroid is genuinely inside a real reserve, and its MPA name + severity are
   regraded from the matched real zone (so a no-take area reads as high severity).
2. The synthetic round-coordinate SAR sample is swapped for real Sentinel-1
   dark-vessel detections (Paolo et al., Nature 2024) inside the real MPAs, keeping
   a temporally and spatially diverse subset (spread across the year and reserves,
   not one dense satellite pass).

The whole results/incidents set is then re-written via write_dossiers so the JSON,
per-incident Markdown, INDEX.md and tracks.geojson stay mutually consistent (AIS
tracks are re-attached first so they survive the rebuild).

Run:  uv run python scripts/swap_real_sar.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Make `seavigil` importable when run as a standalone script (package is not installed).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from seavigil.dossier import write_dossiers  # noqa: E402
from seavigil.evidence import enrich_evidence  # noqa: E402
from seavigil.jurisdiction import enrich_jurisdiction  # noqa: E402
from seavigil.mpa import MPAIndex, grade_severity  # noqa: E402
from seavigil.sar import _slug, build_sar_dossiers, load_sar_detections  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INC_DIR = ROOT / "results" / "incidents"
INC_JSON = INC_DIR / "incidents.json"
TRACKS = INC_DIR / "tracks.geojson"
REAL_SAR = ROOT / "data" / "sar" / "gfw_sar_detections.geojson"
MPA = ROOT / "data" / "mpa" / "wdpa_marine_showcase.geojson"
EEZ = ROOT / "web" / "data" / "eez.geojson"
MAX_SAR = 55
CAP_PER_PASS = 20  # dark detections cluster on few Sentinel-1 passes; allow density


def _select_diverse(alld: list[dict]) -> list[dict]:
    """Round-robin across MPAs, capping picks per satellite pass (timestamp), so the
    showcase spreads across the year and both reserves, not one dense Jan-1 pass."""
    by_mpa: dict = {}
    for d in sorted(alld, key=lambda d: d.get("time_start_utc") or ""):
        by_mpa.setdefault(d["mpa_name"], []).append(d)
    xy = lambda d: (round(d["centroid_lon"], 2), round(d["centroid_lat"], 2))  # noqa: E731

    out, seen_xy, per_pass = [], set(), {}
    buckets = list(by_mpa.values())
    progressed = True
    while len(out) < MAX_SAR and progressed:
        progressed = False
        for bucket in buckets:
            for i, d in enumerate(bucket):
                t = d.get("time_start_utc")
                if xy(d) in seen_xy or per_pass.get(t, 0) >= CAP_PER_PASS:
                    continue
                bucket.pop(i)
                seen_xy.add(xy(d))
                per_pass[t] = per_pass.get(t, 0) + 1
                out.append(d)
                progressed = True
                break
            if len(out) >= MAX_SAR:
                break
    # Contiguous incident ids per MPA (0000, 0001, ...).
    seq: dict = {}
    for d in out:
        n = seq.get(d["mpa_name"], 0)
        seq[d["mpa_name"]] = n + 1
        d["incident_id"] = f"sar__{_slug(d['mpa_name'])}_{n:04d}"
    return out


def _revalidate_ais(ais: list[dict], idx: MPAIndex) -> list[dict]:
    """Keep only AIS incidents whose centroid is genuinely inside a real WDPA
    polygon; reassign mpa_name and regrade severity from the matched real zone.

    The curated incidents were segmented against approximate boxes; this makes them
    honest against the real boundaries now drawn on the map (a vessel in the old box
    but outside the precise reserve is dropped, not silently shown as an incursion).
    """
    kept = []
    for d in ais:
        a = idx.assign([d["centroid_lon"]], [d["centroid_lat"]])
        mi = int(a[0])
        if mi < 0:
            continue
        mpa = idx.mpas[mi]
        d["mpa_name"] = mpa.name
        d["wdpa_id"] = mpa.wdpa_id
        d["mpa_iucn_cat"] = mpa.iucn_cat
        d["mpa_no_take"] = mpa.no_take
        d["mpa_version"] = mpa.version
        sev, reason = grade_severity(mpa.iucn_cat, mpa.no_take)
        d["severity"], d["severity_reason"] = sev, reason
        # Re-key the incident id to the new MPA slug so files/links stay consistent.
        suffix = d["incident_id"].split("__", 1)[-1]
        d["incident_id"] = f"{_slug(mpa.name)}__{suffix}"
        kept.append(d)
    return kept


def _escalate_by_mpa(dossiers: list[dict], mpa_idx: MPAIndex) -> None:
    """Dark detections were segmented against the EEZ (so mpa_name holds the EEZ name).
    Escalate severity and relabel when a detection also sits inside a real MPA: a dark
    vessel in a no-take reserve is the worst case; one merely inside the EEZ is a lead.
    """
    for d in dossiers:
        eez_name = d.get("mpa_name")  # build_sar_dossiers set this to the EEZ name
        length = d.get("length_m")
        a = mpa_idx.assign([d["centroid_lon"]], [d["centroid_lat"]])
        mi = int(a[0])
        if mi >= 0:
            m = mpa_idx.mpas[mi]
            d["mpa_name"] = m.name
            d["wdpa_id"] = m.wdpa_id
            d["mpa_iucn_cat"] = m.iucn_cat
            d["mpa_no_take"] = m.no_take
            d["mpa_version"] = m.version
            # A non-broadcasting vessel inside a reserve is a serious incursion: high.
            no_take = (m.no_take or "").strip().lower() in ("all", "part") or m.iucn_cat in ("Ia", "Ib", "II")
            d["severity"] = "high"
            d["severity_reason"] = (f"dark vessel inside {'no-take ' if no_take else ''}MPA")
            drivers = [f"inside MPA: {m.name} (within {eez_name})",
                       "not broadcasting AIS (dark vessel)"]
        else:
            d["mpa_name"] = f"{eez_name} (outside MPA)"
            d["wdpa_id"] = d["mpa_iucn_cat"] = d["mpa_no_take"] = None
            d["severity"] = "medium"
            d["severity_reason"] = "dark vessel inside national EEZ, outside any protected area"
            drivers = [f"inside national EEZ: {eez_name}, outside any MPA",
                       "not broadcasting AIS (dark vessel)"]
        if length is not None:
            drivers.append(f"length: {length:.0f} m ({'industrial' if length >= 24 else 'small'})")
        method = (d.get("explanation") or {}).get("method", "SAR detection attributes")
        d["explanation"] = {"method": method, "drivers": drivers}


def _load_behaviors() -> list[dict]:
    """Behavioral dossiers from real AIS: spoofing from NOAA terrestrial tracks, and
    going-dark from GFW's satellite AIS-disabling events (consumed, like the SAR dark
    fleet, because terrestrial AIS cannot see offshore disabling). Both are optional."""
    out: list[dict] = []
    tracks = ROOT / "data" / "positions" / "noaa_tracks.csv"
    if tracks.exists():
        import pandas as pd  # noqa: PLC0415

        from seavigil import spoofing  # noqa: PLC0415
        out += spoofing.build_spoofing_dossiers(pd.read_csv(tracks))
    disabling = ROOT / "data" / "disabling" / "disabling_events.csv"
    if disabling.exists():
        from seavigil import going_dark  # noqa: PLC0415
        from seavigil.jurisdiction import EEZIndex  # noqa: PLC0415
        out += going_dark.build_from_gfw_disabling(str(disabling), EEZIndex())
    return out


def main() -> None:
    existing = json.loads(INC_JSON.read_text())
    ais = [d for d in existing if d.get("type") != "dark_vessel_sar"]

    # Re-attach AIS tracks (stripped from incidents.json) so write_dossiers can
    # regenerate tracks.geojson without losing them.
    track_of = {f["properties"]["id"]: f["geometry"]["coordinates"]
                for f in json.loads(TRACKS.read_text()).get("features", [])}
    for d in ais:
        if d["incident_id"] in track_of:
            d["track"] = track_of[d["incident_id"]]

    mpa_idx = MPAIndex.from_geojson(str(MPA))
    n_before = len(ais)
    ais = _revalidate_ais(ais, mpa_idx)
    print(f"AIS re-validated against real polygons: kept {len(ais)} of {n_before}")

    # Dark fleet = dark SAR detections inside a national EEZ (the real IUU hotspot;
    # dark vessels lurk at EEZ scale far more than inside the small reserves). Build
    # against the EEZ polygons, keep only genuinely dark (unmatched) blips, then
    # escalate severity for any that also fall inside an MPA (no-take = worst).
    eez_idx = MPAIndex.from_geojson(str(EEZ))
    dets = load_sar_detections(str(REAL_SAR))
    alld = build_sar_dossiers(dets, eez_idx, min_fishing_score=0.5,
                              include_dark=True, max_dossiers=100_000)
    dark = [d for d in alld if not d.get("matched_to_ais")]
    _escalate_by_mpa(dark, mpa_idx)
    sar = _select_diverse(dark)

    behaviors = _load_behaviors()  # AIS spoofing from real NOAA tracks (if present)

    # Clean slate: drop every old per-incident Markdown so no orphans linger.
    for p in INC_DIR.glob("*.md"):
        if p.name != "INDEX.md":
            p.unlink()

    merged = enrich_jurisdiction(ais + sar + behaviors)  # tag each with its EEZ + foreign flag
    enrich_evidence(merged)                               # stamp tamper-evident hash + schema
    write_dossiers(merged, INC_DIR)

    by_mpa: dict = {}
    for d in sar:
        by_mpa[d["mpa_name"]] = by_mpa.get(d["mpa_name"], 0) + 1
    spans = sorted({d.get("time_start_utc") for d in sar})
    print(f"wrote {len(ais)} AIS + {len(sar)} real GFW dark-vessel SAR dossiers")
    print(f"real SAR by MPA: {by_mpa}")
    if spans:
        print(f"SAR spans {len(spans)} satellite passes: {spans[0][:10]} -> {spans[-1][:10]}")


if __name__ == "__main__":
    main()
