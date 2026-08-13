# ADR 0004: Consolidate the Collection into Six Effective Disciplines

- Status: Accepted
- Date: 2026-07-31
- Execution plan: [RFC 0001](../rfc/0001-effective-disciplines.md)
- Migration table: [MIGRATION.md](../../MIGRATION.md)

## Context

The collection had grown to 33 first-party skills and 273 focused references.
Three problems followed from that shape rather than from the guidance itself.

The skill namespace is flat and global. In every agent environment, installed
skills appear in one undifferentiated list, and belonging to a collection is
invisible there. The names also followed four different grammars —
`effective-web` (adjective plus domain), `create-social-content` (imperative),
`smart-dependency-updater` (agent noun), `metro-english` (brand) — so the set
read as accumulated rather than designed.

Thirty-three descriptions competed for activation. Three LinkedIn and social
skills, and nine writing- and marketing-adjacent skills, overlapped at the
trigger level and forced routing boundaries to do work that one router could do
internally. `effective-web` already proved the alternative at 25 intent routes
and 116 references: a lean `SKILL.md`, a route table, and a flat reference
directory that loads only what the task needs.

## Decision

Consolidate into six top-level discipline skills that share one naming grammar
and the routed `effective-web` architecture:

| # | Discipline | Owns |
| --- | --- | --- |
| 01 | `effective-product` | Decide what to build and how it should work |
| 02 | `effective-web` | Build the browser experience as one system |
| 03 | `effective-engineering` | Design and write the software itself |
| 04 | `effective-delivery` | Move repositories and teams forward safely |
| 05 | `effective-writing` | Prose that people trust and act on |
| 06 | `effective-marketing` | Take verified value to market |

1. No guidance is deleted. Every absorbed `SKILL.md` body became a route
   reference; every `references/` file moved with `git mv` so history survives.
2. Each discipline follows the documented pattern: `SKILL.md` at or below 300
   lines with a `## Route by Intent` table, one `references/route-<intent>.md`
   per route, references one level deep, and cross-discipline handoffs confined
   to `## Routing Boundaries`.
3. Engineering and delivery stay separate. Producing source code and operating
   on a repository as a workflow are different disciplines with different
   evidence and different verbs. Route count is not the warning sign; low
   cohesion is.
4. Language depth is a route inside `effective-engineering`, not a standalone
   skill. This also avoids colliding with the "Effective TypeScript" and
   "Effective C++" book titles that are the cultural source of the pattern.
5. Old slugs remain installable for one release window as deprecation stubs
   registered in `docs/deprecated-skills.json`. Each keeps its original
   frontmatter so existing selections and triggers still resolve, carries a
   redirect body and nothing else, and is exempt from the full skill anatomy,
   the root README inventory, and site card parity.

### Deviations from the RFC

- Four routes were split rather than registered as context exceptions, because
  their pooled references exceeded the 900-line route budget: consultant profile
  into three, Rust into four, PR review into two, and testing into testing plus
  benchmarks. `issue-autopilot`, added after this RFC was accepted, became the
  tenth Effective Delivery route when the migration branch caught up with
  `main`. Total routes: 74 rather than the projected 69.
- LinkedIn social-selling references took the `linkedin-` prefix alongside the
  LinkedIn post references, and locale-typography references took a `locale-`
  prefix, because their original names (`content-system.md`,
  `implementation.md`, `german.md`) became ambiguous once pooled. The RFC's rule
  5 already allows this.
- Where several routes shared one contract, that contract became one shared
  reference rather than being repeated per route:
  `product-decision-contract.md`, `design-inquiry-contract.md`,
  `market-facing-decisions.md`, and `nonfiction-assignment.md`.

## Alternatives Considered

### One `effective-engineering` absorbing all thirteen engineering-adjacent skills

Rejected. It failed the cohesion test: architecture, data, TypeScript, Rust, and
tests produce source code, while audits, ports, reviews, dependency updates,
validation runs, docs, and team leadership operate on a repository as a
workflow. A useful byproduct of the split is that the previously
hard-to-explain `software-testing` / `software-validation` pair becomes legible:
writing tests is engineering, running existing checks is delivery.

### Keep 33 skills and rely on descriptions to disambiguate

Rejected. The overlap is structural. Nine writing- and marketing-adjacent skills
cannot be separated by wording alone when a single request legitimately touches
positioning, copy, and prose.

### Rename without consolidating

Rejected. A consistent prefix would fix recognizability in the flat namespace
but leave trigger competition and the routing-boundary maintenance burden
untouched.

### Name aliases instead of stub directories

Deferred. Whether the skills CLI or DALO supports aliases was not established
during execution. Stubs work today and are the documented fallback either way.

## Consequences

- Marketing surface changes from "34 skills with a filter bar" to "six
  disciplines, 74 routes, 331 references" — a product story rather than a
  catalog story. The root README, homepage inventory, cards, filter counts,
  structured data, and Open Graph copy all move with it.
- Granular installation of a single small skill is gone by design. "Install one
  discipline" replaces "install one small skill"; DALO selections re-pin once.
- Six broad descriptions carry more trigger surface than 33 narrow ones. Merged
  eval suites plus new cross-discipline disambiguation cases guard the sharpest
  boundaries: hero copy versus editorial prose versus page implementation;
  research versus messaging; writing a test versus running the suite; reviewing
  a PR versus reviewing an API design; German UI punctuation versus frontend
  work.
- Description length remains the live risk. Four of six descriptions sit between
  970 and 1023 characters, above the roughly 750 characters `effective-web` had
  proven and near the 1024-character repository limit. Verify rendering in
  Claude Code, Codex, and DALO before relying on the full trigger text. Trimming
  to fit that limit already caused one routing defect (see below), so treat a
  future trim as a behavior change, not as copy editing.
- Routing is now covered by a contract rather than by review alone.
  `docs/activation-matrix.json` pairs 49 realistic requests with their owning
  discipline, including at least one per superseded slug and three controls that
  no discipline should claim. `scripts/validate-activation-matrix.py` fails CI
  when a superseded slug loses its coverage, when one prompt gets two owners, or
  when a discipline falls below three cases.
- Both validators now understand deprecation stubs. The byte-identical
  `worktree-safety.md` copies, including the later Issue Autopilot copy, merged
  into one shared file with a uniqueness guard replacing the previous sync
  check.

## Behavioral Evidence

The six descriptions were reviewed blind against the routing matrix: an agent
received only the six frontmatter descriptions and the 41 prompts in shuffled
order — no case names, no expected owners, no route tables — and picked one
skill per request or `none`.

Runtime: Claude Code subagents, provider-default sampling, models
`claude-opus-5`, `claude-sonnet-5`, and `claude-haiku-4-5-20251001`.
Regenerate the input with `scripts/build-routing-review-input.py`.

The recorded Claude rounds cover the original 41 prompts. A later
[GPT installed-catalog review](../model-evaluation-2026-08-13.md) covers the
current 49-case matrix, including Issue Queue Autopilot, the preservation cases,
and all deprecation stubs.

| Round | Descriptions under test | Opus 5 | Sonnet 5 | Haiku 4.5 |
| --- | --- | --- | --- | --- |
| 1 | as first written | 40/41 | 40/41 | 41/41 |
| 2 | after the research fix | 41/41 | 41/41 | 40/41 |
| 3 | after the port fix | not run | 41/41 | 41/41 |

Round 1 found a real defect. `effective-product` lost the words "win/loss" and
"churn interviews" while its description was trimmed under the 1024-character
limit, and `effective-marketing` kept "win/loss and adoption learning". Two of
three models therefore routed "interview our lost deals and synthesize what we
learn" to marketing — the exact boundary this ADR's alternatives section calls
structural. The fix restores the fieldwork verbs to `effective-product` and adds
an explicit reverse handoff to `effective-marketing`.

Round 2's single miss was a weaker model reading "rewrite this C library in
Rust" as Rust work rather than as a behavior-preserving port. The wording now
names rewriting an existing library in another language; round 3 confirms it.

What these Claude rounds alone do not establish:

- The runs use a subagent as a proxy for a host's skill-selection step, not the
  real mechanism. `docs/model-evaluation-2026-07-29.md` used a stronger method
  for the previous layout — fresh ephemeral Codex sessions against the actually
  installed catalog, recording which skills' full instructions were invoked.
  This review does not meet that bar.
- They do not exercise a GPT runtime or the installed catalog. The follow-up
  review does both and records a cumulative 48/49 result across its baseline
  round and two targeted post-change reruns, one remaining clarification-only
  miss, and the actual description truncation.

It is evidence about description discrimination, not proof of production
activation.

### Description context budget

The previous evaluation recorded Codex shortening descriptions once the
installed catalog exceeded its 2% description context budget. The consolidation
improves that materially after sunset and worsens it during the window:

| State | Skills | Description bytes | Versus before |
| --- | --- | --- | --- |
| 34 skills, before | 34 | 21,196 | — |
| 6 disciplines, after sunset | 6 | 5,801 | 27% |
| 6 disciplines plus 33 stubs | 39 | 26,811 | 126% |

Keeping the stubs' original descriptions verbatim is what makes existing
triggers resolve, and it is also what pushes the catalog 26% past its previous
size. A host that truncates on that budget will truncate more during the
deprecation window than it did before, which is an argument for a shorter window
rather than for shortening the stub descriptions — shortening them would defeat
their only purpose.

## Validation and Review Triggers

`python3 scripts/validate-readmes.py`, `python3 scripts/validate-site.py`,
`python3 scripts/validate-activation-matrix.py`, and
`python3 -m unittest discover -s scripts/tests -p 'test_*.py'` must pass, with
route-level reference totals inside the 900-line budget.

Re-run the blind routing review whenever a description changes, a discipline
gains a route that shifts a boundary, or a stub is removed at sunset.

Revisit when: telemetry or issue traffic shows old-name installs have stopped,
at which point the stubs and `docs/deprecated-skills.json` can be removed; a
discipline's routes still mirror old skill boundaries rather than user intent
after real use; or a harness truncates a discipline description, which would
force shorter triggers ahead of the planned Phase 2 content re-slicing.

Phase 2 remains out of scope here: unifying `rust-testing.md` with the Rust
quality references, regraining routes, deduplicating voice and prose guidance
between the PR review voice and `effective-writing`, and tightening descriptions
from eval telemetry.
