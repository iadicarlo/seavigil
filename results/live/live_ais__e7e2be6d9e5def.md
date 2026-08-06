# Incident `live_ais__e7e2be6d9e5def`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Mauritanian Exclusive Economic Zone (Mauritania) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC  ·  IMO 9747560
- **Vessel:** 🇪🇸 GARBOLA  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-02T05:39:58.000Z → 2026-08-02T19:29:53.000Z
- **Gap:** 13.8 h dark, 106.0 nm offshore
- **Where:** 19.526, -18.114

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 106 nm offshore for 14 h
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
- **Integrity (SHA-256 of canonical facts):** `1a0018fb92a04a766a8f2fe34f6ae4528fa851c9e9d3cb530c3fb32121ba04c7`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
