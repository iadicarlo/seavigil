# Incident `live_ais__a44ac1d59ef6de`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Liberian Exclusive Economic Zone (Liberia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9000625
- **Vessel:** 🇩🇪 OCEAN ZEPHYR  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-06T08:57:10.000Z → 2026-08-11T02:50:37.000Z
- **Gap:** 113.9 h dark, 190.0 nm offshore
- **Where:** 1.952, -10.104

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 190 nm offshore for 114 h
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
- **Integrity (SHA-256 of canonical facts):** `5490699286d8cfb1006c57a6d836561628913fef7e33514966df61ec54f3fa33`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
