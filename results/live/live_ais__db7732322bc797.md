# Incident `live_ais__db7732322bc797`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Micronesian Exclusive Economic Zone (Micronesia) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IATTC, WCPFC  ·  IMO 9741243
- **Vessel:** 🇨🇳 SHEN GANG FA 715  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-24T15:06:33.000Z → 2026-06-28T00:11:03.000Z
- **Gap:** 81.1 h dark, 52.0 nm offshore
- **Where:** 0.948, 155.383

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 52 nm offshore for 81 h
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
- **Integrity (SHA-256 of canonical facts):** `e604118ad6e41be753a79e38c7b9cc63037230306039ade54b2fef28251201b1`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
