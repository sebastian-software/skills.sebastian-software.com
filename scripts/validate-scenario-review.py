#!/usr/bin/env python3
"""Prepare and validate recorded reviews of unrun skill scenarios.

This tool deliberately does not call a model or infer whether an answer is good.
It makes activation, single-run, and with/without-skill review records complete,
traceable, and tied to the scenario fixtures that CI validates structurally.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
RUNTIME_FIELDS = ("agent", "model", "sampling")
ISOLATED_RUNTIME_FIELDS = (*RUNTIME_FIELDS, "isolation")
RESULT_FIELDS = ("grading_evidence", "name", "response", "result")
RESULT_VALUES = {"pass", "fail"}
CONDITION_FIELDS = (
    "duration_ms",
    "input_tokens",
    "output_tokens",
    "response",
    "result",
)
COMPARISON_RESULT_FIELDS = (
    "comparison",
    "name",
    "winner",
    "with_skill",
    "without_skill",
)
WINNER_VALUES = {"tie", "with_skill", "without_skill"}
ACTIVATION_RESULT_FIELDS = (
    "evidence",
    "expected_trigger",
    "name",
    "observed_trigger",
    "result",
)


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


def load_activation_cases(
    skill_directory: Path, errors: list[str]
) -> dict[str, bool]:
    path = skill_directory / "evals" / "evals.json"
    payload = load_json(path, str(path), errors)
    activation = payload.get("activation") if isinstance(payload, dict) else None
    if activation is None:
        errors.append(f"{path}: activation cases are not defined")
        return {}
    if not isinstance(activation, list) or not activation:
        errors.append(f"{path}: activation must be a non-empty array")
        return {}

    cases: dict[str, bool] = {}
    for index, evaluation in enumerate(activation):
        location = f"{path}: activation[{index}]"
        if not isinstance(evaluation, dict):
            errors.append(f"{location} must be an object")
            continue
        name = evaluation.get("name")
        should_trigger = evaluation.get("should_trigger")
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{location}.name must be a non-empty string")
            continue
        if not isinstance(should_trigger, bool):
            errors.append(f"{location}.should_trigger must be a boolean")
            continue
        if name in cases:
            errors.append(f"{location}.name duplicates {name!r}")
        cases[name] = should_trigger
    return cases


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
                "result": "",
                "grading_evidence": "",
            }
            for name in sorted(scenario_names)
        ],
    }


def isolated_runtime_template() -> dict[str, str]:
    return {
        "agent": "replace with the reviewed agent/runtime",
        "model": "replace with the model and version",
        "sampling": "replace with temperature, seed, and other relevant settings",
        "isolation": "use a fresh session for every condition and case",
    }


def activation_template(
    skill: str, activation_cases: dict[str, bool]
) -> dict[str, object]:
    return {
        "kind": "activation",
        "skill": skill,
        "runtime": isolated_runtime_template(),
        "results": [
            {
                "name": name,
                "expected_trigger": activation_cases[name],
                "observed_trigger": None,
                "result": "",
                "evidence": "",
            }
            for name in sorted(activation_cases)
        ],
    }


def comparison_template(skill: str, scenario_names: set[str]) -> dict[str, object]:
    condition = {
        "response": "",
        "result": "",
        "duration_ms": None,
        "input_tokens": None,
        "output_tokens": None,
    }
    return {
        "kind": "with-without-skill",
        "skill": skill,
        "runtime": isolated_runtime_template(),
        "results": [
            {
                "name": name,
                "with_skill": dict(condition),
                "without_skill": dict(condition),
                "winner": "",
                "comparison": "",
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


def validate_isolated_runtime(runtime: object, errors: list[str]) -> None:
    if not isinstance(runtime, dict) or set(runtime) != set(ISOLATED_RUNTIME_FIELDS):
        errors.append(
            "report.runtime keys must be exactly "
            "['agent', 'isolation', 'model', 'sampling']"
        )
        return
    if any(
        not isinstance(runtime[field], str) or not runtime[field].strip()
        for field in ISOLATED_RUNTIME_FIELDS
    ):
        errors.append("report.runtime values must be non-empty strings")


def validate_activation_report(
    payload: object,
    skill: str,
    activation_cases: dict[str, bool],
) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    counts = {"pass": 0, "fail": 0}
    expected_top_level = {"kind", "results", "runtime", "skill"}
    if not isinstance(payload, dict) or set(payload) != expected_top_level:
        return (
            [
                "report: activation report keys must be exactly "
                "['kind', 'results', 'runtime', 'skill']"
            ],
            counts,
        )
    if payload["kind"] != "activation":
        errors.append("report.kind must be 'activation'")
    if payload["skill"] != skill:
        errors.append(f"report.skill must be {skill!r}")
    validate_isolated_runtime(payload["runtime"], errors)

    results = payload["results"]
    if not isinstance(results, list) or not results:
        errors.append("report.results must be a non-empty array")
        return errors, counts

    recorded_names: set[str] = set()
    for index, result in enumerate(results):
        location = f"report.results[{index}]"
        if not isinstance(result, dict) or set(result) != set(ACTIVATION_RESULT_FIELDS):
            errors.append(
                f"{location} keys must be exactly "
                "['evidence', 'expected_trigger', 'name', 'observed_trigger', 'result']"
            )
            continue
        name = result["name"]
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{location}.name must be a non-empty string")
            expected_trigger = None
        elif name not in activation_cases:
            errors.append(
                f"{location}.name {name!r} is not an activation case for {skill}"
            )
            expected_trigger = None
        elif name in recorded_names:
            errors.append(f"{location}.name duplicates {name!r}")
            expected_trigger = activation_cases[name]
        else:
            recorded_names.add(name)
            expected_trigger = activation_cases[name]

        if (
            not isinstance(result["expected_trigger"], bool)
            or (
                expected_trigger is not None
                and result["expected_trigger"] is not expected_trigger
            )
        ):
            errors.append(
                f"{location}.expected_trigger must match the activation fixture"
            )
        observed_trigger = result["observed_trigger"]
        if not isinstance(observed_trigger, bool):
            errors.append(f"{location}.observed_trigger must be a boolean")
        evidence = result["evidence"]
        if not isinstance(evidence, str) or not evidence.strip():
            errors.append(f"{location}.evidence must be a non-empty string")

        outcome = result["result"]
        if not isinstance(outcome, str) or outcome not in RESULT_VALUES:
            errors.append(f"{location}.result must be 'pass' or 'fail'")
        else:
            counts[outcome] += 1
            if (
                isinstance(observed_trigger, bool)
                and expected_trigger is not None
                and (observed_trigger is expected_trigger) != (outcome == "pass")
            ):
                errors.append(
                    f"{location}.result must agree with expected and observed activation"
                )
    return errors, counts


def validate_condition(
    condition: object,
    location: str,
    errors: list[str],
) -> str | None:
    if not isinstance(condition, dict) or set(condition) != set(CONDITION_FIELDS):
        errors.append(
            f"{location} keys must be exactly "
            "['duration_ms', 'input_tokens', 'output_tokens', 'response', 'result']"
        )
        return None
    response = condition["response"]
    if not isinstance(response, str) or not response.strip():
        errors.append(f"{location}.response must be a non-empty string")
    outcome = condition["result"]
    if not isinstance(outcome, str) or outcome not in RESULT_VALUES:
        errors.append(f"{location}.result must be 'pass' or 'fail'")
        valid_outcome = None
    else:
        valid_outcome = outcome
    duration = condition["duration_ms"]
    if duration is not None and (
        not isinstance(duration, int) or isinstance(duration, bool) or duration < 0
    ):
        errors.append(
            f"{location}.duration_ms must be null or a non-negative integer"
        )
    for field in ("input_tokens", "output_tokens"):
        value = condition[field]
        if value is not None and (
            not isinstance(value, int) or isinstance(value, bool) or value < 0
        ):
            errors.append(f"{location}.{field} must be null or a non-negative integer")
    return valid_outcome


def validate_comparison_report(
    payload: object,
    skill: str,
    scenario_names: set[str],
) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    counts = {
        "with_skill_pass": 0,
        "without_skill_pass": 0,
        "with_skill_wins": 0,
        "without_skill_wins": 0,
        "ties": 0,
    }
    expected_top_level = {"kind", "results", "runtime", "skill"}
    if not isinstance(payload, dict) or set(payload) != expected_top_level:
        return (
            [
                "report: comparison report keys must be exactly "
                "['kind', 'results', 'runtime', 'skill']"
            ],
            counts,
        )
    if payload["kind"] != "with-without-skill":
        errors.append("report.kind must be 'with-without-skill'")
    if payload["skill"] != skill:
        errors.append(f"report.skill must be {skill!r}")
    validate_isolated_runtime(payload["runtime"], errors)

    results = payload["results"]
    if not isinstance(results, list) or not results:
        errors.append("report.results must be a non-empty array")
        return errors, counts

    recorded_names: set[str] = set()
    for index, result in enumerate(results):
        location = f"report.results[{index}]"
        if not isinstance(result, dict) or set(result) != set(COMPARISON_RESULT_FIELDS):
            errors.append(
                f"{location} keys must be exactly "
                "['comparison', 'name', 'winner', 'with_skill', 'without_skill']"
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

        with_outcome = validate_condition(
            result["with_skill"], f"{location}.with_skill", errors
        )
        without_outcome = validate_condition(
            result["without_skill"], f"{location}.without_skill", errors
        )
        if with_outcome == "pass":
            counts["with_skill_pass"] += 1
        if without_outcome == "pass":
            counts["without_skill_pass"] += 1

        winner = result["winner"]
        if not isinstance(winner, str) or winner not in WINNER_VALUES:
            errors.append(
                f"{location}.winner must be 'with_skill', 'without_skill', or 'tie'"
            )
        else:
            counts[
                {
                    "with_skill": "with_skill_wins",
                    "without_skill": "without_skill_wins",
                    "tie": "ties",
                }[winner]
            ] += 1
        comparison = result["comparison"]
        if not isinstance(comparison, str) or not comparison.strip():
            errors.append(f"{location}.comparison must be a non-empty string")
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
    mode.add_argument(
        "--activation-template",
        action="store_true",
        help="Print a should-trigger/should-not-trigger review template",
    )
    mode.add_argument(
        "--comparison-template",
        action="store_true",
        help="Print a fresh-session with/without-skill comparison template",
    )
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
    activation_cases: dict[str, bool] = {}
    if arguments.activation_template:
        activation_cases = load_activation_cases(directory, errors)
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
    if arguments.activation_template:
        if arguments.require_failure:
            print("--require-failure can only validate a --report", file=sys.stderr)
            return 2
        print(json.dumps(activation_template(arguments.skill, activation_cases), indent=2))
        return 0
    if arguments.comparison_template:
        if arguments.require_failure:
            print("--require-failure can only validate a --report", file=sys.stderr)
            return 2
        print(json.dumps(comparison_template(arguments.skill, scenarios), indent=2))
        return 0

    payload = load_json(arguments.report, "report", errors)
    if payload is not None:
        kind = payload.get("kind") if isinstance(payload, dict) else None
        if arguments.require_failure and kind in {
            "activation",
            "with-without-skill",
        }:
            errors.append(
                "--require-failure only applies to the legacy single-run report"
            )
        if kind == "activation":
            activation_cases = load_activation_cases(directory, errors)
            validation_errors, counts = validate_activation_report(
                payload, arguments.skill, activation_cases
            )
        elif kind == "with-without-skill":
            validation_errors, counts = validate_comparison_report(
                payload, arguments.skill, scenarios
            )
        else:
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

    if isinstance(payload, dict) and payload.get("kind") == "with-without-skill":
        print(
            f"Comparison report validated: {arguments.skill}, "
            f"{counts['with_skill_pass']} with-skill passes, "
            f"{counts['without_skill_pass']} baseline passes, "
            f"{counts['with_skill_wins']} with-skill wins, "
            f"{counts['without_skill_wins']} baseline wins, and "
            f"{counts['ties']} ties. Response quality remains manually graded."
        )
    elif isinstance(payload, dict) and payload.get("kind") == "activation":
        print(
            f"Activation report validated: {arguments.skill}, "
            f"{counts['pass']} pass and {counts['fail']} fail results. "
            "Observed invocation evidence remains manually recorded."
        )
    else:
        print(
            f"Scenario review report validated: {arguments.skill}, "
            f"{counts['pass']} pass and {counts['fail']} fail results. "
            "This validates traceability fields; response quality remains manually graded."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
