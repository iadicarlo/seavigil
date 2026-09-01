# Incident `phoenix_islands_protected_area__drifting_longlines_251022003811177_0010`

- **MPA:** Phoenix Islands Protected Area
- **Severity:** HIGH (strict no-take reserve)  ·  boundary sample-approx-2024
- **EEZ:** Kiribati Exclusive Economic Zone (Phoenix Group) (Kiribati)
- **Vessel:** `drifting_longlines_251022003811177`  ·  **gear:** drifting_longlines
- **When (UTC):** 2014-12-13T06:48:46Z → 2014-12-13T10:52:38Z (4.064 h)
- **Apparent fishing:** 146 of 148 in-MPA positions; mean p=0.88, max p=0.98
- **Where:** -3.482, -171.037 (centroid)
- **Track:** 148 positions, (-3.494, -171.139) → (-3.472, -170.928)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; the rule agrees on this slow visit, but globally the model beats the speed rule by a wide margin (PR-AUC 0.93 vs 0.40), rejecting slow non-fishing transits and catching fast working passes.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions (sampled 50 of 146)._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `speed_roll_mean` | 4.314 | +0.161 |
| `speed` | 4.352 | +0.140 |
| `speed_roll_std` | 0.752 | +0.036 |
| `distance_from_shore` | 37393.766 | +0.027 |
| `hour_cos` | -0.660 | +0.012 |

## Could be innocent

Apparent-fishing movement can also be slow transit or drifting; the model rejects most such cases but not all.

## Caveats

- Apparent fishing inferred from AIS movement, not proven illegal fishing.
- AIS-only: blind to vessels not broadcasting AIS (~75% of industrial fishing vessels).
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.

## Provenance & integrity

- Global Fishing Watch labelled AIS training data (Kroodsma et al., Science 2018). CC BY 4.0.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Model confidence:** Fishing probabilities are well-calibrated (Brier 0.0915 on 408,194 held-out positions from vessels not seen in training); read the score as a probability.
- **Integrity (SHA-256 of canonical facts):** `a9540bfe39f805864e6163d4d0e5f1761e0ce63ecf5de15ad437f399c92c1b81`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
