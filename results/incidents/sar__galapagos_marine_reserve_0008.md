# Dark-vessel detection `sar__galapagos_marine_reserve_0008`

- **MPA:** Galapagos Marine Reserve (WDPA 11753)
- **Severity:** HIGH (dark vessel inside MPA)  ·  boundary WDPA/WD-OECM Jun2026
- **EEZ:** Galapagos EEZ (Ecuador) (Ecuador)
- **Vessel:** (dark -- no AIS identity)  ·  **source:** SAR (dark)
- **When (UTC):** 2024-01-02T11:42:31Z
- **Length:** n/a  ·  **broadcasting AIS:** no (dark)  ·  **GFW fishing-score:** n/a (Portal-only)
- **Where:** -0.440, -90.800

## Why this was flagged

_SAR detection attributes (no AIS track or identity; not SHAP-explainable)._

- inside MPA: Galapagos Marine Reserve (within Galapagos EEZ (Ecuador))
- not broadcasting AIS (dark vessel)

## Caveats

- Dark vessel: detected by satellite SAR but not broadcasting AIS.
- Not SHAP-explainable -- a SAR detection has no movement track to attribute.
- length_m and fishing_score are GFW model estimates from imagery, not ground truth.
- MPA boundary may be approximate; verify against official WDPA limits.
- An inspection lead, not courtroom evidence.
