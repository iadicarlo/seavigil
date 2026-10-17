# Incident `live_ais__56a9a462ba386e`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Mauritian Exclusive Economic Zone (Republic of Mauritius) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇲🇹 PS FRAMURA  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-07T11:33:12.000Z → 2026-10-13T10:17:18.000Z
- **Gap:** 142.7 h dark, 262.0 nm offshore
- **Where:** -9.192, 54.440

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 262 nm offshore for 143 h
- satellite-confirmed AIS gap (GFW Events)

## Could be innocent

Going dark is frequently benign: in open water, where gaps are commonly protecting a fishing ground or waiting out weather. It is most actionable inside or beside a closed zone.

## Caveats

- AIS gaps can be reception loss, not always intentional disabling.
- The position is where AIS dropped; the path while dark is unknown.
- An inspection lead from GFW Events, not proof of illegal activity.

## Provenance & integrity

- NOAA Marine Cadastre AIS (marinecadastre.gov/ais (vessel positions)). US public domain.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Integrity (SHA-256 of canonical facts):** `f3f54af00a4826bf5aa5e9818e2934d8cc6fd68a9cdfcc952fdb8442f4ccff65`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
