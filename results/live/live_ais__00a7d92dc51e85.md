# Incident `live_ais__00a7d92dc51e85`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** Kiribati Exclusive Economic Zone (Line Group) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇹🇫 FY6-07-99%  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-25T06:56:57.000Z → 2026-09-26T13:38:35.000Z
- **Gap:** 30.7 h dark, 130.0 nm offshore
- **Where:** -7.021, -152.741

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 130 nm offshore for 31 h
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
- **Integrity (SHA-256 of canonical facts):** `25caf28fd2e48142e410d396eb2128d0c3117b5fe7aeacd302e1fc8881fbdf94`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
