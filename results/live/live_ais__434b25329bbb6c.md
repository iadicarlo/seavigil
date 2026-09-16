# Incident `live_ais__434b25329bbb6c`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Mauritanian Exclusive Economic Zone (Mauritania) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, ICCAT, IOTC  ·  IMO 7827495
- **Vessel:** 🇸🇳 ORIENTAL KIM  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-11T22:56:33.000Z → 2026-09-12T13:37:23.000Z
- **Gap:** 14.7 h dark, 147.0 nm offshore
- **Where:** 16.621, -18.816

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 147 nm offshore for 15 h
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
- **Integrity (SHA-256 of canonical facts):** `37b62fcd7330c77779edcd896bec812a6d3a2d1facab9378d5e39a8f1845e850`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
