# Incident `live_ais__3e3cdd1492127c`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Guyanese Exclusive Economic Zone (Guyana) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9590307
- **Vessel:** 🇱🇷 RED MOON  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-22T17:29:09.000Z → 2026-10-23T22:41:22.000Z
- **Gap:** 29.2 h dark, 94.0 nm offshore
- **Where:** 8.010, -56.996

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- possible name match to 'Asian Warrior' on the CCAMLR IUU list (verify identity)
- went dark 94 nm offshore for 29 h
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
- **Integrity (SHA-256 of canonical facts):** `b641578f9fedf55b2ad5107c95b5f31726fef12da3c89d6b139c8ddd5914a063`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
