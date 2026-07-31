# RFC 0001: Consolidate the Collection into Six Effective Disciplines

- Status: Draft
- Date: 2026-07-31
- Revised: 2026-07-31 — incorporates `market-research` and
  `marketing-writing`, added on `main` the same day (33 skills, 273
  references)
- Deciders: Sebastian Werner
- Outcome artifact: on acceptance, record the decision as an ADR in
  `docs/adr/` and treat this RFC as the detailed execution plan.

## Summary

Consolidate the 33 first-party skills into six top-level discipline skills
that share one naming grammar and one internal architecture — the routed
model that `effective-web` already proves at 25 routes and 116 references:

| # | Discipline | One-line story |
| --- | --- | --- |
| 01 | `effective-product` | Decide what to build and how it should work |
| 02 | `effective-web` | Build the browser experience as one system |
| 03 | `effective-engineering` | Design and write the software itself |
| 04 | `effective-delivery` | Move repositories and teams forward safely |
| 05 | `effective-writing` | Prose that people trust and act on |
| 06 | `effective-marketing` | Take verified value to market |

No guidance is deleted. Every absorbed `SKILL.md` body becomes a route
reference inside its discipline; every `references/` file moves with it.
Old slugs remain as deprecation stubs for one release window.

## Motivation

1. **The skill namespace is flat and global.** In every agent environment,
   installed skills appear in one undifferentiated list. Belonging to a
   collection is invisible there. A consistent `effective-` prefix makes the
   family recognizable in the only surface we do not control, and the six
   skills sort adjacently in any alphabetical listing.
2. **The current names follow four different grammars.** `effective-web`
   (adjective + domain), `create-social-content` (imperative), `smart-
   dependency-updater` (agent noun), `metro-english` (brand). The collection
   reads as accumulated rather than designed. A single grammar communicates
   intent.
3. **Trigger competition.** 33 descriptions compete for activation. Related
   skills (three `linkedin`/social skills, nine writing- and
   marketing-adjacent skills)
   overlap at the trigger level and force routing boundaries to do work that
   one router could do internally — exactly what `effective-web` already
   does for 25 formerly separate concerns.
4. **Marketing.** "Six disciplines, one quality bar" is a product story.
   "33 skills with a filter bar" is a catalog story. The consolidation is a
   prerequisite for the planned homepage relaunch.

### Why six, not five or one

An earlier draft merged all engineering-adjacent skills into one
`effective-engineering` with 13 absorbed skills. That failed the cohesion
test: producing source code (architecture, data, TypeScript, Rust, tests)
and operating on a repository as a workflow (audits, ports, reviews,
dependency updates, validation runs, docs, team leadership) are different
disciplines with different evidence and different verbs. `effective-web`
carries 25+ routes only because its routes are genuinely interwoven; route
count is not the warning sign, low cohesion is. Hence the split into
`effective-engineering` (craft) and `effective-delivery` (process).

A useful byproduct: the previously hard-to-explain pair
`software-testing` / `software-validation` becomes legible. Writing tests
is producing code (engineering); running existing checks is workflow
(delivery).

## Goals

- One top-level naming grammar: `effective-<discipline>`.
- Six skills, each following the routed `effective-web` anatomy.
- Zero guidance loss: every current reference and every current `SKILL.md`
  body survives as a route or reference.
- Stable behavior: absorbed triggers keep firing via the discipline
  descriptions; eval suites are merged, not discarded.
- A migration that external installs survive via deprecation stubs and a
  published mapping.

## Non-Goals

- No new guidance content. Phase 1 is a mechanical re-homing; content
  re-slicing (deduplication, regrained routes) is Phase 2 and explicitly
  out of scope for the initial move.
- No umbrella product rebrand (a name above the six). Deferred.
- No standalone `effective-typescript` / `effective-rust`. Language depth
  becomes routes inside `effective-engineering`; this also avoids colliding
  with the well-known "Effective TypeScript" / "Effective C++" book titles,
  which are the cultural source of the naming pattern.
- The homepage relaunch itself. It consumes this RFC's outcome but is a
  separate effort.

## Design Rules for a Discipline Skill

Derived from `docs/authoring-skills.md` and the `effective-web` precedent;
these become the normative pattern for all six:

1. `SKILL.md` ≤ 300 lines (CI-enforced): frontmatter trigger, short
   workflow, a `## Route by Intent` table, `## Routing Boundaries`.
2. Every route is a `references/route-<intent>.md` file linked directly
   from `SKILL.md`; references stay one level deep (flat directory).
3. A route normally exposes ≤ 900 direct-reference lines; a single
   reference stays ≤ 500 lines or gets registered in
   `docs/reference-context-exceptions.json`.
4. An absorbed skill's `SKILL.md` body converts into its route file(s):
   frontmatter dropped, trigger prose folded into the discipline
   description, workflow and operating rules kept as the route content.
   All current bodies are 70–300 lines, so each fits the 500-line cap.
5. Moved reference files keep their filenames except:
   - name collisions, resolved with a short domain prefix;
   - language families in `effective-engineering`, always prefixed
     (`typescript-*.md`, `rust-*.md`) for scanability;
   - files whose name only made sense inside the old skill (for example
     `workflow.md` from `smart-dependency-updater` becomes
     `dependency-workflow.md`).
6. Cross-discipline handoffs stay in `## Routing Boundaries`, referencing
   the six names only. Handoffs between two absorbed skills that now share
   a discipline become in-skill route cross-links.
7. Moves use `git mv` so file history survives.

## Target Architecture in Detail

Reference counts below are the current file counts; "route files" are new.

### 01 `effective-product`

Absorbs `product-management` (11 refs), `product-design` (7),
`market-research` (3), `product-naming` (2), `pricing-and-packaging` (3),
`decision-records` (2). Resulting size: 28 moved references + ~10 route
files.

Draft frontmatter description:

```yaml
name: effective-product
description: >-
  Decide what to build and how the product should work, on gathered
  rather than invented evidence: decision-led customer and market research
  from interviews, surveys, observation, transcripts, review and community
  mining, and market landscapes to Voice of Customer, Jobs to Be Done,
  personas, and market sizing; product discovery, evidence review,
  strategy, outcomes, scope, prioritization, roadmaps, experiments,
  release decisions, marketplaces and network effects, product operating
  models and empowered teams; design research, problem framing,
  object and journey modeling, information architecture, wireframes,
  prototypes, habit and retention loops; product and feature naming
  research, generation, and screening; pricing and packaging, value
  metrics, tiers, discounts, and trials; and Architecture Decision Records
  for durable decisions. Use when evidence must be gathered or a product
  decision made: what, whether, or for whom to build, how the experience
  should behave, what to charge, what to name it, or how to record the
  decision. Do not use to implement the product, write marketing copy, or
  operate a channel.
```

Route table:

| Route | Absorbs |
| --- | --- |
| `route-discovery.md` | product-management: `discovery-and-evidence.md`, `evidence-review.md`, `review-modes.md`, `review-calibration.md` |
| `route-strategy.md` | product-management: `strategy-and-outcomes.md`, `product-operating-model.md`, `networked-products.md` |
| `route-scope-and-shipping.md` | product-management: `scope-and-prioritization.md`, `shipping-and-learning.md`, `product-quality-and-delight.md` |
| `route-design-research.md` | product-design: `research-and-synthesis.md`, `problem-framing.md`, `process-and-environments.md` |
| `route-design-modeling.md` | product-design: `solution-modeling.md`, `structure-and-prototyping.md` |
| `route-behavioral-design.md` | product-design: `habit-and-retention-design.md`, `autonomy-and-motivation.md` |
| `route-naming.md` | product-naming: `name-generation.md`, `screening-and-verification.md` |
| `route-pricing.md` | pricing-and-packaging: all 3 |
| `route-research.md` | market-research: `program-design-and-fieldwork.md`, `market-and-source-research.md`, `synthesis-and-handoffs.md` |
| `route-decisions.md` | decision-records: `adr-format.md`, `communication-decisions.md` |

`go-to-market-handoff.md` stays as a shared reference linked from
`route-strategy.md` and the boundary with `effective-marketing`.
No filename collisions.

### 02 `effective-web`

Keeps its 116 references and 25 routes. Absorbs `reference-analysis` (2),
`originality-review` (2), `web-legal-compliance` (8). Releases nothing —
but its boundary to locale typography now points at `effective-writing`
(see 05). Resulting size: ~128 references, 28 routes.

New routes:

| Route | Absorbs |
| --- | --- |
| `route-reference-analysis.md` | reference-analysis: `evidence-capture.md`, `specification-and-handoff.md` |
| `route-originality.md` | originality-review: `audit-rubric.md`, `provenance-and-history.md` |
| `route-compliance.md` | web-legal-compliance: all 8, jurisdiction files prefixed `legal-` (`legal-european-union.md`, `legal-united-states.md`, …) |

Description change: extend the existing trigger with reference capture and
specification, originality and provenance audits, and jurisdiction-aware
web compliance; keep every existing negative guard.

Note: `originality-review` and `reference-analysis` are broader than the
web (campaigns, documents, media). They land here because their dominant
inputs and outputs are experiences; `effective-marketing` reaches them via
a boundary line for campaign-only audits. See Open Questions.

### 03 `effective-engineering`

Absorbs `software-architecture` (2), `data-systems` (4),
`typescript-engineering` (5), `rust-engineering` (9),
`software-testing` (6). Resulting size: 26 moved references + ~6 route
files.

Draft frontmatter description:

```yaml
name: effective-engineering
description: >-
  Design and write the software itself: software and system architecture,
  service and module boundaries, quality attributes, operational
  readiness, testing strategy; data models, datastores, transactions,
  consistency, replication, partitioning, batch and streaming pipelines,
  schema evolution and data migrations; server-side and shared-library
  TypeScript type, module, async, and error contracts; Rust crates,
  ownership, APIs, unsafe code, concurrency, and performance; and focused
  non-frontend tests, regression guards, and benchmark methodology. Use
  for architecture options, database and event-model decisions, writing or
  reviewing TypeScript or Rust, protecting behavior with tests, or
  designing benchmarks. Do not use for browser-facing work, for repository
  lifecycle workflows such as audits, ports, reviews, dependency updates,
  or validation runs, or for frontend testing.
```

Route table:

| Route | Absorbs |
| --- | --- |
| `route-architecture.md` | software-architecture: `architecture-foundations.md`, `operability-and-twelve-factor.md` |
| `route-data.md` | data-systems: all 4 |
| `route-typescript.md` | typescript-engineering: all 5, prefixed `typescript-` |
| `route-rust.md` | rust-engineering: all 9, prefixed `rust-` |
| `route-testing.md` | software-testing: `select-test-evidence.md`, `services-data-and-async.md`, `cli-contracts.md`, `modularity-and-testability.md`, `rust-testing.md` |
| `route-benchmarks.md` | software-testing: `benchmark-methodology.md` (per ADR 0001 ownership) |

Collision resolved by rule: `quality-and-review.md` exists in both language
skills and becomes `typescript-quality-and-review.md` /
`rust-quality-and-review.md`. Phase 2 candidate: unify `rust-testing.md`
(from software-testing) with the Rust quality references.

### 04 `effective-delivery`

Absorbs `effective-workflow` (2), `codebase-improvement` (5),
`port-codebases` (5), `pr-review` (8), `smart-dependency-updater` (3),
`software-validation` (2), `tech-docs` (6), `engineering-management` (4).
Resulting size: ~33 moved references (after deduplication) + ~8 route
files.

Draft frontmatter description:

```yaml
name: effective-delivery
description: >-
  Move an existing repository and the team around it forward: coordinate
  multi-stage software work from an unclear request to a verified,
  review-ready handoff; audit codebases, explain surprising behavior, and
  prioritize improvements; plan and execute behavior-preserving ports
  across languages, runtimes, and frameworks; review and maintain pull
  requests across providers; research, group, and implement dependency
  changes; discover and run repository-native validation checks and report
  the evidence; design and verify technical documentation from READMEs and
  guides to API references, migration notes, and controlled language; and
  lead product, design, and engineering teams with clear responsibilities
  and sustainable load. Use when the task operates on a repository, a
  change, a pull request, dependencies, documentation, checks, or team
  responsibilities. Do not use to design or write new system code depth or
  browser experiences.
```

Route table:

| Route | Absorbs |
| --- | --- |
| `route-orchestration.md` | effective-workflow: `routing-and-fallbacks.md`, `evidence-and-delivery.md` |
| `route-audit.md` | codebase-improvement: all 5 |
| `route-porting.md` | port-codebases: `migration-contract.md`, `execution-profiles.md`, `model-tiering.md`, `review-and-verification.md` |
| `route-review.md` | pr-review: all 8 (`voice.md` → `review-voice.md`, `voice-examples.md` → `review-voice-examples.md`) |
| `route-dependencies.md` | smart-dependency-updater: `ecosystem-notes.md`, `workflow.md` → `dependency-workflow.md` |
| `route-validation.md` | software-validation: `command-discovery.md`, `execution-and-reporting.md` |
| `route-docs.md` | tech-docs: all 6 |
| `route-leadership.md` | engineering-management: all 4 |

Deduplication (Phase 1, mandatory because of the filename collision):
`worktree-safety.md` exists three times (port-codebases, pr-review,
smart-dependency-updater). All three copies are byte-identical as of
2026-07-31 (verified via checksum), so the merge is a plain keep-one:
one shared `worktree-safety.md` linked from the three routes. Re-verify
identity at execution time; if the copies have diverged by then, keep the
union and note the merge in the PR.

### 05 `effective-writing`

Absorbs `nonfiction-writing` (5), `metro-english` (0 refs, 292-line body),
`locale-typography` (16). Resulting size: 21 moved references + 1
converted body + ~7 route files.

Draft frontmatter description:

```yaml
name: effective-writing
description: >-
  Plan, write, revise, and critique nonfiction prose from supplied ideas
  and evidence: articles, essays, newsletters, thought leadership,
  engineering blog posts, technical articles, case studies, About pages,
  product descriptions, and long-form homepage prose; evidence-based
  audits of formulaic, AI-sounding text without authorship claims; relaxed
  US metropolitan team English for Slack threads, issue comments, PR
  notes, and async updates; and locale-appropriate typography in visible
  prose for German, English, French, and ten further European languages.
  Use to turn notes into a draft, improve structure, clarity, voice, and
  rhythm, audit or humanize prose, turn stiff or German text into natural
  team English, or fix quotation marks, punctuation, spacing, numbers,
  dates, and hyphenation for a locale. Do not invent facts, statistics, or
  quotations. Route market positioning and claims to effective-marketing
  and durable technical documentation to effective-delivery.
```

Route table:

| Route | Absorbs |
| --- | --- |
| `route-structure.md` | nonfiction-writing: `structure-and-story.md` |
| `route-prose.md` | nonfiction-writing: `prose-and-revision.md` |
| `route-voice-audit.md` | nonfiction-writing: `human-voice-editing.md` |
| `route-persuasion.md` | nonfiction-writing: `persuasive-nonfiction.md` |
| `route-technical-prose.md` | nonfiction-writing: `technical-subject-matter.md` |
| `route-metro-english.md` | metro-english: `SKILL.md` body → `metro-english.md` reference (292 lines, fits the cap); the route keeps the Metro English name as an in-discipline brand |
| `route-locale-typography.md` | locale-typography: all 16 (`locale-matrix.md`, `shared-rules.md`, `implementation.md`, 13 language profiles) |

`locale-typography` moves here rather than staying web-adjacent because
its subject is language-level prose convention across any medium
(Markdown, HTML, JSX, documents, print). `effective-web` already routes
out for it today; the boundary line simply changes its target. No
filename collisions.

### 06 `effective-marketing`

Absorbs `product-marketing` (4), `marketing-writing` (4),
`conversion-optimization` (3), `create-social-content` (3),
`linkedin-posts` (10), `linkedin-social-selling` (5),
`consultant-profile` (6). Resulting size: 35 moved references + ~10 route
files.

Draft frontmatter description:

```yaml
name: effective-marketing
description: >-
  Take a verified product or professional offer to market: positioning,
  segmentation, category choice, message architecture, claims and proof,
  launches, sales enablement, win/loss and adoption learning; persuasive
  marketing copy for homepages, landing pages, product and pricing pages,
  campaigns, sales pages, emails, headlines, and calls to action; funnel
  diagnosis, conversion audits, and ethical experiment design with
  guardrails; social content for X or Twitter, Threads, Bluesky,
  Instagram, and Mastodon; LinkedIn posts, content calendars, and B2B
  social-selling systems from profile visit to qualified meeting; and
  consultant CVs, LinkedIn profiles, bios, project narratives, and case
  study selection. Use for positioning briefs, message or claim reviews,
  launch plans, funnel drop-off, A/B test design, social or LinkedIn
  content, or professional profile positioning. Do not invent customer
  evidence, market certainty, or differentiation. Route finished long-form
  prose to effective-writing and page implementation to effective-web.
```

Route table:

| Route | Absorbs |
| --- | --- |
| `route-positioning.md` | product-marketing: `positioning-and-segmentation.md` |
| `route-messaging.md` | product-marketing: `messaging-and-proof.md` |
| `route-launch.md` | product-marketing: `launch-and-enablement.md` |
| `route-market-learning.md` | product-marketing: `market-learning.md` |
| `route-copywriting.md` | marketing-writing: all 4 (`brief-and-reader-state.md`, `persuasive-paths-and-artifacts.md`, `emotion-and-behavior.md`, `marketing-copy-revision.md`) |
| `route-conversion.md` | conversion-optimization: all 3 |
| `route-social.md` | create-social-content: all 3 |
| `route-linkedin-posts.md` | linkedin-posts: all 10, prefixed `linkedin-` (their current names — `educational-content.md`, `networking-community.md`, … — are too generic once pooled) |
| `route-linkedin-selling.md` | linkedin-social-selling: all 5 |
| `route-profile.md` | consultant-profile: all 6 |

`consultant-profile` lands here (acquisition context) rather than in
`effective-writing`; the profile-prose handoff becomes a boundary line.
See Open Questions.

`marketing-writing` lands here, not in `effective-writing`: its own
boundary with `nonfiction-writing` already draws the line this RFC needs
— commercial-choice copy is marketing, inform-and-explain prose is
writing. That boundary language moves verbatim into the two discipline
descriptions.

### Resulting totals

| Discipline | Routes | References (approx.) |
| --- | --- | --- |
| effective-product | 10 | 38 |
| effective-web | 28 | 131 |
| effective-engineering | 6 | 32 |
| effective-delivery | 8 | 41 |
| effective-writing | 7 | 29 |
| effective-marketing | 10 | 45 |
| **Total** | **69** | **~316** |

Reference growth over today's 273 comes from converted `SKILL.md` bodies
and new route files, not new content. Marketing surface: "6 disciplines ·
69 routes · 300+ references".

## Cross-Cutting Mechanics

### Routing-boundary rewrite

Every current `## Routing Boundaries` section references sibling skills by
old name; the validator treats those backticked identifiers as first-party
references, so stale names fail CI. The rewrite map:

| Old reference | Becomes |
| --- | --- |
| `product-management`, `product-design`, `market-research`, `product-naming`, `pricing-and-packaging`, `decision-records` | `effective-product` |
| `reference-analysis`, `originality-review`, `web-legal-compliance` | `effective-web` |
| `software-architecture`, `data-systems`, `typescript-engineering`, `rust-engineering`, `software-testing` | `effective-engineering` |
| `effective-workflow`, `codebase-improvement`, `port-codebases`, `pr-review`, `smart-dependency-updater`, `software-validation`, `tech-docs`, `engineering-management` | `effective-delivery` |
| `nonfiction-writing`, `metro-english`, `locale-typography` | `effective-writing` |
| `product-marketing`, `marketing-writing`, `conversion-optimization`, `create-social-content`, `linkedin-posts`, `linkedin-social-selling`, `consultant-profile` | `effective-marketing` |

Handoffs between two skills that now share a discipline (for example
`product-marketing` ↔ `conversion-optimization`) turn into in-route
cross-links, not boundary lines. Boundary sections shrink accordingly;
the remaining lines carry route hints ("route X in `effective-product`").

### Evals

Each absorbed skill ships `evals/evals.json`. The discipline eval file is
the union of its sources, plus new **cross-discipline disambiguation
cases** — the highest-risk behavior in this consolidation. Minimum new
cases per discipline: one positive per absorbed skill (old trigger still
fires), plus negative pairs across the sharpest boundaries:

- write a homepage hero section → `effective-marketing` (persuasive copy
  via the copywriting route) vs `effective-writing` (long-form editorial
  prose) vs `effective-web` (page hierarchy and implementation). The new
  `marketing-writing` skill sharpened exactly this boundary on the old
  layout; carry its nonfiction-writing boundary language into the two
  discipline descriptions.
- interview customers about churn and synthesize findings →
  `effective-product` (research route); turning those findings into
  win/loss messaging → `effective-marketing`
- add a test for a bug fix → `effective-engineering`; run the repo's
  checks → `effective-delivery`
- review this PR → `effective-delivery`; review this Rust API design →
  `effective-engineering`
- fix quotation marks in German UI copy → `effective-writing` route
  locale typography, not `effective-web`

### `agents/openai.yaml` and READMEs

Six new `agents/openai.yaml` files (display name, short description,
`$skill-name` invocation). Six new READMEs following the collection README
contract (value proposition, capabilities, example prompts, selective
install, boundaries, canonical links, license notice). Absorbed skill
READMEs are deleted with their directories; their example prompts fold
into the discipline README.

### Deprecation stubs

For one release window, each old slug remains installable:

- `skills/<old-name>/SKILL.md`: old frontmatter name and description kept
  verbatim (so old triggers resolve), body reduced to ~10 lines: the
  skill is superseded; load `effective-<x>` and use route `<y>`.
- `skills/<old-name>/README.md`: migration notice, new install command.
- Validator change: stubs listed in a new `docs/deprecated-skills.json`
  are exempt from full anatomy (evals, agents) and from site inventory
  parity, and are rendered on the site only as a migration table, not as
  cards.
- Sunset: remove stubs and the allowlist after one quarter (target
  2026-10-31) or one release cycle, whichever is later.
- `MIGRATION.md` at the repository root: the full old → new mapping table
  (old slug → discipline + route), linked from the README and release
  notes.

### Site, README, and metadata

Must change in the same release: root `README.md` (story, counts, find-a-
skill table, install examples), `site/index.html` (inventory, cards,
filter counts, structured data `ItemList`), `site/comparisons.html`,
`site/sitemap.xml`, OG copy ("33 skills" → "6 disciplines"),
`docs/dalo.md` examples (`dalo source select sebastian effective-web`
stays valid; other examples re-pointed), `docs/authoring-skills.md`
(document the discipline pattern; rewrite the language-specific-skills
section since TypeScript and Rust are now routes; update the required
structure examples), and `docs/reference-context-exceptions.json` (re-path
any registered exceptions whose files move).

### Validation gates per PR

Every consolidation PR must pass `python3 scripts/validate-readmes.py`,
`python3 scripts/validate-site.py`, and the eval suite for the affected
discipline, and must keep route-level reference-line totals within the
900-line review threshold (split routes when a converted body pushes a
route over).

## Migration Sequencing

Land the consolidation on an integration branch
(`release/effective-disciplines`) as stacked, individually reviewable PRs,
then merge to `main` once, together with the homepage relaunch, as a
single visible release. Rationale: sequential merges to `main` would leave
the public site and README in a mixed 27-skills-plus-one-discipline state
for weeks; a single release gives one coherent launch moment and one
migration story.

Order (smallest blast radius first; each step includes its boundary
rewrites, eval merge, README, stub, and site-inventory updates):

1. **`effective-writing`** — pilot. Smallest surface, exercises every
   mechanic once: body→route conversion (metro-english), reference move
   (locale-typography), boundary re-target from `effective-web`.
   Review the pilot before continuing; adjust the pattern here.
2. **`effective-marketing`** — the most trigger-diverse absorption
   (seven skills from positioning to profiles); proves trigger breadth,
   the linkedin prefix rule, and the sharpened copywriting boundary with
   `effective-writing`.
3. **`effective-product`** — proves multi-skill route regraining.
4. **`effective-engineering`** — proves the language-prefix rule and the
   testing/benchmarks split.
5. **`effective-delivery`** — largest reference set; includes the
   `worktree-safety.md` dedup.
6. **`effective-web` absorption** — last, since it is the live flagship
   and touches the most existing content.
7. **Cross-sweep** — README, site, comparisons, sitemap, OG, dalo docs,
   authoring docs, `MIGRATION.md`, stub allowlist, final validator run
   across the whole tree.
8. **Release** — merge to `main` with the homepage relaunch; publish
   release notes with the migration table.

Phase 2 (separate, post-release): content re-slicing within disciplines —
unify `rust-testing.md` with the Rust quality references, regrain routes
that still mirror old skill boundaries rather than user intent, dedupe
overlapping voice/prose guidance between `route-review.md` (PR voice) and
`effective-writing`, and tighten descriptions using eval telemetry.

## Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Over- or under-triggering of broad descriptions | Keep every existing negative guard; merged eval suites plus new disambiguation cases; pilot with `effective-writing` before committing the pattern |
| Harness description-length limits truncating triggers | Keep each description at or below the proven `effective-web` length (~750 characters); verify rendering in Claude Code, Codex, and DALO during the pilot |
| Loss of granular install (`linkedin-posts` alone) | Deliberate product decision: "install one discipline" replaces "install one small skill"; stubs bridge the window; DALO selections re-pin once |
| External links to old GitHub paths break | Stubs for one window, `MIGRATION.md`, release notes; old README anchors redirect via the migration table |
| Route context budgets exceeded after conversion | Converted bodies are 70–300 lines each; validator prints route totals per PR; split routes when over 900 |
| In-flight PRs conflict with mass `git mv` | Sequence on the integration branch; land or close open skill PRs per area before its consolidation step |
| Public site inconsistent during migration | Integration branch; `main` and the live site never show a mixed state |
| Diverged `worktree-safety.md` copies silently merged | Mandatory three-way diff in the `effective-delivery` PR with the union kept and the merge noted |

## Open Questions

1. **`reference-analysis` / `originality-review` placement.** Chosen:
   `effective-web` (dominant inputs are experiences). Alternative:
   `effective-product` (they are analysis, not construction). Decide at
   step 6; moving them later is cheap since both are two references each.
2. **`engineering-management` placement.** Chosen: `effective-delivery`
   (teams as the human part of how work flows). Alternative:
   `effective-product` (operating model). Decide at step 5.
3. **`consultant-profile` placement.** Chosen: `effective-marketing`
   (acquisition context). Alternative: `effective-writing` (career
   evidence as prose). Decide at step 2.
4. **Alias support.** Whether the skills CLI or DALO supports name
   aliases that could replace stub directories. Investigate during the
   pilot; stubs are the fallback either way.
5. **Stub window length.** One quarter proposed; shorten if telemetry or
   issue traffic shows no old-name installs.
6. **Eval regression tooling.** Whether merged evals can run comparatively
   (old skill set vs. new disciplines) to catch trigger regressions
   quantitatively rather than by review.
7. **`market-research` placement.** Chosen: `effective-product` — it is
   the evidence-gathering arm of the "decide" discipline, and its sibling
   routes (discovery, design research) live there. Alternative:
   `effective-marketing` (win/loss, buyer language, market sizing serve
   go-to-market). The marketing side reaches it via a boundary line
   either way. Decide at step 3.

## Acceptance

Accepting this RFC means: the six-discipline target, the design rules, the
per-discipline plans, and the sequencing above are agreed; execution
starts with the `effective-writing` pilot on the integration branch; and
the decision is recorded as a new ADR in `docs/adr/` referencing this
document as its execution plan.
