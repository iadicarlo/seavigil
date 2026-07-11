# Incident `live_ais__3121f7d83fd833`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Mauritian Exclusive Economic Zone (Republic of Mauritius) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇱🇷 DIAS I  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-07T05:21:38.000Z → 2026-07-07T17:33:29.000Z
- **Gap:** 12.2 h dark, 202.0 nm offshore
- **Where:** -16.959, 62.997

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 202 nm offshore for 12 h
- satellite-confirmed AIS gap (GFW Events)

## Could be innocent

Going dark is frequently benign: in open water, where gaps are commonly protecting a fishing ground or waiting out weather. It is most actionable inside or beside a closed zone.

## Caveats

- IUU match is by name only; IUU vessels reuse names, so confirm the identity.
- AIS gaps can be reception loss, not always intentional disabling.
- The position is where AIS dropped; the path while dark is unknown.
- An inspection lead from GFW Events, not proof of illegal activity.

## Provenance & integrity

- NOAA Marine Cadastre AIS (marinecadastre.gov/ais (vessel positions)). US public domain.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Integrity (SHA-256 of canonical facts):** `d83bd329f2ac2bc6bcc53d5e3ac8addb633129bd410602e5d050af8a3f60778a`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
