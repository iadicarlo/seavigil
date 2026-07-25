# Incident `live_ais__fb8b1a3c063256`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Japanese Exclusive Economic Zone (Japan) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9733404
- **Vessel:** 🇨🇳 JIN HUI 18  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-20T18:20:19.000Z → 2026-07-21T20:09:54.000Z
- **Gap:** 25.8 h dark, 179.0 nm offshore
- **Where:** 23.567, 136.579

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 179 nm offshore for 26 h
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
- **Integrity (SHA-256 of canonical facts):** `c836a9633fb00a7f2feefceebb9071dcf4259171ca2805303be7cdb9954bed0b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
