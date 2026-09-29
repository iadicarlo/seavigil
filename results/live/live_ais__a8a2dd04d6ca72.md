# Incident `live_ais__a8a2dd04d6ca72`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Ecuadorian Exclusive Economic Zone (Galapagos) (Ecuador) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇵🇦 RIA DE ALDAN  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-20T12:17:15.000Z → 2026-09-25T10:24:57.000Z
- **Gap:** 118.1 h dark, 179.0 nm offshore
- **Where:** 3.275, -90.829

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 179 nm offshore for 118 h
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
- **Integrity (SHA-256 of canonical facts):** `a3ba3d95d3ba6e10a85e886f7c94112ad763696c97dd5f2ffa9053148d301d9e`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
