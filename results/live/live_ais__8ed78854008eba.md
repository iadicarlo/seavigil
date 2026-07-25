# Incident `live_ais__8ed78854008eba`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Costa Rican Exclusive Economic Zone (Costa Rica) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: IATTC  ·  IMO 9017850
- **Vessel:** 🇻🇪 F/V VIA MISTRAL  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-15T10:42:22.000Z → 2026-07-21T02:45:58.000Z
- **Gap:** 136.1 h dark, 89.0 nm offshore
- **Where:** 8.142, -85.122

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 89 nm offshore for 136 h
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
- **Integrity (SHA-256 of canonical facts):** `ef08753205d86ef9e50f9dd6da55dc51227f80eede1e59f91ea81097bd62a10c`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
