# Incident `live_ais__c035fefe71e774`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Japanese Exclusive Economic Zone (Japan) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: FFA, IATTC, ICCAT, IOTC, WCPFC  ·  IMO 9019315
- **Vessel:** 🇰🇷 ORYONG NO.723  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-09T17:44:58.000Z → 2026-10-12T09:55:24.000Z
- **Gap:** 64.2 h dark, 330.0 nm offshore
- **Where:** 21.931, 153.121

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 330 nm offshore for 64 h
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
- **Integrity (SHA-256 of canonical facts):** `6b1cac054f164f1a0bed47f87c14c8489327b6e76c3880d86740a1ed5693d255`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
