import { promises as fs } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

import { parseSkillFrontmatter } from "../src/frontmatter.js";
import { makeTempDir } from "./helpers.js";

describe("parseSkillFrontmatter", () => {
  it("reads indented multiline scalar fields", async () => {
    const skillRoot = await makeTempDir("skill-sync-frontmatter-");
    await fs.writeFile(
      path.join(skillRoot, "SKILL.md"),
      `---
name: convex
description:
  Routes general Convex requests to the right project skill. Use when the user
  asks which Convex skill to use or gives an underspecified Convex app task.
---

# Convex
`,
    );

    await expect(parseSkillFrontmatter(skillRoot)).resolves.toMatchObject({
      name: "convex",
      description:
        "Routes general Convex requests to the right project skill. Use when the user asks which Convex skill to use or gives an underspecified Convex app task.",
    });
  });
});
