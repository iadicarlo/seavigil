"""Deliver high-severity SeaVigil incidents to an operator: a webhook push, so a lead reaches someone
who can act instead of only being drawn on a map. This is the operational half of the system: a
detection nobody is paged about is a demo, not a tool.

It posts only NEW high-severity incidents (deduplicated against data/alert_state.json, so a six-hourly
cron does not re-alert the same lead), as a generic JSON payload with a Slack/Discord-compatible
``text`` field plus a structured ``incidents`` array for custom consumers. The webhook URL comes from
the SEAVIGIL_WEBHOOK_URL environment variable (never committed). No URL set means delivery is skipped
with a clear log line, not silently; a configured webhook that fails raises.
"""

from __future__ import annotations

import json
import os
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "data" / "alert_state.json"
WEBHOOK_ENV = "SEAVIGIL_WEBHOOK_URL"


def _alertable(d: dict) -> bool:
    return (d.get("severity") or "").lower() == "high"


def _line(d: dict) -> str:
    """One scannable line for an incident."""
    lat, lon = d.get("centroid_lat"), d.get("centroid_lon")
    where = f"{abs(lat):.2f}{'N' if (lat or 0) >= 0 else 'S'} {abs(lon):.2f}{'E' if (lon or 0) >= 0 else 'W'}" \
        if lat is not None and lon is not None else (d.get("mpa_name") or "")
    eez = d.get("eez_iso_sov") or ""
    flag = d.get("flag") or ""
    foreign = " foreign" if d.get("eez_foreign") else ""
    why = ""
    if d.get("iuu_match"):
        m = d["iuu_match"]
        why = f" | {'ON' if d.get('iuu_listed') else 'possible'} {m['source']} IUU list ({m.get('listed_name') or '?'})"
    elif d.get("severity_reason"):
        why = f" | {d['severity_reason']}"
    return f"HIGH {d.get('type', 'incident')} | {where}" \
           f"{(' | EEZ ' + eez) if eez else ''}{(' flag ' + flag + foreign) if flag else ''}{why}"


def _compact(d: dict) -> dict:
    return {k: d.get(k) for k in (
        "incident_id", "type", "severity", "severity_reason", "centroid_lat", "centroid_lon",
        "eez_iso_sov", "eez_foreign", "flag", "ship_name", "vessel_id", "authorization_status",
        "iuu_listed", "iuu_match", "time_start_utc")}


def _payload(items: list[dict]) -> dict:
    head = f"SeaVigil: {len(items)} new high-severity IUU lead(s)"
    body = "\n".join(_line(d) for d in items[:20])
    extra = "" if len(items) <= 20 else f"\n... and {len(items) - 20} more"
    return {"text": f"{head}\n{body}{extra}", "count": len(items),
            "incidents": [_compact(d) for d in items[:50]]}


def _load_state(path) -> dict:
    p = Path(path)
    return json.loads(p.read_text()) if p.exists() else {"sent": {}}


def _save_state(path, sent: dict, keep_days: int) -> None:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=keep_days)).isoformat()
    pruned = {k: v for k, v in sent.items() if v >= cutoff}
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps({"sent": pruned}, indent=0, sort_keys=True))


def _post(url: str, payload: dict) -> None:
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json", "User-Agent": "SeaVigil/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:   # raises on non-2xx / network error
        r.read()


def notify_incidents(dossiers: list[dict], webhook_url: str | None = None,
                     state_path=STATE, dry_run: bool = False, keep_days: int = 45) -> int:
    """Push new high-severity incidents to the webhook. Returns the number delivered (or shown)."""
    url = webhook_url or os.environ.get(WEBHOOK_ENV) or ""
    alertable = [d for d in dossiers if _alertable(d)]
    state = _load_state(state_path)
    sent = dict(state.get("sent", {}))
    fresh = [d for d in alertable if d.get("incident_id") and d["incident_id"] not in sent]
    if not fresh:
        print(f"notify: {len(alertable)} high-severity incident(s), 0 new to deliver")
        return 0
    if not url and not dry_run:
        print(f"notify: {len(fresh)} new high-severity incident(s), but {WEBHOOK_ENV} is not set; "
              f"not delivered (set the webhook to enable alerting)")
        return 0
    payload = _payload(fresh)
    if dry_run:
        print("notify (dry-run) would deliver:\n" + json.dumps(payload, indent=1)[:1600])
    else:
        _post(url, payload)
        print(f"notify: delivered {len(fresh)} new high-severity incident(s) to the webhook")
    now = datetime.now(timezone.utc).isoformat()
    for d in fresh:
        sent[d["incident_id"]] = now
    _save_state(state_path, sent, keep_days)
    return len(fresh)
