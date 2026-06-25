"""SHAP explanations for the fishing-behaviour classifier.

Uses shap.TreeExplainer on the trained random forest, evaluated on a sample of
the held-out test set. Produces:
  - a beeswarm summary plot (results/figures/shap_summary.png),
  - the global feature ranking by mean |SHAP|,
  - one or two per-position example explanations (local attributions).

Only the positive-class ("fishing") SHAP values are reported, so a positive
attribution means "this feature pushed the call toward fishing".
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # headless / CPU
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import shap  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "results" / "figures"


def _positive_class_shap(explainer, X):
    """Return SHAP values for the positive class as a (n_samples, n_features) array.

    shap's TreeExplainer on a binary RandomForestClassifier may return either a
    list [neg, pos] or a 3-D array (n, features, classes). Normalize both.
    """
    vals = explainer.shap_values(X, check_additivity=False)
    if isinstance(vals, list):
        return np.asarray(vals[1])
    vals = np.asarray(vals)
    if vals.ndim == 3:
        return vals[:, :, 1]
    return vals


def explain(
    rf,
    X_test: np.ndarray,
    feature_names: list[str],
    *,
    sample_size: int = 2000,
    random_state: int = 42,
):
    """Compute SHAP on a test sample and write the beeswarm plot.

    Returns a dict with the global ranking and example local explanations.
    """
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(random_state)
    n = min(sample_size, len(X_test))
    idx = rng.choice(len(X_test), size=n, replace=False)
    X_sample = X_test[idx]

    explainer = shap.TreeExplainer(rf)
    shap_pos = _positive_class_shap(explainer, X_sample)

    # Global ranking by mean |SHAP|.
    mean_abs = np.abs(shap_pos).mean(axis=0)
    order = np.argsort(mean_abs)[::-1]
    ranking = [
        {"feature": feature_names[i], "mean_abs_shap": float(mean_abs[i])}
        for i in order
    ]

    # Beeswarm summary plot.
    plt.figure()
    shap.summary_plot(
        shap_pos,
        X_sample,
        feature_names=feature_names,
        show=False,
        plot_size=(8, 5),
    )
    plt.title("SHAP summary: drivers of the fishing call (positive class)")
    plt.tight_layout()
    fig_path = FIG_DIR / "shap_summary.png"
    plt.savefig(fig_path, dpi=150, bbox_inches="tight")
    plt.close()

    # Per-position example explanations: pick one confident fishing call and one
    # confident non-fishing call from the sample.
    proba = rf.predict_proba(X_sample)[:, 1]
    examples = []
    for label_name, pos in (("fishing", int(np.argmax(proba))),
                            ("non_fishing", int(np.argmin(proba)))):
        contribs = sorted(
            (
                {"feature": feature_names[j],
                 "value": float(X_sample[pos, j]),
                 "shap": float(shap_pos[pos, j])}
                for j in range(len(feature_names))
            ),
            key=lambda d: abs(d["shap"]),
            reverse=True,
        )
        examples.append(
            {
                "kind": label_name,
                "predicted_fishing_proba": float(proba[pos]),
                "top_contributions": contribs[:5],
            }
        )

    return {
        "figure": str(fig_path),
        "sample_size": int(n),
        "global_ranking": ranking,
        "examples": examples,
    }
