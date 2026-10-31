# Incident `live_ais__cd79f26cb1b8cf`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (inside a no-take reserve)
- **EEZ:** Seychellois Exclusive Economic Zone (Seychelles)
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** LWYY288-79-96%  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-26T10:57:45.000Z → 2026-10-27T04:15:35.000Z
- **Gap:** 17.3 h dark, 53.0 nm offshore
- **Where:** -8.849, 45.992

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 53 nm offshore for 17 h
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
- **Integrity (SHA-256 of canonical facts):** `fb048484ec153e7a1295cdb092f3c1505ec82b9168286ff34584f1e7010492ca`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
