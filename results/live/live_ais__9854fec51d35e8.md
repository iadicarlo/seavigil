# Incident `live_ais__9854fec51d35e8`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Papua New Guinean Exclusive Economic Zone (Papua New Guinea) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9868637
- **Vessel:** 🇹🇼 WIN RICH 707  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-17T14:14:56.000Z → 2026-09-23T05:57:47.000Z
- **Gap:** 135.7 h dark, 81.0 nm offshore
- **Where:** -1.688, 149.736

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 81 nm offshore for 136 h
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
- **Integrity (SHA-256 of canonical facts):** `cd93d5001ebdf9b01165cdac93b5d97a2c563504a9ce1369d70055b1bf85c6a3`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
