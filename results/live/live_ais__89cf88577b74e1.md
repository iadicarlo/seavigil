# Incident `live_ais__89cf88577b74e1`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** South African Exclusive Economic Zone (South Africa) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9531478
- **Vessel:** 🇱🇷 NAVIGATOR GRACE  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-04T13:23:26.000Z → 2026-07-06T05:23:37.000Z
- **Gap:** 40.0 h dark, 200.0 nm offshore
- **Where:** -32.512, 30.451

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 200 nm offshore for 40 h
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
- **Integrity (SHA-256 of canonical facts):** `cc2de5595dcf33134ec76a7893664598b3f8d495b472d379c1d653c4a886cb7f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
