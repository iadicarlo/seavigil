# SeaVigil

**Explainable detection of suspicious fishing activity from vessel movement.**

SeaVigil scores AIS vessel tracks for likely fishing behaviour and flags apparent fishing
inside Marine Protected Areas, with **SHAP** explanations so every flag is auditable. v1 is
the model; a live interactive map follows.

## Why it matters

Illegal, unreported and unregulated (IUU) fishing drains coastal food security and marine
ecosystems. Enforcement agencies do not just need a flag, they need a defensible reason to
act on one. SeaVigil pairs a behaviour model with a per-flag explanation.

## v1 (this stage)

- **Data:** [Global Fishing Watch labeled AIS training data](https://github.com/GlobalFishingWatch/training-data)
  (positions manually labeled fishing vs not, by gear type; Kroodsma et al., Science 2018).
- **Model:** a gradient-boosted classifier predicting fishing from per-position movement
  features (speed, turning rate, time of day, and track context).
- **Explainability:** SHAP showing which behaviours drive each fishing call, globally and
  per vessel.
- **Output:** a fishing-behaviour score, and an example of apparent fishing inside a Marine
  Protected Area.

Runs locally on CPU. No GPU required.

## Reproduce

```bash
uv sync
uv run python -m seavigil.run
```

## Roadmap

- **v2:** anomaly flags (AIS gaps / "going dark", loitering at MPA edges), an interactive
  live map, and dark-vessel detection from satellite imagery.

## Credits

Author: Isma Abdelkader Di Carlo. Vessel data: Global Fishing Watch. License: MIT.
