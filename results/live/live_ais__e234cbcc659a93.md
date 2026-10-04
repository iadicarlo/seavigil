# Incident `live_ais__e234cbcc659a93`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** British Exclusive Economic Zone (Bermuda) (United Kingdom) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9000625
- **Vessel:** 🇩🇪 OCEAN ZEPHYR  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-11T11:02:53.000Z → 2026-09-30T07:43:20.000Z
- **Gap:** 452.7 h dark, 206.0 nm offshore
- **Where:** 34.514, -62.687

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 206 nm offshore for 453 h
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
- **Integrity (SHA-256 of canonical facts):** `3d15066e1086f584a3a9caae4d7bec8878c85f18b01cf7777d907120c0aecdc3`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
