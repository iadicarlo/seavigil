# Incident `live_ais__880d558b9b8fea`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Spanish Exclusive Economic Zone (Canary Islands) (Spain) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇲🇭 FRONT BEAULY  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-12T19:55:46.000Z → 2026-09-22T09:51:34.000Z
- **Gap:** 229.9 h dark, 571.0 nm offshore
- **Where:** 28.153, -19.800

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 571 nm offshore for 230 h
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
- **Integrity (SHA-256 of canonical facts):** `5322b3a0b6f0ad278ac7c65299849f1e1e83ca04cb7b580f395349d4ba9fe1d1`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
