#!/usr/bin/env python3
"""Validate the public README inventory and local Markdown link graph."""

from __future__ import annotations

import re
import sys
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
OSS_URL = "https://oss.sebastian-software.com/"
CONSULTING_URL = "https://sebastian-consulting.com/en"
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$")
MARKDOWN_FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")


def github_anchor(heading: str) -> str:
    """Return the GitHub-style anchor used by the headings in this repository."""
    heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
    return heading.replace(" ", "-")


def without_fenced_code(text: str) -> str:
    """Return Markdown content outside fenced code blocks."""
    lines: list[str] = []
    fence: tuple[str, int] | None = None

    for line in text.splitlines():
        fence_match = MARKDOWN_FENCE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
                continue
            if (
                marker[0] == fence[0]
                and len(marker) >= fence[1]
                and not fence_match.group(2).strip()
            ):
                fence = None
                continue
        if fence is None:
            lines.append(line)

    return "\n".join(lines)


@lru_cache
def anchors(markdown: Path) -> set[str]:
    found: set[str] = set()
    occurrences: dict[str, int] = {}

    for line in without_fenced_code(markdown.read_text(encoding="utf-8")).splitlines():
        heading_match = MARKDOWN_HEADING.match(line)
        if not heading_match:
            continue
        heading = heading_match.group(1)
        base = github_anchor(heading)
        suffix = occurrences.get(base, 0)
        found.add(base if suffix == 0 else f"{base}-{suffix}")
        occurrences[base] = suffix + 1
    return found


def validate_local_links(markdown: Path, errors: list[str]) -> None:
    text = without_fenced_code(markdown.read_text(encoding="utf-8"))
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue

        path_part, separator, fragment = target.partition("#")
        destination = markdown if not path_part else markdown.parent / unquote(path_part)
        destination = destination.resolve()

        if not destination.exists():
            errors.append(f"{markdown.relative_to(REPOSITORY_ROOT)}: missing {target}")
            continue

        if separator and fragment:
            anchor_file = destination / "README.md" if destination.is_dir() else destination
            if anchor_file.suffix.lower() == ".md" and fragment not in anchors(anchor_file):
                errors.append(
                    f"{markdown.relative_to(REPOSITORY_ROOT)}: missing anchor #{fragment} "
                    f"in {anchor_file.relative_to(REPOSITORY_ROOT)}"
                )


def main() -> int:
    errors: list[str] = []
    root_readme = REPOSITORY_ROOT / "README.md"
    root_text = root_readme.read_text(encoding="utf-8")
    skill_directories = sorted(path.parent for path in SKILLS_ROOT.glob("*/SKILL.md"))

    markdown_files = [root_readme]
    for skill_directory in skill_directories:
        name = skill_directory.name
        readme = skill_directory / "README.md"
        if not readme.is_file():
            errors.append(f"skills/{name}: missing README.md")
            continue

        markdown_files.extend((readme, skill_directory / "SKILL.md"))
        references_directory = skill_directory / "references"
        if references_directory.is_dir():
            markdown_files.extend(sorted(references_directory.rglob("*.md")))
        text = readme.read_text(encoding="utf-8")
        required_fragments = {
            "collection backlink": "../../README.md",
            "agent interface": "[SKILL.md](SKILL.md)",
            "skills CLI install": f"--skill {name}",
            "DALO setup guide": "../../docs/dalo.md",
            "DALO initialization": "dalo init",
            "DALO target link": "dalo target link codex",
            "DALO selection": f"source select sebastian {name}",
            "DALO approval": f"approve skill sebastian:{name}",
            "Sebastian Software OSS link": OSS_URL,
            "Sebastian Software consulting link": CONSULTING_URL,
        }
        for label, fragment in required_fragments.items():
            if fragment not in text:
                errors.append(f"skills/{name}/README.md: missing {label}")

        if f"skills/{name}/" not in root_text:
            errors.append(f"README.md: skill {name} is not linked")

    for label, url in (
        ("Sebastian Software OSS link", OSS_URL),
        ("Sebastian Software consulting link", CONSULTING_URL),
    ):
        if url not in root_text:
            errors.append(f"README.md: missing {label}")

    for markdown in markdown_files:
        validate_local_links(markdown, errors)

    if errors:
        print("README validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"README validation passed: {len(skill_directories)} skill READMEs, "
        f"{len(markdown_files)} public Markdown files, all required links present"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
