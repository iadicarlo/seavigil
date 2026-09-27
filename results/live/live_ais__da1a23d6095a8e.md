# Incident `live_ais__da1a23d6095a8e`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Mauritian Exclusive Economic Zone (Republic of Mauritius) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇻🇦 03-1          [100%]  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-10T08:43:54.000Z → 2026-09-23T06:06:52.000Z
- **Gap:** 309.4 h dark, 383.0 nm offshore
- **Where:** -18.006, 63.380

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 383 nm offshore for 309 h
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
- **Integrity (SHA-256 of canonical facts):** `d986daee697ca0e3680cd7a2565af513980c47de2ca2b5f689464a5627ddbd88`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
