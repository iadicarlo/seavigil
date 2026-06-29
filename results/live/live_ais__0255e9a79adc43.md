# Incident `live_ais__0255e9a79adc43`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Japanese Exclusive Economic Zone (Japan) -- FOREIGN-flagged vessel
- **Authorization:** No authorization on record
- **Vessel:** 🇱🇷 SAPPHIRE A  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-24T02:33:50.000Z → 2026-06-24T16:12:23.000Z
- **Gap:** 13.6 h dark, 123.0 nm offshore
- **Where:** 31.192, 136.164

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 123 nm offshore for 14 h
- satellite-confirmed AIS gap (GFW Events)

## Caveats

- AIS gaps can be reception loss, not always intentional disabling.
- The position is where AIS dropped; the path while dark is unknown.
- An inspection lead from GFW Events, not proof of illegal activity.

## Provenance & integrity

- NOAA Marine Cadastre AIS (marinecadastre.gov/ais (vessel positions)). US public domain.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Integrity (SHA-256 of canonical facts):** `98731a9601ee068ecc154bdc95c94892ab07df4b43732f003e26df10f7bf5746`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
