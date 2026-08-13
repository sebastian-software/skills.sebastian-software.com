from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location(
    "validate_activation_matrix", ROOT / "scripts" / "validate-activation-matrix.py"
)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VALIDATOR)


DISCIPLINES = {"effective-product", "effective-delivery"}
DEPRECATED = {"pr-review", "tech-docs"}


def case(name: str, owner: str, prompt: str, covers: list[str] | None = None) -> dict:
    return {
        "name": name,
        "owner": owner,
        "prompt": prompt,
        "covers": covers if covers is not None else [],
    }


def full_coverage() -> list[dict]:
    """A matrix that satisfies every rule, used as the baseline to mutate."""
    return [
        case("review-queue", "effective-delivery", "Review my open PRs.", ["pr-review"]),
        case("migration-notes", "effective-delivery", "Write migration notes.", ["tech-docs"]),
        case("run-checks", "effective-delivery", "Run the repository checks."),
        case("scope-release", "effective-product", "Decide the next release scope."),
        case("price-tiers", "effective-product", "Choose a value metric."),
        case("name-feature", "effective-product", "Name this feature."),
        case("control-time", "none", "What time is it in Tokyo?"),
        case("control-pivot", "none", "Build me a pivot table."),
    ]


class ActivationMatrixTests(unittest.TestCase):
    def validate(self, cases: object) -> list[str]:
        errors: list[str] = []
        VALIDATOR.validate_cases(cases, DISCIPLINES, DEPRECATED, errors)
        return errors

    def test_accepts_a_complete_matrix(self) -> None:
        self.assertEqual(self.validate(full_coverage()), [])

    def test_rejects_an_uncovered_superseded_slug(self) -> None:
        cases = [entry for entry in full_coverage() if entry["name"] != "migration-notes"]
        cases.append(case("extra", "effective-delivery", "Audit the repository."))

        errors = self.validate(cases)

        self.assertIn(
            "docs/activation-matrix.json: superseded slug 'tech-docs' is not covered "
            "by any case; its absorbed trigger would be untested",
            errors,
        )

    def test_rejects_an_unknown_owner(self) -> None:
        cases = full_coverage()
        cases[0] = case("review-queue", "pr-review", "Review my open PRs.", ["pr-review"])

        errors = self.validate(cases)

        self.assertTrue(
            any("owner must be 'none' or a published discipline" in error for error in errors),
            errors,
        )

    def test_rejects_the_same_prompt_under_two_owners(self) -> None:
        cases = full_coverage()
        cases.append(case("duplicate", "effective-product", "  Review   my open PRs.  "))

        errors = self.validate(cases)

        self.assertTrue(
            any("one request cannot have two owners" in error for error in errors), errors
        )

    def test_rejects_a_control_that_claims_coverage(self) -> None:
        cases = full_coverage()
        cases[6] = case("control-time", "none", "What time is it in Tokyo?", ["pr-review"])

        errors = self.validate(cases)

        self.assertIn(
            "docs/activation-matrix.json: cases[6]: a control case cannot cover a "
            "superseded slug",
            errors,
        )

    def test_requires_minimum_cases_per_discipline(self) -> None:
        cases = [entry for entry in full_coverage() if entry["name"] != "name-feature"]

        errors = self.validate(cases)

        self.assertTrue(
            any("effective-product owns 2 cases" in error for error in errors), errors
        )

    def test_requires_control_cases(self) -> None:
        cases = [entry for entry in full_coverage() if entry["owner"] != "none"]

        errors = self.validate(cases)

        self.assertTrue(
            any("control cases with owner 'none'" in error for error in errors), errors
        )

    def test_rejects_a_slug_covered_twice(self) -> None:
        cases = full_coverage()
        cases.append(case("second-review", "effective-delivery", "Approve PR 12.", ["pr-review"]))

        errors = self.validate(cases)

        self.assertTrue(
            any("repeats 'pr-review' from an earlier case" in error for error in errors),
            errors,
        )


class ShippedMatrixTests(unittest.TestCase):
    def test_repository_matrix_passes_its_own_contract(self) -> None:
        self.assertEqual(VALIDATOR.main(), 0)

    def test_every_matrix_prompt_is_distinct_from_its_case_name(self) -> None:
        payload = json.loads(
            (ROOT / "docs" / "activation-matrix.json").read_text(encoding="utf-8")
        )
        for entry in payload["cases"]:
            self.assertNotIn(
                entry["name"].replace("-", " "),
                entry["prompt"].casefold(),
                "a prompt must not leak its own case name to a blind classifier",
            )


class MissingRegistryTests(unittest.TestCase):
    def test_reports_a_missing_matrix(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            original = VALIDATOR.REPOSITORY_ROOT
            VALIDATOR.REPOSITORY_ROOT = Path(directory)
            try:
                errors: list[str] = []
                VALIDATOR.load_json("docs/activation-matrix.json", errors)
            finally:
                VALIDATOR.REPOSITORY_ROOT = original

        self.assertEqual(errors, ["docs/activation-matrix.json: missing"])


if __name__ == "__main__":
    unittest.main()
