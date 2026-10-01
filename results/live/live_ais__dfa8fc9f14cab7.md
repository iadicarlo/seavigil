# Incident `live_ais__dfa8fc9f14cab7`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Danish Exclusive Economic Zone (Greenland) (Denmark) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9886586
- **Vessel:** 🇬🇱 NATAARNAQ  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-26T00:20:14.000Z → 2026-09-27T01:11:53.000Z
- **Gap:** 24.9 h dark, 75.0 nm offshore
- **Where:** 72.545, -60.358

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 75 nm offshore for 25 h
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
- **Integrity (SHA-256 of canonical facts):** `71c9a3180dd64948fd61d5dada109eebf0e0d9439bd055d67b7a9f0a07ea5d17`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
