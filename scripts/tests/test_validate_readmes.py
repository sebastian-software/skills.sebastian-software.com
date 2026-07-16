from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "validate-readmes.py"
SPEC = importlib.util.spec_from_file_location("validate_readmes", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Could not load {MODULE_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class EvalValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.skill = self.root / "skills" / "example"
        self.skill.mkdir(parents=True)
        self.original_root = VALIDATOR.REPOSITORY_ROOT
        VALIDATOR.REPOSITORY_ROOT = self.root

    def tearDown(self) -> None:
        VALIDATOR.REPOSITORY_ROOT = self.original_root
        self.temporary_directory.cleanup()

    def write_evals(self, payload: object) -> None:
        evals_directory = self.skill / "evals"
        evals_directory.mkdir()
        (evals_directory / "evals.json").write_text(
            json.dumps(payload), encoding="utf-8"
        )

    def test_accepts_the_documented_eval_shape(self) -> None:
        self.write_evals(
            {
                "evals": [
                    {
                        "name": "reject-shortcut",
                        "prompt": "Take the tempting shortcut.",
                        "expected": "Reject it with evidence.",
                    }
                ]
            }
        )
        errors: list[str] = []

        VALIDATOR.validate_evals(self.skill, errors)

        self.assertEqual(errors, [])

    def test_requires_the_eval_file(self) -> None:
        errors: list[str] = []

        VALIDATOR.validate_evals(self.skill, errors)

        self.assertEqual(errors, ["skills/example: missing evals/evals.json"])

    def test_rejects_empty_fields_and_duplicate_names(self) -> None:
        self.write_evals(
            {
                "evals": [
                    {"name": "duplicate", "prompt": "", "expected": "First"},
                    {"name": "duplicate", "prompt": "Second", "expected": ""},
                ]
            }
        )
        errors: list[str] = []

        VALIDATOR.validate_evals(self.skill, errors)

        self.assertEqual(len(errors), 3)
        self.assertTrue(any("prompt must be a non-empty string" in error for error in errors))
        self.assertTrue(any("expected must be a non-empty string" in error for error in errors))
        self.assertTrue(any("duplicates 'duplicate'" in error for error in errors))

    def test_rejects_legacy_top_level_eval_keys(self) -> None:
        self.write_evals(
            {
                "skill_name": "example",
                "evals": [
                    {"name": "case", "prompt": "Prompt", "expected": "Expected"}
                ],
            }
        )
        errors: list[str] = []

        VALIDATOR.validate_evals(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/evals/evals.json: top-level keys must be exactly ['evals']"
            ],
        )


class SkillMetadataValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.skill = self.root / "skills" / "example"
        self.skill.mkdir(parents=True)
        self.original_root = VALIDATOR.REPOSITORY_ROOT
        VALIDATOR.REPOSITORY_ROOT = self.root

    def tearDown(self) -> None:
        VALIDATOR.REPOSITORY_ROOT = self.original_root
        self.temporary_directory.cleanup()

    def write_skill(self, description_style: str = ">-", include_metadata: bool = True) -> None:
        (self.skill / "SKILL.md").write_text(
            f"---\nname: example\ndescription: {description_style}\n  Example skill.\n---\n",
            encoding="utf-8",
        )
        if include_metadata:
            agents = self.skill / "agents"
            agents.mkdir()
            (agents / "openai.yaml").write_text(
                'interface:\n'
                '  display_name: "Example"\n'
                '  short_description: "Describe the example"\n'
                '  default_prompt: "Use $example for this task."\n',
                encoding="utf-8",
            )

    def test_accepts_canonical_frontmatter_and_metadata(self) -> None:
        self.write_skill()
        errors: list[str] = []

        VALIDATOR.validate_skill_metadata(self.skill, errors)

        self.assertEqual(errors, [])

    def test_requires_folded_frontmatter_and_openai_metadata(self) -> None:
        self.write_skill(description_style="|", include_metadata=False)
        errors: list[str] = []

        VALIDATOR.validate_skill_metadata(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/SKILL.md: frontmatter must use description: >-",
                "skills/example: missing agents/openai.yaml",
            ],
        )


if __name__ == "__main__":
    unittest.main()
