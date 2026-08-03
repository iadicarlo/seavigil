# Incident `live_ais__d1e58414f799d3`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Marshallese Exclusive Economic Zone (Marshall Islands) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, NPFC, WCPFC  ·  IMO 8815023
- **Vessel:** 🇰🇷 YUN RUN 1  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-29T21:38:03.000Z → 2026-07-30T13:10:36.000Z
- **Gap:** 15.5 h dark, 161.0 nm offshore
- **Where:** 10.801, 160.395

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 161 nm offshore for 16 h
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
- **Integrity (SHA-256 of canonical facts):** `2cc8bb2961981800db808f4c8b5c99f8b742c790e45435063fbcb94d2311d23f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
