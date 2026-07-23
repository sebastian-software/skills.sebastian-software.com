# Authoring Skills

Skills are focused instruction packages. A skill may route a cohesive domain to
multiple workflows, but it must remain understandable from `SKILL.md` without
loading every bundled resource into context.

## Required Structure

First-party skills live directly under `skills/`:

```text
skills/skill-name/
  README.md
  SKILL.md
  evals/
    evals.json
  agents/
    openai.yaml
  references/  # optional focused guidance
  scripts/     # optional deterministic helpers
```

Every public skill requires `README.md`, `SKILL.md`, `evals/evals.json`, and
`agents/openai.yaml`. Add the other directories when they serve a clear purpose.
Do not add external snapshots or generated copies.

## Human-Facing `README.md`

Treat every independently installable skill as a small product. Its README is
for people deciding whether the skill fits their work; do not duplicate the
agent instructions from `SKILL.md`.

Each skill README must include:

- a link back to the collection README
- a specific, outcome-led value proposition
- representative capabilities, use cases, and example prompts
- a link to the local `SKILL.md` agent interface
- selective installation commands for the skills CLI and DALO
- an honest scope or boundary section
- where a handoff matters, inline references to relevant first-party skills,
  naming the owner and the handoff
- the canonical Sebastian Software open-source and English consulting links
- the portable license notice `MIT — see the collection [LICENSE](../../LICENSE).`

Use `https://oss.sebastian-software.com/` for Sebastian Software open source and
`https://sebastian-consulting.com/en` for consulting. Keep related-skill
references purposeful: explain where the workflow hands work to the other skill
instead of building a generic cross-promotion list. In `SKILL.md` and
`references/`, name related skills inline rather than linking into sibling
directories, because selective installs do not include those files.

Run `python3 scripts/validate-readmes.py` after adding or changing a README. CI
requires one README per public skill and verifies collection links, agent
interface links, selective install commands, Sebastian Software links, local
Markdown paths, and Markdown anchors. When adding a skill, also add its card and
inventory metadata to `site/index.html`, then run
`python3 scripts/validate-site.py`. That validator requires the site inventory,
filter counts, structured data, and public skill directory to agree.

## `SKILL.md` Frontmatter

Every new skill starts with valid YAML frontmatter containing only `name` and
`description`:

```yaml
---
name: effective-web
description: >-
  Design, build, review, and improve user-facing web experiences. Use for UI/UX,
  CSS, React, accessibility, frontend SEO, performance, or frontend testing.
---
```

DALO parses standard YAML, including literal and folded block scalars. It still
tolerates legacy metadata on existing skills, but do not add new fields unless
the repository contract changes.

### Writing the description

The description is what an agent sees before deciding whether to load a skill.

- State what the skill covers and name concrete trigger situations.
- Prefer terms users actually mention over abstract goals.
- Keep the trigger concise; details belong in the body and references.
- Keep the frontmatter name portable: lowercase ASCII letters, digits, `.`, `_`,
  and `-` only.

## `SKILL.md` Body Conventions

- Name the boundary section exactly `## Routing Boundaries`. It states what the
  skill must not invent and where it hands work to another skill; keep that
  canonical heading so agents and reviewers find the section in every skill.
- Cross-reference other skills by their frontmatter name in inline code, for
  example: route frontend work through `effective-web`. Do not use prose names,
  quotes, or bare links for skill-name cross references.
- Keep `SKILL.md` at or below 300 lines. The body owns the trigger, workflow,
  routing, and boundaries; detailed tables, policy text, and examples belong in
  `references/`. `scripts/validate-readmes.py` enforces this limit and the
  canonical boundary heading in CI.

## Resource Directories

- Use `agents/openai.yaml` for the required product-facing display name, short
  description, and `$skill-name` invocation prompt; never store project
  decisions or agent memory there.
- Use `references/` for detailed guidance loaded only when needed.
- Use `scripts/` for deterministic helpers agents can run.
- Use `assets/` or `examples/` only when a skill genuinely needs reusable output
  resources or complete examples; neither directory is part of the default
  first-party anatomy.

Keep `SKILL.md` lean. For a routed skill, link every route directly from
`SKILL.md` and keep references one level deep. Move long tables, examples,
policy text, and API details into references so agents load only the context
needed for the current task.

## Distill, Don't Archive

This repository ships skills, not an intake log. When a source is useful, absorb
its knowledge into an actionable rule, checklist item, or short example.

- Write imperative guidance an agent can act on.
- Remove source-review commentary and internal tracking notes.
- Do not paste source material merely to preserve it.
- Classify fast-moving platform guidance and keep experimental behavior gated.

Normative specifications and compatibility data may change defaults. Practice
material can improve workflows and examples. Experimental or single-source
claims stay support-gated and never become unconditional defaults.

## Persist Decisions in Shared ADRs

When a skill needs to preserve durable project rationale, use the project's
Architecture Decision Record convention instead of inventing a skill-specific
dot folder, memory file, or private schema.

- Discover and follow existing ADR directories, templates, numbering, statuses,
  and indexes before creating anything.
- Use `docs/adr/` with plain Markdown only when the project has no convention and
  the decision genuinely warrants a durable record.
- Record cross-cutting technical, product, design, content, marketing,
  communication, security, operational, and process choices when their rationale
  must survive contributors, tools, channels, or sessions.
- Keep exact values and executable behavior in code, configuration, design
  tokens, editorial guides, or tests. The ADR owns direction, rationale,
  tradeoffs, consequences, and review triggers.
- Preserve accepted history. Supersede decisions instead of silently rewriting
  them to match current implementation.
- Route ADR creation, review, and lifecycle details through `decision-records`.

## Keep Findings, Plans, and Decisions Distinct

Use the repository's shared artifacts according to what they own:

- An audit finding owns verified evidence, impact, confidence, and a possible
  correction.
- An implementation plan or issue owns delivery scope, sequencing,
  dependencies, verification, owners, and temporary status.
- An ADR owns a durable choice, rationale, tradeoffs, consequences, and review
  triggers.

Discover existing issue trackers and plan directories before writing. Do not
make every skill create `plans/`, a private dot folder, or a custom debt ledger.
When no convention exists and the user explicitly asks to save a plan, use plain
Markdown under `docs/plans/`; create an index only when several plans require
ordering. Route repository audits, plan creation, complexity review, and backlog
reconciliation through `codebase-improvement`.

## Behavioral Evals

For consequential workflow or judgment changes, add an eval that tests the
failure mode the new rule is meant to prevent.

Store evals in `skills/<name>/evals/evals.json`. New files use a top-level
`evals` array whose entries contain `name`, `prompt`, and `expected`:

```json
{
  "evals": [
    {
      "name": "reject-shortcut",
      "prompt": "A realistic request containing the tempting shortcut.",
      "expected": "The decision, evidence, and tradeoff a strong response must surface."
    }
  ]
}
```

Keep `name` stable and descriptive. Treat `prompt` as the user input and
`expected` as behavioral acceptance criteria, not a golden response string.

- Use a realistic prompt containing a plausible misconception, incomplete fix,
  or tempting shortcut; do not merely ask the agent to repeat the rule.
- State the expected decision and the evidence or tradeoff it must surface,
  without prescribing incidental wording or one exact implementation.
- Include fallback and degraded-state scenarios for progressive enhancements.
- Prefer a few discriminating cases over broad happy-path coverage that a
  baseline model would already pass.

## First-Party Boundary

Everything below `skills/` is maintained here as Sebastian Software source.
External skills must be configured as DALO catalog sources. Do not copy them,
rename their frontmatter, add `SOURCE.md` snapshots, or maintain repository-local
source and lock manifests.

Label an external dependency at every mention site as "`<name>` from the
separately managed DALO `<catalog>` catalog." Reference files can be loaded
without their parent `SKILL.md`, so do not rely on provenance stated elsewhere
and never describe a catalog skill as local.

## Delivery Worktree Inventory

Keep every independently installed owner safe without requiring a shared
runtime or private receipt file.

| Skill | Worktree behavior | Local safety owner |
| --- | --- | --- |
| `pr-review` | Creates or adopts a PR worktree; writes, validates, stages, commits, pushes, rebases when authorized, and removes workflow-created worktrees | [`pr-review/references/worktree-safety.md`](../skills/pr-review/references/worktree-safety.md) |
| `smart-dependency-updater` | Creates or adopts one worktree per dependency PR group; writes manifests and lockfiles, validates, stages, commits, pushes, publishes, and cleans up owned worktrees | [`smart-dependency-updater/references/worktree-safety.md`](../skills/smart-dependency-updater/references/worktree-safety.md) |
| `port-codebases` | Creates or adopts isolated worktrees for port shards; writes, validates, stages, checkpoints, integrates, and cleans up owned shard worktrees | [`port-codebases/references/worktree-safety.md`](../skills/port-codebases/references/worktree-safety.md) |
| `effective-workflow` | Coordinates delivery but provides no worktree creation, staging, commit, or cleanup recipe | Requires the selected delivery owner to apply its local contract |
| `software-testing`, `tech-docs`, `codebase-improvement` | Mention worktree or delivery state only as caller-owned context or a planning boundary | No direct Git worktree mutation |

When a skill gains the ability to create, adopt, write in, stage from, commit in,
push from, integrate from, or remove a worktree, update this inventory and give
that skill a local contract covering Git identity, absolute execution root,
dirty and staged state, collisions, resume revalidation, explicit per-command
working directories, narrow staging, and cleanup ownership.

## Review

Before merging a change:

1. Confirm the trigger description still selects the skill for the right tasks.
2. Confirm links to bundled references, scripts, and any optional resources resolve.
3. When adding a skill, create `agents/openai.yaml` and `evals/evals.json`; add
   or update behavioral cases for consequential changes.
4. When adding a skill, add its `site/index.html` card and inventory metadata.
5. Run `python3 scripts/validate-readmes.py`,
   `python3 scripts/validate-site.py`, and
   `python3 -m unittest discover -s scripts/tests -p 'test_*.py'`.
6. Run the repository's DALO CI smoke test.
7. Check that `dalo status` reports no inventory warnings or duplicate slots.
8. For routed skills, confirm every reference is linked directly from `SKILL.md`
   and that old public skill names no longer appear in internal links.
