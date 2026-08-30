# Incident `live_ais__1d3da58edbe18a`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Joint regime area: São Tomé and Principe / Nigeria (São Tomé and Principe) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9337810
- **Vessel:** 🇵🇦 PANTELIS  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-24T07:37:13.000Z → 2026-08-26T00:01:38.000Z
- **Gap:** 40.4 h dark, 148.0 nm offshore
- **Where:** 2.190, 5.824

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 148 nm offshore for 40 h
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
- **Integrity (SHA-256 of canonical facts):** `d323b1dcc196ecbc524107a5055a98dd22e693450b475306902b6a30b499cb8f`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
