# Incident `live_ais__4c4e8a8c97f88c`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Nigerian Exclusive Economic Zone (Nigeria)
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC, NEAFC, SPRFMO, WCPFC  ·  IMO 9163403
- **Vessel:** SIERRA LAUREL  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-28T07:40:24.000Z → 2026-06-29T22:45:30.000Z
- **Gap:** 39.1 h dark, 105.0 nm offshore
- **Where:** 3.399, 3.076

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 105 nm offshore for 39 h
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
- **Integrity (SHA-256 of canonical facts):** `e40d54f8b4d3cdd44ff70b8b09b9a299553fa6243dfc564d81edb8ef65769610`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
