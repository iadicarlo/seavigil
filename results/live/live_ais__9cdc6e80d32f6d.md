# Incident `live_ais__9cdc6e80d32f6d`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Mexican Exclusive Economic Zone (Mexico) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇲🇭 FLEX ENDEAVOUR  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-20T23:10:09.000Z → 2026-08-21T19:45:08.000Z
- **Gap:** 20.6 h dark, 221.0 nm offshore
- **Where:** 25.989, -93.997

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 221 nm offshore for 21 h
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
- **Integrity (SHA-256 of canonical facts):** `bd2deb44619b5a85c0b768e3cee263c071dd482dc54e57ba2e68282844d3451a`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
