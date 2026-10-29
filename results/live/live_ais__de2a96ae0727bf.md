# Incident `live_ais__de2a96ae0727bf`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (inside a no-take reserve)
- **EEZ:** Seychellois Exclusive Economic Zone (Seychelles)
- **Authorization:** Flag unknown; authorization not checkable
- **Vessel:** 992884508-99%  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-25T00:29:59.000Z → 2026-10-25T12:33:59.000Z
- **Gap:** 12.1 h dark, 102.0 nm offshore
- **Where:** -8.281, 49.237

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 102 nm offshore for 12 h
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
- **Integrity (SHA-256 of canonical facts):** `966d7a5b1e98a23929e7906ff9437815da0504bf1db57efebad6d39c0149b9a9`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
