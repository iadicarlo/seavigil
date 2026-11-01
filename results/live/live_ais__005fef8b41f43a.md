# Incident `live_ais__005fef8b41f43a`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (inside a no-take reserve)
- **EEZ:** Seychellois Exclusive Economic Zone (Seychelles)
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** LWYY288-81-99%  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-27T13:14:01.000Z → 2026-10-28T02:44:59.000Z
- **Gap:** 13.5 h dark, 65.0 nm offshore
- **Where:** -9.090, 45.371

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 65 nm offshore for 14 h
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
- **Integrity (SHA-256 of canonical facts):** `70fa38aedb0746bc86ab665717e1e351d288ad997dda2e598f0f295f24ac7217`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
