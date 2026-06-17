# Authoring Skills

Skills are small, focused instruction packages. Each skill must be understandable
from its `SKILL.md` without loading every bundled resource into context.

## Required Structure

```txt
skill-name/
  SKILL.md
  references/
  scripts/
  assets/
  examples/
```

Only `SKILL.md` is required. Add the other directories when they serve a clear
purpose.

## `SKILL.md` Frontmatter

Every skill must start with YAML frontmatter containing at least `name` and
`description`:

```yaml
---
name: s7n-forms-ux
description: >-
  Form layout, labels, validation, field states, and completion flows. Use when
  building or reviewing sign-up, checkout, settings, or any multi-field form, and
  when handling inline validation, error recovery, autocomplete, or input types.
---
```

The `name` field is the install name used in the flat `dist/skills` output. It
must be unique across internal and vendor skills.

### Writing the `description`

The `description` is the only thing an agent sees before deciding whether to load
a skill, so it is the most important field for getting the right skill to trigger
at the right time.

- State what the skill covers, then list concrete situations that should trigger
  it ("Use when …"). Name the artifacts and tasks a user would actually mention
  (forms, checkout, validation, RTL, passkeys), not abstract goals.
- Prefer specific trigger phrases over vague summaries. `Use when designing
interfaces` triggers unreliably; the form example above triggers because it
  names the concrete work.
- Keep it to a few sentences. Detail belongs in the body and `references/`, not
  the description.

## Resource Directories

- Use `references/` for detailed guidance that should be loaded only when
  needed.
- Use `scripts/` for deterministic helpers that agents can run instead of
  rewriting repeatedly.
- Use `assets/` for templates, images, fonts, or other output resources.
- Use `examples/` for complete examples that clarify expected usage.

Keep `SKILL.md` lean. Move long tables, examples, policy text, and API details
into references so the agent can load only what the current task needs.

## Distill, Don't Archive

This repository ships skills, not an intake log. When an article, talk, or spec
is useful, absorb its **knowledge** into an actionable rule, checklist item, or
short example. The source itself does not belong in the skill.

A reference file should read as instructions an agent can act on directly:

- **Do** write imperative rules: "Prefer native `<dialog>` with `showModal()`;
  still set initial focus, focus return, and `Escape` handling explicitly."
- **Don't** describe the source: "Article covering native dialog, focus, and
  `Escape` behavior; use as context."
- **Don't** leave curation meta-commentary: "duplicate/supporting guidance",
  "use as context only", "radar guidance, not a normative rule", "too small to
  be a rule", or "decide together with `<id>`".
- **Don't** paste source URLs, internal tracking ids, or notes about the author's
  reading preferences into a reference.

If a bullet only rates or points at a source instead of telling the agent what to
do, either rewrite it as a real rule or drop it. A short reference of concrete
rules is worth more than a long one of source summaries.

## Internal Skills

Internal skills live under `skills/internal`. They are first-party Sebastian
Software source after import. Update them through pull requests in this
repository.

Use the `s7n-*` prefix for every internal install name. `s7n` is the compact
Sebastian Software namespace; it keeps bundled first-party skills distinct from
external or generic skills once installed into shared agent skill directories.

## Vendor Skills

Vendor skills live under `skills/vendor`. Every vendor skill must include
`SOURCE.md` documenting where it came from, the reviewed ref, the license, and
whether local modifications exist.
