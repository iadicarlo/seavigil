# Incident `live_ais__b709df6cfc09dd`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Sri Lankan Exclusive Economic Zone (Sri Lanka) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇵🇦 KALLISTA  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-11T14:21:45.000Z → 2026-09-12T09:04:06.000Z
- **Gap:** 18.7 h dark, 176.0 nm offshore
- **Where:** 3.784, 81.075

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 176 nm offshore for 19 h
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
- **Integrity (SHA-256 of canonical facts):** `254a0a1b7df649e7fa5019ff41ba9a12e8aeeec5b5b894a60abff5dc88f07384`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
