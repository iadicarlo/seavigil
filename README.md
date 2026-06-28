# SeaVigil

**The explanation-and-evidence layer for illegal-fishing behaviors in protected and national waters.**

SeaVigil turns vessel-movement signals into a *per-incident, explainable dossier* an
enforcement officer can read, defend, and act on - built to run on a single CPU, with no
cloud account, so an under-resourced coastal authority can actually use it.

It does not try to re-detect fishing (that is Global Fishing Watch's solved, industrial-scale
job). It sits on top of monitoring and explains and evidences the *illegal behaviors* that
matter: apparent fishing inside a Marine Protected Area, fishing or a dark (non-broadcasting)
vessel inside a coastal state's Exclusive Economic Zone, and (in progress) vessels that go
dark or meet at sea to tranship. SeaVigil computes the AIS behaviors itself and consumes
GFW's published Sentinel-1 SAR detections for the dark fleet; every flag carries its reason.

It does **not** try to out-detect [Global Fishing Watch](https://globalfishingwatch.org/map)
(GFW), and it does **not** claim to have invented MPA-incursion alerting - **Skylight**
(Allen Institute for AI) already ships real-time MPA-entry and dark-vessel alerts, free, to
70+ countries. What no one ships is the **last mile for a low-capacity authority**: SeaVigil
adds a **per-flag, SHAP-backed reason** for every call, runs **offline on a laptop with no
cloud account**, and produces an **auditable per-incident dossier**. The alert itself is a
commodity it packages - not a thing it claims to have invented.

---

## Why this, and why it's not a GFW clone

Illegal, unreported and unregulated (IUU) fishing drains coastal food security and marine
ecosystems. Detecting apparent fishing from vessel tracks is, at this point, a solved and
industrialised problem - it is GFW's flagship product, trained on labeled AIS data they
released openly. Re-building that is not new.

What is *not* solved is the **last mile for an under-resourced authority**:

- No IUU-fishing tool exposes a **per-flag explanation _of the fishing detection itself_** - a
  SHAP / feature attribution for *why this position scored as fishing*. GFW labels its output
  **"apparent"** with no per-position *why*; others surface a scalar score, which is not an
  attribution. (Windward explains *risk / anomalies*, not the detection; verified mid-2026.)
- The incumbents are all **cloud platforms or managed services that need an account**: GFW's
  stack is cloud/GPU; **Skylight** is free but requires a vetted login; **Starboard** and
  **OceanMind** are paid/enterprise. An officer who can't depend on a foreign-hosted account
  **can't run any of them**.

SeaVigil targets exactly that seam: **explain → flag-in-MPA → hand a human a defensible
dossier**, offline, on hardware they already own. The MPA *alert* is a commodity (Skylight
does it free); what SeaVigil adds is the **reason** and the **offline, auditable dossier**.

> **Honest scope.** SeaVigil output is an *inspection-triggering intelligence prompt*, not
> courtroom proof. In fisheries law, encrypted VMS outranks public AIS/SAR, and
> remote-sensing-only prosecutions are rare. SeaVigil tells an officer **where to look and
> why**; it does not convict.

## What it is - and isn't

| | |
|---|---|
| **Is** | An explainable behaviour classifier + an MPA-overlay alerting layer + per-incident dossiers, all CPU-only and reproducible. |
| **Isn't** | A new fishing detector, a dark-vessel (satellite) detector, a real-time global map, or legal evidence. GFW and partners already do those. |
| **Builds on** | GFW's open labeled AIS data and (optionally) GFW's live APIs - as a *complement*, not a competitor. |

## Compared to other tools

Detection - and even MPA-incursion alerting - is **already shipped**. SeaVigil does not
reinvent it; the wedge is the two right-hand columns.

| Tool | MPA-entry / dark-vessel alerts | Per-flag explanation | Offline / no account |
|---|---|---|---|
| **Skylight** (Allen Institute) | ✅ free, 70+ countries | ❌ | ❌ vetted account, cloud |
| **Starboard** | ✅ paid | ❌ | ❌ enterprise SaaS |
| **OceanMind** | ✅ managed service | ❌ (human analysts) | ❌ |
| **Global Fishing Watch** | ❌ data/portal, no alerts | ❌ | ❌ cloud / API |
| **SeaVigil** | packages, doesn't claim | ✅ **SHAP per flag** | ✅ **laptop, no account** |

"Per-flag explanation" = a SHAP / feature attribution **of the fishing detection itself** - a
scalar confidence score isn't one. Verified June 2026; GFW's risk-indicator layer reaches the
public map ~Oct 2026, so re-check before then. See [`docs/DEPLOY.md`](docs/DEPLOY.md).

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

- **v1 - done.** A `scikit-learn` RandomForest predicts *fishing vs. not-fishing per AIS
  position* from interpretable movement features (speed, turning rate, distance from
  shore/port, diel pattern). Evaluated honestly: a **vessel-grouped split** (no vessel in
  both train and test), scored against a tuned **speed-threshold baseline** it must beat,
  with **SHAP** attributions for every call.
- **v2 - building now.** Overlay scored positions onto **Marine Protected Area boundaries**,
  aggregate in-MPA fishing into **incidents**, and emit a **dossier** per incident with its
  SHAP rationale.

See [`docs/DESIGN.md`](docs/DESIGN.md) for the full build sketch, the competitive landscape,
and the implementation plan.

## Status

| Stage | Status |
|---|---|
| v1 per-position fishing classifier + SHAP | ✅ implemented |
| Honest eval (vessel-grouped split, baseline) | ✅ implemented |
| MPA boundary overlay (point-in-polygon) | ✅ implemented |
| In-MPA incident aggregation | ✅ implemented |
| Per-incident dossier (JSON + Markdown) | ✅ implemented |
| Dark-fleet SAR dossiers (consume GFW detections; no imagery) | ✅ implemented |
| Interactive static map (MapLibre, GitHub Pages) | ✅ implemented |
| Score your own AIS/VMS feed (`--positions`, offline) | ✅ implemented |
| Live GFW SAR ingestion (`fetch_gfw`, real dark-fleet) | ✅ implemented |
| WDPA severity grading (no-take / IUCN) + boundary versioning | ✅ implemented |
| Baseline comparison + track snippet + full dossier view in map | ✅ implemented |
| Real WDPA via GEE export (`scripts/wdpa_from_gee.py`) | ✅ implemented |
| Distance enrichment - raw AIS feed → scorable (`seavigil.enrich`) | ✅ implemented |
| Open-AIS fetch + verified out-of-sample run (`scripts/fetch_open_ais.py`) | ✅ implemented |
| Near-real-time AIS stream (`scripts/fetch_live_ais.py`, aisstream.io) | ✅ implemented |
| Real WDPA boundaries on the map as non-extractable tiles (`web/tiles/mpas.pmtiles`) | ✅ implemented |
| Dark 3D-globe map (MapLibre GL 5): glowing AIS/SAR, layer toggles, jump-to-MPA, SHAP dossier | ✅ implemented |
| Logo + favicon + responsive UI (mobile/tablet/desktop) | ✅ implemented |
| **Live site**: https://iadicarlo.github.io/seavigil | ✅ deployed |
| UNEP-WCMC goodwill notice for the non-commercial WDPA layer | ⬜ optional (your action) |

## Data

- **Training labels:** [GFW labeled AIS training data](https://github.com/GlobalFishingWatch/training-data)
  - positions hand-labeled fishing vs. not, by gear type (Kroodsma et al., *Science* 2018;
  vessels 2012-2015; trawlers, drifting longlines, purse seines). Licensed **CC BY 4.0**
  (attribution; commercial use permitted). Raw data is **not committed**; the pipeline
  regenerates it.
- **MPA boundaries:** the public map shows the **real WDPA polygons** for the five showcase
  reserves (Galapagos, Great Barrier Reef with its IUCN zones, Phoenix Islands, Papahanaumokuakea,
  Rapa Nui), extracted from the Protected Planet marine `.gdb` by `scripts/extract_showcase_mpas.py`,
  simplified, and shipped as **non-extractable vector tiles** (`web/tiles/mpas.pmtiles`, via
  tippecanoe). The loader still accepts any [WDPA / WD-OECM](https://www.protectedplanet.net/)
  GeoJSON for offline detection (full-resolution source kept gitignored).
  **Note:** WDPA/WD-OECM is **non-commercial** and may not be redistributed as a downloadable
  web map - it is shown for display only under the Protected Planet Terms of Use, with a clickable
  credit, never as raw GeoJSON. **Citation:** UNEP-WCMC and
  IUCN (2026), Protected Planet: The World Database on Protected Areas (WDPA) and World
  Database on Other Effective Area-based Conservation Measures (WD-OECM), June 2026,
  Cambridge, UK: UNEP-WCMC and IUCN, www.protectedplanet.net.
- **Known blind spot:** AIS-only models cannot see the **~75% of industrial fishing vessels
  that don't broadcast AIS** (the "dark fleet", Paolo et al., *Nature* 2024). The fix is to
  *consume* GFW's already-published Sentinel-1 SAR detections (no imagery processing needed) -
  but those are **CC BY-NC** (non-commercial), so adding the dark fleet binds SeaVigil to
  non-commercial use. See [`docs/DESIGN.md`](docs/DESIGN.md) §6.5.

## Reproduce

```bash
uv sync                              # CPU-only; no GPU
uv run python -m seavigil.run        # v1: train, evaluate, write results/ + SHAP plots
uv run python -m seavigil.alert      # v2: fishing-in-MPA incidents + dossiers (~90 s, full set)
uv run --group dev pytest -q         # tests (no network)
```

`seavigil.alert` scores held-out test vessels by default (out-of-sample); `--scope all` scores
everything (in-sample, for a fuller demonstration), `--mpa <wdpa.geojson>` swaps the
approximate sample boundaries for real ones, and `--sample-sar` (or `--sar <detections.geojson>`)
adds **dark-fleet** dossiers from SAR detections. Outputs land in `results/` (v1: `metrics.json`,
`SUMMARY.md`, `figures/`; v2: `results/incidents/` with `INDEX.md`, `incidents.json`, and one
dossier per record - AIS incidents carry a SHAP "why"; dark-vessel SAR detections carry an
attribute rationale instead, because a radar blip has no movement track to explain).

A committed sample (`results/incidents/`) shows the mechanism end-to-end: 24 apparent-fishing
AIS incidents (2013-2014 labels) re-validated against the **real WDPA boundaries** plus 45 real
GFW Sentinel-1 **dark-vessel** SAR detections (2024) inside the Great Barrier Reef and Galapagos,
graded by the actual IUCN zone (a dark vessel in a no-take zone reads as high severity). It is
**illustrative** - a curated sample, in-sample AIS scores, and "apparent" (era- and rule-dependent)
fishing, not a finding of illegality.

### Your own data + live dark fleet

```bash
# Score YOUR OWN AIS/VMS feed (offline; no account). See data/positions/README.md.
uv run python -m seavigil.alert --positions data/positions/sample_positions.csv --sample-sar

# Pull REAL GFW Sentinel-1 SAR detections (dark fleet) for the MPAs, then score:
export GFW_TOKEN=...                         # free non-commercial token; kept in .env (gitignored)
uv run python -m seavigil.fetch_gfw --date-range 2024-01-01,2025-01-01
uv run python -m seavigil.alert --positions <your_ais.csv> --sar data/sar/gfw_sar_detections.geojson
```

The model is trained on the GFW labels and runs inference on whatever positions you give it -
GFW does **not** publish raw AIS, so per-position scoring uses your own feed, while the **dark
fleet** comes from GFW's published SAR detections (`fetch_gfw`, CC BY-NC; raw pulls are
gitignored - regenerate with your token). Verified live: ~6,200 detections / ~1,100 dark inside
the sample MPAs over 2024.

## Honest caveats

- Reported metrics are on **unseen vessels**, not unseen rows of seen vessels.
- "Fishing" is defined **behaviourally** from human-labeled AIS, not from catch records; it
  is **apparent** fishing, not proven illegal fishing.
- Labels cover a few gear types and a finite vessel set (2012-2015); class balance varies by
  gear, so PR-AUC is reported alongside ROC-AUC.
- This is a per-position behaviour classifier plus an MPA-overlay layer - **not** a legality
  detector. It produces leads for inspection, not verdicts.

## Credits

Author: Isma Abdelkader Di Carlo. Vessel data: Global Fishing Watch. License: MIT (code).
