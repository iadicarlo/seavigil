# Incident `live_ais__d487066e8d39ef`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Guyanese Exclusive Economic Zone (Guyana) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT  ·  IMO 8452041
- **Vessel:** 🇻🇪 FIMAR  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-29T13:35:14.000Z → 2026-10-02T04:27:27.000Z
- **Gap:** 62.9 h dark, 87.0 nm offshore
- **Where:** 9.002, -59.136

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 87 nm offshore for 63 h
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
- **Integrity (SHA-256 of canonical facts):** `6a1014d7b9e943b7d0fbd4336eddb802c6f4806ac3963230621393ade463e63b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
