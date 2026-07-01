# Incident `live_ais__6dba7ed100f190`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Angolan Exclusive Economic Zone (Angola) -- FOREIGN-flagged vessel
- **Authorization:** No authorization on record
- **Vessel:** 🇸🇬 AGOGO FPSO  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-26T18:54:57.000Z → 2026-06-27T06:58:52.000Z
- **Gap:** 12.1 h dark, 83.0 nm offshore
- **Where:** -6.137, 10.850

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 83 nm offshore for 12 h
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
- **Integrity (SHA-256 of canonical facts):** `1d1245213861ffdc73aa05ac7788a7dbbcfc3c47c747c1c13f9b811489a9baf3`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
