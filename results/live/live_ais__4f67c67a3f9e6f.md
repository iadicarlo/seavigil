# Incident `live_ais__4f67c67a3f9e6f`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** United States Exclusive Economic Zone (Northern Mariana Islands) (United States) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇸🇴 `66619`  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-23T17:28:05.000Z → 2026-07-27T03:18:29.000Z
- **Gap:** 81.8 h dark, 302.0 nm offshore
- **Where:** 19.263, 146.326

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 302 nm offshore for 82 h
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
- **Integrity (SHA-256 of canonical facts):** `d2df86c4f2e97b448031a0a5bd0030c6f893110cd193d717d1416ede1e761017`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
