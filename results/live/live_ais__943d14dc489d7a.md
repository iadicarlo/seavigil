# Incident `live_ais__943d14dc489d7a`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Indonesian Exclusive Economic Zone (Indonesia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9516533
- **Vessel:** 🇵🇦 JIN DA HAI  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-15T02:11:34.000Z → 2026-09-16T10:47:17.000Z
- **Gap:** 32.6 h dark, 65.0 nm offshore
- **Where:** -7.569, 116.686

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 65 nm offshore for 33 h
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
- **Integrity (SHA-256 of canonical facts):** `bb924541bcaf74f402497aa3c2acc656ca11c452712322d62ea34d94934a8e6d`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
