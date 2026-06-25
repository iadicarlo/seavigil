"""Train and evaluate the fishing-behaviour classifier.

Key integrity choices
----------------------
- Split BY VESSEL with GroupShuffleSplit on vessel_id, so no vessel appears in
  both train and test. Per-position rows from one track are highly correlated;
  a random row split would leak and inflate every score. This grouped split is
  the honest evaluation.
- RandomForestClassifier with a fixed seed and class_weight="balanced" (the
  per-gear fishing rate is uneven, e.g. purse seines are mostly non-fishing).
- We compare against a trivial baseline: "fishing if speed < threshold", with
  the threshold tuned on the TRAIN split only, then frozen and scored on test.
  The model has to beat this to justify itself.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    average_precision_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import GroupShuffleSplit

RANDOM_STATE = 42
TEST_SIZE = 0.25


@dataclass
class SplitData:
    X_train: np.ndarray
    X_test: np.ndarray
    y_train: np.ndarray
    y_test: np.ndarray
    groups_train: np.ndarray
    groups_test: np.ndarray


def vessel_grouped_split(
    X: np.ndarray,
    y: np.ndarray,
    groups: np.ndarray,
    *,
    test_size: float = TEST_SIZE,
    random_state: int = RANDOM_STATE,
) -> SplitData:
    """Single train/test split where whole vessels go to one side only."""
    splitter = GroupShuffleSplit(
        n_splits=1, test_size=test_size, random_state=random_state
    )
    train_idx, test_idx = next(splitter.split(X, y, groups))
    return SplitData(
        X_train=X[train_idx],
        X_test=X[test_idx],
        y_train=y[train_idx],
        y_test=y[test_idx],
        groups_train=groups[train_idx],
        groups_test=groups[test_idx],
    )


def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    *,
    n_estimators: int = 300,
    random_state: int = RANDOM_STATE,
) -> RandomForestClassifier:
    """Fit a balanced random forest. Depth left unbounded but leaves regularized."""
    rf = RandomForestClassifier(
        n_estimators=n_estimators,
        class_weight="balanced",
        min_samples_leaf=20,
        max_features="sqrt",
        n_jobs=-1,
        random_state=random_state,
    )
    rf.fit(X_train, y_train)
    return rf


def _classification_metrics(y_true: np.ndarray, y_pred: np.ndarray, y_score=None) -> dict:
    out = {
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
        "n": int(len(y_true)),
        "positive_rate": float(np.mean(y_true)),
    }
    if y_score is not None:
        out["roc_auc"] = float(roc_auc_score(y_true, y_score))
        out["pr_auc"] = float(average_precision_score(y_true, y_score))
    return out


def evaluate_model(
    rf: RandomForestClassifier, X_test: np.ndarray, y_test: np.ndarray
) -> dict:
    """Probabilistic + thresholded metrics on the held-out vessels."""
    proba = rf.predict_proba(X_test)[:, 1]
    pred = (proba >= 0.5).astype(int)
    return _classification_metrics(y_test, pred, y_score=proba)


@dataclass
class SpeedBaseline:
    """Trivial rule: predict fishing when speed < threshold.

    The threshold is chosen on TRAIN to maximize F1, then frozen.
    """

    feature_index: int
    threshold: float = field(default=0.0)

    def fit(self, X_train: np.ndarray, y_train: np.ndarray) -> "SpeedBaseline":
        speed = X_train[:, self.feature_index]
        # Candidate thresholds across the observed speed range.
        candidates = np.quantile(speed, np.linspace(0.01, 0.99, 99))
        best_thr, best_f1 = candidates[0], -1.0
        for thr in candidates:
            pred = (speed < thr).astype(int)
            f1 = f1_score(y_train, pred, zero_division=0)
            if f1 > best_f1:
                best_f1, best_thr = f1, float(thr)
        self.threshold = best_thr
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        return (X[:, self.feature_index] < self.threshold).astype(int)

    def score(self, X: np.ndarray) -> np.ndarray:
        """A monotone score for AUC: lower speed -> higher fishing score."""
        return -X[:, self.feature_index]


def evaluate_baseline(
    baseline: SpeedBaseline, X_test: np.ndarray, y_test: np.ndarray
) -> dict:
    pred = baseline.predict(X_test)
    score = baseline.score(X_test)
    metrics = _classification_metrics(y_test, pred, y_score=score)
    metrics["threshold_knots"] = float(baseline.threshold)
    return metrics


def beats_baseline(model_metrics: dict, baseline_metrics: dict) -> dict:
    """Report whether the model beats the baseline on the headline metrics."""
    keys = ["roc_auc", "pr_auc", "f1", "precision", "recall"]
    deltas = {k: model_metrics[k] - baseline_metrics[k] for k in keys}
    return {
        "deltas": deltas,
        "model_beats_baseline_pr_auc": bool(deltas["pr_auc"] > 0),
        "model_beats_baseline_roc_auc": bool(deltas["roc_auc"] > 0),
        "model_beats_baseline_f1": bool(deltas["f1"] > 0),
    }
