# Incident `live_ais__6bdf9dfa3d0002`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Bissau-Guinean Exclusive Economic Zone (Guinea-Bissau) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 8733744
- **Vessel:** 🇪🇸 PEIX.MAR.25  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-19T21:57:08.000Z → 2026-10-21T06:18:19.000Z
- **Gap:** 32.4 h dark, 75.0 nm offshore
- **Where:** 10.151, -17.117

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 75 nm offshore for 32 h
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
- **Integrity (SHA-256 of canonical facts):** `4441e4e59bb7067181e3ee12a9905411e73e8ae417aa3c31b9fd6ce7dc232057`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
