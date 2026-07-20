# Incident `live_ais__8386ad1dd405ab`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** United States Exclusive Economic Zone (United States Virgin Islands) (United States) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇵🇹 SENTINEL  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-15T16:13:19.000Z → 2026-07-16T16:03:40.000Z
- **Gap:** 23.8 h dark, 72.0 nm offshore
- **Where:** 19.332, -65.284

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 72 nm offshore for 24 h
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
- **Integrity (SHA-256 of canonical facts):** `33ef22c6ad62ccbd92c415c4b8fc2ee666ebdf8f892484522b7e211914c46b3b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
