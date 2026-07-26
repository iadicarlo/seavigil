# Incident `live_ais__9a9cf54bcbe714`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Somali Exclusive Economic Zone (Federal Republic of Somalia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇺🇸 MAERSK HARTFORD  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-16T21:44:40.000Z → 2026-07-22T06:00:38.000Z
- **Gap:** 128.3 h dark, 234.0 nm offshore
- **Where:** 8.393, 54.007

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 234 nm offshore for 128 h
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
- **Integrity (SHA-256 of canonical facts):** `abc0d3b0ab60d1a4c7675631e6ce2f15c7867774a7f5806b3609232528b91948`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
