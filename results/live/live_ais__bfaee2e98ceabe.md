# Incident `live_ais__bfaee2e98ceabe`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (inside a no-take reserve)
- **EEZ:** Australian Exclusive Economic Zone (Cocos Islands) (Australia)
- **Authorization:** Flag unknown; authorization not checkable
- **Vessel:** BUOY-10           9V  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-14T13:31:40.000Z → 2026-10-17T00:08:15.000Z
- **Gap:** 58.6 h dark, 267.0 nm offshore
- **Where:** -13.684, 96.164

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 267 nm offshore for 59 h
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
- **Integrity (SHA-256 of canonical facts):** `3f27ad1b59a80eb1b95a504ed2dcb3f9bce438a3ccecc4c2a827554c4f487649`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
