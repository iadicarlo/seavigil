# Incident `live_ais__c64cc142035b35`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** Marshallese Exclusive Economic Zone (Marshall Islands) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇨🇳 CFA25-06 82%  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-02T01:39:57.000Z → 2026-07-02T22:19:13.000Z
- **Gap:** 20.7 h dark, 79.0 nm offshore
- **Where:** 3.640, 169.588

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 79 nm offshore for 21 h
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
- **Integrity (SHA-256 of canonical facts):** `cf6655e33e43375caa24df7275e261c6241fcf2e53be04e3e4a7692f32f8452b`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
