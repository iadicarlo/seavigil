# Incident `phoenix_islands_protected_area__drifting_longlines_271347251834362_0001`

- **MPA:** Phoenix Islands Protected Area
- **Severity:** HIGH (strict no-take reserve)  ·  boundary sample-approx-2024
- **EEZ:** Kiribati Exclusive Economic Zone (Phoenix Group) (Kiribati)
- **Vessel:** `drifting_longlines_271347251834362`  ·  **gear:** drifting_longlines
- **When (UTC):** 2014-06-21T02:01:39Z → 2014-06-26T01:02:46Z (119.019 h)
- **Apparent fishing:** 731 of 1004 in-MPA positions; mean p=0.89, max p=1.00
- **Where:** -3.027, -171.336 (centroid)
- **Track:** 1004 positions, (-4.507, -173.447) → (-2.523, -171.385)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; the rule agrees on this slow visit, but globally the model beats the speed rule by a wide margin (PR-AUC 0.93 vs 0.40), rejecting slow non-fishing transits and catching fast working passes.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions (sampled 50 of 731)._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `speed_roll_mean` | 5.264 | +0.103 |
| `speed` | 5.256 | +0.088 |
| `distance_from_shore` | 96669.660 | +0.080 |
| `distance_from_port` | 182832.064 | +0.043 |
| `hour_cos` | -0.091 | +0.030 |

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
- **Integrity (SHA-256 of canonical facts):** `5be3d7249836687a3c133674da23a03aa45884c057d2e628a316e93737f32f4c`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
