# ADR 0004: Consolidate the Collection into Six Effective Disciplines

- Status: Accepted
- Date: 2026-07-31
- Amended: 2026-08-16 — compatibility stubs removed early in issue #217
- Reviewed: 2026-08-17 — Phase 2 route-boundary review in issue #227
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
5. To preserve existing selections during the transition, old slugs remained
   installable for one release window as redirect-only compatibility stubs.
   They kept their original frontmatter but no guidance and were excluded from
   the published inventory.

The transition in item 5 ended on 2026-08-16. All 33 stub directories and the
registry were removed; only the six disciplines remain installable.

### Execution Outcome

- Four routes were split rather than registered as context exceptions, because
  their pooled references exceeded the 900-line route budget: consultant profile
  into three, Rust into four, PR review into two, and testing into testing plus
  benchmarks. `issue-autopilot`, added after the decision was accepted, became
  the tenth Effective Delivery route when the migration branch caught up with
  `main`. Total routes: 74 rather than the projected 69.
- LinkedIn social-selling references took the `linkedin-` prefix alongside the
  LinkedIn post references, and locale-typography references took a `locale-`
  prefix, because their original names (`content-system.md`,
  `implementation.md`, `german.md`) became ambiguous once pooled.
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

Rejected at sunset. The migration table is the durable compatibility aid; old
names no longer resolve through aliases or redirect-only directories.

## Consequences

- Marketing surface changes from "34 skills with a filter bar" to "six
  disciplines, 74 routes, 331 references" — a product story rather than a
  catalog story. The root README, homepage inventory, cards, filter counts,
  structured data, and Open Graph copy all move with it.
- Granular installation of a single small skill is gone by design. "Install one
  discipline" replaces "install one small skill"; pinned DALO selections using
  an old slug must be re-pinned before the next sync.
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
  discipline, preserving representative absorbed intents and three controls
  that no discipline should claim. `scripts/validate-activation-matrix.py`
  fails CI when one prompt gets two owners or a discipline falls below three
  cases.
- The stub-specific validator branches were removed at sunset. The byte-identical
  `worktree-safety.md` copies, including the later Issue Autopilot copy, merged
  into one shared file with a uniqueness guard replacing the previous sync
  check.

## Behavioral Evidence

The decision was tested at three levels because each establishes something
different:

1. `docs/activation-matrix.json` is the static ownership contract. CI checks
   its shape and coverage but does not claim model correctness.
2. A blind classifier receives only the published descriptions and shuffled
   requests. It is useful for finding ambiguous boundaries, but it is a proxy
   for host selection rather than activation proof.
3. Installed-catalog activation runs each request in a fresh, read-only host
   session. A skill counts as activated only when the trace shows its complete
   `SKILL.md` being loaded; mentioning a skill name is insufficient.

The reviews found three durable defects or constraints:

- Trimming `effective-product` removed the fieldwork terms “win/loss” and
  “churn interviews”, causing research requests to route to marketing. The
  terms and reverse handoff were restored.
- A request to rewrite a C library in Rust was initially read as Rust depth
  rather than a behavior-preserving port. The delivery description now names
  cross-language rewrites explicitly.
- Installed-catalog runs showed that a host may truncate descriptions and may
  answer a clarification request before loading a skill. Important triggers
  therefore belong early in the description, but invocation cannot be forced
  reliably through copy changes alone.

The post-sunset blind review retained all 49 routing cases. One model classified
all cases as intended; another disagreed only on German interface typography,
choosing `effective-web` instead of `effective-writing`. That browser-surface
versus visible-prose boundary remains a review trigger.

Raw run logs, per-model pick tables, transient catalog snapshots, and cumulative
scores are evaluation artifacts rather than architecture decisions. Keep them
with the pull request that produces them. The durable procedure lives in
[Reviewing Skill Behavior](../review-scenarios.md).

### Post-consolidation route-boundary review

The Phase 2 review in issue #227 found no route seam that should be regrained.
All 74 routes remain within the 900-line direct-reference budget. The four
families split during consolidation — consultant profiles, Rust, pull-request
review, and testing versus benchmarks — still separate materially different
user intents and keep specialist context selective rather than preserving old
installable-skill boundaries.

Recent contributions exercised the structure without needing another route:
print calibration stayed in Print, Minto analysis extended Structure and Story,
interface review and color work deepened existing Delivery and Web routes, and
the Rust testing cleanup unified a shared quality reference while preserving
the Rust-implementation versus test-evidence intent boundary. The six skills'
466 review scenarios and the 50-case activation matrix cover the current routes
and their sharpest cross-discipline seams.

A fresh blind classification of the 50-case catalog produced 50/50 intended
picks on two models and 49/50 on a weaker model. Its only disagreement was the
already-covered C-to-Rust port, which it assigned to Engineering instead of
Delivery. The behavior-preserving Port route and activation owner remain the
right user-intent boundary; the residual keyword bias is description-selection
evidence for issue #229, not a reason to move or merge a route. The fresh run
used Codex desktop because no Claude runtime was available; earlier cross-host
rounds remain the evidence for the original 41-case catalog.

### Description context budget

Installed-catalog review observed Codex shortening descriptions once the
catalog exceeded its 2% description context budget. The transition catalog made
that problem worse; the post-sunset catalog is materially smaller:

| State | Skills | Description bytes | Versus before |
| --- | --- | --- | --- |
| 34 skills, before | 34 | 21,196 | — |
| 6 disciplines, after sunset | 6 | 5,801 | 27% |
| 6 disciplines plus 33 stubs | 39 | 26,811 | 126% |

During the transition, keeping the stubs' original descriptions verbatim made
existing triggers resolve and pushed the catalog 26% past its previous size. A
host that truncated on that budget therefore exposed less of each successor
description. Completing the sunset restored the catalog to 5,801 description
bytes, 27% of the pre-consolidation size.

## Validation and Review Triggers

`python3 scripts/validate-readmes.py`, `python3 scripts/validate-site.py`,
`python3 scripts/validate-activation-matrix.py`, and
`python3 -m unittest discover -s scripts/tests -p 'test_*.py'` must pass, with
route-level reference totals inside the 900-line budget.

Re-run the blind routing review whenever a description changes or a discipline
gains a route that shifts a boundary. The stub-removal trigger was satisfied on
2026-08-16 as part of issue #217.

Revisit when real use shows that a discipline's routes still mirror old skill
boundaries rather than user intent, or when a host truncates a current
description enough to change activation.
