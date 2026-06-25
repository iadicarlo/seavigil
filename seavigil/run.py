"""End-to-end SeaVigil v1 pipeline.

Run with:  uv run python -m seavigil.run

Steps:
  1. download + load + clean GFW labeled positions,
  2. build interpretable movement features,
  3. vessel-grouped train/test split,
  4. train the random forest + tune the speed baseline,
  5. evaluate both on held-out vessels,
  6. SHAP explanations on a test sample,
  7. write results/metrics.json and results/SUMMARY.md.
"""

from __future__ import annotations

import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import sklearn

from seavigil import data, explain, features, model

ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
FIG_DIR = RESULTS / "figures"


def _vessel_counts(groups_train, groups_test) -> dict:
    return {
        "train_vessels": int(len(np.unique(groups_train))),
        "test_vessels": int(len(np.unique(groups_test))),
        "vessel_overlap": int(
            len(set(np.unique(groups_train)) & set(np.unique(groups_test)))
        ),
    }


def main() -> dict:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    print("[run] 1/7 loading + cleaning data ...")
    clean = data.load_clean()

    print("[run] 2/7 building features ...")
    feats = features.build_features(clean)
    X, y, groups = features.split_xy(feats)

    print("[run] 3/7 vessel-grouped split ...")
    split = model.vessel_grouped_split(X, y, groups)
    vessel_info = _vessel_counts(split.groups_train, split.groups_test)
    assert vessel_info["vessel_overlap"] == 0, "vessel leak between train and test"

    print("[run] 4/7 training random forest + tuning baseline ...")
    rf = model.train_model(split.X_train, split.y_train)
    speed_idx = features.FEATURE_COLUMNS.index("speed")
    baseline = model.SpeedBaseline(feature_index=speed_idx).fit(
        split.X_train, split.y_train
    )

    print("[run] 5/7 evaluating on held-out vessels ...")
    model_metrics = model.evaluate_model(rf, split.X_test, split.y_test)
    baseline_metrics = model.evaluate_baseline(baseline, split.X_test, split.y_test)
    comparison = model.beats_baseline(model_metrics, baseline_metrics)

    print("[run] 6/7 SHAP explanations ...")
    shap_out = explain.explain(rf, split.X_test, features.FEATURE_COLUMNS)

    print("[run] 7/7 writing results ...")
    importances = {
        name: float(imp)
        for name, imp in zip(features.FEATURE_COLUMNS, rf.feature_importances_)
    }

    metrics = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "data_source": {
            "name": "Global Fishing Watch labeled AIS training data",
            "repo": "https://github.com/GlobalFishingWatch/training-data",
            "reference": "Kroodsma et al., Science 2018",
            "gears": data.DEFAULT_GEARS,
            "license": "CC BY 4.0",
        },
        "dataset": {
            "n_positions": int(len(feats)),
            "n_vessels": int(feats["vessel_id"].nunique()),
            "overall_fishing_rate": float(feats["label"].mean()),
            "per_gear_fishing_rate": {
                g: float(v)
                for g, v in feats.groupby("gear")["label"].mean().items()
            },
            "per_gear_positions": {
                g: int(v)
                for g, v in feats.groupby("gear")["label"].count().items()
            },
        },
        "split": {
            "type": "GroupShuffleSplit on vessel_id",
            "test_size": model.TEST_SIZE,
            "random_state": model.RANDOM_STATE,
            **vessel_info,
        },
        "model": {
            "type": "RandomForestClassifier",
            "params": {
                "n_estimators": rf.n_estimators,
                "class_weight": "balanced",
                "min_samples_leaf": 20,
                "max_features": "sqrt",
                "random_state": model.RANDOM_STATE,
            },
            "feature_columns": features.FEATURE_COLUMNS,
            "feature_importances": importances,
            "test_metrics": model_metrics,
        },
        "baseline": {
            "type": "speed threshold (fishing if speed < threshold)",
            "tuned_on": "train (max F1)",
            "test_metrics": baseline_metrics,
        },
        "comparison": comparison,
        "shap": {
            "method": "TreeExplainer (positive class)",
            "sample_size": shap_out["sample_size"],
            "figure": "results/figures/shap_summary.png",
            "global_ranking": shap_out["global_ranking"],
            "examples": shap_out["examples"],
        },
        "environment": {
            "python": platform.python_version(),
            "scikit_learn": sklearn.__version__,
        },
    }

    (RESULTS / "metrics.json").write_text(json.dumps(metrics, indent=2))
    _write_summary(metrics)

    print("\n[run] done.")
    print(f"  model  ROC-AUC={model_metrics['roc_auc']:.3f}  "
          f"PR-AUC={model_metrics['pr_auc']:.3f}  F1={model_metrics['f1']:.3f}")
    print(f"  base   ROC-AUC={baseline_metrics['roc_auc']:.3f}  "
          f"PR-AUC={baseline_metrics['pr_auc']:.3f}  F1={baseline_metrics['f1']:.3f}")
    return metrics


def _fmt_pct(x: float) -> str:
    return f"{100 * x:.1f}%"


def _write_summary(m: dict) -> None:
    md = m["model"]["test_metrics"]
    bd = m["baseline"]["test_metrics"]
    ds = m["dataset"]
    sp = m["split"]

    top_shap = m["shap"]["global_ranking"][:5]
    shap_rows = "\n".join(
        f"| {i + 1} | `{r['feature']}` | {r['mean_abs_shap']:.4f} |"
        for i, r in enumerate(top_shap)
    )

    gear_rows = "\n".join(
        f"| {g} | {ds['per_gear_positions'][g]:,} | {_fmt_pct(rate)} |"
        for g, rate in ds["per_gear_fishing_rate"].items()
    )

    def ex_block(ex: dict) -> str:
        rows = "\n".join(
            f"  - `{c['feature']}` = {c['value']:.3f}  (SHAP {c['shap']:+.3f})"
            for c in ex["top_contributions"]
        )
        return (
            f"- **{ex['kind']}** (predicted fishing probability "
            f"{ex['predicted_fishing_proba']:.3f}); top drivers:\n{rows}"
        )

    examples_md = "\n".join(ex_block(e) for e in m["shap"]["examples"])

    beats = m["comparison"]
    verdict = (
        "The model beats the speed baseline on every headline metric."
        if all(
            beats[k]
            for k in (
                "model_beats_baseline_pr_auc",
                "model_beats_baseline_roc_auc",
                "model_beats_baseline_f1",
            )
        )
        else "The model does not beat the baseline on all metrics; see deltas below."
    )

    text = f"""# SeaVigil v1 - results summary

Generated {m['generated_utc']}.

SeaVigil v1 classifies whether an AIS vessel position is **fishing** or **not
fishing**, from per-position movement behaviour, with SHAP explanations so each
call is auditable.

## Data

- Source: **Global Fishing Watch** labeled AIS training data
  (https://github.com/GlobalFishingWatch/training-data), manually labeled
  fishing vs. not by gear type. Reference: Kroodsma et al., Science 2018.
  Licensed CC BY 4.0. Raw data is not committed (regenerated by the pipeline).
- Gears used: {", ".join(m['data_source']['gears'])}.
- Labeled positions: **{ds['n_positions']:,}** across **{ds['n_vessels']}**
  distinct vessels.
- Overall fishing rate: **{_fmt_pct(ds['overall_fishing_rate'])}**.

| gear | positions | fishing rate |
|------|-----------|--------------|
{gear_rows}

## Evaluation protocol

- **Vessel-grouped split** ({sp['type']}): whole vessels go to either train or
  test, never both. Per-position rows within one track are highly correlated, so
  a random row split would leak and inflate scores. Train vessels:
  **{sp['train_vessels']}**, test vessels: **{sp['test_vessels']}**, overlap:
  **{sp['vessel_overlap']}**.
- Held-out test positions: **{md['n']:,}** (test fishing rate
  {_fmt_pct(md['positive_rate'])}).

## Held-out metrics

| metric | model (random forest) | speed baseline |
|--------|----------------------:|---------------:|
| ROC-AUC | **{md['roc_auc']:.3f}** | {bd['roc_auc']:.3f} |
| PR-AUC (average precision) | **{md['pr_auc']:.3f}** | {bd['pr_auc']:.3f} |
| precision | **{md['precision']:.3f}** | {bd['precision']:.3f} |
| recall | **{md['recall']:.3f}** | {bd['recall']:.3f} |
| F1 | **{md['f1']:.3f}** | {bd['f1']:.3f} |

Confusion matrix (model, rows = true [not, fishing], cols = predicted):
`{md['confusion_matrix']}`

**Baseline:** "fishing if speed < {bd['threshold_knots']:.2f} knots", with the
threshold tuned on train for maximum F1, then frozen. {verdict}

## Top features by mean |SHAP|

| rank | feature | mean abs SHAP |
|------|---------|---------------|
{shap_rows}

SHAP beeswarm: `results/figures/shap_summary.png` (computed on a
{m['shap']['sample_size']}-position sample of held-out vessels).

## Example per-position explanations

{examples_md}

## Honest caveats

- **Vessel-grouped split** is enforced (zero vessel overlap); reported metrics
  are on unseen vessels, not unseen rows of seen vessels.
- **Class balance** varies by gear: purse seines are mostly non-fishing while
  drifting longlines are mostly fishing. We use `class_weight="balanced"` and
  report PR-AUC alongside ROC-AUC for this reason.
- **Baseline comparison** is included so the model has to earn its complexity
  against a one-line speed rule.
- **GFW label caveats**: labels are human annotations (some crowd-sourced and
  averaged, hence fractional values binarized at 0.5); annotators can disagree,
  and "fishing" is defined behaviourally, not from catch records. Coverage is
  limited to a few gear types and a finite set of vessels (2012-2015).
- This is a **per-position behaviour classifier**, not an IUU / legality
  detector; mapping fishing behaviour to Marine Protected Areas is future work.
- Data credited to **Global Fishing Watch**.
"""
    (RESULTS / "SUMMARY.md").write_text(text)


if __name__ == "__main__":
    main()
