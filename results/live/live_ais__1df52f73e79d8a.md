# Incident `live_ais__1df52f73e79d8a`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Kiribati Exclusive Economic Zone (Gilbert Islands) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇵🇦 YU27-10-52%  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-24T10:00:07.000Z → 2026-10-25T19:12:38.000Z
- **Gap:** 33.2 h dark, 75.0 nm offshore
- **Where:** -3.736, 176.554

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 75 nm offshore for 33 h
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
- **Integrity (SHA-256 of canonical facts):** `14f1baf2b86619b4345b75f40ccc6fba1dfb00f1db9a2f8c94a9639b0ed80a59`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
