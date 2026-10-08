# Incident `live_ais__5bd37c19a0a7e5`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Solomon Islands Exclusive Economic Zone (Solomon Islands) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IATTC, WCPFC  ·  IMO 8749092
- **Vessel:** 🇹🇼 JIN JINN YI NO.66  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-03T16:17:06.000Z → 2026-10-04T10:28:17.000Z
- **Gap:** 18.2 h dark, 160.0 nm offshore
- **Where:** -13.184, 163.444

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 160 nm offshore for 18 h
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
- **Integrity (SHA-256 of canonical facts):** `93a635f6fc7546d38178064fdd86de9083b46373d3aed4a57e13788d2dce4efe`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
