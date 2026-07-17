#!/usr/bin/env python3
"""Validate the dependency-free GitHub Pages site and its repository links."""

from __future__ import annotations

import json
import re
import struct
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
INDEX = SITE / "index.html"
EXPECTED_DOMAIN = "skills.sebastian-software.com"
EXPECTED_OG_IMAGE_URL = f"https://{EXPECTED_DOMAIN}/assets/og-card.png"
SKILL_URL_PREFIX = (
    "https://github.com/sebastian-software/"
    "skills.sebastian-software.com/tree/main/skills/"
)
EXPECTED_SKILLS_COMMAND = (
    "npx skills add sebastian-software/skills.sebastian-software.com "
    "--skill effective-web"
)
EXPECTED_DALO_COMMANDS = (
    "curl -fsSL https://dalo.sh/install.sh | sh",
    "dalo init",
    "dalo target link codex",
    "dalo source add-catalog sebastian "
    "https://github.com/sebastian-software/skills.sebastian-software.com.git",
    "dalo source select sebastian effective-web",
    "dalo approve skill sebastian:effective-web",
    "dalo sync",
)


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.assets: list[str] = []
        self.skill_cards: list[tuple[str, str]] = []
        self.filter_counts: dict[str, int] = {}
        self.copy_buttons: list[tuple[str, str]] = []
        self.current_filter: str | None = None
        self.current_filter_text: list[str] = []
        self.h1_count = 0
        self.main_count = 0
        self.lang = ""
        self.has_viewport = False
        self.has_description = False
        self.og_description = ""
        self.canonical = ""
        self.meta_names: dict[str, str] = {}
        self.meta_properties: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)

        if tag == "html":
            self.lang = values.get("lang", "") or ""
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.main_count += 1
        if value := values.get("id"):
            self.ids.append(value)
        if tag == "a" and (value := values.get("href")):
            self.links.append(value)
        if tag == "link":
            rel = set((values.get("rel", "") or "").split())
            if rel.intersection({"stylesheet", "icon", "apple-touch-icon"}) and (
                value := values.get("href")
            ):
                self.assets.append(value)
            if "canonical" in rel:
                self.canonical = values.get("href", "") or ""
        if tag == "script" and (value := values.get("src")):
            self.assets.append(value)
        if tag == "meta":
            content = values.get("content", "") or ""
            if name := values.get("name"):
                self.meta_names[name] = content
            if property_name := values.get("property"):
                self.meta_properties[property_name] = content
            if values.get("name") == "viewport":
                self.has_viewport = True
            if values.get("name") == "description" and values.get("content"):
                self.has_description = True
            if values.get("property") == "og:description":
                self.og_description = values.get("content", "") or ""
        if tag == "article" and (skill := values.get("data-skill")):
            self.skill_cards.append((skill, values.get("data-category", "") or ""))
        if tag == "button" and (filter_name := values.get("data-filter")):
            self.current_filter = filter_name
            self.current_filter_text = []
        if tag == "button" and (copy_target := values.get("data-copy-target")):
            self.copy_buttons.append((copy_target, values.get("aria-label", "") or ""))

    def handle_data(self, data: str) -> None:
        if self.current_filter is not None:
            self.current_filter_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "button" and self.current_filter is not None:
            count = re.search(r"\d+", "".join(self.current_filter_text))
            if count:
                self.filter_counts[self.current_filter] = int(count.group())
            self.current_filter = None
            self.current_filter_text = []


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def local_path(reference: str) -> Path | None:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "tel:")):
        return None
    return SITE / parsed.path.lstrip("/")


def extract_json_ld(html: str) -> dict[str, object] | None:
    match = re.search(
        r'<script\s+type="application/ld\+json">\s*(.*?)\s*</script>', html, re.DOTALL
    )
    if not match:
        return None
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError:
        return None


def proof_row_values(html: str) -> list[int]:
    match = re.search(r'<dl\s+class="proof-row".*?</dl>', html, re.DOTALL)
    return [int(value) for value in re.findall(r"<dt>(\d+)</dt>", match.group())] if match else []


def png_dimensions(path: Path) -> tuple[int, int] | None:
    header = path.read_bytes()[:24]
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", header[16:24])


def ico_dimensions(path: Path) -> set[tuple[int, int]]:
    data = path.read_bytes()
    if len(data) < 6 or data[:4] != b"\x00\x00\x01\x00":
        return set()

    count = int.from_bytes(data[4:6], "little")
    dimensions: set[tuple[int, int]] = set()
    for index in range(count):
        entry = data[6 + index * 16 : 22 + index * 16]
        if len(entry) != 16:
            return set()
        dimensions.add((entry[0] or 256, entry[1] or 256))
    return dimensions


def validate_json_ld_inventory(
    json_ld: dict[str, object] | None,
    expected_skills: list[str],
    failures: list[str],
) -> None:
    require(json_ld is not None, "site must include JSON-LD metadata", failures)
    if json_ld is None:
        return

    expected_count = len(expected_skills)
    item_list = json_ld.get("mainEntity", {})
    items = item_list.get("itemListElement", []) if isinstance(item_list, dict) else []
    require(
        isinstance(item_list, dict) and item_list.get("numberOfItems") == expected_count,
        "JSON-LD skill count must match the repository inventory",
        failures,
    )
    require(
        isinstance(items, list) and len(items) == expected_count,
        "JSON-LD items must match the repository inventory",
        failures,
    )
    urls = [
        item.get("url")
        for item in items
        if isinstance(item, dict) and isinstance(item.get("url"), str)
    ]
    require(
        sorted(urls) == sorted(f"{SKILL_URL_PREFIX}{skill}" for skill in expected_skills),
        "JSON-LD skill items must link every repository skill exactly once",
        failures,
    )


def main() -> int:
    failures: list[str] = []
    required_files = (
        INDEX,
        SITE / "styles.css",
        SITE / "script.js",
        SITE / "assets" / "favicon.svg",
        SITE / "assets" / "favicon-32.png",
        SITE / "assets" / "apple-touch-icon.png",
        SITE / "assets" / "og-card.png",
        SITE / "favicon.ico",
        SITE / "CNAME",
        SITE / ".nojekyll",
        SITE / "robots.txt",
        SITE / "sitemap.xml",
    )

    for path in required_files:
        require(path.is_file(), f"missing required site file: {path.relative_to(ROOT)}", failures)

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    html = INDEX.read_text(encoding="utf-8")
    css = (SITE / "styles.css").read_text(encoding="utf-8")
    script = (SITE / "script.js").read_text(encoding="utf-8")
    parser = SiteParser()
    parser.feed(html)

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    expected_skills = sorted(path.parent.name for path in skill_files)
    reference_count = sum(
        len(list((skill_file.parent / "references").rglob("*.md")))
        for skill_file in skill_files
        if (skill_file.parent / "references").is_dir()
    )
    json_ld = extract_json_ld(html)
    proof_values = proof_row_values(html)
    journey_match = re.search(r'<ol\s+class="journey".*?</ol>', html, re.DOTALL)
    journey_html = journey_match.group() if journey_match else ""

    require(
        local_path("/styles.css") == SITE / "styles.css",
        "root-relative site paths must stay below the site directory",
        failures,
    )
    require(parser.lang == "en", "document language must be English", failures)
    require(parser.h1_count == 1, "site must contain exactly one h1", failures)
    require(parser.main_count == 1, "site must contain exactly one main element", failures)
    require(parser.has_viewport, "site must define a viewport meta tag", failures)
    require(parser.has_description, "site must define a meta description", failures)
    require(
        parser.canonical == f"https://{EXPECTED_DOMAIN}/",
        "canonical URL must match the Pages custom domain",
        failures,
    )
    require(len(parser.ids) == len(set(parser.ids)), "site contains duplicate IDs", failures)
    require("no-js" not in html, "site must not ship an unused no-js hook", failures)
    require("⌘" not in html, "copy buttons must not imply a keyboard shortcut", failures)
    require(
        sorted(skill for skill, _ in parser.skill_cards) == expected_skills,
        "site skill cards must match every SKILL.md exactly",
        failures,
    )

    categories = {category for _, category in parser.skill_cards}
    filter_categories = set(parser.filter_counts) - {"all"}
    require(
        all(category for _, category in parser.skill_cards),
        "every site skill card must define a category",
        failures,
    )
    require(
        categories == filter_categories,
        "site card categories must match the available filters exactly",
        failures,
    )
    require(
        parser.filter_counts.get("all") == len(expected_skills),
        "all-skills filter count must match the skill inventory",
        failures,
    )
    for category in categories:
        require(
            parser.filter_counts.get(category)
            == sum(card_category == category for _, card_category in parser.skill_cards),
            f"{category} filter count must match its skill cards",
            failures,
        )

    require(
        proof_values[:2] == [len(expected_skills), reference_count],
        "hero skill and reference counts must match the repository inventory",
        failures,
    )
    require(
        f"{len(expected_skills)} practice-built skills and {reference_count} focused references"
        in parser.og_description,
        "Open Graph description must match the repository inventory",
        failures,
    )
    require(
        parser.meta_properties.get("og:image") == EXPECTED_OG_IMAGE_URL,
        "Open Graph image must use the canonical 1200x630 asset URL",
        failures,
    )
    require(
        parser.meta_properties.get("og:image:width") == "1200"
        and parser.meta_properties.get("og:image:height") == "630",
        "Open Graph image metadata must declare 1200x630 dimensions",
        failures,
    )
    require(
        bool(parser.meta_properties.get("og:image:alt")),
        "Open Graph image must include alternative text",
        failures,
    )
    require(
        parser.meta_names.get("twitter:card") == "summary_large_image",
        "Twitter card must use summary_large_image",
        failures,
    )
    require(
        parser.meta_names.get("twitter:image") == EXPECTED_OG_IMAGE_URL,
        "Twitter image must match the Open Graph image",
        failures,
    )
    require(
        parser.meta_names.get("twitter:image:alt")
        == parser.meta_properties.get("og:image:alt"),
        "Twitter and Open Graph image alternative text must match",
        failures,
    )
    validate_json_ld_inventory(json_ld, expected_skills, failures)

    require(
        png_dimensions(SITE / "assets" / "og-card.png") == (1200, 630),
        "Open Graph image file must be exactly 1200x630",
        failures,
    )
    require(
        png_dimensions(SITE / "assets" / "favicon-32.png") == (32, 32),
        "PNG favicon must be exactly 32x32",
        failures,
    )
    require(
        png_dimensions(SITE / "assets" / "apple-touch-icon.png") == (180, 180),
        "Apple touch icon must be exactly 180x180",
        failures,
    )
    require(
        {(16, 16), (32, 32), (48, 48)}.issubset(ico_dimensions(SITE / "favicon.ico")),
        "favicon.ico must contain 16x16, 32x32, and 48x48 images",
        failures,
    )

    require(bool(journey_html), "site must contain the connected workflow", failures)
    for skill in expected_skills:
        require(
            f"/skills/{skill}\"" in journey_html,
            f"connected workflow must link skill: {skill}",
            failures,
        )
    require(
        "Improve &amp; deliver" in journey_html,
        "connected workflow must resolve the Delivery node",
        failures,
    )

    expected_copy_buttons = {
        ("hero-command", "Copy Effective Web skills CLI command"),
        ("skills-command", "Copy skills CLI command"),
        ("dalo-command", "Copy DALO setup commands"),
    }
    require(
        set(parser.copy_buttons) == expected_copy_buttons,
        "copy buttons must have unique contextual accessible names",
        failures,
    )
    for class_name in ("command-dock", "route-cloud", "filter-bar"):
        require(
            re.search(
                rf'<div\s+class="[^"]*\b{class_name}\b[^"]*"[^>]*\brole="group"[^>]*\baria-label=',
                html,
            )
            is not None,
            f"named {class_name} div must expose a group role",
            failures,
        )

    for link in parser.links:
        if link.startswith("#"):
            require(link[1:] in parser.ids, f"fragment target does not exist: {link}", failures)
        elif path := local_path(link):
            require(path.is_file(), f"local link target does not exist: {link}", failures)

    for asset in parser.assets:
        path = local_path(asset)
        require(path is not None and path.is_file(), f"local asset does not exist: {asset}", failures)

    require(EXPECTED_SKILLS_COMMAND in html, "selective skills CLI command is missing", failures)
    for command in EXPECTED_DALO_COMMANDS:
        require(command in html, f"DALO command is missing: {command}", failures)

    for url in (
        "https://oss.sebastian-software.com/",
        "https://sebastian-consulting.com/en",
        "https://github.com/sebastian-software/skills.sebastian-software.com",
    ):
        require(url in html, f"required external link is missing: {url}", failures)

    require(":focus-visible" in css, "CSS must provide visible keyboard focus", failures)
    require(
        re.search(r"\.primary-nav\s*\{\s*display:\s*none", css) is None,
        "primary navigation must remain available at responsive widths",
        failures,
    )
    require(
        "prefers-reduced-motion: reduce" in css,
        "CSS must provide a reduced-motion experience",
        failures,
    )
    require("forced-colors: active" in css, "CSS must support forced colors", failures)
    require("transition: all" not in css, "CSS must not use transition: all", failures)
    require("innerHTML" not in script, "JavaScript must not write innerHTML", failures)
    require(
        "IntersectionObserver" in script,
        "JavaScript must progressively enhance scroll reveals",
        failures,
    )

    cname = (SITE / "CNAME").read_text(encoding="utf-8").strip()
    require(cname == EXPECTED_DOMAIN, f"CNAME must be exactly {EXPECTED_DOMAIN}", failures)
    require(
        f"Sitemap: https://{EXPECTED_DOMAIN}/sitemap.xml" in (SITE / "robots.txt").read_text(encoding="utf-8"),
        "robots.txt must reference the canonical sitemap",
        failures,
    )
    sitemap = (SITE / "sitemap.xml").read_text(encoding="utf-8")
    require(
        f"<loc>https://{EXPECTED_DOMAIN}/</loc>" in sitemap,
        "sitemap must reference the canonical URL",
        failures,
    )
    lastmod_match = re.search(r"<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>", sitemap)
    require(lastmod_match is not None, "sitemap must include an ISO lastmod date", failures)
    if lastmod_match is not None:
        try:
            date.fromisoformat(lastmod_match.group(1))
        except ValueError:
            failures.append("sitemap lastmod must be a valid calendar date")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print(
        f"Validated dependency-free site: {len(expected_skills)} skills, "
        f"{len(parser.ids)} unique IDs, {len(parser.links)} links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
