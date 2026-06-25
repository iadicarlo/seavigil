"""Smoke tests for the SeaVigil v1 pipeline on small synthetic inputs.

These do not hit the network; they validate the cleaning rules, feature shapes,
the vessel-grouped split invariant, and the baseline logic.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from seavigil import features, model
from seavigil.data import clean


def _synthetic_positions(n_vessels: int = 6, n_per: int = 40) -> pd.DataFrame:
    rng = np.random.default_rng(0)
    rows = []
    base_ts = 1_350_000_000
    for v in range(n_vessels):
        for k in range(n_per):
            fishing = int(rng.random() < 0.5)
            speed = rng.uniform(0, 2) if fishing else rng.uniform(6, 12)
            rows.append(
                {
                    "mmsi": float(100000 + v),
                    "timestamp": float(base_ts + k * 600),
                    "distance_from_shore": float(rng.uniform(0, 5e5)),
                    "distance_from_port": float(rng.uniform(0, 5e5)),
                    "speed": float(speed),
                    "course": float(rng.uniform(0, 360)),
                    "lat": float(rng.uniform(-40, 40)),
                    "lon": float(rng.uniform(-180, 180)),
                    "is_fishing": float(fishing),
                    "gear": "trawlers",
                    "source": "synthetic",
                }
            )
    return pd.DataFrame(rows)


def test_clean_drops_unlabeled_and_binarizes():
    df = _synthetic_positions()
    # Inject unlabeled and fractional rows.
    df.loc[0, "is_fishing"] = -1.0
    df.loc[1, "is_fishing"] = 0.7  # -> 1
    df.loc[2, "is_fishing"] = 0.3  # -> 0
    out = clean(df)
    assert (out["is_fishing"] >= 0).all()
    assert set(out["label"].unique()) <= {0, 1}
    assert "vessel_id" in out.columns
    assert "datetime" in out.columns


def test_features_shape_and_columns():
    out = clean(_synthetic_positions())
    feats = features.build_features(out)
    assert set(features.FEATURE_COLUMNS).issubset(feats.columns)
    assert len(feats) == len(out)
    assert np.isfinite(feats[features.FEATURE_COLUMNS].to_numpy()).all()


def test_vessel_grouped_split_has_no_overlap():
    out = clean(_synthetic_positions())
    feats = features.build_features(out)
    X, y, groups = features.split_xy(feats)
    split = model.vessel_grouped_split(X, y, groups, test_size=0.34)
    train = set(np.unique(split.groups_train))
    test = set(np.unique(split.groups_test))
    assert train.isdisjoint(test)


def test_speed_baseline_predicts_low_speed_as_fishing():
    out = clean(_synthetic_positions())
    feats = features.build_features(out)
    X, y, _ = features.split_xy(feats)
    idx = features.FEATURE_COLUMNS.index("speed")
    base = model.SpeedBaseline(feature_index=idx).fit(X, y)
    assert base.threshold > 0
    # A clearly slow point is predicted fishing, a fast one is not.
    slow = X[np.argmin(X[:, idx])].reshape(1, -1)
    fast = X[np.argmax(X[:, idx])].reshape(1, -1)
    assert base.predict(slow)[0] == 1
    assert base.predict(fast)[0] == 0
