# Incident `live_ais__8f8d779021d3a2`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Chilean Exclusive Economic Zone (Easter Island) (Chile) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇲🇦 PTR331-11-75%  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-18T12:56:10.000Z → 2026-09-24T10:42:25.000Z
- **Gap:** 141.8 h dark, 302.0 nm offshore
- **Where:** -23.648, -105.622

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 302 nm offshore for 142 h
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
- **Integrity (SHA-256 of canonical facts):** `1bfd55f6db171b4ab47cea698dbd912c5bb96f29599cb8dcd65c81c8532dfb30`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
