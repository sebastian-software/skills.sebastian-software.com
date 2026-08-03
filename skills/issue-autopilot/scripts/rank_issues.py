#!/usr/bin/env python3
"""Rank normalized GitHub/Linear issues with a deliberate recency bias."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PRIORITY_SCORES = {
    "urgent": 35,
    "high": 24,
    "medium": 12,
    "low": 3,
    "none": 0,
    "p0": 35,
    "p1": 24,
    "p2": 12,
    "p3": 3,
    "p4": 0,
    "0": 35,
    "1": 24,
    "2": 12,
    "3": 3,
    "4": 0,
}

LABEL_SCORES = {
    "critical": 42,
    "sev0": 42,
    "outage": 36,
    "data-loss": 34,
    "security": 28,
    "p0": 28,
    "sev1": 26,
    "customer-blocker": 25,
    "data-integrity": 24,
    "compliance": 22,
    "regression": 18,
    "bug": 12,
    "accessibility": 8,
    "performance": 7,
    "enhancement": 3,
    "documentation": 1,
    "cosmetic": -4,
}

CRITICAL_LABELS = {
    "critical",
    "sev0",
    "outage",
    "data-loss",
}


def parse_time(value: Any, field: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty ISO-8601 string")
    normalized = value.strip()
    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def bounded_dimension(issue: dict[str, Any], name: str) -> int:
    raw = issue.get(name, 0)
    if isinstance(raw, bool):
        raise ValueError(f"{issue.get('id', '<unknown>')}: {name} must be 0-5")
    try:
        value = int(raw)
    except (TypeError, ValueError) as exc:
        raise ValueError(
            f"{issue.get('id', '<unknown>')}: {name} must be 0-5"
        ) from exc
    if not 0 <= value <= 5:
        raise ValueError(f"{issue.get('id', '<unknown>')}: {name} must be 0-5")
    return value


def age_days(now: datetime, then: datetime) -> float:
    return max(0.0, (now - then).total_seconds() / 86400)


def recency_score(days: float) -> int:
    if days <= 2:
        return 18
    if days <= 7:
        return 14
    if days <= 14:
        return 10
    if days <= 30:
        return 6
    if days <= 90:
        return 2
    return 0


def activity_score(days: float) -> int:
    if days <= 2:
        return 6
    if days <= 7:
        return 3
    return 0


def normalize_priority(value: Any) -> str:
    if value is None:
        return "none"
    return str(value).strip().lower().replace(" ", "-")


def normalize_labels(value: Any) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError("labels must be an array")
    return sorted(
        {
            str(label).strip().lower().replace("_", "-").replace(" ", "-")
            for label in value
            if str(label).strip()
        }
    )


def rank_issue(issue: dict[str, Any], now: datetime) -> dict[str, Any]:
    issue_id = str(issue.get("id", "")).strip()
    title = str(issue.get("title", "")).strip()
    if not issue_id or not title:
        raise ValueError("every issue requires non-empty id and title")

    created = parse_time(issue.get("created_at"), f"{issue_id}.created_at")
    updated_raw = issue.get("updated_at") or issue.get("created_at")
    updated = parse_time(updated_raw, f"{issue_id}.updated_at")
    priority = normalize_priority(issue.get("priority"))
    labels = normalize_labels(issue.get("labels"))
    impact = bounded_dimension(issue, "impact")
    urgency = bounded_dimension(issue, "urgency")
    relevance = bounded_dimension(issue, "relevance")

    reasons: list[str] = []
    score = 0

    priority_points = PRIORITY_SCORES.get(priority, 0)
    if priority_points:
        score += priority_points
        reasons.append(f"priority {priority} +{priority_points}")

    label_points = sum(LABEL_SCORES.get(label, 0) for label in labels)
    if label_points:
        score += label_points
        reasons.append(f"risk labels {label_points:+d}")

    dimensions = impact * 5 + urgency * 5 + relevance * 4
    score += dimensions
    reasons.append(
        f"impact/urgency/relevance {impact}/{urgency}/{relevance} +{dimensions}"
    )

    created_points = recency_score(age_days(now, created))
    score += created_points
    if created_points:
        reasons.append(f"new issue +{created_points}")

    updated_points = activity_score(age_days(now, updated))
    score += updated_points
    if updated_points:
        reasons.append(f"recent activity +{updated_points}")

    if bool(issue.get("blocks_others")):
        score += 15
        reasons.append("unblocks work +15")

    blocked = bool(issue.get("blocked"))
    if blocked:
        group = "Blocked"
        reasons.append("externally blocked")
    elif CRITICAL_LABELS.intersection(labels) or score >= 115:
        group = "Immediate"
    elif score >= 80:
        group = "Urgent"
    elif score >= 60:
        group = "Next"
    else:
        group = "Later"

    return {
        **issue,
        "id": issue_id,
        "title": title,
        "labels": labels,
        "priority": priority,
        "created_at": created.isoformat().replace("+00:00", "Z"),
        "updated_at": updated.isoformat().replace("+00:00", "Z"),
        "score": score,
        "group": group,
        "ranking_reasons": reasons,
        "_created_sort": created.timestamp(),
        "_updated_sort": updated.timestamp(),
    }


def load_issues(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    issues = payload.get("issues") if isinstance(payload, dict) else payload
    if not isinstance(issues, list):
        raise ValueError("input must be an array or an object with an issues array")
    if not all(isinstance(issue, dict) for issue in issues):
        raise ValueError("every issue must be an object")
    return issues


def sort_ranked(ranked: list[dict[str, Any]]) -> list[dict[str, Any]]:
    group_order = {
        "Immediate": 0,
        "Urgent": 1,
        "Next": 2,
        "Later": 3,
        "Blocked": 4,
    }
    return sorted(
        ranked,
        key=lambda item: (
            group_order[item["group"]],
            -item["score"],
            -item["_created_sort"],
            -item["_updated_sort"],
            item["id"],
        ),
    )


def clean_for_json(issue: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in issue.items() if not key.startswith("_")}


def markdown(ranked: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    for group in ("Immediate", "Urgent", "Next", "Later", "Blocked"):
        items = [issue for issue in ranked if issue["group"] == group]
        if not items:
            continue
        lines.extend((f"## {group}", ""))
        for issue in items:
            url = str(issue.get("url", "")).strip()
            label = f"[{issue['id']}]({url})" if url else issue["id"]
            reasons = "; ".join(issue["ranking_reasons"])
            lines.append(
                f"- {label} — {issue['title']} "
                f"(score {issue['score']}: {reasons})"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + ("\n" if lines else "")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="normalized issue JSON")
    parser.add_argument(
        "--format", choices=("json", "markdown"), default="markdown"
    )
    parser.add_argument(
        "--now",
        help="ISO-8601 snapshot time (defaults to current UTC time)",
    )
    args = parser.parse_args()

    try:
        now = parse_time(args.now, "--now") if args.now else datetime.now(timezone.utc)
        ranked = sort_ranked(
            [rank_issue(issue, now) for issue in load_issues(args.input)]
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        json.dump(
            [clean_for_json(issue) for issue in ranked],
            sys.stdout,
            indent=2,
            ensure_ascii=False,
        )
        sys.stdout.write("\n")
    else:
        sys.stdout.write(markdown(ranked))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
