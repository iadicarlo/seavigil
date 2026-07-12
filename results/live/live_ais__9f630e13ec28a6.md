# Incident `live_ais__9f630e13ec28a6`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Cape Verdean Exclusive Economic Zone (Cape Verde) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT  ·  IMO 9882009
- **Vessel:** 🇪🇸 MONTERAIOLA  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-28T06:05:21.000Z → 2026-07-07T17:25:53.000Z
- **Gap:** 227.3 h dark, 401.0 nm offshore
- **Where:** 13.859, -23.169

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 401 nm offshore for 227 h
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
- **Integrity (SHA-256 of canonical facts):** `d40bd5c27c3eb35e803735c375f26205e922b3723d9f8f46ed1bff56c4c31844`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
