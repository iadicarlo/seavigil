# Incident `live_ais__827b8ffe2e77ef`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Vanuatuan Exclusive Economic Zone (Vanuatu) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9686091
- **Vessel:** 🇨🇳 ZHONGSHUI727  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-11T23:21:42.000Z → 2026-10-12T12:54:03.000Z
- **Gap:** 13.5 h dark, 157.0 nm offshore
- **Where:** -18.470, 172.649

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 157 nm offshore for 14 h
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
- **Integrity (SHA-256 of canonical facts):** `1a754f5d5b7d96449ba9125ae248a385bc5f90fdb1a125a1f5b77baa29876a75`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
