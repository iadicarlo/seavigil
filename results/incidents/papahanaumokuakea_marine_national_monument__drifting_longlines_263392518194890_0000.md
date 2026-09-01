# Incident `papahanaumokuakea_marine_national_monument__drifting_longlines_263392518194890_0000`

- **MPA:** Papahānaumokuākea Marine National Monument
- **Severity:** HIGH (strict no-take reserve)  ·  boundary sample-approx-2024
- **Vessel:** `drifting_longlines_263392518194890`  ·  **gear:** drifting_longlines
- **When (UTC):** 2014-09-30T21:54:30Z → 2014-09-30T21:54:30Z (0.0 h)
- **Apparent fishing:** 1 of 42 in-MPA positions; mean p=0.53, max p=0.53
- **Where:** 28.225, -163.434 (centroid)
- **Track:** 42 positions, (26.179, -163.897) → (28.225, -163.434)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; the rule agrees on this slow visit, but globally the model beats the speed rule by a wide margin (PR-AUC 0.93 vs 0.40), rejecting slow non-fishing transits and catching fast working passes.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_shore` | 592259.875 | +0.118 |
| `speed_roll_mean` | 10.100 | -0.105 |
| `speed` | 10.100 | -0.094 |
| `distance_from_port` | 626661.562 | +0.087 |
| `speed_roll_std` | 0.245 | +0.036 |

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
- **Integrity (SHA-256 of canonical facts):** `84f51bd875a69a0a8d6d88c6ff512b24f97b33913496ebea215450d85d42723d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
