# Dark-vessel detection `sar__australia_eez_outside_mpa_0010`

- **MPA:** Australia EEZ (outside MPA)
- **Severity:** MEDIUM (dark vessel inside national EEZ, outside any protected area)
- **EEZ:** Australia EEZ (Australia)
- **Vessel:** (dark -- no AIS identity)  ·  **source:** SAR (dark)
- **When (UTC):** 2024-06-20T19:44:14Z
- **Length:** n/a  ·  **broadcasting AIS:** no (dark)  ·  **GFW fishing-score:** n/a (Portal-only)
- **Where:** -16.560, 147.040

## Why this was flagged

_SAR detection attributes (no AIS track or identity; not SHAP-explainable)._

- inside national EEZ: Australia EEZ, outside any MPA
- not broadcasting AIS (dark vessel)

## Caveats

- Dark vessel: detected by satellite SAR but not broadcasting AIS.
- Not SHAP-explainable -- a SAR detection has no movement track to attribute.
- length_m and fishing_score are GFW model estimates from imagery, not ground truth.
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.
