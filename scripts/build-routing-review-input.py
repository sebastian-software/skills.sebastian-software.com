#!/usr/bin/env python3
"""Build the blind input for a cross-discipline routing review.

Emits the six published skill descriptions verbatim followed by the shuffled
prompts from docs/activation-matrix.json, with no case names and no expected
owners, so a reviewer can hand it to any model and compare the picks against the
matrix afterwards. The shuffle is seeded, so two runs of this script produce the
same numbering and their results stay comparable.

    python3 scripts/build-routing-review-input.py > /tmp/routing-review.md
    python3 scripts/build-routing-review-input.py --key > /tmp/routing-key.json

Keep the key away from whoever or whatever answers the prompts.
"""

from __future__ import annotations

import argparse
import json
import random
import re
import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
SHUFFLE_SEED = 20260731
FRONTMATTER_KEY = re.compile(r"^([A-Za-z_][\w.-]*):\s*(.*)$")

INSTRUCTIONS = """\
You are choosing which skill an agent should load for a user request.

Below are the installed skills with their trigger descriptions, then a list of
requests. For each request, name the single skill that should be loaded, or
"none" if no skill fits and the request needs no specialist guidance. Judge only
from the descriptions as written; do not assume a skill covers something it does
not mention.

Answer with a JSON object mapping each request number to a skill name or "none".
"""


def parse_description(text: str) -> str | None:
    """Read the folded description out of a SKILL.md frontmatter block."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None

    description: list[str] = []
    collecting = False
    for line in lines[1:end]:
        if collecting:
            if line.startswith((" ", "\t")):
                if line.strip():
                    description.append(line.strip())
                continue
            break
        match = FRONTMATTER_KEY.match(line)
        if match and match.group(1) == "description":
            collecting = True
    return " ".join(description) or None


def published_skills() -> list[tuple[str, str]]:
    skills: list[tuple[str, str]] = []
    for path in sorted(SKILLS_ROOT.glob("*/SKILL.md")):
        name = path.parent.name
        description = parse_description(path.read_text(encoding="utf-8"))
        if description:
            skills.append((name, description))
    return skills


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--key",
        action="store_true",
        help="emit the answer key instead of the blind input",
    )
    arguments = parser.parse_args()
    listed = published_skills()

    matrix = json.loads(
        (REPOSITORY_ROOT / "docs" / "activation-matrix.json").read_text(encoding="utf-8")
    )
    cases = matrix["cases"]
    order = sorted(range(len(cases)), key=lambda index: cases[index]["name"])
    random.Random(SHUFFLE_SEED).shuffle(order)

    if arguments.key:
        json.dump(
            {
                str(position): {
                    "name": cases[index]["name"],
                    "owner": cases[index]["owner"],
                }
                for position, index in enumerate(order, start=1)
            },
            sys.stdout,
            indent=2,
        )
        sys.stdout.write("\n")
        return 0

    print(INSTRUCTIONS)
    print("# Installed skills\n")
    for name, description in listed:
        print(f"## {name}\n{description}\n")
    print("# Requests\n")
    for position, index in enumerate(order, start=1):
        print(f"{position}. {cases[index]['prompt']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
