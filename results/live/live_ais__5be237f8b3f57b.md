# Incident `live_ais__5be237f8b3f57b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Costa Rican Exclusive Economic Zone (Costa Rica) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: IATTC, ICCAT  ·  IMO 7407908
- **Vessel:** 🇻🇪 VENTUARI  ·  **signal:** AIS gap
- **When (UTC):** 2026-06-22T11:37:40.000Z → 2026-06-29T01:50:48.000Z
- **Gap:** 158.2 h dark, 224.0 nm offshore
- **Where:** 3.819, -87.881

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 224 nm offshore for 158 h
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
- **Integrity (SHA-256 of canonical facts):** `aab72986d3b77190bdd319d6572a030594e37eecc0fa2960e48ef34bac3e9d9f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
