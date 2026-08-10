# Incident `live_ais__a62ddb1d4249d2`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Yemeni Exclusive Economic Zone (Yemen) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9516545
- **Vessel:** 🇩🇲 DAISY  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-05T15:25:30.000Z → 2026-08-06T11:13:11.000Z
- **Gap:** 19.8 h dark, 56.0 nm offshore
- **Where:** 11.728, 44.656

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 56 nm offshore for 20 h
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
- **Integrity (SHA-256 of canonical facts):** `6061d6993dc1cfde18e67e5f1c33a28874fdd2f5157245814e2035cacf4ba661`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
