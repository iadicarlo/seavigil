# Incident `live_ais__8dbdc6071e4c78`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (inside a no-take reserve)
- **EEZ:** Australian Exclusive Economic Zone (Australia)
- **Authorization:** Flag unknown; authorization not checkable
- **Vessel:** PAPANUI4  ·  **signal:** AIS gap
- **When (UTC):** 2026-10-17T11:29:56.000Z → 2026-10-23T08:05:19.000Z
- **Gap:** 140.6 h dark, 143.0 nm offshore
- **Where:** -30.987, 156.444

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 143 nm offshore for 141 h
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
- **Integrity (SHA-256 of canonical facts):** `bfe8743d64aeb88e6eabfff6cb6b532c3148ce70dcaf035c1024415ee2346064`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
