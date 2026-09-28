# Incident `live_ais__a821d1238cf4c0`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Chilean Exclusive Economic Zone (Easter Island) (Chile) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇬🇧 PING TAI RONG 331-2  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-18T10:50:38.000Z → 2026-09-24T15:24:05.000Z
- **Gap:** 148.6 h dark, 308.0 nm offshore
- **Where:** -23.618, -105.961

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 308 nm offshore for 149 h
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
- **Integrity (SHA-256 of canonical facts):** `e86feafb5494e3f2a5c02ec6cf6c2f4ba448a2f546a61303c95a8bb7a0923b07`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
