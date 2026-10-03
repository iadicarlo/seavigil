# Incident `live_ais__fb0c88af77a655`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Overlapping claim Western Sahara: Western Sahara / Morocco (Western Sahara) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇪🇸 PLAYA PESMAR UNO  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-28T19:35:21.000Z → 2026-09-29T09:25:15.000Z
- **Gap:** 13.8 h dark, 225.0 nm offshore
- **Where:** 22.248, -20.446

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 225 nm offshore for 14 h
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
- **Integrity (SHA-256 of canonical facts):** `026879776ea316f4f53bd201400e10088922e587ba13f236016de079e7b91b6e`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
