# Incident `live_ais__7242a63bc919d7`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Seychellois Exclusive Economic Zone (Seychelles) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9767388
- **Vessel:** 🇱🇷 MSC RIFAYA  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-13T06:56:52.000Z → 2026-07-30T08:06:16.000Z
- **Gap:** 409.2 h dark, 482.0 nm offshore
- **Where:** -8.379, 45.703

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 482 nm offshore for 409 h
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
- **Integrity (SHA-256 of canonical facts):** `ae1753932dd962784a2d71ee0969c17807e6bdf5ba77ff77ffc26c9b7be80ee6`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
