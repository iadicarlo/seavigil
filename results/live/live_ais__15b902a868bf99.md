# Incident `live_ais__15b902a868bf99`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (inside a no-take reserve)
- **EEZ:** Australian Exclusive Economic Zone (Australia)
- **Authorization:** Flag unknown; authorization not checkable
- **Vessel:** DIAMAX3  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-17T11:29:01.000Z → 2026-10-23T04:44:20.000Z
- **Gap:** 137.3 h dark, 128.0 nm offshore
- **Where:** -31.164, 156.281

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 128 nm offshore for 137 h
- satellite-confirmed AIS gap (GFW Events)

## Could be innocent

Going dark is frequently benign: in open water, where gaps are commonly protecting a fishing ground or waiting out weather. It is most actionable inside or beside a closed zone.

## Caveats

- IUU match is by name only; IUU vessels reuse names, so confirm the identity.
- AIS gaps can be reception loss, not always intentional disabling.
- The position is where AIS dropped; the path while dark is unknown.
- An inspection lead from GFW Events, not proof of illegal activity.

## Provenance & integrity

- NOAA Marine Cadastre AIS (marinecadastre.gov/ais (vessel positions)). US public domain.
- WDPA / WD-OECM (World Database on Protected Areas) (UNEP-WCMC and IUCN (2026), June 2026). Protected Planet Terms of Use (non-commercial, display-only).
- Marine Regions Exclusive Economic Zones v12 (Flanders Marine Institute (2024), DOI 10.14284/632). CC BY 4.0.
- **Integrity (SHA-256 of canonical facts):** `6f204bd4bb0660d68026e3f29f9a1a0c9fc9c98dfd9693bab936dc396bd187f7`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
