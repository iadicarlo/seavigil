# Incident `live_ais__3d91bced0f844f`

- **MPA:** AIS disabling (going dark)
- **Severity:** MEDIUM (foreign vessel, authorization unverified)
- **EEZ:** Kiribati Exclusive Economic Zone (Line Group) (Kiribati) -- FOREIGN-flagged vessel
- **Authorization:** No vessel identity; authorization not checkable
- **Vessel:** 🇹🇫 AB5-1-76%  ·  **signal:** AIS gap
- **When (UTC):** 2026-09-28T03:47:34.000Z → 2026-09-29T02:40:49.000Z
- **Gap:** 22.9 h dark, 149.0 nm offshore
- **Where:** -7.949, -150.397

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 149 nm offshore for 23 h
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
- **Integrity (SHA-256 of canonical facts):** `9f1b210dc5ec11166a6dcf28538c47a1c4f3190caf7ca89de3b91237b1577acb`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
