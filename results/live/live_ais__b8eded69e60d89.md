# Incident `live_ais__b8eded69e60d89`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, authorization lapsed)
- **EEZ:** Ivorian Exclusive Economic Zone (Ivory Coast) -- FOREIGN-flagged vessel
- **Authorization:** Authorization lapsed before this date: ICCAT, WCPFC  ·  IMO 9014444
- **Vessel:** 🇧🇸 PRINCE OF SEAS  ·  **signal:** AIS gap
- **When (UTC):** 2026-07-09T13:56:45.000Z → 2026-07-20T14:51:25.000Z
- **Gap:** 264.9 h dark, 172.0 nm offshore
- **Where:** 2.715, -4.574

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 172 nm offshore for 265 h
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
- **Integrity (SHA-256 of canonical facts):** `c773ac869e59ee60b9039fa0e210790feb051c5a398b234c4d0f541c951ba1ef`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
