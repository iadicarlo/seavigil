# Incident `great_barrier_reef_marine_park__503000239_0000`

- **MPA:** Great Barrier Reef Marine Park
- **Severity:** LOW (multi-use protected area)  ·  boundary sample-approx-2024
- **EEZ:** Australia EEZ (Australia)  (flag matches coastal state)
- **Vessel:** 🇦🇺 REEF KEEPER  ·  **gear:** unknown
- **When (UTC):** 2026-06-27T13:07:02Z → 2026-06-27T13:07:02Z (0.0 h)
- **Apparent fishing:** 1 of 1 in-MPA positions; mean p=0.65, max p=0.65
- **Where:** -16.783, 145.737 (centroid)
- **Vs. speed baseline:** the trivial rule (speed < 10.7 kn) also flags 100% of these positions; here the speed rule alone suffices.

## Why this was flagged

_mean per-position SHAP (fishing class) over the incident's fishing positions._

| feature | mean value | mean SHAP |
|---|---:|---:|
| `distance_from_port` | 16871.153 | +0.226 |
| `speed_roll_mean` | 0.100 | -0.049 |
| `speed_roll_std` | 0.000 | -0.047 |
| `hour_cos` | -0.958 | -0.026 |
| `distance_from_shore` | 5040.994 | +0.025 |

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
- **Integrity (SHA-256 of canonical facts):** `d7e282979bf6272d8c28242346387b52df71d016fea1029a8ef30f415b3915d5`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
