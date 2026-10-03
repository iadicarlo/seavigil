# Incident `live_ais__3de925815a70d6`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Ecuadorian Exclusive Economic Zone (Galapagos) (Ecuador) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)
- **Vessel:** 🇨🇳 BOYA 9 AMELIA 100%  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-28T23:02:05.000Z → 2026-09-29T11:16:32.000Z
- **Gap:** 12.2 h dark, 150.0 nm offshore
- **Where:** -3.414, -92.149

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 150 nm offshore for 12 h
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
- **Integrity (SHA-256 of canonical facts):** `dd09d66c8a540e159a11f36f4e96452b643247faf4fd0c8b73bf44ad60ba2b3f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
