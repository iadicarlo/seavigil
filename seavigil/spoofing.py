"""Detect AIS identity spoofing from position anomalies in AIS tracks.

Some vessels broadcast a false position, or two vessels share one MMSI, to hide who
is where. Both show up as physically impossible movement for a single MMSI: a fix
that implies hundreds of knots, or two fixes at the same instant far apart. A single
such jump can be a bad GPS fix, so SeaVigil only flags an MMSI with several anomalies
(a sustained pattern), and reports the evidence (count, fastest implied speed, spatial
spread) so the dossier is auditable. It says "suspected AIS spoofing or MMSI conflict",
never "illegal", because the cause (deliberate spoofing, MMSI collision, or equipment
fault) is for an investigator to resolve.

Detectable from any AIS feed, including terrestrial (e.g. NOAA Marine Cadastre), unlike
going-dark which needs satellite AIS to tell disabling from out-of-range.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

NM_M = 1852.0

CAVEATS = [
    "Suspected AIS spoofing or MMSI conflict, not proven and not necessarily illegal.",
    "Could also be a faulty GPS/transceiver or a transcription error in the feed.",
    "Flagged only on a sustained pattern (several anomalies), not a single bad fix.",
    "An inspection lead: confirm the vessel identity against authoritative records.",
]
_METHOD = "AIS position-anomaly analysis (impossible-speed jumps and same-instant conflicts)"


def _haversine_nm(lon1, lat1, lon2, lat2) -> float:
    r = 6371000.0
    p1, p2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlmb = np.radians(lon2 - lon1)
    a = np.sin(dphi / 2) ** 2 + np.cos(p1) * np.cos(p2) * np.sin(dlmb / 2) ** 2
    return float(2 * r * np.arcsin(np.sqrt(a)) / NM_M)


def build_spoofing_dossiers(
    df: pd.DataFrame,
    *,
    max_speed_kn: float = 60.0,
    min_jump_nm: float = 2.0,
    dt_max_hours: float = 2.0,
    min_anomalies: int = 3,
    region_label: str = "AIS spoofing",
) -> list[dict]:
    """Return suspected-spoofing dossier dicts (type ``ais_spoofing``) from AIS tracks."""
    needed = {"vessel_id", "timestamp", "lat", "lon"}
    if not needed.issubset(df.columns):
        raise ValueError(f"missing columns: {needed - set(df.columns)}")

    dossiers: list[dict] = []
    seq = 0
    for mmsi, g in df.groupby("vessel_id"):
        g = g.sort_values("timestamp")
        t = g["timestamp"].to_numpy(dtype="float64")
        lat = g["lat"].to_numpy(dtype="float64")
        lon = g["lon"].to_numpy(dtype="float64")
        if len(g) < 3:
            continue

        impossible = 0          # implied speed over threshold
        same_instant = 0        # two fixes same second, far apart (MMSI conflict)
        max_speed = 0.0
        worst = None            # (lon1, lat1, lon2, lat2) of the largest jump
        max_jump_nm = 0.0
        for i in range(len(g) - 1):
            d = _haversine_nm(lon[i], lat[i], lon[i + 1], lat[i + 1])
            if d < min_jump_nm:
                continue
            dt_h = (t[i + 1] - t[i]) / 3600.0
            if dt_h <= 0:
                same_instant += 1
            elif dt_h <= dt_max_hours:
                sp = d / dt_h
                if sp > max_speed_kn:
                    impossible += 1
                    max_speed = max(max_speed, sp)
                else:
                    continue
            else:
                continue
            if d > max_jump_nm:
                max_jump_nm = d
                worst = (lon[i], lat[i], lon[i + 1], lat[i + 1])

        anomalies = impossible + same_instant
        if anomalies < min_anomalies or worst is None:
            continue

        name = next((str(v) for v in g.get("ship_name", pd.Series([], dtype=object)) if v), "")
        flag = next((str(v) for v in g.get("flag", pd.Series([], dtype=object)) if v), "")
        # report position = the median fix (the spoof has the vessel in several places)
        clat, clon = float(np.median(lat)), float(np.median(lon))
        spread_nm = _haversine_nm(float(lon.min()), float(lat.min()),
                                  float(lon.max()), float(lat.max()))
        drivers = [
            f"{anomalies} physically impossible movements for one MMSI",
            (f"fastest implied speed {max_speed:,.0f} kn (a vessel cannot move this fast)"
             if max_speed else f"{same_instant} same-instant fixes far apart"),
            f"positions span {spread_nm:,.0f} nm" + (
                f", including {same_instant} same-instant conflicts (two vessels, one MMSI)"
                if same_instant else ""),
        ]
        dossiers.append({
            "type": "ais_spoofing",
            "incident_id": f"spoof__{mmsi}_{seq:04d}",
            "mpa_name": region_label,
            "severity": "high" if same_instant else "medium",
            "severity_reason": ("same-MMSI conflict (two vessels broadcasting one identity)"
                                if same_instant else "impossible-speed position jumps"),
            "vessel_id": str(mmsi),
            "ship_name": name,
            "flag": flag,
            "ship_type": "Fishing",
            "gear": "AIS anomaly",
            "time_start_utc": pd.to_datetime(t[0], unit="s", utc=True).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "time_end_utc": pd.to_datetime(t[-1], unit="s", utc=True).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "duration_hours": round((t[-1] - t[0]) / 3600.0, 1),
            "n_positions": int(len(g)),
            "n_fishing_positions": 0,
            "mean_fishing_proba": None,
            "max_fishing_proba": None,
            "centroid_lat": clat,
            "centroid_lon": clon,
            "anomaly_count": int(anomalies),
            "max_implied_speed_kn": round(max_speed, 0),
            "spread_nm": round(spread_nm, 0),
            "track": [[float(worst[0]), float(worst[1])], [float(worst[2]), float(worst[3])]],
            "explanation": {"method": _METHOD, "drivers": drivers},
            "caveats": CAVEATS,
        })
        seq += 1
    return dossiers
