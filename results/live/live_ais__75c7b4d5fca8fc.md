# Incident `live_ais__75c7b4d5fca8fc`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** Solomon Islands Exclusive Economic Zone (Solomon Islands) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇷🇺 LONGLINE BUOY 09-56%  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-01T18:28:33.000Z → 2026-07-02T13:25:29.000Z
- **Gap:** 18.9 h dark, 134.0 nm offshore
- **Where:** -7.046, 161.679

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 134 nm offshore for 19 h
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
- **Integrity (SHA-256 of canonical facts):** `8fde0d629e496c55a56cc90c2e08d189234b05b0021a62fda4046258154f353f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
