# Incident `live_ais__7f2fe7cfbe3bb5`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Beninese Exclusive Economic Zone (Benin) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇲🇭 SEA FORTUNE  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-28T03:12:18.000Z → 2026-08-28T18:01:18.000Z
- **Gap:** 14.8 h dark, 96.0 nm offshore
- **Where:** 3.612, 2.896

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 96 nm offshore for 15 h
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
- **Integrity (SHA-256 of canonical facts):** `fa6eac7d6c192f84bdfdff62b26193c290eb4485b2efd9b9e4e3e0c2167c5c72`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
