# Incident `live_ais__2909e32b1d32a5`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Solomon Islands Exclusive Economic Zone (Solomon Islands) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9910040
- **Vessel:** 🇨🇳 ZHONG SHUI 797  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-06T02:27:33.000Z → 2026-07-08T18:51:31.000Z
- **Gap:** 64.4 h dark, 74.0 nm offshore
- **Where:** -11.048, 164.516

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 74 nm offshore for 64 h
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
- **Integrity (SHA-256 of canonical facts):** `73c31d2bb9cf5bdc59a998c11831b071dad1ad56d1e7c5b3777857b7d545a1ee`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
