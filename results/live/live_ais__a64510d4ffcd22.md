# Incident `live_ais__a64510d4ffcd22`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Kiribati Exclusive Economic Zone (Line Group) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 1066790
- **Vessel:** 🇫🇲 PACIFIC ENTERPRISE 7  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-18T01:55:23.000Z → 2026-08-25T04:35:57.000Z
- **Gap:** 170.7 h dark, 65.0 nm offshore
- **Where:** 3.168, -162.120

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 65 nm offshore for 171 h
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
- **Integrity (SHA-256 of canonical facts):** `0250a7c87fc216a47b949378c18d861b690d7513d74b89fe7aaadba024879cc2`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
