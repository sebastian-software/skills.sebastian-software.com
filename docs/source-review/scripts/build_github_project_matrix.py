#!/usr/bin/env python3
"""Build a GitHub project matrix from Things Skill Archive links."""

from __future__ import annotations

import csv
import json
import re
import sqlite3
import subprocess
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path


DB = (
    Path.home()
    / "Library/Group Containers/JLMPQHK86H.com.culturedcode.ThingsMac/ThingsData-VCEI5/Things Database.thingsdatabase/main.sqlite"
)
OUT_DIR = Path("docs/source-review/github-projects")
URL_RE = re.compile(r"https?://[^\s<>\"\]\)]+", re.I)
REPO_RE = re.compile(r"^/([^/]+)/([^/#?]+)")


def normalize_repo(url: str) -> tuple[str, str] | None:
    parsed = urllib.parse.urlparse(url.rstrip(".,;:!?)”’\""))
    host = parsed.netloc.lower().removeprefix("www.")
    if host != "github.com":
        return None
    match = REPO_RE.match(parsed.path)
    if not match:
        return None
    owner = match.group(1)
    name = match.group(2).removesuffix(".git")
    if owner.lower() in {
        "blog",
        "events",
        "features",
        "topics",
        "marketplace",
        "sponsors",
        "settings",
        "notifications",
        "pulls",
        "issues",
    }:
        return None
    return owner, name


def extract_repos() -> dict[str, dict[str, object]]:
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        select
          t.uuid,
          t.title,
          t.notes,
          t.status,
          group_concat(tag.title, ', ') as tags
        from TMTask t
        join TMTaskTag tt0 on tt0.tasks=t.uuid
        join TMTag skill on skill.uuid=tt0.tags and skill.title='Skill Archive'
        left join TMTaskTag tt on tt.tasks=t.uuid
        left join TMTag tag on tag.uuid=tt.tags
        where t.trashed=0
        group by t.uuid
        """
    ).fetchall()

    repos: dict[str, dict[str, object]] = {}
    for row in rows:
        text = (row["title"] or "") + "\n" + (row["notes"] or "")
        for url in URL_RE.findall(text):
            normalized = normalize_repo(url)
            if not normalized:
                continue
            owner, name = normalized
            key = f"{owner}/{name}"
            entry = repos.setdefault(
                key,
                {
                    "owner": owner,
                    "name": name,
                    "urls": set(),
                    "things_ids": set(),
                    "things_titles": set(),
                    "things_tags": set(),
                    "open_things": 0,
                    "completed_things": 0,
                },
            )
            entry["urls"].add(url.rstrip(".,;:!?)”’\""))  # type: ignore[index]
            entry["things_ids"].add(row["uuid"])  # type: ignore[index]
            if row["title"]:
                entry["things_titles"].add(row["title"])  # type: ignore[index]
            if row["tags"]:
                for tag in row["tags"].split(", "):
                    entry["things_tags"].add(tag)  # type: ignore[index]
            if row["status"] == 3:
                entry["completed_things"] += 1  # type: ignore[operator]
            else:
                entry["open_things"] += 1  # type: ignore[operator]
    return repos


def gh_graphql(repos: list[tuple[str, str]]) -> dict[str, dict[str, object]]:
    aliases = []
    for idx, (owner, name) in enumerate(repos):
        aliases.append(
            f'''
            r{idx}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{
              nameWithOwner
              description
              url
              stargazerCount
              forkCount
              isArchived
              isFork
              isDisabled
              pushedAt
              updatedAt
              primaryLanguage {{ name }}
              licenseInfo {{ spdxId }}
              repositoryTopics(first: 10) {{
                nodes {{ topic {{ name }} }}
              }}
              latestRelease {{
                tagName
                publishedAt
              }}
              defaultBranchRef {{
                name
                target {{
                  ... on Commit {{
                    oid
                    committedDate
                  }}
                }}
              }}
            }}
            '''
        )
    query = "query {\n" + "\n".join(aliases) + "\n}"
    try:
        result = subprocess.run(
            ["gh", "api", "graphql", "-f", f"query={query}"],
            text=True,
            capture_output=True,
            check=False,
            timeout=45,
        )
    except subprocess.TimeoutExpired as error:
        raise RuntimeError(f"GitHub GraphQL request timed out after {error.timeout}s") from error
    if result.returncode:
        raise RuntimeError(result.stderr or result.stdout)
    payload = json.loads(result.stdout)
    data = payload.get("data", {})
    out: dict[str, dict[str, object]] = {}
    for idx, value in data.items():
        if not value:
            continue
        requested_owner, requested_name = repos[int(idx.removeprefix("r"))]
        value["canonicalNameWithOwner"] = value["nameWithOwner"]
        out[f"{requested_owner}/{requested_name}"] = value
    return out


def fetch_metadata(keys: list[str]) -> dict[str, dict[str, object]]:
    metadata: dict[str, dict[str, object]] = {}
    pairs = [tuple(key.split("/", 1)) for key in keys]

    missing: list[str] = []

    def fetch_batch(batch: list[tuple[str, str]]) -> dict[str, dict[str, object]]:
        try:
            return gh_graphql(batch)
        except RuntimeError as error:
            if len(batch) == 1:
                owner, name = batch[0]
                missing.append(f"{owner}/{name}")
                print(f"missing {owner}/{name}: {str(error).strip().splitlines()[0]}", flush=True)
                return {}
            mid = len(batch) // 2
            out: dict[str, dict[str, object]] = {}
            out.update(fetch_batch(batch[:mid]))
            out.update(fetch_batch(batch[mid:]))
            return out

    for start in range(0, len(pairs), 20):
        batch = pairs[start : start + 20]
        metadata.update(fetch_batch(batch))
        print(f"fetched {min(start + len(batch), len(pairs))}/{len(pairs)}", flush=True)

    if missing:
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        (OUT_DIR / "missing-repos.txt").write_text("\n".join(sorted(missing)) + "\n")
    return metadata


def join_sorted(values: object) -> str:
    if isinstance(values, set):
        return "; ".join(sorted(str(value) for value in values))
    return ""


def write_outputs(repos: dict[str, dict[str, object]], metadata: dict[str, dict[str, object]]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = OUT_DIR / "github-project-matrix.csv"
    fieldnames = [
        "repo",
        "canonical_repo",
        "description",
        "stars",
        "forks",
        "archived",
        "fork",
        "disabled",
        "language",
        "license",
        "topics",
        "last_push",
        "last_commit",
        "default_branch",
        "latest_release",
        "latest_release_date",
        "open_things",
        "completed_things",
        "things_ids",
        "things_titles",
        "things_tags",
        "url",
    ]
    with csv_path.open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for key in sorted(repos):
            entry = repos[key]
            meta = metadata.get(key, {})
            topics = ""
            if meta.get("repositoryTopics"):
                topics = "; ".join(
                    node["topic"]["name"]
                    for node in meta["repositoryTopics"]["nodes"]  # type: ignore[index]
                )
            latest = meta.get("latestRelease") or {}
            branch = meta.get("defaultBranchRef") or {}
            target = branch.get("target") if isinstance(branch, dict) else {}
            writer.writerow(
                {
                    "repo": key,
                    "canonical_repo": meta.get("canonicalNameWithOwner", meta.get("nameWithOwner", "")),
                    "description": meta.get("description", ""),
                    "stars": meta.get("stargazerCount", ""),
                    "forks": meta.get("forkCount", ""),
                    "archived": meta.get("isArchived", ""),
                    "fork": meta.get("isFork", ""),
                    "disabled": meta.get("isDisabled", ""),
                    "language": (meta.get("primaryLanguage") or {}).get("name", "")
                    if isinstance(meta.get("primaryLanguage"), dict)
                    else "",
                    "license": (meta.get("licenseInfo") or {}).get("spdxId", "")
                    if isinstance(meta.get("licenseInfo"), dict)
                    else "",
                    "topics": topics,
                    "last_push": meta.get("pushedAt", ""),
                    "last_commit": target.get("committedDate", "") if isinstance(target, dict) else "",
                    "default_branch": branch.get("name", "") if isinstance(branch, dict) else "",
                    "latest_release": latest.get("tagName", "") if isinstance(latest, dict) else "",
                    "latest_release_date": latest.get("publishedAt", "") if isinstance(latest, dict) else "",
                    "open_things": entry["open_things"],
                    "completed_things": entry["completed_things"],
                    "things_ids": join_sorted(entry["things_ids"]),
                    "things_titles": join_sorted(entry["things_titles"]),
                    "things_tags": join_sorted(entry["things_tags"]),
                    "url": meta.get("url", f"https://github.com/{key}"),
                }
            )

    canonical_top: dict[str, tuple[str, dict[str, object], int]] = {}
    for key in repos:
        meta = metadata.get(key, {})
        if not meta:
            continue
        canonical = str(meta.get("canonicalNameWithOwner") or meta.get("nameWithOwner") or key)
        existing = canonical_top.get(canonical)
        alias_count = (existing[2] if existing else 0) + 1
        if not existing or int(meta.get("stargazerCount") or 0) > int(existing[1].get("stargazerCount") or 0):
            canonical_top[canonical] = (key, meta, alias_count)
        else:
            canonical_top[canonical] = (existing[0], existing[1], alias_count)

    top = sorted(
        canonical_top.items(),
        key=lambda item: int(item[1][1].get("stargazerCount") or 0),
        reverse=True,
    )[:30]
    archived_count = sum(1 for key in repos if metadata.get(key, {}).get("isArchived"))
    missing_count = len(repos) - len(metadata)
    readme = [
        "# GitHub Project Matrix",
        "",
        "GitHub projects are tracked as an inventory, not as direct skill sources.",
        "Use this matrix to inspect interesting tools separately from source cards",
        "and cluster briefs.",
        "",
        f"- Repositories extracted from Things Skill Archive links: {len(repos)}",
        f"- Metadata fetched: {len(metadata)}",
        f"- Canonical repositories with metadata: {len(canonical_top)}",
        f"- Missing/inaccessible repositories: {missing_count}",
        f"- Archived repositories: {archived_count}",
        "",
        "Matrix file: [`github-project-matrix.csv`](github-project-matrix.csv)",
        "",
        "## Top Repositories By Stars",
        "",
        "| Repo | Aliases | Stars | Last commit | Latest release | Description |",
        "| --- | ---: | ---: | --- | --- | --- |",
    ]
    for canonical, (key, meta, alias_count) in top:
        latest = meta.get("latestRelease") or {}
        branch = meta.get("defaultBranchRef") or {}
        target = branch.get("target") if isinstance(branch, dict) else {}
        description = str(meta.get("description") or "").replace("|", "\\|")
        label = canonical if canonical else key
        readme.append(
            f"| [{label}]({meta.get('url', f'https://github.com/{key}')}) | "
            f"{alias_count} | "
            f"{meta.get('stargazerCount', '')} | "
            f"{target.get('committedDate', '') if isinstance(target, dict) else ''} | "
            f"{latest.get('tagName', '') if isinstance(latest, dict) else ''} | "
            f"{description[:140]} |"
        )
    (OUT_DIR / "README.md").write_text("\n".join(readme) + "\n")


def main() -> None:
    repos = extract_repos()
    metadata = fetch_metadata(sorted(repos))
    write_outputs(repos, metadata)


if __name__ == "__main__":
    main()
