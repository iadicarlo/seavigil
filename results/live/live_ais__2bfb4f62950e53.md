# Incident `live_ais__2bfb4f62950e53`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Madagascan Exclusive Economic Zone (Madagascar) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇪🇸 HAIZEA BOST  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-27T07:26:54.000Z → 2026-10-28T17:45:21.000Z
- **Gap:** 34.3 h dark, 149.0 nm offshore
- **Where:** -18.621, 42.179

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 149 nm offshore for 34 h
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
- **Integrity (SHA-256 of canonical facts):** `a5202ddfbbd0718e85b084e44b38b4c355919d7decb1f9c384e43609fa0937dd`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
