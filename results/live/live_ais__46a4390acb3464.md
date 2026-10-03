# Incident `live_ais__46a4390acb3464`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** New Zealand Exclusive Economic Zone (Cook Islands) (New Zealand) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇬🇧 PENELOPE  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-28T17:15:20.000Z → 2026-09-29T05:47:00.000Z
- **Gap:** 12.5 h dark, 185.0 nm offshore
- **Where:** -16.162, -165.066

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 185 nm offshore for 13 h
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
- **Integrity (SHA-256 of canonical facts):** `86be6b4e363826973f9444b7b45ed207a4ffd9b58a68ee1c3c9de11cc3d95fb0`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
