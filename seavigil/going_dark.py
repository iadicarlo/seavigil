"""Detect suspected AIS disabling ("going dark") from continuous AIS tracks.

A fishing vessel that broadcasts steadily, then stops for a long stretch far from
shore, then reappears, may have intentionally disabled its transponder, a known IUU
behavior. This reproduces the core of Global Fishing Watch's published methodology
(Welch et al., Science Advances 2022, DOI 10.1126/sciadv.abq2109): an intentional
disabling gap is a gap of at least 12 hours that begins well offshore (so it is not a
port stop), with good AIS coverage in the hours just before (so the silence is not a
reception artifact). Each event records the exact criteria it meets, so the dossier
shows an auditable pass/fail table rather than a black-box flag, and it is always
phrased as "suspected disabling", never "illegal".

Needs a positions frame with vessel_id, timestamp (epoch s), lat, lon, speed, and
distance_from_shore (metres, from seavigil.enrich).
"""

from __future__ import annotations

import numpy as np
import pandas as pd

NM_M = 1852.0

CAVEATS = [
    "Suspected AIS disabling, not proven and not necessarily illegal.",
    "A gap can also be a receiver outage, satellite coverage hole, or equipment fault.",
    "Reproduces Welch et al. (2022) intentional-disabling criteria; an inspection lead.",
    "AIS identity (MMSI/name) can itself be spoofed; verify against authoritative records.",
]
_METHOD = "AIS gap analysis (Welch et al. 2022 intentional-disabling criteria)"


def _haversine_nm(lon1, lat1, lon2, lat2) -> float:
    r = 6371000.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlmb = np.radians(lon2 - lon1)
    a = np.sin(dphi / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dlmb / 2) ** 2
    return float(2 * r * np.arcsin(np.sqrt(a)) / NM_M)


def build_disabling_dossiers(
    df: pd.DataFrame,
    *,
    min_gap_hours: float = 12.0,
    min_offshore_nm: float = 50.0,
    min_positions_before: int = 14,
    before_window_hours: float = 12.0,
    max_events_per_vessel: int = 2,
    region_label: str = "AIS disabling",
) -> list[dict]:
    """Return dark-gap dossier dicts (type ``ais_disabling``) from continuous tracks."""
    needed = {"vessel_id", "timestamp", "lat", "lon", "distance_from_shore"}
    if not needed.issubset(df.columns):
        raise ValueError(f"missing columns: {needed - set(df.columns)}")

    dossiers: list[dict] = []
    seq = 0
    for mmsi, g in df.groupby("vessel_id"):
        g = g.sort_values("timestamp")
        t = g["timestamp"].to_numpy(dtype="float64")
        lat = g["lat"].to_numpy(dtype="float64")
        lon = g["lon"].to_numpy(dtype="float64")
        dshore = g["distance_from_shore"].to_numpy(dtype="float64")
        name = next((str(v) for v in g.get("ship_name", pd.Series([], dtype=object)) if v), "")
        flag = next((str(v) for v in g.get("flag", pd.Series([], dtype=object)) if v), "")
        n = len(g)
        if n < 2:
            continue
        per_vessel = 0
        for i in range(n - 1):
            gap_h = (t[i + 1] - t[i]) / 3600.0
            off_nm = dshore[i] / NM_M
            before = int(((t > t[i] - before_window_hours * 3600) & (t <= t[i])).sum())
            checks = [
                ("gap >= 12 h", min_gap_hours, round(gap_h, 1), gap_h >= min_gap_hours),
                ("offshore > 50 nm", min_offshore_nm, round(off_nm, 1), off_nm >= min_offshore_nm),
                (f"coverage before (>={min_positions_before} fixes / {before_window_hours:.0f} h)",
                 min_positions_before, before, before >= min_positions_before),
            ]
            if not all(c[3] for c in checks):
                continue
            disp_nm = _haversine_nm(lon[i], lat[i], lon[i + 1], lat[i + 1])
            off_iso = pd.to_datetime(t[i], unit="s", utc=True).strftime("%Y-%m-%dT%H:%M:%SZ")
            on_iso = pd.to_datetime(t[i + 1], unit="s", utc=True).strftime("%Y-%m-%dT%H:%M:%SZ")
            drivers = [
                f"went dark {off_nm:.0f} nm offshore for {gap_h:.1f} h",
                f"reappeared {disp_nm:.0f} nm away",
                f"{before} AIS fixes in the {before_window_hours:.0f} h before going dark "
                "(so not a reception gap)",
            ]
            dossiers.append({
                "type": "ais_disabling",
                "incident_id": f"darkgap__{mmsi}_{seq:04d}",
                "mpa_name": region_label,
                "severity": "high",
                "severity_reason": "suspected intentional AIS disabling offshore",
                "vessel_id": str(mmsi),
                "ship_name": name,
                "flag": flag,
                "ship_type": "Fishing",
                "gear": "AIS gap",
                "time_start_utc": off_iso,
                "time_end_utc": on_iso,
                "duration_hours": round(gap_h, 1),
                "n_positions": n,
                "n_fishing_positions": 0,
                "mean_fishing_proba": None,
                "max_fishing_proba": None,
                "centroid_lat": float(lat[i]),
                "centroid_lon": float(lon[i]),
                "gap_hours": round(gap_h, 1),
                "off_distance_nm": round(off_nm, 1),
                "displacement_nm": round(disp_nm, 1),
                # the dark segment: where it vanished -> where it returned
                "track": [[float(lon[i]), float(lat[i])], [float(lon[i + 1]), float(lat[i + 1])]],
                "criteria": [{"check": c[0], "threshold": c[1], "measured": c[2], "met": c[3]}
                             for c in checks],
                "explanation": {"method": _METHOD, "drivers": drivers},
                "caveats": CAVEATS,
            })
            seq += 1
            per_vessel += 1
            if per_vessel >= max_events_per_vessel:
                break
    return dossiers
