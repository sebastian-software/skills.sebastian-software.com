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

    def test_rejects_missing_or_unquoted_metadata_fields(self) -> None:
        self.write_skill()
        (self.skill / "agents" / "openai.yaml").write_text(
            'interface:\n'
            '  display_name: Example\n'
            '  default_prompt: "Use $example for this task."\n',
            encoding="utf-8",
        )
        errors: list[str] = []

        VALIDATOR.validate_skill_metadata(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/agents/openai.yaml: missing quoted display_name",
                "skills/example/agents/openai.yaml: missing quoted short_description",
            ],
        )

    def test_rejects_a_longer_invocation_token_with_the_skill_prefix(self) -> None:
        self.write_skill()
        metadata_file = self.skill / "agents" / "openai.yaml"
        metadata_file.write_text(
            metadata_file.read_text(encoding="utf-8").replace(
                "$example for", "$example-extended for"
            ),
            encoding="utf-8",
        )
        errors: list[str] = []

        VALIDATOR.validate_skill_metadata(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/agents/openai.yaml: default_prompt must invoke $example"
            ],
        )


class SkillReadmeRequirementsTests(unittest.TestCase):
    def test_accepts_all_required_fragments(self) -> None:
        text = "\n".join(VALIDATOR.required_readme_fragments("example").values())
        errors: list[str] = []

        VALIDATOR.validate_required_readme_fragments("example", text, errors)

        self.assertEqual(errors, [])

    def test_requires_the_portable_mit_license_notice(self) -> None:
        fragments = VALIDATOR.required_readme_fragments("example")
        text = "\n".join(
            fragment
            for label, fragment in fragments.items()
            if label != "MIT license notice"
        )
        errors: list[str] = []

        VALIDATOR.validate_required_readme_fragments("example", text, errors)

        self.assertEqual(
            errors,
            ["skills/example/README.md: missing MIT license notice"],
        )


class FrontmatterValidationTests(unittest.TestCase):
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

    def write_skill(self, frontmatter: str) -> None:
        (self.skill / "SKILL.md").write_text(
            f"{frontmatter}\n# Example\n", encoding="utf-8"
        )

    def test_accepts_canonical_folded_frontmatter(self) -> None:
        self.write_skill(
            "---\nname: example\ndescription: >-\n  Example skill.\n  More detail.\n---"
        )
        errors: list[str] = []

        VALIDATOR.validate_frontmatter(self.skill, errors)

        self.assertEqual(errors, [])

    def test_folds_the_description_across_lines(self) -> None:
        parsed = VALIDATOR.parse_skill_frontmatter(
            "---\nname: example\ndescription: >-\n  One line.\n  Two lines.\n---\n"
        )

        self.assertEqual(
            parsed, {"name": "example", "description": "One line. Two lines."}
        )

    def test_rejects_extra_frontmatter_keys(self) -> None:
        self.write_skill(
            "---\nname: example\ndescription: >-\n  Example.\nlicense: MIT\n---"
        )
        errors: list[str] = []

        VALIDATOR.validate_frontmatter(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/SKILL.md: frontmatter keys must be exactly "
                "['description', 'name']"
            ],
        )

    def test_rejects_a_name_that_does_not_match_the_directory(self) -> None:
        self.write_skill("---\nname: other\ndescription: >-\n  Example.\n---")
        errors: list[str] = []

        VALIDATOR.validate_frontmatter(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/SKILL.md: frontmatter name 'other' "
                "must match the directory name 'example'"
            ],
        )

    def test_rejects_a_description_beyond_the_limit(self) -> None:
        long_line = "x" * 200
        folded_lines = "\n".join(f"  {long_line}" for _ in range(6))
        self.write_skill(f"---\nname: example\ndescription: >-\n{folded_lines}\n---")
        errors: list[str] = []

        VALIDATOR.validate_frontmatter(self.skill, errors)

        self.assertEqual(len(errors), 1)
        self.assertIn("description is 1205 characters", errors[0])

    def test_rejects_missing_frontmatter(self) -> None:
        self.write_skill("# No frontmatter")
        errors: list[str] = []

        VALIDATOR.validate_frontmatter(self.skill, errors)

        self.assertEqual(
            errors,
            ["skills/example/SKILL.md: missing or malformed YAML frontmatter"],
        )


class InlineCodeLinkExtractionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.root.joinpath("skills").mkdir()
        self.original_root = VALIDATOR.REPOSITORY_ROOT
        VALIDATOR.REPOSITORY_ROOT = self.root

    def tearDown(self) -> None:
        VALIDATOR.REPOSITORY_ROOT = self.original_root
        self.temporary_directory.cleanup()

    def test_ignores_markdown_links_inside_inline_code_spans(self) -> None:
        markdown = self.root / "README.md"
        markdown.write_text(
            "Use `[text](missing-inline.md)` literally and "
            "``[other](also-missing.md)`` too.\n",
            encoding="utf-8",
        )
        errors: list[str] = []

        VALIDATOR.validate_local_links(markdown, errors)

        self.assertEqual(errors, [])

    def test_still_reports_real_missing_links(self) -> None:
        markdown = self.root / "README.md"
        markdown.write_text("A real [link](missing.md).\n", encoding="utf-8")
        errors: list[str] = []

        VALIDATOR.validate_local_links(markdown, errors)

        self.assertEqual(errors, ["README.md: missing missing.md"])


class IsolatedSkillRuntimeLinkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.skill = self.root / "skills" / "example"
        self.references = self.skill / "references"
        self.references.mkdir(parents=True)
        self.skill.joinpath("SKILL.md").write_text("# Example\n", encoding="utf-8")
        self.original_root = VALIDATOR.REPOSITORY_ROOT
        VALIDATOR.REPOSITORY_ROOT = self.root

    def tearDown(self) -> None:
        VALIDATOR.REPOSITORY_ROOT = self.original_root
        self.temporary_directory.cleanup()

    def test_accepts_links_within_an_isolated_skill_artifact(self) -> None:
        guide = self.references / "guide.md"
        guide.write_text("See [another section](other.md).\n", encoding="utf-8")
        self.references.joinpath("other.md").write_text("# Other\n", encoding="utf-8")
        errors: list[str] = []

        VALIDATOR.validate_isolated_skill_runtime_links(self.skill, errors)

        self.assertEqual(errors, [])

    def test_rejects_a_sibling_skill_link_from_a_reference(self) -> None:
        sibling = self.root / "skills" / "other"
        sibling.mkdir()
        sibling.joinpath("SKILL.md").write_text("# Other\n", encoding="utf-8")
        guide = self.references / "guide.md"
        guide.write_text("See [Other](../../other/SKILL.md).\n", encoding="utf-8")
        errors: list[str] = []

        VALIDATOR.validate_isolated_skill_runtime_links(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/references/guide.md: sibling-skill link "
                "../../other/SKILL.md; use inline `other` guidance instead"
            ],
        )

    def test_rejects_a_sibling_skill_link_from_skill_instructions(self) -> None:
        sibling = self.root / "skills" / "other"
        sibling.mkdir()
        sibling.joinpath("SKILL.md").write_text("# Other\n", encoding="utf-8")
        self.skill.joinpath("SKILL.md").write_text(
            "See [Other](../other/SKILL.md).\n", encoding="utf-8"
        )
        errors: list[str] = []

        VALIDATOR.validate_isolated_skill_runtime_links(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/SKILL.md: sibling-skill link ../other/SKILL.md; "
                "use inline `other` guidance instead"
            ],
        )


class ReferenceOrphanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.skill = self.root / "skills" / "example"
        (self.skill / "references").mkdir(parents=True)
        self.original_root = VALIDATOR.REPOSITORY_ROOT
        VALIDATOR.REPOSITORY_ROOT = self.root

    def tearDown(self) -> None:
        VALIDATOR.REPOSITORY_ROOT = self.original_root
        self.temporary_directory.cleanup()

    def test_accepts_references_linked_from_the_skill(self) -> None:
        (self.skill / "references" / "guide.md").write_text("# Guide\n", encoding="utf-8")
        (self.skill / "SKILL.md").write_text(
            "See [Guide](references/guide.md).\n", encoding="utf-8"
        )
        errors: list[str] = []

        VALIDATOR.validate_reference_orphans(self.skill, errors)

        self.assertEqual(errors, [])

    def test_reports_an_unlinked_reference(self) -> None:
        (self.skill / "references" / "orphan.md").write_text("# Orphan\n", encoding="utf-8")
        (self.skill / "SKILL.md").write_text("No links here.\n", encoding="utf-8")
        errors: list[str] = []

        VALIDATOR.validate_reference_orphans(self.skill, errors)

        self.assertEqual(len(errors), 1)
        self.assertIn("skills/example/references/orphan.md: orphaned reference", errors[0])

    def test_a_self_link_does_not_satisfy_reachability(self) -> None:
        (self.skill / "references" / "loop.md").write_text(
            "See [myself](loop.md).\n", encoding="utf-8"
        )
        errors: list[str] = []

        VALIDATOR.validate_reference_orphans(self.skill, errors)

        self.assertEqual(len(errors), 1)
        self.assertIn("skills/example/references/loop.md: orphaned reference", errors[0])


class WorktreeSafetySyncTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.skills_root = Path(self.temporary_directory.name) / "skills"
        self.skills_root.mkdir()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write_contract(self, skill: str, content: str) -> None:
        references = self.skills_root / skill / "references"
        references.mkdir(parents=True)
        (references / "worktree-safety.md").write_text(content, encoding="utf-8")

    def test_accepts_byte_identical_contracts(self) -> None:
        for skill in VALIDATOR.WORKTREE_SAFETY_SKILLS:
            self.write_contract(skill, "# Worktree Safety\n\nShared contract.\n")
        errors: list[str] = []

        VALIDATOR.validate_worktree_safety_sync(self.skills_root, errors)

        self.assertEqual(errors, [])

    def test_reports_divergent_contracts(self) -> None:
        self.write_contract("pr-review", "# Worktree Safety\n")
        self.write_contract("smart-dependency-updater", "# Worktree Safety\n")
        self.write_contract("port-codebases", "# Worktree Safety, but different\n")
        errors: list[str] = []

        VALIDATOR.validate_worktree_safety_sync(self.skills_root, errors)

        self.assertEqual(
            errors,
            [
                "skills/port-codebases/references/worktree-safety.md: "
                "must be byte-identical to "
                "skills/pr-review/references/worktree-safety.md"
            ],
        )

    def test_skips_when_fewer_than_two_contracts_exist(self) -> None:
        self.write_contract("pr-review", "# Worktree Safety\n")
        errors: list[str] = []

        VALIDATOR.validate_worktree_safety_sync(self.skills_root, errors)

        self.assertEqual(errors, [])


class SkillBodyConventionTests(unittest.TestCase):
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

    def test_accepts_canonical_boundary_and_line_limit(self) -> None:
        (self.skill / "SKILL.md").write_text(
            "## Routing Boundaries\n"
            + "\n".join(["line"] * (VALIDATOR.SKILL_LINE_LIMIT - 1)),
            encoding="utf-8",
        )
        errors: list[str] = []

        VALIDATOR.validate_skill_body_conventions(self.skill, errors)

        self.assertEqual(errors, [])

    def test_requires_the_exact_boundary_heading(self) -> None:
        (self.skill / "SKILL.md").write_text("## Boundaries\n", encoding="utf-8")
        errors: list[str] = []

        VALIDATOR.validate_skill_body_conventions(self.skill, errors)

        self.assertEqual(
            errors,
            ["skills/example/SKILL.md: missing exact '## Routing Boundaries' section"],
        )

    def test_rejects_a_skill_above_the_line_limit(self) -> None:
        (self.skill / "SKILL.md").write_text(
            "## Routing Boundaries\n"
            + "\n".join(["line"] * VALIDATOR.SKILL_LINE_LIMIT),
            encoding="utf-8",
        )
        errors: list[str] = []

        VALIDATOR.validate_skill_body_conventions(self.skill, errors)

        self.assertEqual(
            errors,
            [
                "skills/example/SKILL.md: 301 lines exceeds the 300-line limit; "
                "move detail into references/"
            ],
        )


if __name__ == "__main__":
    unittest.main()
