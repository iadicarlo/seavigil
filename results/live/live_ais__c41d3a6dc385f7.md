# Incident `live_ais__c41d3a6dc385f7`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** Kiribati Exclusive Economic Zone (Phoenix Group) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇹🇫 AB5-1-90%  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-20T02:51:17.000Z → 2026-08-21T01:02:22.000Z
- **Gap:** 22.2 h dark, 173.0 nm offshore
- **Where:** -0.206, -170.105

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 173 nm offshore for 22 h
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
- **Integrity (SHA-256 of canonical facts):** `28f85cab61e11752ca71dd449604e64a5743f27f9e988033158ebf906941e56e`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
