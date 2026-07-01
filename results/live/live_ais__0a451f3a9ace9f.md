# Incident `live_ais__0a451f3a9ace9f`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Micronesian Exclusive Economic Zone (Micronesia) -- FOREIGN-flagged vessel
- **Authorization:** No authorization on record  ·  IMO 9633135
- **Vessel:** 🇰🇷 ORIENTAL LEADER  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-24T05:56:06.000Z → 2026-06-25T18:29:17.000Z
- **Gap:** 36.6 h dark, 213.0 nm offshore
- **Where:** 4.937, 141.882

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 213 nm offshore for 37 h
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
- **Integrity (SHA-256 of canonical facts):** `bbbf9ae2636d4d02beb55fe7526515b8a08326b947a7398fb57a13d9a87f0465`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
