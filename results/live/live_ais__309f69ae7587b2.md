# Incident `live_ais__309f69ae7587b2`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Togolese Exclusive Economic Zone (Togo) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 8996281
- **Vessel:** 🇳🇷 OCEAN ENCOUNTER  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-29T21:10:00.000Z → 2026-10-19T00:29:11.000Z
- **Gap:** 459.3 h dark, 361.0 nm offshore
- **Where:** 4.272, 2.074

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 361 nm offshore for 459 h
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
- **Integrity (SHA-256 of canonical facts):** `a5bd5fd9212373d971d32b71cc34ce78dcf947c574243bdadb6781e88b33ec75`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
