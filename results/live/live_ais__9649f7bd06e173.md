# Incident `live_ais__9649f7bd06e173`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Mauritanian Exclusive Economic Zone (Mauritania) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC, WCPFC  ·  IMO 8613267
- **Vessel:** 🇪🇸 ALBONIGA  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-31T09:03:02.000Z → 2026-08-04T20:01:42.000Z
- **Gap:** 107.0 h dark, 75.0 nm offshore
- **Where:** 17.887, -18.666

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 75 nm offshore for 107 h
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
- **Integrity (SHA-256 of canonical facts):** `db86686f0e1b63e578a4cf8327359b2c4dcb8c6e0a199a3cf9e5ee2d37aa065d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
