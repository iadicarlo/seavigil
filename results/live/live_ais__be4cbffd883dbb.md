# Incident `live_ais__be4cbffd883dbb`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Ghanaian Exclusive Economic Zone (Ghana) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC, WCPFC  ·  IMO 8912998
- **Vessel:** 🇫🇷 F/V GUERIDEN  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-04T05:06:21.000Z → 2026-07-07T19:10:45.000Z
- **Gap:** 86.1 h dark, 147.0 nm offshore
- **Where:** 3.387, -0.315

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 147 nm offshore for 86 h
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
- **Integrity (SHA-256 of canonical facts):** `1aa78478c9b6249ebea011fd351ad908f04d9724432f766b4e52592d00950dc6`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
