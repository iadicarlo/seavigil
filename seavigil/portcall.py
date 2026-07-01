"""Port-call provenance: where a flagged carrier next lands the catch.

An at-sea encounter, a fishing vessel offloading to a refrigerated carrier, only
matters to an enforcer if you can follow the fish. This resolves a carrier's MMSI to
its Global Fishing Watch identity and finds the next port it entered after the
encounter, marking ports that are documented transshipment / distant-water landing
hubs where high offload volume and uneven port-state control let catch of mixed
provenance enter the legal market. That turns an at-sea blip into a port-state-measures
(PSMA) inspection lead: "this carrier next docked at Montevideo, nine days later." It is
a lead to check, never proof, and naming a hub describes throughput, not an accusation
against a port authority.

Consumes GFW's published port-visit events (CC BY-NC), the same consume-not-recompute
pattern as the SAR dark fleet and the encounters themselves. Runs at build time and
caches every lookup to data/portcall_cache.json, so the static site carries the chain
and rebuilds neither re-hit the API nor need a token.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

_BASE = "https://gateway.api.globalfishingwatch.org/v3"
_UA = "SeaVigil/1.0 (open IUU research; seavigil.org)"
ROOT = Path(__file__).resolve().parent.parent
CACHE_PATH = ROOT / "data" / "portcall_cache.json"

# Documented transshipment / distant-water landing hubs: ports repeatedly named in the
# transshipment and IUU literature (Global Fishing Watch, Pew, EJF, C4ADS) for high
# offload throughput, not a judgement on any port authority. Matched by GFW anchorage name.
PERMISSIVE_HUBS = {
    "MONTEVIDEO": "UY, Southwest Atlantic squid + toothfish landing hub",
    "LAS PALMAS": "ES, main West Africa transshipment gateway",
    "CALLAO": "PE, distant-water fleet landing",
    "CHIMBOTE": "PE, distant-water fleet landing",
    "PAITA": "PE, distant-water fleet landing",
    "ZHOUSHAN": "CN, largest distant-water fleet base",
    "SHIDAO": "CN, distant-water fleet base",
    "DALIAN": "CN, distant-water fleet base",
    "BUSAN": "KR, distant-water fleet base",
    "VLADIVOSTOK": "RU, Russian Far East fleet base, high transshipment throughput",
    "NAKHODKA": "RU, Russian Far East fleet base",
    "BANGKOK": "TH, historic transshipment / processing hub",
    "SAMUT PRAKAN": "TH, historic transshipment / processing hub",
    "WALVIS BAY": "NA, Southeast Atlantic landing",
    "ABIDJAN": "CI, West Africa landing",
    "TEMA": "GH, West Africa landing",
    "DAKAR": "SN, West Africa landing",
    "PORT LOUIS": "MU, Indian Ocean transshipment hub",
    "GENERAL SANTOS": "PH, tuna transshipment hub",
}


def load_token(token: str | None = None) -> str | None:
    """GFW token from the argument, the environment, or a gitignored .env (never committed)."""
    if token:
        return token
    tok = os.environ.get("GFW_TOKEN")
    if tok:
        return tok
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("GFW_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def _get(path: str, token: str, tries: int = 4, pace: float = 1.2):
    """GET a GFW v3 endpoint, backing off on the hard 429 rate limit. Returns parsed JSON."""
    req = urllib.request.Request(f"{_BASE}{path}",
                                 headers={"Authorization": f"Bearer {token}", "User-Agent": _UA})
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                time.sleep(pace)  # stay under the rate limit between successful calls too
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < tries - 1:
                time.sleep(2.5 * (attempt + 1))
                continue
            raise
    return None


def _load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def _save_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=0, sort_keys=True))


def _resolve_vessel_id(mmsi: str, token: str) -> str | None:
    # note: /vessels/search rejects an offset param (422); only /events requires one
    q = urllib.parse.urlencode({"query": mmsi,
                                "datasets[0]": "public-global-vessel-identity:latest",
                                "limit": 1})
    body = _get(f"/vessels/search?{q}", token) or {}
    for ent in body.get("entries", []):
        sri = ent.get("selfReportedInfo") or []
        vid = (sri[0].get("id") if sri else None) or ent.get("id")
        if vid:
            return vid
    return None


def _port_visits(vid: str, after_iso: str, token: str) -> list[dict]:
    q = urllib.parse.urlencode({"datasets[0]": "public-global-port-visits-events:latest",
                                "vessels[0]": vid, "start-date": after_iso[:10],
                                "end-date": "2030-01-01", "limit": 50, "offset": 0,
                                "confidences[0]": 3, "confidences[1]": 4})
    body = _get(f"/events?{q}", token) or {}
    return body.get("entries", [])


def _anchorage(pv: dict) -> dict:
    """The port anchorage of a visit event: prefer the docked intermediate point, else the entry."""
    for key in ("intermediateAnchorage", "startAnchorage", "endAnchorage"):
        a = pv.get("port_visit", {}).get(key) or {}
        if a.get("name"):
            return a
    return {}


def next_port_call(mmsi: str, after_iso: str, token: str, cache: dict | None = None,
                   max_days: float = 60.0) -> dict | None:
    """The first port a carrier entered within ``max_days`` after ``after_iso``.

    Returns {name, flag, lat, lon, start, days_after, hub, hub_note} or None. The window
    matters for honesty: a carrier that only reaches port years later is a data gap, not the
    landing of this catch, so we do not claim it as provenance. Cached per (mmsi) so a build
    resolves each carrier once; the visit list is filtered by ``after_iso`` at call time, so
    the same cached carrier serves encounters at different dates.
    """
    if not (mmsi and after_iso and token):
        return None
    cache = _load_cache() if cache is None else cache
    key = str(mmsi)
    if key not in cache:
        try:
            vid = _resolve_vessel_id(key, token)
            visits = _port_visits(vid, after_iso, token) if vid else []
            cache[key] = {"vid": vid, "visits": [
                {"start": v.get("start"), **_anchorage(v)} for v in visits if _anchorage(v)]}
        except urllib.error.HTTPError as e:
            cache[key] = {"vid": None, "visits": [], "error": f"HTTP {e.code}"}
    entry = cache[key]

    after = after_iso[:19].replace(" ", "T")  # normalize CSV "date time" to GFW "dateTtime"
    nxt = None
    for v in sorted(entry.get("visits", []), key=lambda v: v.get("start") or ""):
        if (v.get("start") or "")[:19] > after:
            nxt = v
            break
    if not nxt:
        return None
    name = (nxt.get("name") or "").upper()
    try:
        from datetime import datetime
        d0 = datetime.fromisoformat(after.replace("Z", ""))
        d1 = datetime.fromisoformat((nxt["start"] or "")[:19].replace("Z", ""))
        days = round((d1 - d0).total_seconds() / 86400, 1)
    except (ValueError, TypeError, KeyError):
        days = None
    if days is not None and days > max_days:
        return None  # next recorded port is too far out to be this catch's landing
    return {"name": name.title(), "flag": nxt.get("flag"), "lat": nxt.get("lat"),
            "lon": nxt.get("lon"), "start": nxt.get("start"), "days_after": days,
            "hub": name in PERMISSIVE_HUBS, "hub_note": PERMISSIVE_HUBS.get(name)}


def enrich_encounters(dossiers: list[dict], token: str | None = None,
                      max_days: float = 60.0) -> int:
    """Add the carrier's next port call to each encounter dossier, in place.

    Sets a structured ``next_port`` field and appends a provenance line to the encounter's
    explanation drivers, so it surfaces in the popup (site._why), the markdown dossier and the
    download with no further wiring. Safe with no token or no network: it simply enriches
    nothing and the encounters build exactly as before.
    """
    token = load_token(token)
    if not token:
        return 0
    cache = _load_cache()
    n = 0
    for d in dossiers:
        if d.get("type") != "encounter":
            continue
        np_ = next_port_call(d.get("carrier_mmsi"), d.get("time_end_utc"), token, cache,
                             max_days=max_days)
        if not np_:
            continue
        d["next_port"] = np_
        expl = d.setdefault("explanation", {})
        expl.setdefault("drivers", []).append(driver_line(np_))
        n += 1
    _save_cache(cache)
    return n


def driver_line(np_: dict) -> str:
    """A one-line provenance driver for a dossier, e.g. for the encounter drivers list."""
    when = f", {np_['days_after']:.0f} days later" if np_.get("days_after") is not None else ""
    where = np_["name"] + (f" ({np_['flag']})" if np_.get("flag") else "")
    if np_.get("hub"):
        return f"carrier next entered {where}{when}: documented landing hub ({np_['hub_note']})"
    return f"carrier next entered port at {where}{when}"


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser(description="Resolve a carrier MMSI's next port call after a date")
    ap.add_argument("--mmsi", required=True)
    ap.add_argument("--after", required=True, help="ISO date/time the encounter ended")
    a = ap.parse_args()
    token = load_token()
    if not token:
        raise SystemExit("GFW_TOKEN not set")
    print(json.dumps(next_port_call(a.mmsi, a.after, token), indent=2))


if __name__ == "__main__":
    main()
