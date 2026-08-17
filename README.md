# Sebastian Software Skills

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Website:** [skills.sebastian-software.com](https://skills.sebastian-software.com/)

**Open-source skills for the professional judgment that capable AI agents still
need to do dependable product and software work.**

Six disciplines, one quality bar:
6 practice-built skills, 333 focused references, and 2 optional instruction packs
covering product decisions and research, browser experiences, software
architecture and code, repository and team delivery, nonfiction prose, and
go-to-market work, plus standing contracts for request completion and
documentation truth that can be enabled independently.

Install one discipline when an agent needs deeper judgment for a domain, or
combine several in your own downstream agent stack. Each discipline turns
repeated professional practice into an explicit workflow with evidence
requirements, boundaries, and verification checks — and routes internally so an
agent loads the one reference the task needs.

> **Migrating from the old 34-skill layout?** The compatibility stubs were
> removed on 2026-08-16. Re-pin old selections to one of the six disciplines
> using the complete mapping in [MIGRATION.md](MIGRATION.md).

## Quick Start

Install the discipline that matches the work. `effective-web` is a useful
starting point for broad frontend tasks:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-web
```

Then ask for the outcome in normal language:

```text
Audit this dashboard, fix the highest-impact accessibility and responsive
issues, and verify the result.
```

The discipline tells a compatible agent what to inspect, which route and
references to load, where its authority stops, and what evidence is needed
before the task is complete.

Install all six only when you want the complete first-party collection:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --all
```

Selective installation also works with [DALO](#installation) when selections
should be pinned and shared across multiple agent targets. DALO can also enable
the collection's optional instruction packs as standing guidance without making
them a dependency of any skill.

## The Six Disciplines

| # | Discipline | One-line story | Routes |
| --- | --- | --- | --- |
| 01 | [`effective-product`](skills/effective-product/) | Decide what to build and how it should work | 10 |
| 02 | [`effective-web`](skills/effective-web/) | Build the browser experience as one system | 26 |
| 03 | [`effective-engineering`](skills/effective-engineering/) | Design and write the software itself | 9 |
| 04 | [`effective-delivery`](skills/effective-delivery/) | Move repositories and teams forward safely | 10 |
| 05 | [`effective-writing`](skills/effective-writing/) | Prose that people trust and act on | 7 |
| 06 | [`effective-marketing`](skills/effective-marketing/) | Take verified value to market | 12 |

## Find the Right Discipline

Start with the job you need done rather than the repository taxonomy.

| When you need to… | Start with… |
| --- | --- |
| Plan, conduct, and synthesize traceable customer and market research | [`effective-product`](skills/effective-product/) |
| Turn incomplete evidence into product direction, scope, or a durable decision | [`effective-product`](skills/effective-product/) |
| Model the experience: research, problem framing, objects, flows, IA, prototypes | [`effective-product`](skills/effective-product/) |
| Decide what to charge, how to package it, or what to name it | [`effective-product`](skills/effective-product/) |
| Design, build, review, or improve a production web experience | [`effective-web`](skills/effective-web/) |
| Turn websites, screenshots, prototypes, or videos into a traceable specification, or audit the result against those sources | [`effective-web`](skills/effective-web/) |
| Scope Impressum, privacy, consent, and online-sales disclosures across jurisdictions | [`effective-web`](skills/effective-web/) |
| Choose system boundaries, data models, or consistency guarantees | [`effective-engineering`](skills/effective-engineering/) |
| Write or review server-side TypeScript or Rust, or protect behavior with a test | [`effective-engineering`](skills/effective-engineering/) |
| Diagnose a repository, prioritize improvements, or plan a risky legacy change | [`effective-delivery`](skills/effective-delivery/) |
| Discover, prioritize, process, or monitor an unspecified live issue queue | [`effective-delivery`](skills/effective-delivery/) |
| Review a pull request, update dependencies, port a codebase, or run the repo's checks | [`effective-delivery`](skills/effective-delivery/) |
| Write technical documentation, or clarify ownership and team load around the work | [`effective-delivery`](skills/effective-delivery/) |
| Turn expertise into credible articles, essays, or editorial case studies | [`effective-writing`](skills/effective-writing/) |
| Make an internal message sound human, or fix locale typography | [`effective-writing`](skills/effective-writing/) |
| Position an offer, write commercial copy, or diagnose a funnel | [`effective-marketing`](skills/effective-marketing/) |
| Create social or LinkedIn content, or position a consultant profile | [`effective-marketing`](skills/effective-marketing/) |

`effective-delivery` coordinates the path from an unclear software request to a
verified handoff while leaving specialist depth with the other disciplines. The
broadest discipline, `effective-web`, routes work across UI/UX, CSS, React,
components, forms, tables, accessibility, internationalization, interface copy,
auth and error states, frontend SEO and AI search, performance, testing, SVG,
motion, textures, print stylesheets, and web-to-print.

## What the Collection Adds

General models can generate plausible answers. Shipping good work requires more:
knowing what evidence is missing, which tradeoff matters, what not to invent,
how far the user's authority extends, and what must be verified before calling
the work done.

The collection is designed around that gap:

- **Practice-built:** guidance is distilled from engineering, design review,
  product work, consulting, and repeated agent sessions.
- **Outcome-oriented:** skills cover discovery, implementation, review, and
  follow-through rather than stopping at generic advice.
- **Evidence-led:** research, repository state, user data, and observed behavior
  outrank confident assumptions.
- **Progressively disclosed:** agents load the relevant route and references,
  not the entire library for every request.
- **Explicit about boundaries:** each skill states when it applies, what it must
  not invent, and when a specialist or narrower workflow is needed.
- **Portable and inspectable:** the public interface is plain `SKILL.md`, with
  focused Markdown references and deterministic helpers where useful.
- **First-party maintained:** external collections are not silently vendored or
  renamed into this repository.

This is a focused collection for digital product, web, software-delivery, and
go-to-market work, not an attempt to cover every agent task. It does not replace
qualified legal advice, dedicated security review, infrastructure expertise, or
the external tools and credentials required to act on third-party systems.

## Collection Boundary

This repository owns Sebastian Software's public, first-party agent guidance:
independently installable skills under `skills/` and optional standing
instruction packs under `instructions/`.

Content ownership and activation stay separate. A skill remains complete when
installed alone, and discovering this source never activates an instruction
pack. DALO or another compatible manager owns explicit enablement and target
projection. External catalogs, cross-catalog precedence, named agents,
stack-specific routing, and the final choice of active instructions still
belong in a downstream agent stack.

The accepted boundary and activation contract are recorded in
[ADR 0005](docs/adr/0005-first-party-instruction-packs.md).

## Disciplines

| Discipline | Focus |
| --- | --- |
| [`effective-product`](skills/effective-product/) | Decision-led customer and market research, discovery, strategy, scope and release decisions, design research and modeling, behavioral and retention design, pricing and packaging, product naming, and Architecture Decision Records. |
| [`effective-web`](skills/effective-web/) | Routed web design and engineering across UI/UX, CSS, React, accessibility, SEO, performance, testing, SVG, motion, and web-to-print, plus reference capture and specification, originality and provenance audits, and jurisdiction-aware web compliance. |
| [`effective-engineering`](skills/effective-engineering/) | System architecture and operability, data models and consistency guarantees, server-side TypeScript and Rust depth, focused non-frontend tests, and repository-native benchmark methodology. |
| [`effective-delivery`](skills/effective-delivery/) | Workflow orchestration, repository audits and root-cause investigation, behavior-preserving ports, pull-request review and upkeep, delegated issue queues, dependency portfolios, repository validation, technical documentation, and engineering leadership. |
| [`effective-writing`](skills/effective-writing/) | Structure and prose craft for articles, essays, and editorial case studies, evidence-based AI-pattern audits, natural US team English for internal messages, and locale typography for thirteen European languages. |
| [`effective-marketing`](skills/effective-marketing/) | Positioning and segmentation, messaging and proof, launch and sales enablement, market learning, commercial copywriting, conversion optimization, social and LinkedIn content, and consultant profile positioning. |

All six share one naming grammar and one internal architecture: a lean
`SKILL.md` with a `## Route by Intent` table, and a flat `references/` directory
where each route is a file that names the smallest guidance set for the task.

## How the Collection Is Built

Every public discipline lives directly below `skills/`:

```text
skills/<name>/
├── README.md     # human-facing overview, use cases, and installation
├── SKILL.md      # agent-facing trigger, workflow, and routes
├── evals/
│   └── evals.json # unrun review-scenario fixtures for consequential decisions
├── agents/
│   └── openai.yaml # product-facing display and invocation metadata
├── references/   # optional focused guidance loaded only when needed
└── scripts/      # optional deterministic helpers
```

Standing cross-task conventions live separately from triggerable skills:

```text
instructions/<id>.md        # versioned provider-neutral instruction pack
instructions/evals/<id>.json # unrun behavioral review scenarios
```

`README.md` explains the value, use cases, scope, installation, and related
skills for people evaluating the skill on its own. `SKILL.md` is the agent-facing
interface: its YAML frontmatter gives the skill a portable name and tells
compatible agents when to load it. The body defines the core workflow and routes
specialized concerns into `references/` so a form problem loads form guidance
without filling the context window with unrelated material.

`evals/evals.json` contains unrun review-scenario fixtures, not an automated
model-quality gate. When behavior evidence is needed, use the documented
[manual review-scenario workflow](docs/review-scenarios.md) to record a
human-gradeable result with its runtime and evidence.

An instruction pack has no user-intent trigger. It applies across tasks only
after explicit activation, declares a semantic version and overlap topics, and
has matching behavioral scenarios. The collection currently provides
[`request-and-completion`](instructions/request-and-completion.md) for authority,
autonomy, and terminal-state behavior, and
[`documentation-truth`](instructions/documentation-truth.md) for preventing
documentation from becoming a competing, untestable shadow of its owning
artifacts. See [`docs/authoring-skills.md`](docs/authoring-skills.md) for the
authoring contract.

The hand-maintained catalog website lives in `site/`. Adding a discipline also
means adding its site card and inventory metadata, then running both repository
validators documented in [`docs/authoring-skills.md`](docs/authoring-skills.md).

The 33 superseded slugs were removed on 2026-08-16 after the transition to six
disciplines. [MIGRATION.md](MIGRATION.md) remains the authoritative old-to-new
mapping; only the six disciplines are installable from this repository.

The repository contains the first-party guidance itself: no installer, vendored
third-party snapshots, generated distribution tree, or dependency lockfiles.
Skill installation is handled by an Agent Skills-compatible manager such as
[DALO](https://dalo.sh) or Vercel's [skills CLI](https://skills.sh/docs);
instruction-pack projection requires a manager such as DALO that supports
explicit managed instruction blocks.

## Installation

### Selective setup with DALO

DALO can install one reviewed skill without activating the rest of the
collection. Register the repository as a catalog, select `effective-web`,
approve that exact skill, and sync it into the linked agent target:

```sh
curl -fsSL https://dalo.sh/install.sh | sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source inspect sebastian
dalo source select sebastian effective-web
dalo approve skill sebastian:effective-web
dalo sync
dalo doctor
```

Replace `effective-web` with another discipline name, or pass several names to
`dalo source select`. Catalog selections are pinned, and newly added repository
skills do not become active automatically. Review selected skills before
granting the source-qualified approval. A pinned pre-consolidation slug no
longer exists upstream: `dalo source refresh sebastian --check` reports it as
`selected_removed` while preserving the current pin. Re-pin it to its discipline
using [MIGRATION.md](MIGRATION.md), then sync again.

After reviewing the optional standing contracts, a DALO version with
source-backed instruction packs can enable either or both for verified targets:

```sh
dalo instructions enable sebastian:request-and-completion --target codex --target claude
dalo instructions enable sebastian:documentation-truth --target codex --target claude
```

This is a separate activation boundary. Selecting or approving a skill does not
enable either pack, and refreshing the source does not add one silently.

### Quick install with skills.sh

Vercel's [skills CLI](https://skills.sh/docs) is a lightweight alternative for
trying the collection or installing individual skills without setting up a
separate source manager:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-web
```

Omit `--skill effective-web` to choose interactively, or pass `--all` to install
the complete collection. The skills CLI is convenient for direct installation
and broad agent compatibility; DALO adds reproducible multi-source management,
explicit trust and selection state, and health checks for long-lived team setups.

## Contributing

Good contributions sharpen agent behavior: a specific rule, a missing edge
case, a clearer trigger, or a focused reference that reduces repeated
explanation.

- Do not add article archives, source-review notes, or generic inspiration lists.
- Group cohesive domains behind a clear router; keep unrelated work separate.
- Put standing cross-task conventions with no independent trigger in an
  instruction pack, and keep activation and stack-specific precedence outside
  the source artifact.
- Prefer practical rules, examples, and checks over broad advice.
- Keep `SKILL.md` lean and move detail into `references/`.
- Keep external source selection and cross-catalog precedence in a downstream
  agent stack; do not vendor or configure external skills here.

Read [docs/authoring-skills.md](docs/authoring-skills.md) before changing a skill.

## About Sebastian Software

This collection is maintained by
[Sebastian Software](https://oss.sebastian-software.com/), where we build and
support open-source software. We also help teams design, modernize, and ship
ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see [LICENSE](LICENSE).
