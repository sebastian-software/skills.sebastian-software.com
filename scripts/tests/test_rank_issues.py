from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "skills" / "issue-autopilot" / "scripts" / "rank_issues.py"
NOW = "2026-08-03T12:00:00Z"


def run_ranker(payload: object, output_format: str = "json") -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as directory:
        input_file = Path(directory) / "issues.json"
        input_file.write_text(json.dumps(payload), encoding="utf-8")
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                str(input_file),
                "--format",
                output_format,
                "--now",
                NOW,
            ],
            capture_output=True,
            text=True,
        )


class RankIssuesTests(unittest.TestCase):
    def test_critical_older_issue_outranks_new_cosmetic_work(self) -> None:
        result = run_ranker(
            {
                "issues": [
                    {
                        "id": "NEW-1",
                        "title": "Polish empty-state icon",
                        "created_at": "2026-08-03T10:00:00Z",
                        "labels": ["cosmetic"],
                        "impact": 1,
                        "urgency": 1,
                        "relevance": 5,
                    },
                    {
                        "id": "OLD-1",
                        "title": "Prevent account data loss",
                        "created_at": "2026-06-20T10:00:00Z",
                        "labels": ["data-loss"],
                        "impact": 5,
                        "urgency": 5,
                        "relevance": 5,
                    },
                ]
            }
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        ranked = json.loads(result.stdout)
        self.assertEqual([issue["id"] for issue in ranked], ["OLD-1", "NEW-1"])
        self.assertEqual(ranked[0]["group"], "Immediate")

    def test_recency_breaks_an_otherwise_equal_later_group(self) -> None:
        result = run_ranker(
            [
                {
                    "id": "OLD-2",
                    "title": "Older maintenance task",
                    "created_at": "2025-12-01T10:00:00Z",
                },
                {
                    "id": "NEW-2",
                    "title": "New maintenance task",
                    "created_at": "2026-08-02T10:00:00Z",
                },
            ]
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        ranked = json.loads(result.stdout)
        self.assertEqual([issue["id"] for issue in ranked], ["NEW-2", "OLD-2"])
        self.assertGreater(ranked[0]["score"], ranked[1]["score"])

    def test_blocked_issue_remains_in_blocked_group(self) -> None:
        result = run_ranker(
            [
                {
                    "id": "BLOCKED-1",
                    "title": "Externally blocked outage repair",
                    "created_at": "2026-08-03T10:00:00Z",
                    "priority": "urgent",
                    "labels": ["outage"],
                    "impact": 5,
                    "urgency": 5,
                    "relevance": 5,
                    "blocked": True,
                }
            ]
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        ranked = json.loads(result.stdout)
        self.assertEqual(ranked[0]["group"], "Blocked")
        self.assertIn("externally blocked", ranked[0]["ranking_reasons"])

    def test_invalid_dimension_fails_without_partial_output(self) -> None:
        result = run_ranker(
            [
                {
                    "id": "BAD-1",
                    "title": "Invalid input",
                    "created_at": "2026-08-03T10:00:00Z",
                    "impact": 6,
                }
            ]
        )

        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("BAD-1: impact must be 0-5", result.stderr)


if __name__ == "__main__":
    unittest.main()
