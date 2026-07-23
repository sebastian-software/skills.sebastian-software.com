from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "validate-scenario-review.py"
SPEC = importlib.util.spec_from_file_location("validate_scenario_review", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Could not load {MODULE_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ScenarioReviewReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scenarios = {"good-case", "negative-control"}
        self.runtime = {
            "agent": "Codex desktop",
            "model": "gpt-5.6",
            "sampling": "temperature 0",
        }

    def report(self, results: object) -> dict[str, object]:
        return {"skill": "example", "runtime": self.runtime, "results": results}

    def result(self, name: str, outcome: str = "pass") -> dict[str, str]:
        return {
            "name": name,
            "response": "Recorded response.",
            "result": outcome,
            "grading_evidence": "Compared against the scenario expectation.",
        }

    def test_accepts_a_traceable_manual_report(self) -> None:
        errors, counts = VALIDATOR.validate_review_report(
            self.report([self.result("good-case"), self.result("negative-control", "fail")]),
            "example",
            self.scenarios,
            require_failure=True,
        )

        self.assertEqual(errors, [])
        self.assertEqual(counts, {"pass": 1, "fail": 1})

    def test_requires_a_recorded_negative_control_when_requested(self) -> None:
        errors, counts = VALIDATOR.validate_review_report(
            self.report([self.result("good-case")]),
            "example",
            self.scenarios,
            require_failure=True,
        )

        self.assertEqual(counts, {"pass": 1, "fail": 0})
        self.assertEqual(
            errors, ["report must include at least one deliberately failed scenario"]
        )

    def test_rejects_an_unknown_or_unexplained_result(self) -> None:
        result = self.result("missing-case")
        result["grading_evidence"] = ""
        errors, _ = VALIDATOR.validate_review_report(
            self.report([result]), "example", self.scenarios, require_failure=False
        )

        self.assertEqual(
            errors,
            [
                "report.results[0].name 'missing-case' is not a scenario for example",
                "report.results[0].grading_evidence must be a non-empty string",
            ],
        )

    def test_rejects_a_non_string_result_without_crashing(self) -> None:
        result = self.result("good-case")
        result["result"] = []

        errors, counts = VALIDATOR.validate_review_report(
            self.report([result]), "example", self.scenarios, require_failure=False
        )

        self.assertEqual(counts, {"pass": 0, "fail": 0})
        self.assertEqual(
            errors, ["report.results[0].result must be 'pass' or 'fail'"]
        )

    def test_template_contains_every_named_scenario(self) -> None:
        template = VALIDATOR.review_template("example", self.scenarios)

        self.assertEqual(template["skill"], "example")
        self.assertEqual(
            [result["name"] for result in template["results"]],
            ["good-case", "negative-control"],
        )


if __name__ == "__main__":
    unittest.main()
