# Incident `live_ais__49f09f2023bc85`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Ghanaian Exclusive Economic Zone (Ghana) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC, WCPFC  ·  IMO 8908026
- **Vessel:** 🇫🇷 F/V CAP BOJADOR  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-22T15:32:19.000Z → 2026-10-07T08:47:18.000Z
- **Gap:** 353.2 h dark, 163.0 nm offshore
- **Where:** 2.722, -0.425

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 163 nm offshore for 353 h
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
- **Integrity (SHA-256 of canonical facts):** `c7d50145c18d5fac55c05a9638e88b37f0435d76d59373747f8fd0890f785a5f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
