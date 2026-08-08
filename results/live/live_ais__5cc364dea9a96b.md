# Incident `live_ais__5cc364dea9a96b`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Ghanaian Exclusive Economic Zone (Ghana) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: NEAFC, NPFC  ·  IMO 8834483
- **Vessel:** 🇷🇺 KAPITAN PRYAKHA  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-02T11:36:08.000Z → 2026-08-03T19:24:15.000Z
- **Gap:** 31.8 h dark, 146.0 nm offshore
- **Where:** 2.820, -3.097

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 146 nm offshore for 32 h
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
- **Integrity (SHA-256 of canonical facts):** `2ec55e82a3e14854021df5adf75b6d59239b079850ae98370815274191828fbb`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
