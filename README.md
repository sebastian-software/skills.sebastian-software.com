# Sebastian Software Skills

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Website:** [skills.sebastian-software.com](https://skills.sebastian-software.com/)

**Open-source skills for the professional judgment that capable AI agents still
need to do dependable product and software work.**

22 practice-built skills and 221 focused references for product decisions, web
experiences, codebase improvement, delivery, go-to-market positioning,
professional communication, and web compliance.

Use one skill when an agent needs deeper judgment for a specific job, or combine
several in your own downstream agent stack. Each skill turns repeated
professional practice into an explicit workflow with evidence requirements,
boundaries, and verification checks.

## Quick Start

Install the skill that matches the work. `effective-web` is a useful starting
point for broad frontend tasks:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-web
```

Then ask for the outcome in normal language:

```text
Audit this dashboard, fix the highest-impact accessibility and responsive
issues, and verify the result.
```

The skill tells a compatible agent what to inspect, which specialist guidance
to load, where its authority stops, and what evidence is needed before the task
is complete.

Install all 22 skills only when you want the complete first-party collection:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --all
```

Selective installation also works with [DALO](#installation) when selections
should be pinned and shared across multiple agent targets.

## Find the Right Skill

Start with the job you need done rather than the repository taxonomy.

| When you need to… | Start with… |
| --- | --- | --- |
| Turn incomplete evidence into product direction, scope, or a durable decision | [`product-management`](skills/product-management/), [`product-design`](skills/product-design/), [`decision-records`](skills/decision-records/) |
| Design, build, review, or improve a production web experience | [`effective-web`](skills/effective-web/), [`locale-typography`](skills/locale-typography/), [`web-legal-compliance`](skills/web-legal-compliance/) |
| Diagnose a repository and choose the highest-leverage next move | [`codebase-improvement`](skills/codebase-improvement/), [`software-architecture`](skills/software-architecture/) |
| Take an authorized software change through implementation and verification | [`effective-workflow`](skills/effective-workflow/), [`software-testing`](skills/software-testing/), [`software-validation`](skills/software-validation/) |
| Review, document, modernize, or port an existing codebase | [`pr-review`](skills/pr-review/), [`tech-docs`](skills/tech-docs/), [`smart-dependency-updater`](skills/smart-dependency-updater/), [`port-codebases`](skills/port-codebases/) |
| Turn expertise into credible positioning, content, and professional communication | [`consultant-profile`](skills/consultant-profile/), [`linkedin-social-selling`](skills/linkedin-social-selling/), [`linkedin-posts`](skills/linkedin-posts/), [`metro-english`](skills/metro-english/) |

`effective-workflow` coordinates the path from an unclear software request to a
verified handoff while leaving specialist depth with its first-party owners.
The broadest specialist skill, `effective-web`, routes work across UI/UX, CSS,
React, components, forms, tables, accessibility, internationalization,
interface copy, auth and error states, frontend SEO and AI search, performance,
testing, SVG, motion, textures, print stylesheets, and web-to-print.

## What the Skills Add

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

This repository owns the public, first-party skills themselves. Their portable
interface is a flat `skills/<name>/SKILL.md` layout that works with compatible
agent environments and source managers.

It intentionally does not define a universal agent setup. External catalogs,
cross-catalog precedence, named agents, project instructions, and routing across
first- and third-party sources belong in a separate downstream agent stack.
That keeps each skill independently useful and prevents one public source
repository from silently deciding how a user's complete environment behaves.

## Skills

### Product and design

| Skill | Focus |
| --- | --- |
| [`product-management`](skills/product-management/) | Evidence-led discovery, product strategy, outcomes, scope, prioritization, product quality, release decisions, and learning loops. |
| [`product-design`](skills/product-design/) | Evidence-led research synthesis, problem framing, interaction and object modeling, information architecture, prototyping, autonomy, and design delivery. |
| [`product-naming`](skills/product-naming/) | Strategic name generation, multilingual spoken-name testing, live conflict research, and evidence-backed shortlists. |

### Web design and engineering

| Skill | Focus |
| --- | --- |
| [`effective-web`](skills/effective-web/) | Routed web design and engineering guidance across UI/UX, CSS, React, accessibility, SEO, performance, testing, SVG, motion, and web-to-print. |
| [`locale-typography`](skills/locale-typography/) | Locale-aware punctuation, spacing, quotes, dashes, numbers, dates, currency, and formatting for 26 European and North American locales. |
| [`web-legal-compliance`](skills/web-legal-compliance/) | Evidence-backed website disclosures, privacy, and consent surfaces across the EU/EEA, UK, Canada, and the United States. |

### Engineering and delivery

| Skill | Focus |
| --- | --- |
| [`effective-workflow`](skills/effective-workflow/) | Lean, repository-native orchestration from understanding through authorized change and focused verification to a review-ready handoff. |
| [`codebase-improvement`](skills/codebase-improvement/) | Read-only root-cause investigation, repository audits, leverage-based prioritization, executable plans, and focused improvements. |
| [`decision-records`](skills/decision-records/) | Repository-native ADR creation, supersession, review, and drift control for durable cross-functional decisions. |
| [`port-codebases`](skills/port-codebases/) | Resource-aware, behavior-preserving ports across languages, runtimes, frameworks, platforms, and major APIs. |
| [`pr-review`](skills/pr-review/) | Human, impact-led PR review, maintenance, feedback resolution, and CI recovery. |
| [`rust-engineering`](skills/rust-engineering/) | Strict, readable Rust implementation and review across ownership, errors, concurrency, unsafe code, and FFI. |
| [`smart-dependency-updater`](skills/smart-dependency-updater/) | Evidence-backed dependency selection, introduction, update portfolios, local adaptation, validation, and PR delivery. |
| [`software-architecture`](skills/software-architecture/) | Evidence-led system boundaries, operability, architecture tradeoffs, and evolutionary migration paths. |
| [`software-testing`](skills/software-testing/) | Focused non-frontend test and repository-native benchmark design, implementation, and verification. |
| [`software-validation`](skills/software-validation/) | Repository-native discovery and execution of existing typecheck, lint, test, benchmark, load, build, package, and documentation gates with explicit evidence gaps. |
| [`tech-docs`](skills/tech-docs/) | Repository-native READMEs, guides, API and CLI references, migration notes, code documentation, examples, and verification. |
| [`typescript-engineering`](skills/typescript-engineering/) | Strict, honest server-side and general TypeScript implementation and review across types, modules, async, errors, and tooling contracts. |

### Positioning, marketing, and communication

| Skill | Focus |
| --- | --- |
| [`consultant-profile`](skills/consultant-profile/) | Consultant profiles, CVs, case studies, project selection, career narratives, and positioning. |
| [`linkedin-social-selling`](skills/linkedin-social-selling/) | Evidence-led B2B LinkedIn positioning, profile, network, content, conversations, lead magnets, funnels, and measurement. |
| [`linkedin-posts`](skills/linkedin-posts/) | LinkedIn ideas, formats, calendars, and post writing for a defined audience, voice, and goal. |
| [`metro-english`](skills/metro-english/) | Natural metropolitan US team English for Slack, GitHub, Linear, PR notes, and other professional communication. |

The broad web domain uses the memorable `effective-web` identity. Specialist
skills use descriptive, portable names without a repository-specific prefix.

## How the Collection Is Built

Every public skill lives directly below `skills/`:

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

The hand-maintained catalog website lives in `site/`. Adding a skill also means
adding its site card and inventory metadata, then running both repository
validators documented in [`docs/authoring-skills.md`](docs/authoring-skills.md).

The repository contains the skills themselves: no installer, vendored
third-party snapshots, generated distribution tree, or dependency lockfiles.
Installation is handled by an Agent Skills-compatible manager such as
[DALO](https://dalo.sh) or Vercel's [skills CLI](https://skills.sh/docs).

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

Replace `effective-web` with another skill name, or pass several names to
`dalo source select`. Catalog selections are pinned, and newly added repository
skills do not become active automatically. Review selected skills before
granting the source-qualified approval.

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
