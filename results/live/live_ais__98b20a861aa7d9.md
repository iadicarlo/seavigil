# Incident `live_ais__98b20a861aa7d9`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Micronesian Exclusive Economic Zone (Micronesia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇯🇵 WAKABAMARU NO11  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-11T15:20:22.000Z → 2026-07-21T21:09:57.000Z
- **Gap:** 245.8 h dark, 166.0 nm offshore
- **Where:** 4.686, 151.500

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 166 nm offshore for 246 h
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
- **Integrity (SHA-256 of canonical facts):** `1dafd0da912f70923cb5da4f45e780d89cef9112a3373a6ad29f7c5685a04f2d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
