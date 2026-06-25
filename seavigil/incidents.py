"""Aggregate in-MPA, model-flagged fishing positions into discrete incidents.

An *incident* is one visit by one vessel to one MPA that contains apparent
fishing: a contiguous run of in-MPA positions (split when the MPA changes or the
time gap exceeds ``gap_minutes``) that includes at least one position the model
flags as fishing. Incidents are the unit a human acts on -- each becomes a dossier
(see ``dossier.py``).

Input: a "scored" positions frame carrying at least::

    vessel_id, gear, timestamp (s), datetime (tz-aware UTC), lat, lon,
    fishing_proba, mpa_idx, mpa_name[, wdpa_id]

with a unique index (so dossiers can pull the model rationale for an incident's
fishing positions by index).
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict, dataclass, field

import numpy as np
import pandas as pd

from seavigil.features import MAX_GAP_MINUTES

DEFAULT_PROBA_THRESHOLD = 0.5
DEFAULT_GAP_MINUTES = MAX_GAP_MINUTES  # 6 h; same tolerance used for movement features


@dataclass
class Incident:
    incident_id: str
    mpa_name: str
    wdpa_id: str | None
    vessel_id: str
    gear: str
    time_start_utc: str
    time_end_utc: str
    duration_hours: float
    n_positions: int          # all in-MPA positions in the visit
    n_fishing_positions: int  # the subset flagged as fishing
    mean_fishing_proba: float
    max_fishing_proba: float
    centroid_lat: float
    centroid_lon: float
    fishing_ids: list = field(default_factory=list)  # index labels of the fishing rows
    mpa_iucn_cat: str | None = None
    mpa_no_take: str | None = None
    mpa_version: str | None = None
    track: list = field(default_factory=list)  # [[lon, lat], ...] over the visit, time-ordered

    def to_dict(self) -> dict:
        d = asdict(self)
        d["fishing_ids"] = list(self.fishing_ids)
        return d


def _slug(text: str) -> str:
    """ASCII, lowercase, underscore-separated slug (handles é, ā, ...)."""
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", ascii_text.lower()).strip("_") or "mpa"


def _opt(run: pd.DataFrame, col: str) -> str | None:
    if col in run.columns:
        v = run[col].iloc[0]
        return str(v) if pd.notna(v) else None
    return None


def _make_incident(run: pd.DataFrame, fish: pd.DataFrame, seq: int) -> Incident:
    mpa_name = str(run["mpa_name"].iloc[0])
    wdpa_id = _opt(run, "wdpa_id")
    vessel_id = str(run["vessel_id"].iloc[0])
    t0, t1 = fish["datetime"].min(), fish["datetime"].max()
    duration_h = float((t1 - t0).total_seconds() / 3600.0)
    trk = run.sort_values("timestamp")
    pts = [[round(float(lo), 5), round(float(la), 5)]
           for lo, la in zip(trk["lon"], trk["lat"])]
    # Downsample to a <=60-point snippet, preserving the first and last fix (shape +
    # correct endpoints) without bloating the artifacts.
    if len(pts) > 60:
        keep = sorted({round(i * (len(pts) - 1) / 59) for i in range(60)})
        pts = [pts[i] for i in keep]
    track = pts
    return Incident(
        incident_id=f"{_slug(mpa_name)}__{vessel_id}_{seq:04d}",
        mpa_name=mpa_name,
        wdpa_id=wdpa_id,
        vessel_id=vessel_id,
        gear=str(run["gear"].iloc[0]) if "gear" in run.columns else "unknown",
        time_start_utc=t0.strftime("%Y-%m-%dT%H:%M:%SZ"),
        time_end_utc=t1.strftime("%Y-%m-%dT%H:%M:%SZ"),
        duration_hours=round(duration_h, 3),
        n_positions=int(len(run)),
        n_fishing_positions=int(len(fish)),
        mean_fishing_proba=float(fish["fishing_proba"].mean()),
        max_fishing_proba=float(fish["fishing_proba"].max()),
        centroid_lat=float(fish["lat"].mean()),
        centroid_lon=float(fish["lon"].mean()),
        fishing_ids=list(fish.index),
        mpa_iucn_cat=_opt(run, "mpa_iucn_cat"),
        mpa_no_take=_opt(run, "mpa_no_take"),
        mpa_version=_opt(run, "mpa_version"),
        track=track,
    )


def build_incidents(
    scored: pd.DataFrame,
    *,
    proba_threshold: float = DEFAULT_PROBA_THRESHOLD,
    gap_minutes: float = DEFAULT_GAP_MINUTES,
    min_fishing_positions: int = 1,
) -> list[Incident]:
    """Segment a scored positions frame into in-MPA fishing incidents.

    A position is "fishing" when ``fishing_proba >= proba_threshold``. A new visit
    starts when the MPA changes or the gap to the previous in-MPA position exceeds
    ``gap_minutes``. A visit becomes an incident when it holds at least
    ``min_fishing_positions`` fishing positions.
    """
    inside = scored[scored["mpa_idx"] >= 0]
    if inside.empty:
        return []

    inside = inside.assign(_fishing=inside["fishing_proba"].to_numpy() >= proba_threshold)

    incidents: list[Incident] = []
    seq_counter: dict[tuple[str, str], int] = {}

    for _, g in inside.groupby("vessel_id", sort=False):
        g = g.sort_values("timestamp")
        ts = g["timestamp"].to_numpy(dtype="float64")
        mpa = g["mpa_idx"].to_numpy()

        gap_min = np.zeros(len(g))
        gap_min[1:] = (ts[1:] - ts[:-1]) / 60.0
        mpa_change = np.zeros(len(g), dtype=bool)
        mpa_change[1:] = mpa[1:] != mpa[:-1]
        new_run = (gap_min > gap_minutes) | mpa_change
        run_id = np.cumsum(new_run)

        for _, run in g.groupby(run_id, sort=False):
            fish = run[run["_fishing"]]
            if len(fish) < min_fishing_positions:
                continue
            key = (str(run["mpa_name"].iloc[0]), str(run["vessel_id"].iloc[0]))
            seq = seq_counter.get(key, 0)
            seq_counter[key] = seq + 1
            incidents.append(_make_incident(run, fish, seq))

    return incidents


def incidents_to_frame(incidents: list[Incident]) -> pd.DataFrame:
    """Tabular summary of incidents (drops the per-row index list)."""
    if not incidents:
        return pd.DataFrame()
    rows = [{k: v for k, v in inc.to_dict().items() if k != "fishing_ids"} for inc in incidents]
    return pd.DataFrame(rows)
