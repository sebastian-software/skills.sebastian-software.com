#!/usr/bin/env python3
"""Prepare and validate recorded manual reviews of unrun skill scenarios.

This tool deliberately does not call a model or infer whether an answer is good.
It makes the human review record complete, traceable, and tied to the scenario
fixtures that CI validates structurally.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
RUNTIME_FIELDS = ("agent", "model", "sampling")
RESULT_FIELDS = ("grading_evidence", "name", "response", "result")
RESULT_VALUES = {"pass", "fail"}


def load_json(path: Path, label: str, errors: list[str]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{label}: file not found")
    except UnicodeDecodeError as error:
        errors.append(f"{label}: invalid UTF-8: {error.reason}")
    except OSError as error:
        errors.append(f"{label}: could not read file: {error.strerror or error}")
    except json.JSONDecodeError as error:
        errors.append(f"{label}: invalid JSON: {error.msg}")
    return None


def load_scenarios(skill_directory: Path, errors: list[str]) -> set[str]:
    path = skill_directory / "evals" / "evals.json"
    payload = load_json(path, str(path), errors)
    evaluations = payload.get("evals") if isinstance(payload, dict) else None
    if not isinstance(evaluations, list):
        if payload is not None:
            errors.append(f"{path}: evals must be an array")
        return set()

    names: set[str] = set()
    for index, evaluation in enumerate(evaluations):
        name = evaluation.get("name") if isinstance(evaluation, dict) else None
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{path}: evals[{index}].name must be a non-empty string")
            continue
        if name in names:
            errors.append(f"{path}: evals[{index}].name duplicates {name!r}")
        names.add(name)
    return names


def review_template(skill: str, scenario_names: set[str]) -> dict[str, object]:
    return {
        "skill": skill,
        "runtime": {
            "agent": "replace with the reviewed agent/runtime",
            "model": "replace with the model and version",
            "sampling": "replace with temperature, seed, and other relevant settings",
        },
        "results": [
            {
                "name": name,
                "response": "",
                "result": "pass",
                "grading_evidence": "",
            }
            for name in sorted(scenario_names)
        ],
    }


def validate_review_report(
    payload: object,
    skill: str,
    scenario_names: set[str],
    require_failure: bool,
) -> tuple[list[str], dict[str, int]]:
    """Validate traceability fields, not the semantic quality of responses."""
    errors: list[str] = []
    counts = {"pass": 0, "fail": 0}
    if not isinstance(payload, dict) or set(payload) != {"results", "runtime", "skill"}:
        return (
            ["report: top-level keys must be exactly ['results', 'runtime', 'skill']"],
            counts,
        )
    if payload["skill"] != skill:
        errors.append(f"report.skill must be {skill!r}")

    runtime = payload["runtime"]
    if not isinstance(runtime, dict) or set(runtime) != set(RUNTIME_FIELDS):
        errors.append(
            "report.runtime keys must be exactly ['agent', 'model', 'sampling']"
        )
    elif any(
        not isinstance(runtime[field], str) or not runtime[field].strip()
        for field in RUNTIME_FIELDS
    ):
        errors.append("report.runtime values must be non-empty strings")

    results = payload["results"]
    if not isinstance(results, list) or not results:
        errors.append("report.results must be a non-empty array")
        return errors, counts

    recorded_names: set[str] = set()
    for index, result in enumerate(results):
        location = f"report.results[{index}]"
        if not isinstance(result, dict) or set(result) != set(RESULT_FIELDS):
            errors.append(
                f"{location} keys must be exactly "
                "['grading_evidence', 'name', 'response', 'result']"
            )
            continue
        name = result["name"]
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{location}.name must be a non-empty string")
        elif name not in scenario_names:
            errors.append(f"{location}.name {name!r} is not a scenario for {skill}")
        elif name in recorded_names:
            errors.append(f"{location}.name duplicates {name!r}")
        else:
            recorded_names.add(name)

        for field in ("response", "grading_evidence"):
            value = result[field]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{location}.{field} must be a non-empty string")

        outcome = result["result"]
        if not isinstance(outcome, str) or outcome not in RESULT_VALUES:
            errors.append(f"{location}.result must be 'pass' or 'fail'")
        else:
            counts[outcome] += 1

    if require_failure and counts["fail"] == 0:
        errors.append("report must include at least one deliberately failed scenario")
    return errors, counts


def skill_directory(name: str) -> Path | None:
    candidate = (SKILLS_ROOT / name).resolve()
    if candidate.parent != SKILLS_ROOT.resolve() or not candidate.is_dir():
        return None
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare or validate a manually graded skill review scenario report."
    )
    parser.add_argument("--skill", required=True, help="First-party skill name")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--template", action="store_true", help="Print a report template")
    mode.add_argument("--report", type=Path, help="Recorded manual review JSON")
    parser.add_argument(
        "--require-failure",
        action="store_true",
        help="Require one recorded fail result, for a negative-control review",
    )
    arguments = parser.parse_args()

    directory = skill_directory(arguments.skill)
    if directory is None:
        print(f"Unknown first-party skill: {arguments.skill}", file=sys.stderr)
        return 2

    errors: list[str] = []
    scenarios = load_scenarios(directory, errors)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    if arguments.template:
        if arguments.require_failure:
            print("--require-failure can only validate a --report", file=sys.stderr)
            return 2
        print(json.dumps(review_template(arguments.skill, scenarios), indent=2))
        return 0

    payload = load_json(arguments.report, "report", errors)
    if payload is not None:
        validation_errors, counts = validate_review_report(
            payload, arguments.skill, scenarios, arguments.require_failure
        )
        errors.extend(validation_errors)
    else:
        counts = {"pass": 0, "fail": 0}
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(
        f"Scenario review report validated: {arguments.skill}, "
        f"{counts['pass']} pass and {counts['fail']} fail results. "
        "This validates traceability fields; response quality remains manually graded."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
