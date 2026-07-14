#!/usr/bin/env python3
"""Validate the public README inventory and local Markdown link graph."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
OSS_URL = "https://oss.sebastian-software.com/"
CONSULTING_URL = "https://sebastian-consulting.com/en"
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def github_anchor(heading: str) -> str:
    """Return the GitHub-style anchor used by the headings in this repository."""
    heading = re.sub(r"<[^>]+>", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
    return re.sub(r"[ -]+", "-", heading).strip("-")


def anchors(markdown: Path) -> set[str]:
    text = markdown.read_text(encoding="utf-8")
    found: set[str] = set()
    occurrences: dict[str, int] = {}
    for heading in MARKDOWN_HEADING.findall(text):
        base = github_anchor(heading)
        suffix = occurrences.get(base, 0)
        found.add(base if suffix == 0 else f"{base}-{suffix}")
        occurrences[base] = suffix + 1
    return found


def validate_local_links(markdown: Path, errors: list[str]) -> None:
    text = markdown.read_text(encoding="utf-8")
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
    skill_directories = sorted(path.parent for path in SKILLS_ROOT.glob("*/SKILL.md"))

    public_readmes = [root_readme]
    for skill_directory in skill_directories:
        name = skill_directory.name
        readme = skill_directory / "README.md"
        if not readme.is_file():
            errors.append(f"skills/{name}: missing README.md")
            continue

        public_readmes.append(readme)
        text = readme.read_text(encoding="utf-8")
        required_fragments = {
            "collection backlink": "../../README.md",
            "agent interface": "[SKILL.md](SKILL.md)",
            "skills CLI install": f"--skill {name}",
            "DALO selection": f"source select sebastian {name}",
            "DALO approval": f"approve skill sebastian:{name}",
            "Sebastian Software OSS link": OSS_URL,
            "Sebastian Software consulting link": CONSULTING_URL,
        }
        for label, fragment in required_fragments.items():
            if fragment not in text:
                errors.append(f"skills/{name}/README.md: missing {label}")

        if f"skills/{name}/" not in root_readme.read_text(encoding="utf-8"):
            errors.append(f"README.md: skill {name} is not linked")

    root_text = root_readme.read_text(encoding="utf-8")
    for label, url in (
        ("Sebastian Software OSS link", OSS_URL),
        ("Sebastian Software consulting link", CONSULTING_URL),
    ):
        if url not in root_text:
            errors.append(f"README.md: missing {label}")

    for readme in sorted(REPOSITORY_ROOT.rglob("README.md")):
        validate_local_links(readme, errors)

    if errors:
        print("README validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"README validation passed: {len(skill_directories)} skill READMEs, "
        f"{len(list(REPOSITORY_ROOT.rglob('README.md')))} README files, "
        "all required links present"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
