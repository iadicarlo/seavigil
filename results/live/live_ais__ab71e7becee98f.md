# Incident `live_ais__ab71e7becee98f`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Madagascan Exclusive Economic Zone (Madagascar) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9374026
- **Vessel:** 🇵🇦 XIN RUI OCEAN  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-19T18:28:37.000Z → 2026-08-20T11:29:44.000Z
- **Gap:** 17.0 h dark, 286.0 nm offshore
- **Where:** -27.937, 42.116

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 286 nm offshore for 17 h
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
- **Integrity (SHA-256 of canonical facts):** `a9f7da5e865338bf5b6ad83d849f9b896a79f9c909ab5f0ff913b6d2f9a8a275`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
