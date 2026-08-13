#!/usr/bin/env python3
"""Inspect common dependency manifests and lockfiles for update planning."""

from __future__ import annotations

import ast
import configparser
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None  # type: ignore[assignment]


LOCKFILES = {
    "package-lock.json": "npm",
    "npm-shrinkwrap.json": "npm",
    "pnpm-lock.yaml": "pnpm",
    "yarn.lock": "yarn",
    "bun.lock": "bun",
    "bun.lockb": "bun",
    "Cargo.lock": "cargo",
    "poetry.lock": "poetry",
    "uv.lock": "uv",
    "Pipfile.lock": "pipenv",
    "go.sum": "go",
    "Gemfile.lock": "bundler",
    "gradle.lockfile": "gradle",
    "packages.lock.json": "dotnet",
}

MANIFESTS = {
    "package.json": "javascript",
    "Cargo.toml": "rust",
    "pyproject.toml": "python",
    "requirements.txt": "python",
    "requirements-dev.txt": "python",
    "setup.cfg": "python",
    "setup.py": "python",
    "go.mod": "go",
    "Gemfile": "ruby",
    "pom.xml": "java",
    "build.gradle": "jvm",
    "build.gradle.kts": "jvm",
    "Directory.Packages.props": "dotnet",
}

REQUIREMENTS_FILENAME = re.compile(
    r"^requirements(?:[-_.][A-Za-z0-9][A-Za-z0-9_.-]*)?\.txt$",
    re.IGNORECASE,
)
REQUIREMENT_ENTRY = re.compile(
    r"^(?:"
    r"-[-A-Za-z][^\s]*(?:\s+.+)?|"
    r"[A-Za-z0-9][A-Za-z0-9_.-]*(?:\[[^]]+])?"
    r"(?:\s*(?:===|==|!=|<=|>=|<|>|~=|@)\s*[^;]+)?(?:\s*;\s*.+)?|"
    r"(?:git|hg|svn|bzr)\+\S+(?:\s*;\s*.+)?|"
    r"(?:https?|file)://\S+(?:\s*;\s*.+)?|"
    r"(?:\.{1,2}/|/|~/)\S+(?:\s*;\s*.+)?"
    r")$"
)
GO_MODULE_VERSION = re.compile(r"^[^\s()]+\s+v[\w.\-+]+$")
GO_REQUIRE_LINE = re.compile(r"^require\s+[^\s()]+\s+v[\w.\-+]+$")


def read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {"_error": "JSON root is not an object"}
    except Exception as exc:
        return {"_error": str(exc)}


def read_toml(path: Path) -> dict[str, Any]:
    if tomllib is None:
        return {"_error": "tomllib unavailable"}
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_error": str(exc)}


def is_requirements_candidate(name: str) -> bool:
    return bool(REQUIREMENTS_FILENAME.fullmatch(name))


def find_files(root: Path, names: set[str]) -> list[Path]:
    ignored = {
        ".git",
        "node_modules",
        "target",
        ".venv",
        "venv",
        "dist",
        "build",
        ".next",
        "vendor",
    }
    matches: list[Path] = []
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ignored]
        for name in files:
            if (
                name in names
                or is_requirements_candidate(name)
                or name.endswith(".csproj")
                or name.endswith(".fsproj")
            ):
                matches.append(Path(current, name))
    return sorted(matches)


def parse_package_json(path: Path) -> dict[str, Any]:
    data = read_json(path)
    if "_error" in data:
        return {"path": str(path), "_error": data["_error"]}
    dep_sections = [
        "dependencies",
        "devDependencies",
        "peerDependencies",
        "optionalDependencies",
        "overrides",
        "resolutions",
    ]
    return {
        "path": str(path),
        "package_manager": data.get("packageManager"),
        "engines": data.get("engines", {}),
        "workspaces": data.get("workspaces"),
        "scripts": data.get("scripts", {}),
        "dependency_counts": {
            section: len(data.get(section, {}) or {}) for section in dep_sections
        },
    }


def parse_cargo_toml(path: Path) -> dict[str, Any]:
    data = read_toml(path)
    if "_error" in data:
        return {"path": str(path), "_error": data["_error"]}
    sections = ["dependencies", "dev-dependencies", "build-dependencies"]
    package = data.get("package", {}) if isinstance(data, dict) else {}
    workspace = data.get("workspace", {}) if isinstance(data, dict) else {}
    return {
        "path": str(path),
        "package": {
            "name": package.get("name"),
            "version": package.get("version"),
            "rust_version": package.get("rust-version"),
            "edition": package.get("edition"),
        },
        "workspace": bool(workspace),
        "dependency_counts": {
            section: len(data.get(section, {}) or {}) for section in sections
        },
    }


def parse_pyproject(path: Path) -> dict[str, Any]:
    data = read_toml(path)
    if "_error" in data:
        return {"path": str(path), "_error": data["_error"]}
    project = data.get("project", {}) if isinstance(data, dict) else {}
    tool = data.get("tool", {}) if isinstance(data, dict) else {}
    return {
        "path": str(path),
        "project": {
            "name": project.get("name"),
            "requires_python": project.get("requires-python"),
            "dependencies": len(project.get("dependencies", []) or []),
            "optional_dependency_groups": sorted((project.get("optional-dependencies") or {}).keys()),
        },
        "tools": sorted(tool.keys()),
    }


def requirement_entry_count(value: str) -> int:
    return len([line for line in value.splitlines() if line.strip() and not line.strip().startswith("#")])


def parse_setup_cfg(path: Path) -> dict[str, Any]:
    config = configparser.RawConfigParser()
    try:
        with path.open(encoding="utf-8") as file:
            config.read_file(file)
    except (OSError, configparser.Error) as exc:
        return {"path": str(path), "_error": str(exc)}

    install_requires = config.get("options", "install_requires", fallback="")
    extras = {
        name: requirement_entry_count(value)
        for name, value in config.items("options.extras_require")
    } if config.has_section("options.extras_require") else {}
    return {
        "path": str(path),
        "setuptools": {
            "install_requires": requirement_entry_count(install_requires),
            "extras": extras,
        },
    }


def literal_dependency_count(node: ast.AST) -> int | None:
    try:
        value = ast.literal_eval(node)
    except (ValueError, TypeError):
        return None
    return len(value) if isinstance(value, (list, tuple, set)) else None


def parse_setup_py(path: Path) -> dict[str, Any]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError) as exc:
        return {"path": str(path), "_error": str(exc)}

    dependency_counts: dict[str, int | None] = {}
    extras: dict[str, int | None] = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not (
            isinstance(node.func, ast.Name) and node.func.id == "setup"
        ):
            continue
        for keyword in node.keywords:
            if keyword.arg in {"install_requires", "setup_requires"}:
                dependency_counts[keyword.arg] = literal_dependency_count(keyword.value)
            elif keyword.arg == "extras_require" and isinstance(keyword.value, ast.Dict):
                for key, value in zip(keyword.value.keys, keyword.value.values, strict=True):
                    if isinstance(key, ast.Constant) and isinstance(key.value, str):
                        extras[key.value] = literal_dependency_count(value)
        break
    return {
        "path": str(path),
        "setuptools": {"dependency_counts": dependency_counts, "extras": extras},
    }


def parse_go_mod(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return {"path": str(path), "_error": str(exc)}
    module = re.search(r"^module\s+(.+)$", text, re.MULTILINE)
    go_version = re.search(r"^go\s+(.+)$", text, re.MULTILINE)
    require_entries = 0
    in_require_block = False
    for raw_line in text.splitlines():
        line = raw_line.split("//", 1)[0].strip()
        if re.fullmatch(r"require\s*\(", line):
            in_require_block = True
            continue
        if in_require_block and line == ")":
            in_require_block = False
            continue
        if in_require_block and GO_MODULE_VERSION.fullmatch(line):
            require_entries += 1
        elif GO_REQUIRE_LINE.fullmatch(line):
            require_entries += 1
    return {
        "path": str(path),
        "module": module.group(1) if module else None,
        "go": go_version.group(1) if go_version else None,
        "require_entries_estimate": require_entries,
    }


def parse_requirements(path: Path) -> dict[str, Any]:
    try:
        lines = [
            line.strip()
            for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
            if line.strip() and not line.strip().startswith("#")
        ]
    except OSError as exc:
        return {"path": str(path), "_error": str(exc)}
    parsed_entries = sum(bool(REQUIREMENT_ENTRY.fullmatch(line)) for line in lines)
    return {
        "path": str(path),
        "entries": len(lines),
        "parsed_entries": parsed_entries,
        "unparsed_entries": len(lines) - parsed_entries,
    }


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd().resolve()
    files = find_files(root, set(LOCKFILES) | set(MANIFESTS))
    result: dict[str, Any] = {
        "root": str(root),
        "lockfiles": [],
        "manifests": [],
        "package_json": [],
        "cargo": [],
        "python": [],
        "go": [],
        "hints": [],
    }

    for path in files:
        rel = path.relative_to(root)
        name = path.name
        requirements = None
        if is_requirements_candidate(name):
            requirements = parse_requirements(path)
        is_requirements = requirements is not None
        if name in LOCKFILES:
            result["lockfiles"].append({"path": str(rel), "manager": LOCKFILES[name]})
        if name in MANIFESTS or is_requirements or name.endswith(".csproj") or name.endswith(".fsproj"):
            ecosystem = MANIFESTS.get(name, "python" if is_requirements else "dotnet")
            result["manifests"].append({"path": str(rel), "ecosystem": ecosystem})
        if name == "package.json":
            parsed = parse_package_json(path)
            parsed["path"] = str(rel)
            result["package_json"].append(parsed)
        elif name == "Cargo.toml":
            parsed = parse_cargo_toml(path)
            parsed["path"] = str(rel)
            result["cargo"].append(parsed)
        elif name == "pyproject.toml":
            parsed = parse_pyproject(path)
            parsed["path"] = str(rel)
            result["python"].append(parsed)
        elif name == "setup.cfg":
            parsed = parse_setup_cfg(path)
            parsed["path"] = str(rel)
            result["python"].append(parsed)
        elif name == "setup.py":
            parsed = parse_setup_py(path)
            parsed["path"] = str(rel)
            result["python"].append(parsed)
        elif is_requirements:
            parsed = requirements
            assert parsed is not None
            parsed["path"] = str(rel)
            result["python"].append(parsed)
        elif name == "go.mod":
            parsed = parse_go_mod(path)
            parsed["path"] = str(rel)
            result["go"].append(parsed)

    managers = sorted({item["manager"] for item in result["lockfiles"]})
    if len(managers) > 1:
        result["hints"].append(f"Multiple lockfile managers detected: {', '.join(managers)}")
    if result["package_json"]:
        scripts = {}
        for pkg in result["package_json"]:
            scripts[str(pkg["path"])] = {
                key: value
                for key, value in pkg.get("scripts", {}).items()
                if re.search(r"test|check|lint|type|build|format", key)
            }
        result["js_validation_scripts"] = scripts

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
