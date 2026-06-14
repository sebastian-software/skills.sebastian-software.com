import { promises as fs } from "node:fs";
import path from "node:path";

import type { SkillFrontmatter } from "./types.js";

import { SkillSyncError } from "./errors.js";

function cleanScalar(value: string): string {
  return value.trim().replace(/^['"]/, "").replace(/['"]$/, "");
}

function extractFrontmatter(text: string, skillFile: string): string {
  if (!text.startsWith("---\n")) {
    throw new SkillSyncError(`${skillFile} must start with YAML frontmatter`);
  }

  const end = text.indexOf("\n---", 4);
  if (end === -1) {
    throw new SkillSyncError(`${skillFile} has unterminated frontmatter`);
  }

  return text.slice(4, end);
}

function isTopLevelField(line: string): boolean {
  return line.trim() !== "" && !line.startsWith(" ") && !line.startsWith("-") && line.includes(":");
}

function parseFieldLine(line: string): { key: string; value: string } | undefined {
  const separator = line.indexOf(":");
  if (separator <= 0) {
    return undefined;
  }

  return {
    key: line.slice(0, separator),
    value: line.slice(separator + 1),
  };
}

function readIndentedContinuation(lines: string[], startIndex: number): string {
  const continuation: string[] = [];
  for (const line of lines.slice(startIndex)) {
    if (!line.startsWith(" ") && !line.startsWith("\t")) {
      break;
    }

    const value = line.trim();
    if (value !== "") {
      continuation.push(value);
    }
  }

  return continuation.join(" ");
}

function parseFrontmatterLines(frontmatter: string): Record<string, string> {
  const metadata: Record<string, string> = {};
  const lines = frontmatter.split("\n");

  for (const [index, line] of lines.entries()) {
    if (!isTopLevelField(line)) {
      continue;
    }

    const field = parseFieldLine(line);
    if (field === undefined) {
      continue;
    }

    const scalar = cleanScalar(field.value);
    metadata[field.key] = scalar === "" ? readIndentedContinuation(lines, index + 1) : scalar;
  }

  return metadata;
}

function requireFrontmatterField(
  metadata: Record<string, string>,
  key: "description" | "name",
  skillFile: string,
): string {
  const value = metadata[key];
  if (value === undefined || value === "") {
    throw new SkillSyncError(`${skillFile} is missing frontmatter field: ${key}`);
  }

  return value;
}

export async function parseSkillFrontmatter(skillRoot: string): Promise<SkillFrontmatter> {
  const skillFile = path.join(skillRoot, "SKILL.md");
  const text = await fs.readFile(skillFile, "utf8");
  const metadata = parseFrontmatterLines(extractFrontmatter(text, skillFile));
  const name = requireFrontmatterField(metadata, "name", skillFile);
  const description = requireFrontmatterField(metadata, "description", skillFile);

  return {
    name,
    description,
    metadata,
  };
}
