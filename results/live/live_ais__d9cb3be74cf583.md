# Incident `live_ais__d9cb3be74cf583`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Tuvaluan Exclusive Economic Zone (Tuvalu) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇨🇳 WANGBIAO-8597  100%  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-09T17:29:16.000Z → 2026-08-15T07:04:37.000Z
- **Gap:** 133.6 h dark, 103.0 nm offshore
- **Where:** -7.557, 174.933

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 103 nm offshore for 134 h
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
- **Integrity (SHA-256 of canonical facts):** `d8bee2d39743b0c01472682d857faf2f9fb79c19790d15eb670358dcbf251862`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
