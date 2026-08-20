# Incident `live_ais__ba3938aafc13ed`

- **MPA:** AIS disabling (going dark)
- **Severity:** HIGH (foreign vessel, no authorization on record)
- **EEZ:** Seychellois Exclusive Economic Zone (Seychelles) -- FOREIGN-flagged vessel
- **Authorization:** No public authorization record (check coastal state)  ·  IMO 9364447
- **Vessel:** 🇭🇰 MINOAN GLORY  ·  **signal:** AIS gap
- **When (UTC):** 2026-08-14T19:51:04.000Z → 2026-08-16T05:33:19.000Z
- **Gap:** 33.7 h dark, 178.0 nm offshore
- **Where:** -5.726, 49.539

## Why this was flagged

_GFW Events gaps dataset (satellite AIS).._

- went dark 178 nm offshore for 34 h
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
- **Integrity (SHA-256 of canonical facts):** `272d642a2fa3b7bfe219c5d1a915a17ac379631b974d6181e2f375244f7af134`
- **Evidence schema:** seavigil-evidence-1.0

_Apparent activity and an inspection lead, not proof of illegality. AIS and SAR evidence have known coverage gaps and spoofing risks; verify against authoritative sources before any enforcement action._
