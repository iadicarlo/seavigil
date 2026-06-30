"""Human triage: the VERIFY stage of the pipeline.

Detection, adjudication and fusion produce ranked leads; an operational system also needs a person to
say "yes, investigate" or "no, false alarm", and it needs to remember and learn from that. This is that
record. An operator reviews a fused case and sets a status; the decision is stored with who, when, a
note, and a fingerprint of the case at review time, so it is auditable and goes stale if the underlying
case materially changes. Two payoffs: the map can show what has been triaged, and the confirm / dismiss
decisions become the real labelled set that turns the false-positive rate from an estimate into a
measurement (closing the loop back to MEASURE).

State lives in data/review_state.json (committed, so the audit trail travels with the repo). No backend
needed: an operator triages with scripts/review.py and the decisions are applied at build time.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_PATH = ROOT / "data" / "review_state.json"
STATUSES = ("confirmed", "dismissed", "escalated", "watch")


def case_fingerprint(case: dict) -> str:
    """A short hash of the material content, so a review is flagged stale if the case changes."""
    key = json.dumps([
        case.get("severity"), round(case.get("confidence") or 0, 2),
        round(case.get("centroid_lat") or 0, 3), round(case.get("centroid_lon") or 0, 3),
        sorted(str(m.get("incident_id")) for m in case.get("members", [])),
    ], sort_keys=True)
    return hashlib.sha1(key.encode()).hexdigest()[:12]  # noqa: S324 (fingerprint, not security)


def load_state(path: str | Path = STATE_PATH) -> dict:
    p = Path(path)
    return json.loads(p.read_text()) if p.exists() else {"reviews": {}}


def save_state(state: dict, path: str | Path = STATE_PATH) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(state, indent=1, sort_keys=True))


def set_review(state: dict, case_id: str, status: str, fingerprint: str,
               by: str = "operator", note: str = "") -> dict:
    if status not in STATUSES:
        raise ValueError(f"status must be one of {STATUSES}, got {status!r}")
    state.setdefault("reviews", {})[case_id] = {
        "status": status, "by": by or "operator", "note": note or "",
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"), "fingerprint": fingerprint,
    }
    return state


def apply_review(cases: list[dict], state: dict | None = None) -> int:
    """Annotate cases in place with review_status (+ who/when/note/stale). Returns the reviewed count."""
    reviews = (state or load_state()).get("reviews", {})
    reviewed = 0
    for c in cases:
        r = reviews.get(c.get("case_id"))
        if not r:
            c["review_status"] = "new"
            continue
        reviewed += 1
        c["review_status"] = r["status"]
        c["review_by"] = r.get("by", "")
        c["review_note"] = r.get("note", "")
        c["review_ts"] = r.get("ts", "")
        c["review_stale"] = r.get("fingerprint") != case_fingerprint(c)
    return reviewed


def precision_from_reviews(cases: list[dict]) -> dict:
    """Operator-derived accuracy: once humans confirm/dismiss, the false-positive rate is measured,
    not estimated. Counts escalated as confirmed (a real lead worth acting on)."""
    s = lambda st: sum(1 for c in cases if c.get("review_status") == st)  # noqa: E731
    confirmed, dismissed, escalated, watch = s("confirmed"), s("dismissed"), s("escalated"), s("watch")
    positive = confirmed + escalated
    judged = positive + dismissed
    return {
        "total_cases": len(cases),
        "reviewed": confirmed + dismissed + escalated + watch,
        "confirmed": confirmed, "dismissed": dismissed, "escalated": escalated, "watch": watch,
        "judged": judged,
        "operator_precision": round(positive / judged, 3) if judged else None,
        "false_positive_rate": round(dismissed / judged, 3) if judged else None,
    }
