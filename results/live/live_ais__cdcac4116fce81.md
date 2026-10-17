# Incident `live_ais__cdcac4116fce81`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** United States Exclusive Economic Zone (Jarvis Islands) (United States) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 7827469
- **Vessel:** 🇫🇲 SOKEHS  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-04T16:59:16.000Z → 2026-10-13T12:18:09.000Z
- **Gap:** 211.3 h dark, 191.0 nm offshore
- **Where:** -0.210, -162.161

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 191 nm offshore for 211 h
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
- **Integrity (SHA-256 of canonical facts):** `8b5ec6fee435ad255ce5e5c46d2b58e2de212aef78d6e520eec4ce1ebcb2cfa8`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
