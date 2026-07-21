# Incident `live_ais__3d7e223a609bbb`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Papua New Guinean Exclusive Economic Zone (Papua New Guinea) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IOTC, WCPFC  ·  IMO 9991018
- **Vessel:** 🇯🇵 KOYOMARU NO.78  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-14T20:24:08.000Z → 2026-07-17T23:16:06.000Z
- **Gap:** 74.9 h dark, 63.0 nm offshore
- **Where:** 0.270, 151.144

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 63 nm offshore for 75 h
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
- **Integrity (SHA-256 of canonical facts):** `b083ea4e473afc6fcee647726654ea33c669db490a3235542aab8f09e9094b6b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
