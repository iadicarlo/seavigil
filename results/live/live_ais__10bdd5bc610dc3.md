# Incident `live_ais__10bdd5bc610dc3`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** French Exclusive Economic Zone (Réunion) (France) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9279484
- **Vessel:** 🇨🇾 STARLIGHT  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-04T06:41:35.000Z → 2026-07-12T04:49:17.000Z
- **Gap:** 190.1 h dark, 213.0 nm offshore
- **Where:** -21.159, 56.051

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 213 nm offshore for 190 h
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
- **Integrity (SHA-256 of canonical facts):** `0e9eed82121a949d5bd3348e1ca7d2e82761b9cc8e499f6a52108da2ae49bb66`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
