from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = (
    ROOT
    / "skills"
    / "smart-dependency-updater"
    / "scripts"
    / "discover_dependency_context.py"
)


def discover(project: Path) -> dict[str, object]:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(project)],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


class DiscoverDependencyContextTests(unittest.TestCase):
    def test_requirements_candidates_remain_visible_with_unparsed_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "requirements-prod.txt").write_text(
                "\n".join(
                    (
                        "requests==2.32.4",
                        "git+https://example.com/team/package.git@main#egg=package",
                        "https://example.com/packages/archive.whl",
                        "./local/package",
                        'typing-extensions; python_version < "3.9"',
                        "unrecognized entry with spaces",
                    )
                ),
                encoding="utf-8",
            )

            result = discover(project)

            self.assertIn(
                {"path": "requirements-prod.txt", "ecosystem": "python"},
                result["manifests"],
            )
            self.assertEqual(
                result["python"],
                [
                    {
                        "path": "requirements-prod.txt",
                        "entries": 6,
                        "parsed_entries": 5,
                        "unparsed_entries": 1,
                    }
                ],
            )

    def test_go_require_count_ignores_other_directive_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            (project / "go.mod").write_text(
                """module example.com/project

go 1.24

require example.com/direct v3.1.4

require  (
    example.com/first v1.2.3
    example.com/second v2.0.0 // indirect
) // require block

replace (
    example.com/first v1.2.3 => ./local/first
)

exclude (
    example.com/second v1.9.0
)

retract (
    v0.9.0
)
""",
                encoding="utf-8",
            )

            result = discover(project)

            self.assertEqual(result["go"][0]["require_entries_estimate"], 3)


if __name__ == "__main__":
    unittest.main()
