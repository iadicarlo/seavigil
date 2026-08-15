# Incident `live_ais__11c743ec0f61ba`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Irish Exclusive Economic Zone (Ireland) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: NEAFC  ·  IMO 9362671
- **Vessel:** 🇪🇸 CANTABRICO TRES  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-09T21:10:41.000Z → 2026-08-11T07:18:01.000Z
- **Gap:** 34.1 h dark, 150.0 nm offshore
- **Where:** 53.029, -14.326

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 150 nm offshore for 34 h
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
- **Integrity (SHA-256 of canonical facts):** `bc9b6b9c121c1fccf36998ecf339edade16098913a4872bac1b23cfd5baae17d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
