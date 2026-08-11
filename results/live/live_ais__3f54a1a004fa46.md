# Incident `live_ais__3f54a1a004fa46`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Ghanaian Exclusive Economic Zone (Ghana) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, IOTC, SPRFMO, WCPFC  ·  IMO 9019652
- **Vessel:** 🇱🇷 ACONCAGUA BAY  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-05T13:06:18.000Z → 2026-08-06T06:40:43.000Z
- **Gap:** 17.6 h dark, 124.0 nm offshore
- **Where:** 3.495, -0.099

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 124 nm offshore for 18 h
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
- **Integrity (SHA-256 of canonical facts):** `d73def04ce183df46e36f0467d32b2ec85331a09579c40c3ab508a44a3523438`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
