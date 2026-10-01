# Incident `live_ais__744f570b426a6a`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Danish Exclusive Economic Zone (Greenland) (Denmark) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: NAFO, NEAFC  ·  IMO 9829708
- **Vessel:** 🇬🇱 AVATAQ  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-25T23:37:04.000Z → 2026-09-27T00:35:20.000Z
- **Gap:** 25.0 h dark, 70.0 nm offshore
- **Where:** 72.711, -60.328

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 70 nm offshore for 25 h
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
- **Integrity (SHA-256 of canonical facts):** `e2ea37944fe11f1527ba6d9fbe5b30dd03c7801afeb33f7b55e91e6accdec2d6`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
