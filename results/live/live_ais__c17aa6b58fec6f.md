# Incident `live_ais__c17aa6b58fec6f`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Argentinian Exclusive Economic Zone (Argentina) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9486594
- **Vessel:** 🇲🇭 PARITY  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-04T17:49:12.000Z → 2026-09-06T10:40:09.000Z
- **Gap:** 40.8 h dark, 149.0 nm offshore
- **Where:** -43.147, -60.228

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 149 nm offshore for 41 h
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
- **Integrity (SHA-256 of canonical facts):** `5c371d1e0182ba0dc2a2f4aa3c7b99cbd29ccdec62656c42617acc92ee81a793`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
