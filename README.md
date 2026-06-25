# SeaVigil

**An auditable, laptop-deployable triage layer for fishing inside Marine Protected Areas.**

SeaVigil turns vessel-movement signals into a *per-incident, explainable dossier* an
enforcement officer can read, defend, and act on — built to run on a single CPU, with no
cloud account, so an under-resourced coastal authority can actually use it.

It does **not** try to out-detect [Global Fishing Watch](https://globalfishingwatch.org/map)
(GFW). It sits on top of that kind of signal and adds the three things the detection layer
deliberately leaves to others: a **per-flag reason**, an **automated "fishing inside *this*
MPA" alert**, and **deployability on a laptop**.

---

## Why this, and why it's not a GFW clone

Illegal, unreported and unregulated (IUU) fishing drains coastal food security and marine
ecosystems. Detecting apparent fishing from vessel tracks is, at this point, a solved and
industrialised problem — it is GFW's flagship product, trained on labeled AIS data they
released openly. Re-building that is not new.

What is *not* solved is the **last mile**:

- GFW explicitly labels its output **"apparent" fishing effort** and **"not evidence of
  wrongdoing"**, and exposes **no per-position explanation** of *why* a point was called
  fishing.
- GFW supplies all the ingredients for MPA monitoring — fishing effort, MPA boundaries, the
  Marine Manager portal — but **does not ship a turnkey "this vessel is fishing inside this
  MPA, here's the alert" product**.
- Its stack is cloud/GPU/GCP. A fisheries officer in a low-capacity coastal state often
  **cannot run it**.

SeaVigil targets exactly that seam: **explain → alert-in-MPA → hand a human a defensible
dossier**, on hardware they already own.

> **Honest scope.** SeaVigil output is an *inspection-triggering intelligence prompt*, not
> courtroom proof. In fisheries law, encrypted VMS outranks public AIS/SAR, and
> remote-sensing-only prosecutions are rare. SeaVigil tells an officer **where to look and
> why**; it does not convict.

## What it is — and isn't

| | |
|---|---|
| **Is** | An explainable behaviour classifier + an MPA-overlay alerting layer + per-incident dossiers, all CPU-only and reproducible. |
| **Isn't** | A new fishing detector, a dark-vessel (satellite) detector, a real-time global map, or legal evidence. GFW and partners already do those. |
| **Builds on** | GFW's open labeled AIS data and (optionally) GFW's live APIs — as a *complement*, not a competitor. |

## How it works

```
 AIS positions ─▶ movement features ─▶ fishing-behaviour model ─▶ SHAP reason per point
                                                                          │
                          MPA boundaries ──▶ point-in-MPA overlay ◀───────┘
                                                     │
                                                     ▼
                                   per-incident dossier  (who · where · when ·
                                   apparent-fishing score · the SHAP "why")
```

- **v1 — done.** A `scikit-learn` RandomForest predicts *fishing vs. not-fishing per AIS
  position* from interpretable movement features (speed, turning rate, distance from
  shore/port, diel pattern). Evaluated honestly: a **vessel-grouped split** (no vessel in
  both train and test), scored against a tuned **speed-threshold baseline** it must beat,
  with **SHAP** attributions for every call.
- **v2 — building now.** Overlay scored positions onto **Marine Protected Area boundaries**,
  aggregate in-MPA fishing into **incidents**, and emit a **dossier** per incident with its
  SHAP rationale.

See [`docs/DESIGN.md`](docs/DESIGN.md) for the full build sketch, the competitive landscape,
and the implementation plan.

## Status

| Stage | Status |
|---|---|
| v1 per-position fishing classifier + SHAP | ✅ implemented |
| Honest eval (vessel-grouped split, baseline) | ✅ implemented |
| MPA boundary overlay (point-in-polygon) | 🔨 in progress |
| In-MPA incident aggregation | 🔨 in progress |
| Per-incident dossier (JSON + Markdown) | 🔨 in progress |
| Interactive map | ⬜ later |
| GFW live-API ingestion (consume, don't re-detect) | ⬜ later |
| AIS + SAR fusion (dark fleet) | ⬜ later |

## Data

- **Training labels:** [GFW labeled AIS training data](https://github.com/GlobalFishingWatch/training-data)
  — positions hand-labeled fishing vs. not, by gear type (Kroodsma et al., *Science* 2018;
  vessels 2012–2015; trawlers, drifting longlines, purse seines). Licensed **CC BY-NC** —
  **non-commercial**; SeaVigil is a non-commercial / public-good tool accordingly. Raw data
  is **not committed**; the pipeline regenerates it.
- **MPA boundaries:** a small bundled sample of large MPAs for reproducibility; the loader
  accepts any [WDPA](https://www.protectedplanet.net/) MPA polygon set (GeoJSON).
- **Known blind spot:** AIS-only models cannot see the **~75% of industrial fishing vessels
  that don't broadcast AIS** (the "dark fleet", Paolo et al., *Nature* 2024). SeaVigil is
  honest about this; SAR fusion is a later, additive step, not a claim made today.

## Reproduce

```bash
uv sync                              # CPU-only; no GPU
uv run python -m seavigil.run        # v1: train, evaluate, write results/ + SHAP plots
uv run --group dev pytest -q         # smoke tests (no network)
```

Outputs land in `results/` (`metrics.json`, `SUMMARY.md`, `figures/`). The MPA-alerting
entrypoint is documented in `docs/DESIGN.md` as it lands.

## Honest caveats

- Reported metrics are on **unseen vessels**, not unseen rows of seen vessels.
- "Fishing" is defined **behaviourally** from human-labeled AIS, not from catch records; it
  is **apparent** fishing, not proven illegal fishing.
- Labels cover a few gear types and a finite vessel set (2012–2015); class balance varies by
  gear, so PR-AUC is reported alongside ROC-AUC.
- This is a per-position behaviour classifier plus an MPA-overlay layer — **not** a legality
  detector. It produces leads for inspection, not verdicts.

## Credits

Author: Isma Abdelkader Di Carlo. Vessel data: Global Fishing Watch. License: MIT (code).
