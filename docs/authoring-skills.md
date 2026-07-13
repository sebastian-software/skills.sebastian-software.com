# Authoring Skills

Skills are focused instruction packages. A skill may route a cohesive domain to
multiple workflows, but it must remain understandable from `SKILL.md` without
loading every bundled resource into context.

## Required Structure

First-party skills live directly under `skills/`:

```text
skills/skill-name/
  SKILL.md
  references/
  scripts/
  assets/
  examples/
```

Only `SKILL.md` is required. Add the other directories when they serve a clear
purpose. Do not add external snapshots or generated copies.

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

## Resource Directories

- Use `references/` for detailed guidance loaded only when needed.
- Use `scripts/` for deterministic helpers agents can run.
- Use `assets/` for templates, images, fonts, or output resources.
- Use `examples/` for complete examples that clarify expected usage.

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

## Behavioral Evals

For consequential workflow or judgment changes, add an eval that tests the
failure mode the new rule is meant to prevent.

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

## Review

Before merging a change:

1. Confirm the trigger description still selects the skill for the right tasks.
2. Confirm links to bundled references, scripts, assets, and examples resolve.
3. Run the repository's DALO CI smoke test.
4. Check that `dalo status` reports no inventory warnings or duplicate slots.
5. For routed skills, confirm every reference is linked directly from `SKILL.md`
   and that old public skill names no longer appear in internal links.
