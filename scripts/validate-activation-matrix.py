#!/usr/bin/env python3
"""Validate the cross-discipline routing contract in docs/activation-matrix.json.

The matrix records which discipline should own a realistic request. It exists
because consolidating many skills into a few can silently drop an absorbed
trigger: the guidance still ships, but nothing routes to it any more. This
checker enforces that every superseded slug stays reachable and that the matrix
itself stays well formed.

It deliberately does not call a model. Running the cases and recording observed
behavior is the manual workflow in docs/review-scenarios.md.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
MATRIX_PATH = "docs/activation-matrix.json"
DEPRECATED_PATH = "docs/deprecated-skills.json"
NO_OWNER = "none"
CASE_FIELDS = {"covers", "name", "owner", "prompt"}
MINIMUM_CASES_PER_DISCIPLINE = 3
MINIMUM_CONTROLS = 2
NAME_PATTERN = re.compile(r"^[a-z][a-z0-9-]*$")


def load_json(relative: str, errors: list[str]) -> object | None:
    path = REPOSITORY_ROOT / relative
    if not path.is_file():
        errors.append(f"{relative}: missing")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"{relative}: invalid JSON: {error.msg}")
        return None


def published_disciplines(deprecated: set[str]) -> set[str]:
    return {
        path.parent.name
        for path in SKILLS_ROOT.glob("*/SKILL.md")
        if path.parent.name not in deprecated
    }


def validate_cases(
    cases: object,
    disciplines: set[str],
    deprecated: set[str],
    errors: list[str],
) -> None:
    if not isinstance(cases, list) or not cases:
        errors.append(f"{MATRIX_PATH}: cases must be a non-empty array")
        return

    seen_names: set[str] = set()
    seen_prompts: dict[str, str] = {}
    owner_counts: dict[str, int] = {}
    covered: set[str] = set()

    for index, case in enumerate(cases):
        location = f"{MATRIX_PATH}: cases[{index}]"
        if not isinstance(case, dict) or set(case) != CASE_FIELDS:
            errors.append(
                f"{location} keys must be exactly ['covers', 'name', 'owner', 'prompt']"
            )
            continue

        name, prompt, owner, covers = (
            case["name"],
            case["prompt"],
            case["owner"],
            case["covers"],
        )

        if not isinstance(name, str) or not NAME_PATTERN.match(name):
            errors.append(f"{location}.name must be a lowercase kebab-case identifier")
        elif name in seen_names:
            errors.append(f"{location}.name duplicates {name!r}")
        else:
            seen_names.add(name)

        if not isinstance(prompt, str) or not prompt.strip():
            errors.append(f"{location}.prompt must be a non-empty string")
        else:
            normalized = " ".join(prompt.split()).casefold()
            if normalized in seen_prompts:
                errors.append(
                    f"{location}.prompt duplicates the prompt in "
                    f"{seen_prompts[normalized]!r}; one request cannot have two owners"
                )
            else:
                seen_prompts[normalized] = name if isinstance(name, str) else location

        if not isinstance(owner, str) or (
            owner != NO_OWNER and owner not in disciplines
        ):
            errors.append(
                f"{location}.owner must be {NO_OWNER!r} or a published discipline; "
                f"got {owner!r}"
            )
        elif isinstance(owner, str):
            owner_counts[owner] = owner_counts.get(owner, 0) + 1

        if not isinstance(covers, list) or not all(
            isinstance(slug, str) for slug in covers
        ):
            errors.append(f"{location}.covers must be an array of strings")
            continue

        if covers and owner == NO_OWNER:
            errors.append(
                f"{location}: a control case cannot cover a superseded slug"
            )
        for slug in covers:
            if slug not in deprecated:
                errors.append(
                    f"{location}.covers names {slug!r}, which is not a superseded "
                    f"slug in {DEPRECATED_PATH}"
                )
            elif slug in covered:
                errors.append(f"{location}.covers repeats {slug!r} from an earlier case")
            else:
                covered.add(slug)

    for discipline in sorted(disciplines):
        count = owner_counts.get(discipline, 0)
        if count < MINIMUM_CASES_PER_DISCIPLINE:
            errors.append(
                f"{MATRIX_PATH}: {discipline} owns {count} cases; at least "
                f"{MINIMUM_CASES_PER_DISCIPLINE} are required so a single reworded "
                "trigger cannot pass unnoticed"
            )

    controls = owner_counts.get(NO_OWNER, 0)
    if controls < MINIMUM_CONTROLS:
        errors.append(
            f"{MATRIX_PATH}: {controls} control cases with owner {NO_OWNER!r}; at "
            f"least {MINIMUM_CONTROLS} are required to detect over-triggering"
        )

    for slug in sorted(deprecated - covered):
        errors.append(
            f"{MATRIX_PATH}: superseded slug {slug!r} is not covered by any case; "
            "its absorbed trigger would be untested"
        )


def main() -> int:
    errors: list[str] = []

    deprecated_payload = load_json(DEPRECATED_PATH, errors)
    deprecated: set[str] = set()
    if isinstance(deprecated_payload, dict) and isinstance(
        deprecated_payload.get("deprecated"), dict
    ):
        deprecated = set(deprecated_payload["deprecated"])

    matrix = load_json(MATRIX_PATH, errors)
    if isinstance(matrix, dict):
        if matrix.get("version") != 1:
            errors.append(f"{MATRIX_PATH}: version must be 1")
        if not isinstance(matrix.get("note"), str) or not matrix["note"].strip():
            errors.append(f"{MATRIX_PATH}: note must explain what the matrix is for")
        validate_cases(
            matrix.get("cases"), published_disciplines(deprecated), deprecated, errors
        )
    elif matrix is not None:
        errors.append(f"{MATRIX_PATH}: top level must be an object")

    if errors:
        print("Activation matrix validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    cases = matrix["cases"]
    owners = {case["owner"] for case in cases}
    print(
        f"Activation matrix validated: {len(cases)} routing cases across "
        f"{len(owners - {NO_OWNER})} disciplines, every superseded slug covered; "
        "model behavior is not executed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
