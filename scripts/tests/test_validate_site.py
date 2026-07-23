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
    inventory = [("one", "One"), ("two", "Two")]

    def test_missing_metadata_reports_a_failure_without_crashing(self) -> None:
        failures: list[str] = []

        VALIDATOR.validate_json_ld_inventory(None, self.inventory, failures)

        self.assertEqual(failures, ["site must include JSON-LD metadata"])

    def test_mismatched_items_report_a_failure(self) -> None:
        failures: list[str] = []
        json_ld = {
            "mainEntity": {
                "numberOfItems": 2,
                "itemListElement": [{"name": "One"}, {"name": "Two"}],
            }
        }

        VALIDATOR.validate_json_ld_inventory(json_ld, self.inventory, failures)

        self.assertEqual(
            failures,
            [
                "JSON-LD skill items must match visible skill cards in order, "
                "name, position, and URL"
            ],
        )

    def test_matching_inventory_passes(self) -> None:
        failures: list[str] = []
        json_ld = {
            "mainEntity": {
                "numberOfItems": 2,
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "One",
                        "url": f"{VALIDATOR.SKILL_URL_PREFIX}one",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Two",
                        "url": f"{VALIDATOR.SKILL_URL_PREFIX}two",
                    },
                ],
            }
        }

        VALIDATOR.validate_json_ld_inventory(json_ld, self.inventory, failures)

        self.assertEqual(failures, [])

    def test_rejects_an_order_or_position_mismatch(self) -> None:
        failures: list[str] = []
        json_ld = {
            "mainEntity": {
                "numberOfItems": 2,
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Two",
                        "url": f"{VALIDATOR.SKILL_URL_PREFIX}two",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "One",
                        "url": f"{VALIDATOR.SKILL_URL_PREFIX}one",
                    },
                ],
            }
        }

        VALIDATOR.validate_json_ld_inventory(json_ld, self.inventory, failures)

        self.assertEqual(
            failures,
            [
                "JSON-LD skill items must match visible skill cards in order, "
                "name, position, and URL"
            ],
        )

    def test_accepts_additional_valid_list_item_properties(self) -> None:
        failures: list[str] = []
        json_ld = {
            "mainEntity": {
                "numberOfItems": 2,
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "One",
                        "url": f"{VALIDATOR.SKILL_URL_PREFIX}one",
                        "description": "An optional Schema.org property.",
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Two",
                        "url": f"{VALIDATOR.SKILL_URL_PREFIX}two",
                    },
                ],
            }
        }

        VALIDATOR.validate_json_ld_inventory(json_ld, self.inventory, failures)

        self.assertEqual(failures, [])


class VisibleSkillInventoryTests(unittest.TestCase):
    def test_reads_card_order_and_display_name(self) -> None:
        html = (
            '<article class="skill-card" data-skill="one"><h3>One &amp; Only</h3></article>'
            '<article data-skill="two"><h3>Two</h3></article>'
        )

        self.assertEqual(
            VALIDATOR.visible_skill_inventory(html),
            [("one", "One & Only"), ("two", "Two")],
        )

    def test_accepts_single_quoted_skill_attributes(self) -> None:
        html = "<article data-skill='one'><H3>One</H3></article>"

        self.assertEqual(VALIDATOR.visible_skill_inventory(html), [("one", "One")])


class ProofRowValuesTests(unittest.TestCase):
    def test_reads_values_from_dd_elements(self) -> None:
        html = (
            '<dl class="proof-row" aria-label="Collection facts">'
            "<div><dt>practice-built skills</dt><dd>20</dd></div>"
            "<div><dt>focused references</dt><dd>184</dd></div>"
            "<div><dt>connected quality system</dt><dd>1</dd></div>"
            "</dl>"
        )

        self.assertEqual(VALIDATOR.proof_row_values(html), [20, 184, 1])


class EffectiveWebStatsValidationTests(unittest.TestCase):
    @staticmethod
    def page(routes: int, references: int, chip: int) -> str:
        return (
            '<div class="flagship-stats">'
            f"<div><strong>{routes}</strong><span>intent routes</span></div>"
            f"<div><strong>{references}</strong><span>focused references</span></div>"
            "<div><strong>1</strong><span>coherent quality bar</span></div>"
            "</div>"
            '<a class="text-link" href="https://example.com/">Explore</a>'
            f"<ul><li>{chip} routed workflows</li></ul>"
        )

    def test_matching_stats_pass(self) -> None:
        failures: list[str] = []

        VALIDATOR.validate_effective_web_stats(self.page(25, 93, 25), 25, 93, failures)

        self.assertEqual(failures, [])

    def test_stale_stats_report_each_mismatch(self) -> None:
        failures: list[str] = []

        VALIDATOR.validate_effective_web_stats(self.page(24, 90, 23), 25, 93, failures)

        self.assertEqual(
            failures,
            [
                "flagship intent-route stat must match the SKILL.md routing table: 25",
                "flagship reference stat must match skills/effective-web/references: 93",
                "effective-web card chip must match the SKILL.md routing table: 25",
            ],
        )

    def test_missing_stats_block_reports_a_failure(self) -> None:
        failures: list[str] = []

        VALIDATOR.validate_effective_web_stats("<main></main>", 25, 93, failures)

        self.assertIn("site must contain the flagship stats block", failures)

    def test_inventory_counts_agree_with_the_repository(self) -> None:
        routes, references = VALIDATOR.effective_web_inventory()

        self.assertGreater(routes, 0)
        self.assertGreater(references, 0)
        self.assertGreaterEqual(references, routes)


class SitemapLastmodValidationTests(unittest.TestCase):
    def test_matching_lastmod_passes(self) -> None:
        failures: list[str] = []

        VALIDATOR.validate_sitemap_lastmod(
            "<lastmod>2026-07-17</lastmod>",
            "2026-07-17",
            failures,
        )

        self.assertEqual(failures, [])

    def test_stale_lastmod_reports_latest_site_date(self) -> None:
        failures: list[str] = []

        VALIDATOR.validate_sitemap_lastmod(
            "<lastmod>2026-07-16</lastmod>",
            "2026-07-17",
            failures,
        )

        self.assertEqual(
            failures,
            ["sitemap lastmod must match the latest site change: 2026-07-17"],
        )


if __name__ == "__main__":
    unittest.main()
