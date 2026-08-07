# Incident `live_ais__b70d281c630c6a`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Brazilian Exclusive Economic Zone (Brazil) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9200847
- **Vessel:** 🇵🇦 CIDADE DE MARICA  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-02T20:25:38.000Z → 2026-08-03T19:54:55.000Z
- **Gap:** 23.5 h dark, 145.0 nm offshore
- **Where:** -25.447, -42.752

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 145 nm offshore for 23 h
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
- **Integrity (SHA-256 of canonical facts):** `73c29fd69db878af51d202ba259cd615d0d030e61078c548bcc61066519b86b9`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
