# Incident `live_ais__b93ad0b59854ea`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Papua New Guinean Exclusive Economic Zone (Papua New Guinea) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9805790
- **Vessel:** 🇱🇷 TAHO EUROPE  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-29T14:29:48.000Z → 2026-07-30T21:40:42.000Z
- **Gap:** 31.2 h dark, 154.0 nm offshore
- **Where:** -12.326, 152.031

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 154 nm offshore for 31 h
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
- **Integrity (SHA-256 of canonical facts):** `c8407cf510715e38669442050679ad8e9efc16041487456b9f48255ecdf2cffc`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
