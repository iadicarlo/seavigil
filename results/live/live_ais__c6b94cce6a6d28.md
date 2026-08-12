# Incident `live_ais__c6b94cce6a6d28`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Micronesian Exclusive Economic Zone (Micronesia) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9587908
- **Vessel:** 🇸🇬 BOGA INDAH  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-02T15:35:06.000Z → 2026-08-06T18:22:48.000Z
- **Gap:** 98.8 h dark, 293.0 nm offshore
- **Where:** 10.572, 141.560

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 293 nm offshore for 99 h
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
- **Integrity (SHA-256 of canonical facts):** `2f37fce7fd7f21ea844d424f3e71e64a67d8f3fc5a0ffba44e7360ad38b97d0f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
