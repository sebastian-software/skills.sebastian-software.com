#!/usr/bin/env python3
"""Validate the public README inventory and local Markdown link graph."""

from __future__ import annotations

import json
import re
import sys
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPOSITORY_ROOT / "skills"
OSS_URL = "https://oss.sebastian-software.com/"
CONSULTING_URL = "https://sebastian-consulting.com/en"
LICENSE_NOTICE = "MIT — see the collection [LICENSE](../../LICENSE)."
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$")
MARKDOWN_FENCE = re.compile(r"^\s{0,3}(`{3,}|~{3,})(.*)$")
INLINE_CODE = re.compile(r"``[^`]*``|`[^`\n]*`")
INLINE_IDENTIFIER = re.compile(r"`([a-z][a-z0-9-]*)`")
EXPLICIT_SKILL_REFERENCE = re.compile(
    r"`([a-z][a-z0-9-]*)`\s+skills?\b|\bskills?\s+`([a-z][a-z0-9-]*)`",
    re.IGNORECASE,
)
FRONTMATTER_KEY = re.compile(r"^([A-Za-z_][\w.-]*):\s*(.*)$")
MAX_DESCRIPTION_LENGTH = 1024
SKILL_LINE_LIMIT = 300
REFERENCE_LINE_LIMIT = 500
ROUTE_CONTEXT_REPORT_LIMIT = 900
DEPRECATED_REGISTRY = "docs/deprecated-skills.json"


def load_deprecated_skills(errors: list[str]) -> dict[str, dict[str, str]]:
    """Load the superseded slugs that stay installable for one release window.

    A deprecated stub keeps its original frontmatter so existing selections and
    triggers still resolve, but it carries no guidance. It is therefore exempt
    from the full skill anatomy (review scenarios, agent metadata, the public
    README contract) and from the root inventory, and it is listed in
    MIGRATION.md instead of receiving a site card.
    """
    registry = REPOSITORY_ROOT / DEPRECATED_REGISTRY
    if not registry.is_file():
        return {}

    try:
        payload = json.loads(registry.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"{DEPRECATED_REGISTRY}: invalid JSON: {error.msg}")
        return {}

    deprecated = payload.get("deprecated") if isinstance(payload, dict) else None
    if not isinstance(deprecated, dict):
        errors.append(f"{DEPRECATED_REGISTRY}: 'deprecated' must be an object")
        return {}

    entries: dict[str, dict[str, str]] = {}
    for name, details in deprecated.items():
        if not isinstance(details, dict) or set(details) != {"route", "successor"}:
            errors.append(
                f"{DEPRECATED_REGISTRY}: {name!r} must contain exactly successor and route"
            )
            continue
        if not (SKILLS_ROOT / name / "SKILL.md").is_file():
            errors.append(
                f"{DEPRECATED_REGISTRY}: {name!r} has no skills/{name}/SKILL.md; "
                "remove the entry when the stub is deleted"
            )
            continue
        entries[name] = details
    return entries


def validate_deprecation_stub(
    skill_directory: Path, successor: str, skill_names: set[str], errors: list[str]
) -> None:
    """Require a stub to redirect rather than carry guidance."""
    name = skill_directory.name
    if successor not in skill_names:
        errors.append(
            f"{DEPRECATED_REGISTRY}: {name!r} names successor {successor!r}, "
            "which is not a first-party skill directory"
        )
        return

    skill_text = (skill_directory / "SKILL.md").read_text(encoding="utf-8")
    if f"`{successor}`" not in skill_text:
        errors.append(f"skills/{name}/SKILL.md: stub must name `{successor}`")

    readme_text = (skill_directory / "README.md").read_text(encoding="utf-8")
    for label, fragment in (
        ("successor README link", f"../{successor}/README.md"),
        ("migration table link", "../../MIGRATION.md"),
        ("successor install command", f"--skill {successor}"),
    ):
        if fragment not in readme_text:
            errors.append(f"skills/{name}/README.md: missing {label}")


def validate_worktree_safety_uniqueness(skills_root: Path, errors: list[str]) -> None:
    """Require one shared worktree-safety contract across the collection.

    The three former copies were merged into a single file; a reintroduced copy
    must stay byte-identical rather than drifting silently.
    """
    paths = sorted(skills_root.glob("*/references/worktree-safety.md"))
    if len(paths) < 2:
        return

    baseline = paths[0]
    baseline_bytes = baseline.read_bytes()
    for path in paths[1:]:
        if path.read_bytes() != baseline_bytes:
            errors.append(
                f"{path.relative_to(skills_root.parent)}: must be byte-identical "
                f"to {baseline.relative_to(skills_root.parent)}"
            )


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


def linkable_text(markdown: Path) -> str:
    """Return Markdown content outside fenced code blocks and inline code spans."""
    return INLINE_CODE.sub("", without_fenced_code(markdown.read_text(encoding="utf-8")))


def validate_local_links(markdown: Path, errors: list[str]) -> None:
    text = linkable_text(markdown)
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


def validate_isolated_skill_runtime_links(
    skill_directory: Path, errors: list[str]
) -> None:
    """Reject sibling-skill links that would break selective installation."""
    runtime_documents = [skill_directory / "SKILL.md"]
    references_directory = skill_directory / "references"
    if references_directory.is_dir():
        runtime_documents.extend(sorted(references_directory.rglob("*.md")))

    skills_root = (REPOSITORY_ROOT / "skills").resolve()
    for markdown in runtime_documents:
        for raw_target in MARKDOWN_LINK.findall(linkable_text(markdown)):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue

            path_part = target.partition("#")[0]
            if not path_part:
                continue
            destination = (markdown.parent / unquote(path_part)).resolve()
            try:
                sibling_path = destination.relative_to(skills_root)
            except ValueError:
                continue

            if sibling_path.parts and sibling_path.parts[0] != skill_directory.name:
                errors.append(
                    f"{markdown.relative_to(REPOSITORY_ROOT)}: sibling-skill link "
                    f"{target}; use inline `{sibling_path.parts[0]}` guidance instead"
                )


def validate_first_party_skill_references(
    skill_directory: Path, skill_names: set[str], errors: list[str]
) -> None:
    """Reject named runtime handoffs to skills outside this repository."""
    runtime_documents = [skill_directory / "SKILL.md"]
    references_directory = skill_directory / "references"
    if references_directory.is_dir():
        runtime_documents.extend(sorted(references_directory.rglob("*.md")))

    for markdown in runtime_documents:
        text = without_fenced_code(markdown.read_text(encoding="utf-8"))
        candidates: set[str] = set()

        for match in EXPLICIT_SKILL_REFERENCE.finditer(text):
            candidates.add(match.group(1) or match.group(2))

        if markdown == skill_directory / "SKILL.md":
            routing = re.split(
                r"^## Routing Boundaries\s*$", text, maxsplit=1, flags=re.MULTILINE
            )
            if len(routing) == 2:
                candidates.update(INLINE_IDENTIFIER.findall(routing[1]))

        for candidate in sorted(candidates - skill_names):
            errors.append(
                f"{markdown.relative_to(REPOSITORY_ROOT)}: named skill reference "
                f"`{candidate}` does not match a first-party skill directory"
            )


def parse_skill_frontmatter(text: str) -> dict[str, str] | None:
    """Parse the flat SKILL.md frontmatter without an external YAML dependency.

    Supports plain scalar values plus folded (>-) and literal (|) block scalars,
    which is the full shape this repository allows. Returns None when the
    document has no parseable frontmatter block.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None

    data: dict[str, str] = {}
    current_key: str | None = None
    in_block_scalar = False
    for line in lines[1:end]:
        if in_block_scalar and (line.startswith((" ", "\t")) or not line.strip()):
            if current_key is not None and line.strip():
                folded = data[current_key]
                data[current_key] = f"{folded} {line.strip()}".strip()
            continue

        in_block_scalar = False
        key_match = FRONTMATTER_KEY.match(line)
        if key_match is None:
            return None
        current_key, value = key_match.group(1), key_match.group(2).strip()
        if value in {">", ">-", ">+", "|", "|-", "|+"}:
            in_block_scalar = True
            data[current_key] = ""
        else:
            data[current_key] = value.strip("'\"")
    return data


def validate_frontmatter(skill_directory: Path, errors: list[str]) -> None:
    """Validate the parsed SKILL.md frontmatter keys, name, and description."""
    name = skill_directory.name
    relative = skill_directory.relative_to(REPOSITORY_ROOT)
    skill_file = skill_directory / "SKILL.md"
    frontmatter = parse_skill_frontmatter(skill_file.read_text(encoding="utf-8"))
    if frontmatter is None:
        errors.append(f"{relative}/SKILL.md: missing or malformed YAML frontmatter")
        return

    if set(frontmatter) != {"name", "description"}:
        errors.append(
            f"{relative}/SKILL.md: frontmatter keys must be exactly "
            "['description', 'name']"
        )
    if "name" in frontmatter and frontmatter["name"] != name:
        errors.append(
            f"{relative}/SKILL.md: frontmatter name {frontmatter['name']!r} "
            f"must match the directory name {name!r}"
        )
    description = frontmatter.get("description", "")
    if not description:
        errors.append(f"{relative}/SKILL.md: frontmatter description must not be empty")
    elif len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"{relative}/SKILL.md: description is {len(description)} characters "
            f"after folding; the limit is {MAX_DESCRIPTION_LENGTH}"
        )


def validate_skill_body_conventions(skill_directory: Path, errors: list[str]) -> None:
    """Require the documented routing heading and size limit for every skill."""
    skill_file = skill_directory / "SKILL.md"
    skill_text = skill_file.read_text(encoding="utf-8")
    relative = skill_directory.relative_to(REPOSITORY_ROOT)
    if re.search(
        r"^## Routing Boundaries\s*$", without_fenced_code(skill_text), re.MULTILINE
    ) is None:
        errors.append(
            f"{relative}/SKILL.md: missing exact '## Routing Boundaries' section"
        )

    line_count = len(skill_text.splitlines())
    if line_count > SKILL_LINE_LIMIT:
        errors.append(
            f"{relative}/SKILL.md: {line_count} lines exceeds the "
            f"{SKILL_LINE_LIMIT}-line limit; move detail into references/"
        )


def load_reference_context_exceptions(errors: list[str]) -> dict[str, dict[str, object]]:
    """Load the reviewed exceptions to the default reference-size budget."""
    exception_file = REPOSITORY_ROOT / "docs" / "reference-context-exceptions.json"
    relative = exception_file.relative_to(REPOSITORY_ROOT)
    if not exception_file.is_file():
        errors.append(f"{relative}: missing reference context exception registry")
        return {}

    try:
        payload = json.loads(exception_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"{relative}: invalid JSON: {error.msg}")
        return {}

    if (
        not isinstance(payload, dict)
        or not {"exceptions", "version"}.issubset(payload)
        or not set(payload).issubset({"exceptions", "routes", "version"})
    ):
        errors.append(
            f"{relative}: top-level keys must include ['exceptions', 'version'] "
            "with an optional 'routes' section"
        )
        return {}
    if payload["version"] != 1 or not isinstance(payload["exceptions"], dict):
        errors.append(f"{relative}: version must be 1 and exceptions must be an object")
        return {}

    exceptions: dict[str, dict[str, object]] = {}
    for reference, details in payload["exceptions"].items():
        if not isinstance(reference, str) or not reference.startswith("skills/"):
            errors.append(f"{relative}: exception path must be a skills/ reference")
            continue
        if not isinstance(details, dict) or set(details) != {"defaults", "reason"}:
            errors.append(
                f"{relative}: exception {reference!r} must contain defaults and reason"
            )
            continue
        defaults = details["defaults"]
        reason = details["reason"]
        if (
            not isinstance(defaults, list)
            or not defaults
            or not all(isinstance(default, str) and default.strip() for default in defaults)
            or not isinstance(reason, str)
            or not reason.strip()
        ):
            errors.append(
                f"{relative}: exception {reference!r} defaults must be a non-empty "
                "array of strings and reason must be a non-empty string"
            )
            continue
        reference_file = REPOSITORY_ROOT / reference
        if not reference_file.is_file() or reference_file.suffix != ".md":
            errors.append(
                f"{relative}: exception {reference!r} must name an existing Markdown reference"
            )
            continue
        if len(reference_file.read_text(encoding="utf-8").splitlines()) <= REFERENCE_LINE_LIMIT:
            errors.append(
                f"{relative}: exception {reference!r} no longer exceeds the "
                f"{REFERENCE_LINE_LIMIT}-line limit; remove it from the registry"
            )
            continue
        reference_root = reference_file.parent.resolve()
        invalid_default = next(
            (
                default
                for default in defaults
                if not isinstance(default, str)
                or not (default_file := (reference_root / default).resolve()).is_file()
                or default_file.suffix != ".md"
                or default_file == reference_file.resolve()
                or not default_file.is_relative_to(reference_root)
            ),
            None,
        )
        if invalid_default is not None:
            errors.append(
                f"{relative}: exception {reference!r} default {invalid_default!r} "
                "must name a different existing Markdown reference in the same skill"
            )
            continue
        exceptions[reference] = details
    return exceptions


def load_route_context_exceptions(errors: list[str]) -> dict[str, dict[str, object]]:
    """Load the reviewed exceptions to the advisory route context budget.

    A registered route stays advisory (it emits a warning, not a failure). An
    optional integer ``ceiling`` sets a hard upper bound above the advisory
    limit; a route with no ceiling is never failed on size. JSON, file, and
    top-level-key errors are owned by load_reference_context_exceptions, so this
    loader only reports problems specific to the routes section.
    """
    exception_file = REPOSITORY_ROOT / "docs" / "reference-context-exceptions.json"
    relative = exception_file.relative_to(REPOSITORY_ROOT)
    if not exception_file.is_file():
        return {}
    try:
        payload = json.loads(exception_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    if not isinstance(payload, dict):
        return {}

    routes = payload.get("routes", {})
    if not isinstance(routes, dict):
        errors.append(f"{relative}: routes must be an object")
        return {}

    parsed: dict[str, dict[str, object]] = {}
    for route, details in routes.items():
        if not isinstance(route, str) or not route.startswith("skills/"):
            errors.append(f"{relative}: route path must be a skills/ reference")
            continue
        if (
            not isinstance(details, dict)
            or "reason" not in details
            or not set(details).issubset({"ceiling", "reason"})
        ):
            errors.append(
                f"{relative}: route {route!r} must contain a reason and may set a ceiling"
            )
            continue
        reason = details["reason"]
        if not isinstance(reason, str) or not reason.strip():
            errors.append(
                f"{relative}: route {route!r} reason must be a non-empty string"
            )
            continue
        ceiling = details.get("ceiling")
        if ceiling is not None and (
            not isinstance(ceiling, int)
            or isinstance(ceiling, bool)
            or ceiling <= ROUTE_CONTEXT_REPORT_LIMIT
        ):
            errors.append(
                f"{relative}: route {route!r} ceiling must be an integer above the "
                f"{ROUTE_CONTEXT_REPORT_LIMIT}-line advisory limit"
            )
            continue
        route_file = REPOSITORY_ROOT / route
        if not route_file.is_file() or route_file.suffix != ".md":
            errors.append(
                f"{relative}: route {route!r} must name an existing Markdown route"
            )
            continue
        parsed[route] = details
    return parsed


def validate_reference_context_budgets(
    skill_directory: Path,
    exceptions: dict[str, dict[str, object]],
    route_exceptions: dict[str, dict[str, object]],
    errors: list[str],
    reports: list[str],
) -> None:
    """Enforce focused references and gate broad route-level context."""
    references_directory = skill_directory / "references"
    if not references_directory.is_dir():
        return

    for reference in sorted(references_directory.rglob("*.md")):
        line_count = len(reference.read_text(encoding="utf-8").splitlines())
        if line_count <= REFERENCE_LINE_LIMIT:
            continue
        relative = reference.relative_to(REPOSITORY_ROOT).as_posix()
        exception = exceptions.get(relative)
        if exception is None:
            errors.append(
                f"{relative}: {line_count} lines exceeds the {REFERENCE_LINE_LIMIT}-line "
                "reference limit; split it or register a reviewed context exception"
            )
            continue
        reports.append(
            f"{relative}: {line_count} lines (documented deep-reference exception; "
            f"defaults: {', '.join(exception['defaults'])})"
        )

    for route in sorted(references_directory.glob("route-*.md")):
        direct_references: set[Path] = set()
        for raw_target in MARKDOWN_LINK.findall(linkable_text(route)):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.partition("#")[0]
            destination = (route.parent / unquote(path_part)).resolve()
            if destination.is_file() and destination.is_relative_to(
                references_directory.resolve()
            ):
                direct_references.add(destination)
        line_count = sum(
            len(reference.read_text(encoding="utf-8").splitlines())
            for reference in direct_references
        )
        if line_count <= ROUTE_CONTEXT_REPORT_LIMIT:
            continue

        route_key = route.relative_to(REPOSITORY_ROOT).as_posix()
        registration = route_exceptions.get(route_key)
        if registration is None:
            errors.append(
                f"{route_key}: {line_count} direct-reference lines exceeds the "
                f"{ROUTE_CONTEXT_REPORT_LIMIT}-line advisory budget; make the route "
                "selection explicit or register a reviewed route context exception"
            )
            continue

        ceiling = registration.get("ceiling")
        if isinstance(ceiling, int) and not isinstance(ceiling, bool) and line_count > ceiling:
            errors.append(
                f"{route_key}: {line_count} direct-reference lines exceeds its "
                f"registered ceiling of {ceiling}; trim the route or raise the ceiling"
            )
            continue

        reports.append(
            f"{route_key}: {line_count} direct-reference lines "
            f"(registered route exception, advisory limit {ROUTE_CONTEXT_REPORT_LIMIT})"
        )
        print(
            f"::warning::{route_key}: {line_count} direct-reference lines over the "
            f"{ROUTE_CONTEXT_REPORT_LIMIT}-line advisory budget (registered exception)"
        )


def validate_reference_orphans(skill_directory: Path, errors: list[str]) -> None:
    """Require every reference file to be linked from its own skill directory."""
    references_directory = skill_directory / "references"
    if not references_directory.is_dir():
        return

    linked: dict[Path, set[Path]] = {}
    for markdown in sorted(skill_directory.rglob("*.md")):
        for raw_target in MARKDOWN_LINK.findall(linkable_text(markdown)):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.partition("#")[0]
            if not path_part:
                continue
            destination = (markdown.parent / unquote(path_part)).resolve()
            linked.setdefault(destination, set()).add(markdown.resolve())

    for reference in sorted(references_directory.rglob("*.md")):
        resolved = reference.resolve()
        inbound = linked.get(resolved, set()) - {resolved}
        if not inbound:
            errors.append(
                f"{reference.relative_to(REPOSITORY_ROOT)}: orphaned reference; "
                "it must be linked from at least one Markdown file in its skill"
            )


def validate_evals(skill_directory: Path, errors: list[str]) -> None:
    """Validate unrun review-scenario fixtures without executing model behavior."""
    relative = skill_directory.relative_to(REPOSITORY_ROOT)
    evals_file = skill_directory / "evals" / "evals.json"
    if not evals_file.is_file():
        errors.append(f"{relative}: missing evals/evals.json")
        return

    try:
        payload = json.loads(evals_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        errors.append(f"{relative}/evals/evals.json: invalid JSON: {error.msg}")
        return

    evals = payload.get("evals") if isinstance(payload, dict) else None
    allowed_top_level_keys = {"activation", "evals"}
    if isinstance(payload, dict) and (
        "evals" not in payload or not set(payload).issubset(allowed_top_level_keys)
    ):
        errors.append(
            f"{relative}/evals/evals.json: top-level keys must contain 'evals' "
            "and may include 'activation'"
        )
        return
    if not isinstance(evals, list) or not evals:
        errors.append(f"{relative}/evals/evals.json: evals must be a non-empty array")
        return

    names: set[str] = set()
    for index, evaluation in enumerate(evals):
        location = f"{relative}/evals/evals.json: evals[{index}]"
        if not isinstance(evaluation, dict):
            errors.append(f"{location} must be an object")
            continue
        for field in ("name", "prompt", "expected"):
            value = evaluation.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{location}.{field} must be a non-empty string")
        name = evaluation.get("name")
        if isinstance(name, str) and name.strip():
            if name in names:
                errors.append(f"{location}.name duplicates {name!r}")
            names.add(name)

    if not isinstance(payload, dict) or "activation" not in payload:
        return

    activation = payload["activation"]
    if not isinstance(activation, list) or not activation:
        errors.append(
            f"{relative}/evals/evals.json: activation must be a non-empty array"
        )
        return

    activation_names: set[str] = set()
    trigger_values: set[bool] = set()
    expected_fields = {"name", "prompt", "should_trigger"}
    for index, evaluation in enumerate(activation):
        location = f"{relative}/evals/evals.json: activation[{index}]"
        if not isinstance(evaluation, dict):
            errors.append(f"{location} must be an object")
            continue
        if set(evaluation) != expected_fields:
            errors.append(
                f"{location} keys must be exactly "
                "['name', 'prompt', 'should_trigger']"
            )
            continue
        for field in ("name", "prompt"):
            value = evaluation[field]
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{location}.{field} must be a non-empty string")
        should_trigger = evaluation["should_trigger"]
        if not isinstance(should_trigger, bool):
            errors.append(f"{location}.should_trigger must be a boolean")
        else:
            trigger_values.add(should_trigger)
        name = evaluation["name"]
        if isinstance(name, str) and name.strip():
            if name in activation_names:
                errors.append(f"{location}.name duplicates {name!r}")
            activation_names.add(name)

    if trigger_values != {False, True}:
        errors.append(
            f"{relative}/evals/evals.json: activation must include at least one "
            "should-trigger and one should-not-trigger case"
        )


def validate_skill_metadata(skill_directory: Path, errors: list[str]) -> None:
    """Validate canonical frontmatter and OpenAI-facing skill metadata."""
    name = skill_directory.name
    relative = skill_directory.relative_to(REPOSITORY_ROOT)
    skill_file = skill_directory / "SKILL.md"
    skill_text = skill_file.read_text(encoding="utf-8")
    expected_prefix = f"---\nname: {name}\ndescription: >-\n"
    if not skill_text.startswith(expected_prefix):
        errors.append(f"{relative}/SKILL.md: frontmatter must use description: >-")

    metadata_file = skill_directory / "agents" / "openai.yaml"
    if not metadata_file.is_file():
        errors.append(f"{relative}: missing agents/openai.yaml")
        return

    metadata = metadata_file.read_text(encoding="utf-8")
    for field in ("display_name", "short_description", "default_prompt"):
        if re.search(rf'^  {field}: "[^"\n]+"$', metadata, re.MULTILINE) is None:
            errors.append(f"{relative}/agents/openai.yaml: missing quoted {field}")
    invocation = re.compile(rf"\${re.escape(name)}(?![A-Za-z0-9._-])")
    if invocation.search(metadata) is None:
        errors.append(
            f"{relative}/agents/openai.yaml: default_prompt must invoke ${name}"
        )


def required_readme_fragments(name: str) -> dict[str, str]:
    """Return the public contract every independently installable skill exposes."""
    return {
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
        "MIT license notice": LICENSE_NOTICE,
    }


def validate_required_readme_fragments(
    name: str, text: str, errors: list[str]
) -> None:
    """Validate the human-facing contract for one skill README."""
    for label, fragment in required_readme_fragments(name).items():
        if fragment not in text:
            errors.append(f"skills/{name}/README.md: missing {label}")


def count_references(skill_directories: list[Path]) -> int:
    """Count every focused Markdown reference across the skill collection."""
    return sum(
        len(list((skill_directory / "references").rglob("*.md")))
        for skill_directory in skill_directories
        if (skill_directory / "references").is_dir()
    )


def validate_root_inventory_sentence(
    root_text: str,
    skill_count: int,
    reference_count: int,
    errors: list[str],
) -> None:
    """Tie the README inventory sentence to the computed filesystem counts.

    Mirrors the Open Graph inventory guard in validate-site.py so the public
    skill and reference counts cannot silently drift from the repository.
    """
    expected = (
        f"{skill_count} practice-built skills and "
        f"{reference_count} focused references"
    )
    if expected not in root_text:
        sentence = re.search(
            r"(\d+) practice-built skills and (\d+) focused references", root_text
        )
        found = (
            f"found {sentence.group(1)} skills and {sentence.group(2)} references"
            if sentence
            else "the inventory sentence is missing"
        )
        errors.append(
            f"README.md: inventory sentence must read {expected!r}; {found}"
        )


def main() -> int:
    errors: list[str] = []
    reference_context_reports: list[str] = []
    reference_context_exceptions = load_reference_context_exceptions(errors)
    route_context_exceptions = load_route_context_exceptions(errors)
    root_readme = REPOSITORY_ROOT / "README.md"
    root_text = root_readme.read_text(encoding="utf-8")
    skill_directories = sorted(path.parent for path in SKILLS_ROOT.glob("*/SKILL.md"))
    skill_names = {skill_directory.name for skill_directory in skill_directories}
    deprecated = load_deprecated_skills(errors)
    published = [
        skill_directory
        for skill_directory in skill_directories
        if skill_directory.name not in deprecated
    ]

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
        validate_frontmatter(skill_directory, errors)
        validate_skill_body_conventions(skill_directory, errors)
        validate_reference_context_budgets(
            skill_directory,
            reference_context_exceptions,
            route_context_exceptions,
            errors,
            reference_context_reports,
        )
        validate_isolated_skill_runtime_links(skill_directory, errors)
        validate_first_party_skill_references(skill_directory, skill_names, errors)
        validate_reference_orphans(skill_directory, errors)

        if name in deprecated:
            validate_deprecation_stub(
                skill_directory, deprecated[name]["successor"], skill_names, errors
            )
            continue

        validate_evals(skill_directory, errors)
        validate_skill_metadata(skill_directory, errors)
        validate_required_readme_fragments(name, text, errors)

        if f"skills/{name}/" not in root_text:
            errors.append(f"README.md: skill {name} is not linked")

    validate_worktree_safety_uniqueness(SKILLS_ROOT, errors)

    if reference_context_reports:
        print("Reference context report:")
        for report in reference_context_reports:
            print(f"- {report}")

    validate_root_inventory_sentence(
        root_text,
        len(published),
        count_references(published),
        errors,
    )

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
        f"Public documentation and review-scenario schema validation passed: "
        f"{len(published)} skill READMEs plus {len(deprecated)} deprecation stubs, "
        f"{len(markdown_files)} public Markdown files, all required links present; "
        "model behavior is not executed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
