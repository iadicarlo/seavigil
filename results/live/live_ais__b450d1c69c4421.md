# Incident `live_ais__b450d1c69c4421`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Cape Verdean Exclusive Economic Zone (Cape Verde) -- FOREIGN-flagged vessel
- **Authorization:** No authorization on record
- **Vessel:** 🇧🇿 PLAYA DE LAGA  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-16T06:26:43.000Z → 2026-06-27T19:56:08.000Z
- **Gap:** 277.5 h dark, 171.0 nm offshore
- **Where:** 15.352, -20.429

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 171 nm offshore for 277 h
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
- **Integrity (SHA-256 of canonical facts):** `d3f138f7486981bbb55ebc9272c9e01566a3c61b01f1c618e740dfc5e8edc183`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
