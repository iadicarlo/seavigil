# Incident `live_ais__12ae189b27076f`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** British Exclusive Economic Zone (Saint Helena) (United Kingdom) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇪🇸 CARRIZO DOUS  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-25T16:28:34.000Z → 2026-07-26T16:03:23.000Z
- **Gap:** 23.6 h dark, 277.0 nm offshore
- **Where:** -17.580, -5.070

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 277 nm offshore for 24 h
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
- **Integrity (SHA-256 of canonical facts):** `d25476c52b4f9d7993aea1576e0e67b14ea6f48bc3a961e976b7f98ccec37618`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
