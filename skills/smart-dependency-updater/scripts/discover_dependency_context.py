#!/usr/bin/env python3
"""Inspect common dependency manifests and lockfiles for update planning."""

from __future__ import annotations

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
    "packages.lock.json": "dotnet",
}

MANIFESTS = {
    "package.json": "javascript",
    "Cargo.toml": "rust",
    "pyproject.toml": "python",
    "requirements.txt": "python",
    "requirements-dev.txt": "python",
    "go.mod": "go",
    "Gemfile": "ruby",
    "pom.xml": "java",
    "build.gradle": "jvm",
    "build.gradle.kts": "jvm",
    "Directory.Packages.props": "dotnet",
}


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_error": str(exc)}


def read_toml(path: Path) -> dict[str, Any]:
    if tomllib is None:
        return {"_error": "tomllib unavailable"}
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return {"_error": str(exc)}


def find_files(root: Path, names: set[str]) -> list[Path]:
    ignored = {".git", "node_modules", "target", ".venv", "venv", "dist", "build", ".next"}
    matches: list[Path] = []
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in ignored]
        for name in files:
            if name in names or name.endswith(".csproj") or name.endswith(".fsproj"):
                matches.append(Path(current, name))
    return sorted(matches)


def parse_package_json(path: Path) -> dict[str, Any]:
    data = read_json(path)
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


def parse_go_mod(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8", errors="replace")
    module = re.search(r"^module\s+(.+)$", text, re.MULTILINE)
    go_version = re.search(r"^go\s+(.+)$", text, re.MULTILINE)
    requires = re.findall(r"^\s*require\s+(?:\(|([^\s]+)\s+)", text, re.MULTILINE)
    block_requires = re.findall(r"^\s*([^\s()]+)\s+v[\w.\-+]+", text, re.MULTILINE)
    return {
        "path": str(path),
        "module": module.group(1) if module else None,
        "go": go_version.group(1) if go_version else None,
        "require_entries_estimate": len([r for r in requires if r]) + len(block_requires),
    }


def parse_requirements(path: Path) -> dict[str, Any]:
    lines = [
        line.strip()
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    return {"path": str(path), "entries": len(lines)}


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
        if name in LOCKFILES:
            result["lockfiles"].append({"path": str(rel), "manager": LOCKFILES[name]})
        if name in MANIFESTS or name.endswith(".csproj") or name.endswith(".fsproj"):
            ecosystem = MANIFESTS.get(name, "dotnet")
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
        elif name.startswith("requirements") and name.endswith(".txt"):
            parsed = parse_requirements(path)
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
