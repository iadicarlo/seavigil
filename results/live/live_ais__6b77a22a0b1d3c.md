# Incident `live_ais__6b77a22a0b1d3c`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Micronesian Exclusive Economic Zone (Micronesia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇯🇵 78KOYOMARU NO2  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-02T08:39:57.000Z → 2026-07-03T01:31:26.000Z
- **Gap:** 16.9 h dark, 111.0 nm offshore
- **Where:** 2.083, 156.596

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 111 nm offshore for 17 h
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
- **Integrity (SHA-256 of canonical facts):** `8c7efec3282fc93c24c4502fcd2ad23dd78f15b64c5fbc5ca5e99d612378f156`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
