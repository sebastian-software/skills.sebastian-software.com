# Authoring First-Party Agent Guidance

Skills are focused instruction packages. A skill may route a cohesive domain to
multiple workflows, but it must remain understandable from `SKILL.md` without
loading every bundled resource into context. Optional instruction packs hold
standing cross-task conventions and follow a separate activation contract.

## The Discipline Pattern

The collection ships six top-level discipline skills — `effective-product`,
`effective-web`, `effective-engineering`, `effective-delivery`,
`effective-writing`, and `effective-marketing`. They share one naming grammar
(`effective-<discipline>`) and one internal architecture:

1. `SKILL.md` stays at or below 300 lines: frontmatter trigger, a short
   workflow, a `## Route by Intent` table, operating rules, and
   `## Routing Boundaries`.
2. Every route is a `references/route-<intent>.md` file linked directly from
   `SKILL.md`. References stay one level deep in a flat directory.
3. A route normally exposes at most 900 direct-reference lines, and a single
   reference stays at or below 500 lines unless registered in
   `docs/reference-context-exceptions.json`. Split a route rather than
   registering an exception when the material is genuinely two intents.
4. Cross-discipline handoffs live in `## Routing Boundaries` and name only the
   six disciplines. A handoff between two routes inside one discipline is an
   in-skill cross-link, not a boundary line.
5. Where several routes share one contract — an evidence register, a revision
   sequence, a decision framing — put it in one shared reference that those
   routes load, instead of repeating it per route.

Do not add a seventh top-level skill for a capability that fits an existing
discipline's routing table. Promote a new discipline only when its verbs,
evidence, and deliverables are genuinely different from all six, and record that
decision as an ADR.

A discipline description is behavior, not copy. `docs/activation-matrix.json`
records which discipline should own which request, and
`scripts/validate-activation-matrix.py` fails CI when that contract breaks.
Changing a description — including shortening one to fit the 1024-character
limit — can move a boundary silently, so re-run the blind routing review in
[review-scenarios.md](review-scenarios.md) afterwards. That review has already
caught one real defect: trimming `effective-product` dropped the words
"win/loss" and "churn interviews", which sent customer-interview requests to
`effective-marketing`.

The 33 pre-consolidation compatibility stubs were removed on 2026-08-16. Do not
reintroduce aliases or redirect-only skill directories: the public catalog is
the six disciplines, and [MIGRATION.md](../MIGRATION.md) preserves the old-name
mapping for users who need to re-pin a selection.

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

## Instruction Packs

Use an instruction pack instead of a skill when all of these are true:

- the rule should remain active across otherwise unrelated tasks;
- it has no independently requestable outcome or useful activation trigger;
- it governs agent conduct such as authority, completion, communication, or
  orchestration rather than one professional discipline; and
- it can be expressed provider-neutrally without assuming one model, tool name,
  target path, or downstream catalog.

First-party packs live directly under `instructions/` and use DALO's compact
source format:

```text
version: 1.0.0
topics: authority, completion

# Request Contract
```

The filename stem is the stable pack ID. Declare one semantic `version:` entry
in the first five lines and one comma-separated `topics:` or `tags:` entry in
the first eight. Topics use unique lowercase tokens and make potential overlap
visible; they do not establish precedence. Keep a pack at or below 200 lines so
standing context remains cheaper than the task guidance it coordinates.

Every pack requires matching unrun scenarios at
`instructions/evals/<id>.json`. The file contains exactly one non-empty `evals`
array whose entries have `name`, `prompt`, and `expected`. Cover the dangerous
nearby behavior, not only the happy path: missing authority, silent partial
completion, unsafe concurrency, unjustified external action, or a rule that
overrides a more specific artifact contract.

Packs contain canonical Markdown only. Never include DALO managed-block markers
in the source. Discovery and source refresh are passive; activation must remain
an explicit DALO or host action. A skill must stay complete without the pack and
must not assume it is active. Put cross-catalog routing, target selection,
precedence, and stack-specific exceptions in the downstream agent stack.

The asset boundary is recorded in
[ADR 0005](adr/0005-first-party-instruction-packs.md).

### Language Depth Is a Route, Not a Skill

Language-specific depth belongs to `effective-engineering` as a route, not to a
standalone skill. Add one only where the generic architecture and testing routes
demonstrably miss agent failure modes specific to that language — for example
borrow-checker workarounds and written unsafe-proof discipline in Rust, which
the Rust routes own, or casting away type errors, defensive `any`, floating
promises, and cargo-cult strictness in TypeScript.

Frontend and browser-facing TypeScript stays with `effective-web`, and test
evidence stays with the Focused Testing route; a language route does not absorb
those. Give every new language route reciprocal cross-links with the
architecture and testing routes so a review, test, or port hands the
language-depth findings in and keeps lifecycle, merge, and delivery ownership
with `effective-delivery`.

Naming note: language routes deliberately avoid the `effective-<language>` form.
It would collide with the well-known "Effective TypeScript" and "Effective C++"
book titles that are the cultural source of the naming pattern.

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
- Name only first-party skills that exist directly below `skills/`. Describe an
  unowned or external capability as outside the current skill's scope without
  inventing a downstream skill slot. The validator treats backticked
  identifiers in `## Routing Boundaries` and explicit phrases such as
  `` `example` skill `` as first-party skill references.
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

## Prove Behavior, Not Packaging

Add reusable proof only when it changes whether an agent or reviewer can trust a
claimed capability. Do not require a demo from every skill, but do not use a
static screenshot or prose checklist as the sole proof of behavior that is
visual, interactive, responsive, stateful, or time-dependent.

- For reusable visual or interaction mechanics, prefer a small executable
  fixture, existing component workshop story, focused route, or portable demo
  that exposes the important states. Use the real product surface for a one-off
  implementation when a parallel fixture would create drift without reuse.
- For a nonvisual transformation workflow, use a realistic input and expected
  output when a review scenario alone cannot make the artifact contract clear.
- Make proof representative rather than decorative: real content, meaningful
  controls, narrow and wide layouts, keyboard behavior, reduced motion, and
  relevant failure or fallback states.
- Give every consequential claim an observable acceptance condition. A rendered
  still can prove appearance at one moment; it cannot prove focus, interruption,
  cleanup, responsive continuity, or a complete workflow.
- Keep proof self-contained where practical and avoid a dependency or build step
  that exists only to showcase the skill. Never include third-party references,
  private customer material, or copied branding as reusable demo assets.
- Record browser or runtime evidence when the behavior depends on rendering.
  Source inspection can identify risk, but it is not interaction proof.

Treat demos, examples, assets, review scenarios, and deterministic scripts as
different evidence surfaces. Select the smallest one that discriminates the
failure mode the guidance is meant to prevent.

## Incubate Small Patterns Without Inflating the Skill Set

Not every useful pattern needs to become a standalone skill. Small interaction
ideas, visual recipes, style provocations, and tool-specific techniques can
still add real character when they are placed at the right level:

- Add a focused reference to the owning skill when the pattern supplies
  reusable decisions, constraints, or implementation guidance.
- Add a compact executable example when the value is primarily visual,
  interactive, or timing-dependent and prose cannot prove it.
- Keep a pattern as an optional specialist route when it requires a distinct
  runtime, provider, license, or maintenance surface.
- Promote it to a standalone skill only when users can ask for its outcome
  independently, its boundary is clear, and recurring demand justifies its own
  trigger and review scenarios.

A micro-pattern should sharpen the owner skill rather than compete with it.
Preserve the portable principle, state the conditions under which it helps, and
avoid turning a single aesthetic treatment or library recipe into a default
design rule.

### Runtime Context Budgets

References are runtime context, not an archive. A task-level reference should
normally stay at or below 500 lines; prefer a 150–350 line module when a task
needs only one decision area. A route must name the smallest matching reference
set and make a choice explicit when it offers alternatives. Do not present every
link in a route as required reading.

Routes should normally expose no more than 900 direct-reference lines. That is
a review threshold rather than permission to load every linked file: agents
still select the one or two references that match the task. The README validator
prints route-level totals in CI so a growing default context is visible in a PR.

An unusually large deep reference is allowed only when it is a genuine
edge-case appendix and its normal route points to smaller task modules first.
Register it with a concrete reason and existing default modules in
`docs/reference-context-exceptions.json`. The validator rejects an unregistered
reference above 500 lines. Review every exception when the route or its modules
change; splitting a chapter must reduce the default load, not create copies of
the same baseline advice.

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
- Treat RFCs and implementation plans as temporary delivery artifacts. After
  execution, fold only lasting decisions, deviations, and consequences into the
  accepted ADR, then remove the superseded proposal instead of maintaining two
  competing histories.
- Do not turn model-run logs, pick tables, or dated evaluation snapshots into
  ADRs. Keep raw evidence with the pull request; update an ADR only when that
  evidence changes a durable choice, constraint, or review trigger.
- Preserve accepted history. Supersede decisions instead of silently rewriting
  them to match current implementation.
- Route ADR creation, review, and lifecycle details through the decision-records
  route in `effective-product`.

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
reconciliation through the audit route in `effective-delivery`.

## Review Scenarios (Unrun)

For consequential workflow or judgment changes, add a review scenario that
tests the failure mode the new rule is meant to prevent. The historical
`evals/evals.json` path is retained as a portable fixture format, but it is not
an executed behavioral-evaluation harness.

Store review scenarios in `skills/<name>/evals/evals.json`. Use `evals` for
output-quality cases. Add `activation` when the skill has adjacent owners,
high-cost behavior, or a description change that needs trigger evidence:

```json
{
  "evals": [
    {
      "name": "reject-shortcut",
      "prompt": "A realistic request containing the tempting shortcut.",
      "expected": "The decision, evidence, and tradeoff a strong response must surface."
    }
  ],
  "activation": [
    {
      "name": "direct-request",
      "prompt": "A realistic request that should load this skill.",
      "should_trigger": true
    },
    {
      "name": "adjacent-owner",
      "prompt": "A realistic nearby request that should not invoke this skill's full instructions.",
      "should_trigger": false
    }
  ]
}
```

Keep `name` stable and descriptive. Treat `prompt` as the user input and
`expected` as manual review criteria, not a golden response string. CI validates
only the fixture's JSON shape, non-empty fields, and unique names; it does not
submit prompts to a model, score responses, or claim behavioral correctness.
An `activation` set must include both should-trigger and should-not-trigger
cases. Put the most confusable natural-language requests in that set rather
than testing only explicit `$skill-name` invocation. A negative case means that
the host should not invoke this skill's full instructions; merely exposing its
name and description in the catalog does not count as activation. Use a request
owned by another skill or one that needs no skill, and avoid cases where
co-activation would be legitimate.

When a change needs behavior evidence, follow the documented [manual
review-scenario workflow](review-scenarios.md). It generates a report template
and validates that a human-recorded review identifies the skill, case, agent,
model, sampling settings, response, pass/fail result, and grading evidence. The
report validator checks traceability, not whether the human's grade is correct.

Use its fresh-session comparison template when deciding whether a skill or
prompt revision earns its context, latency, and token cost. Run each case once
with the skill available and once with it disabled, without sharing conversation
history between conditions. Record response quality, duration, token usage when
available, and the evidence for the comparison.

- Use a realistic prompt containing a plausible misconception, incomplete fix,
  or tempting shortcut; do not merely ask the agent to repeat the rule.
- State the expected decision and the evidence or tradeoff it must surface,
  without prescribing incidental wording or one exact implementation.
- Include fallback and degraded-state scenarios for progressive enhancements.
- Prefer a few discriminating cases over broad happy-path coverage that a
  baseline model would already pass.

For procedural guidance, give each consequential step an observable completion
condition so an agent can tell whether to continue, stop, or escalate. Review
new wording sentence by sentence: remove a rule when it does not change a
decision, action, or verification outcome. Replace stale or duplicated guidance
at its owner instead of adding another exception to an already layered rule set.

## First-Party Boundary

Everything below `skills/` is maintained here as Sebastian Software source.
Do not copy external skills, rename their frontmatter, add `SOURCE.md`
snapshots, or maintain external source selections and pins in this repository.

State a skill's boundary in capability terms that remain useful when the skill
is installed alone. Exact external slot names, catalog provenance, selections,
version pins, precedence, and cross-source routing belong in a downstream agent
stack.

Named runtime references are closed over this repository: every named skill
must match an existing first-party skill directory. Do not leave a dead named
handoff for an external or formerly installed skill. When no first-party owner
exists, state what the current skill does and does not cover, then stop.

## Delivery Worktree Inventory

Keep every independently installed owner safe without requiring a shared
runtime or private receipt file.

All worktree-mutating work now lives in `effective-delivery` and shares one
contract: [`effective-delivery/references/worktree-safety.md`](../skills/effective-delivery/references/worktree-safety.md).

| Route | Worktree behavior |
| --- | --- |
| PR Review and Upkeep | Creates or adopts a PR worktree; writes, validates, stages, commits, pushes, rebases when authorized, and removes workflow-created worktrees |
| Issue Queue Autopilot | Creates one isolated worktree per selected queue item; delegates implementation, validation, staging, commit, push, and PR repair without merging |
| Dependency Updates | Creates or adopts one worktree per dependency PR group; writes manifests and lockfiles, validates, stages, commits, pushes, publishes, and cleans up owned worktrees |
| Behavior-Preserving Ports | Creates or adopts isolated worktrees for port shards; writes, validates, stages, checkpoints, integrates, and cleans up owned shard worktrees |
| Workflow Orchestration | Coordinates delivery but provides no worktree creation, staging, commit, or cleanup recipe; requires the selected route to apply the shared contract |
| Codebase Audit, Technical Documentation, Repository Validation | Mention worktree or delivery state only as caller-owned context or a planning boundary; no direct Git worktree mutation |

The other five disciplines perform no Git worktree mutation. When any skill
gains the ability to create, adopt, write in, stage from, commit in, push from,
integrate from, or remove a worktree, update this inventory and point it at the
shared contract covering Git identity, absolute execution root, dirty and staged
state, collisions, resume revalidation, explicit per-command working
directories, narrow staging, and cleanup ownership. A second copy of that file
anywhere in the collection must stay byte-identical;
`scripts/validate-readmes.py` enforces that.

## Review

Before merging a change:

1. Confirm the trigger description still selects the skill for the right tasks.
2. Confirm links to bundled references, scripts, and any optional resources resolve.
3. When adding a skill, create `agents/openai.yaml` and `evals/evals.json`; add
   or update unrun output and activation scenarios for consequential changes,
   and record a fresh-session activation or with/without-skill review when
   behavior evidence is needed.
4. When adding a skill, add its `site/index.html` card and inventory metadata.
5. Run `python3 scripts/validate-readmes.py`,
   `python3 scripts/validate-site.py`,
   `python3 scripts/validate-activation-matrix.py`, and
   `python3 -m unittest discover -s scripts/tests -p 'test_*.py'`.
6. Run the repository's DALO CI smoke test.
7. Check that `dalo status` reports no inventory warnings or duplicate slots.
8. For routed skills, confirm every reference is reachable from its matching
   route, the default load is explicit and narrow, and old public skill names no
   longer appear in internal links.
9. When a skill claims visual, interactive, responsive, stateful, or
   time-dependent behavior, confirm that an appropriate rendered or executable
   proof exists or that the real product surface is the deliberate proof target.
10. Confirm useful micro-patterns sit at the smallest durable level instead of
    being discarded or promoted automatically.
11. For an instruction pack, confirm its metadata and matching scenarios pass
    `validate-readmes.py`, its rules remain provider-neutral, no skill depends on
    it, and installation docs preserve explicit activation.
