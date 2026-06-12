#!/usr/bin/env python3
"""Apply a cluster brief's Things Actions table to Things3.

This script intentionally uses Things3 AppleScript instead of writing to the
Things SQLite database. It adds review/final-decision tags, removes the intake
tag, and marks items complete when requested by the table.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ACTION_RE = re.compile(r"^## Things Actions\n(.*?)(?=\n## |\Z)", re.M | re.S)


def osa_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def parse_actions(path: Path) -> list[tuple[str, str, bool]]:
    text = path.read_text()
    match = ACTION_RE.search(text)
    if not match:
        raise SystemExit(f"No '## Things Actions' table found in {path}")

    actions: list[tuple[str, str, bool]] = []
    for line in match.group(1).splitlines():
        if not line.startswith("| `"):
            continue
        cols = [col.strip() for col in line.strip("|").split("|")]
        if len(cols) < 4:
            continue
        things_id = cols[0].strip("`")
        final_tag = cols[2].strip("`")
        complete = cols[3].lower() == "yes"
        actions.append((things_id, final_tag, complete))

    if not actions:
        raise SystemExit(f"No action rows found in {path}")

    ids = [action[0] for action in actions]
    if len(ids) != len(set(ids)):
        raise SystemExit(f"Duplicate Things IDs in {path}")

    return actions


APPLESCRIPT_HEADER = r'''
on ensureTag(tagName)
	tell application "Things3"
		if not (exists tag tagName) then make new tag with properties {name:tagName}
	end tell
end ensureTag

on splitTags(tagText)
	if tagText is missing value then return {}
	set currentText to tagText as text
	if currentText is "" then return {}
	set AppleScript's text item delimiters to ", "
	set parts to text items of currentText
	set AppleScript's text item delimiters to ""
	return parts
end splitTags

on joinTags(parts)
	set AppleScript's text item delimiters to ", "
	set outText to parts as text
	set AppleScript's text item delimiters to ""
	return outText
end joinTags

on normalizeTags(existingNames, finalTag)
	set parts to my splitTags(existingNames)
	set outParts to {}
	repeat with t in parts
		set tv to t as text
		if tv is not "Skill Archive Intake" and tv is not "Skill Archive Candidate" and tv is not "Skill Archive Deferred" and tv is not "Skill Archive Rejected" then
			if outParts does not contain tv then set end of outParts to tv
		end if
	end repeat
	if outParts does not contain "Skill Archive" then set end of outParts to "Skill Archive"
	if outParts does not contain "Skill Archive Reviewed" then set end of outParts to "Skill Archive Reviewed"
	if outParts does not contain finalTag then set end of outParts to finalTag
	return my joinTags(outParts)
end normalizeTags

'''


def run_osascript(script: str) -> None:
    result = subprocess.run(
        ["osascript"],
        input=script,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        sys.stderr.write(result.stderr or result.stdout)
        raise SystemExit(result.returncode)


def apply_actions(actions: list[tuple[str, str, bool]], dry_run: bool) -> None:
    if dry_run:
        for things_id, final_tag, complete in actions:
            print(f"{things_id}\t{final_tag}\tcomplete={complete}")
        return

    for tag in [
        "Skill Archive",
        "Skill Archive Reviewed",
        "Skill Archive Candidate",
        "Skill Archive Deferred",
        "Skill Archive Rejected",
    ]:
        run_osascript(APPLESCRIPT_HEADER + f"my ensureTag({osa_quote(tag)})")

    records = "{" + ", ".join(
        "{"
        + osa_quote(things_id)
        + ", "
        + osa_quote(final_tag)
        + ", "
        + ("true" if complete else "false")
        + "}"
        for things_id, final_tag, complete in actions
    ) + "}"

    script = APPLESCRIPT_HEADER + f'''
set actionRows to {records}
tell application "Things3"
	repeat with rowData in actionRows
		set todoId to item 1 of rowData
		set finalTag to item 2 of rowData
		set shouldComplete to item 3 of rowData
		try
			set itemRef to to do id (todoId as text)
			set tag names of itemRef to my normalizeTags((tag names of itemRef), finalTag)
			if shouldComplete then set status of itemRef to completed
		end try
	end repeat
end tell
'''
    run_osascript(script)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cluster_brief", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    actions = parse_actions(args.cluster_brief)
    apply_actions(actions, args.dry_run)
    print(f"{'would apply' if args.dry_run else 'applied'} {len(actions)} actions")


if __name__ == "__main__":
    main()
