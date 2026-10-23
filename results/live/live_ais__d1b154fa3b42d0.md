# Incident `live_ais__d1b154fa3b42d0`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Marshallese Exclusive Economic Zone (Marshall Islands) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, WCPFC  ·  IMO 9814442
- **Vessel:** 🇨🇳 HNY NAN YU 762  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-11T19:25:56.000Z → 2026-10-19T21:55:54.000Z
- **Gap:** 194.5 h dark, 133.0 nm offshore
- **Where:** 4.997, 169.299

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 133 nm offshore for 194 h
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
- **Integrity (SHA-256 of canonical facts):** `6e4fad02b20ee08e95a29aa8379e51900f2fb79c05709f6ca8e996b4b10258fd`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
