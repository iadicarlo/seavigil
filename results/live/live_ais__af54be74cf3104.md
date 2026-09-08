# Incident `live_ais__af54be74cf3104`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Ecuadorian Exclusive Economic Zone (Ecuador) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: IOTC  ·  IMO 9476238
- **Vessel:** 🇷🇪 RIA DE ALDAN  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-01T11:34:49.000Z → 2026-09-04T10:53:36.000Z
- **Gap:** 71.3 h dark, 64.0 nm offshore
- **Where:** 0.548, -83.719

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 64 nm offshore for 71 h
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
- **Integrity (SHA-256 of canonical facts):** `020fb262c9a9bc7d47d32d4c1d1e4e46e926e69d865c0e3282d1ab38cb6e9b34`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
