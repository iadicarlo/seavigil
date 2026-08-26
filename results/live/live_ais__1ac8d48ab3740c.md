# Incident `live_ais__1ac8d48ab3740c`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** New Zealand Exclusive Economic Zone (Tokelau) (New Zealand) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇳🇴 `259001`  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-19T13:23:19.000Z → 2026-08-22T01:51:28.000Z
- **Gap:** 60.5 h dark, 217.0 nm offshore
- **Where:** -7.888, -171.513

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 217 nm offshore for 60 h
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
- **Integrity (SHA-256 of canonical facts):** `25ea2748699d37162ba2f4583892b03bc5d5a553a42cf04dae860b08f4736c35`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
