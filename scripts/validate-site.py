#!/usr/bin/env python3
"""Validate the dependency-free GitHub Pages site and its repository links."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
INDEX = SITE / "index.html"
EXPECTED_DOMAIN = "skills.sebastian-software.com"
EXPECTED_SKILLS_COMMAND = (
    "npx skills add sebastian-software/skills.sebastian-software.com "
    "--skill effective-web"
)
EXPECTED_DALO_COMMANDS = (
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
        self.styles: list[str] = []
        self.scripts: list[str] = []
        self.skill_cards: list[str] = []
        self.h1_count = 0
        self.main_count = 0
        self.lang = ""
        self.has_viewport = False
        self.has_description = False
        self.canonical = ""

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
            if values.get("rel") == "stylesheet" and (value := values.get("href")):
                self.styles.append(value)
            if values.get("rel") == "canonical":
                self.canonical = values.get("href", "") or ""
        if tag == "script" and (value := values.get("src")):
            self.scripts.append(value)
        if tag == "meta":
            if values.get("name") == "viewport":
                self.has_viewport = True
            if values.get("name") == "description" and values.get("content"):
                self.has_description = True
        if tag == "article" and (value := values.get("data-skill")):
            self.skill_cards.append(value)


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def local_path(reference: str) -> Path | None:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "tel:")):
        return None
    return SITE / parsed.path.lstrip("/")


def main() -> int:
    failures: list[str] = []
    required_files = (
        INDEX,
        SITE / "styles.css",
        SITE / "script.js",
        SITE / "assets" / "favicon.svg",
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

    expected_skills = sorted(
        path.name for path in (ROOT / "skills").iterdir() if path.is_dir()
    )

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
    require(
        sorted(parser.skill_cards) == expected_skills,
        "site skill cards must match every skills/ directory exactly",
        failures,
    )

    for link in parser.links:
        if link.startswith("#"):
            require(link[1:] in parser.ids, f"fragment target does not exist: {link}", failures)
        elif path := local_path(link):
            require(path.is_file(), f"local link target does not exist: {link}", failures)

    for asset in parser.styles + parser.scripts:
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
    require(
        f"<loc>https://{EXPECTED_DOMAIN}/</loc>" in (SITE / "sitemap.xml").read_text(encoding="utf-8"),
        "sitemap must reference the canonical URL",
        failures,
    )

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}")
        return 1

    print(
        f"Validated dependency-free site: {len(parser.skill_cards)} skills, "
        f"{len(parser.ids)} unique IDs, {len(parser.links)} links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
