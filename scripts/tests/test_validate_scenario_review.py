from __future__ import annotations

import importlib.util
import tempfile
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

    def test_unedited_template_rows_fail_validation(self) -> None:
        template = VALIDATOR.review_template("example", self.scenarios)
        template["runtime"] = self.runtime

        errors, counts = VALIDATOR.validate_review_report(
            template, "example", self.scenarios, require_failure=False
        )

        self.assertEqual(counts, {"pass": 0, "fail": 0})
        for name in ("good-case", "negative-control"):
            self.assertNotIn(name, "".join(errors))  # names themselves are valid
        self.assertTrue(
            any(error.endswith(".result must be 'pass' or 'fail'") for error in errors),
            errors,
        )
        self.assertTrue(
            any(error.endswith(".response must be a non-empty string") for error in errors),
            errors,
        )

    def test_reports_unreadable_or_non_text_json_inputs_without_a_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            invalid_encoding = root / "invalid.json"
            invalid_encoding.write_bytes(b"\xff")
            errors: list[str] = []

            payload = VALIDATOR.load_json(invalid_encoding, "report", errors)

            self.assertIsNone(payload)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].startswith("report: invalid UTF-8:"))

            errors = []
            payload = VALIDATOR.load_json(root, "report", errors)

            self.assertIsNone(payload)
            self.assertEqual(len(errors), 1)
            self.assertTrue(errors[0].startswith("report: could not read file:"))


class ActivationReviewReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cases = {"direct-request": True, "adjacent-request": False}
        self.runtime = {
            "agent": "Codex desktop",
            "model": "gpt-5.6",
            "sampling": "temperature 0",
            "isolation": "fresh session per case",
        }

    def result(
        self, name: str, expected: bool, observed: bool
    ) -> dict[str, object]:
        return {
            "name": name,
            "expected_trigger": expected,
            "observed_trigger": observed,
            "result": "pass" if expected is observed else "fail",
            "evidence": "Recorded invocation trace.",
        }

    def report(self, results: object) -> dict[str, object]:
        return {
            "kind": "activation",
            "skill": "example",
            "runtime": self.runtime,
            "results": results,
        }

    def test_accepts_positive_and_negative_activation_evidence(self) -> None:
        errors, counts = VALIDATOR.validate_activation_report(
            self.report(
                [
                    self.result("direct-request", True, True),
                    self.result("adjacent-request", False, False),
                ]
            ),
            "example",
            self.cases,
        )

        self.assertEqual(errors, [])
        self.assertEqual(counts, {"pass": 2, "fail": 0})

    def test_rejects_a_result_that_disagrees_with_observed_activation(self) -> None:
        result = self.result("direct-request", True, False)
        result["result"] = "pass"

        errors, counts = VALIDATOR.validate_activation_report(
            self.report([result]), "example", self.cases
        )

        self.assertEqual(counts, {"pass": 1, "fail": 0})
        self.assertEqual(
            errors,
            [
                "report.results[0].result must agree with expected and observed "
                "activation"
            ],
        )

    def test_activation_template_preserves_fixture_expectations(self) -> None:
        template = VALIDATOR.activation_template("example", self.cases)

        self.assertEqual(template["kind"], "activation")
        self.assertEqual(
            [
                (result["name"], result["expected_trigger"])
                for result in template["results"]
            ],
            [("adjacent-request", False), ("direct-request", True)],
        )


class ComparisonReviewReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scenarios = {"good-case"}
        self.runtime = {
            "agent": "Claude Code",
            "model": "claude-opus-5",
            "sampling": "default",
            "isolation": "fresh session per condition",
        }

    def condition(self, outcome: str, duration_ms: int) -> dict[str, object]:
        return {
            "response": "Recorded response.",
            "result": outcome,
            "duration_ms": duration_ms,
            "input_tokens": 100,
            "output_tokens": 50,
        }

    def report(self) -> dict[str, object]:
        return {
            "kind": "with-without-skill",
            "skill": "example",
            "runtime": self.runtime,
            "results": [
                {
                    "name": "good-case",
                    "with_skill": self.condition("pass", 1200),
                    "without_skill": self.condition("fail", 800),
                    "winner": "with_skill",
                    "comparison": "The skill adds the required boundary evidence.",
                }
            ],
        }

    def test_accepts_a_fresh_session_comparison(self) -> None:
        errors, counts = VALIDATOR.validate_comparison_report(
            self.report(), "example", self.scenarios
        )

        self.assertEqual(errors, [])
        self.assertEqual(
            counts,
            {
                "with_skill_pass": 1,
                "without_skill_pass": 0,
                "with_skill_wins": 1,
                "without_skill_wins": 0,
                "ties": 0,
            },
        )

    def test_rejects_missing_metrics_and_invalid_token_counts(self) -> None:
        report = self.report()
        report["results"][0]["with_skill"]["duration_ms"] = None
        report["results"][0]["without_skill"]["input_tokens"] = -1

        errors, _ = VALIDATOR.validate_comparison_report(
            report, "example", self.scenarios
        )

        self.assertEqual(
            errors,
            [
                "report.results[0].with_skill.duration_ms must be a non-negative integer",
                "report.results[0].without_skill.input_tokens must be null or a "
                "non-negative integer",
            ],
        )

    def test_comparison_template_contains_both_conditions(self) -> None:
        template = VALIDATOR.comparison_template("example", self.scenarios)

        self.assertEqual(template["kind"], "with-without-skill")
        self.assertIn("with_skill", template["results"][0])
        self.assertIn("without_skill", template["results"][0])


if __name__ == "__main__":
    unittest.main()
