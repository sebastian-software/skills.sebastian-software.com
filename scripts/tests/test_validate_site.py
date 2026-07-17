from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "scripts" / "validate-site.py"
SPEC = importlib.util.spec_from_file_location("validate_site", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Could not load {MODULE_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class JsonLdInventoryValidationTests(unittest.TestCase):
    def test_missing_metadata_reports_a_failure_without_crashing(self) -> None:
        failures: list[str] = []

        VALIDATOR.validate_json_ld_inventory(None, ["one", "two"], failures)

        self.assertEqual(failures, ["site must include JSON-LD metadata"])

    def test_unresolvable_items_report_a_failure(self) -> None:
        failures: list[str] = []
        json_ld = {
            "mainEntity": {
                "numberOfItems": 2,
                "itemListElement": [{"name": "One"}, {"name": "Two"}],
            }
        }

        VALIDATOR.validate_json_ld_inventory(json_ld, ["one", "two"], failures)

        self.assertEqual(
            failures,
            ["JSON-LD skill items must link every repository skill exactly once"],
        )

    def test_matching_inventory_passes(self) -> None:
        failures: list[str] = []
        json_ld = {
            "mainEntity": {
                "numberOfItems": 2,
                "itemListElement": [
                    {
                        "name": "One",
                        "url": f"{VALIDATOR.SKILL_URL_PREFIX}one",
                    },
                    {
                        "name": "Two",
                        "url": f"{VALIDATOR.SKILL_URL_PREFIX}two",
                    },
                ],
            }
        }

        VALIDATOR.validate_json_ld_inventory(json_ld, ["one", "two"], failures)

        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
