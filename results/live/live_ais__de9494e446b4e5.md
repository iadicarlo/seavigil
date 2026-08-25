# Incident `live_ais__de9494e446b4e5`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Mauritian Exclusive Economic Zone (Chagos Archipelago) (Republic of Mauritius) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇬🇧 GRAMPIAN ENDURANCE  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-20T02:18:14.000Z → 2026-08-21T13:17:55.000Z
- **Gap:** 35.0 h dark, 89.0 nm offshore
- **Where:** -3.233, 71.203

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 89 nm offshore for 35 h
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
- **Integrity (SHA-256 of canonical facts):** `64268d5b0d77ee786a59a65aa03ed3fc31e026870fc655319bb0f3059549c8e4`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
