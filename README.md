# Sebastian Software Skills

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Website:** [skills.sebastian-software.com](https://skills.sebastian-software.com/)

**Give your AI agent the practical judgment to take product and software work
from an ambiguous brief to a review-ready result.**

19 practice-built skills and 181 focused references for product decisions, web
experiences, codebase improvement, delivery, go-to-market work, professional
communication, and web compliance.

This is not a loose prompt dump. It is a maintained, first-party operating
layer for agents that work on real products and repositories. Each skill turns
repeated professional practice into explicit workflows, boundaries, evidence
requirements, and verification checks that an agent can apply when the task
calls for them.

## Quick Start

Install one skill to try the collection:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-web
```

Or install all 19 skills:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --all
```

Selective installation works with both the skills CLI and DALO. You do not
need to adopt the whole collection to use `effective-web` or any other single
skill. With DALO, register this repository as a catalog instead of a complete
team source; the [selective DALO setup](#selective-setup-with-dalo) below shows
the difference.

Then ask for the work in normal language. A compatible agent selects the
relevant skill from its description and loads the detailed guidance it needs.

```text
Audit this dashboard for accessibility, responsive behavior, and loading cost.

Turn these interview notes into an evidence-led MVP recommendation.

Turn this design brief and research into a problem model, interaction system,
and decision-grade prototype plan.

Review this codebase, rank the highest-leverage improvements, and implement the
agreed scope.

Take this software task from an unclear request through an authorized change,
focused verification, and a review-ready handoff.

Build a LinkedIn positioning and content system that leads to qualified B2B
conversations.
```

For reproducible setups, pinned selections, multiple agent targets, and managed
external catalogs, use [DALO](#installation).

## What This Collection Enables

The collection covers connected parts of the product lifecycle, so the same
agent can carry context and quality standards across disciplines instead of
treating every task as an isolated prompt.

| From | To | Skills that help |
| --- | --- | --- |
| Unclear opportunity | Evidence-led product direction, scope, priorities, and release criteria | [`product-management`](skills/product-management/), [`decision-records`](skills/decision-records/) |
| Product direction and research | Traceable problem framing, interaction model, structure, and prototype plan | [`product-design`](skills/product-design/), [`effective-web`](skills/effective-web/) |
| Product thesis | Distinctive, researched, multilingual name shortlist | [`product-naming`](skills/product-naming/) |
| Brief or existing interface | Designed, implemented, accessible, performant, and tested web experience | [`effective-web`](skills/effective-web/), [`locale-typography`](skills/locale-typography/) |
| Website or digital service | Jurisdiction-aware disclosure, privacy, and consent work product | [`web-legal-compliance`](skills/web-legal-compliance/) |
| Unclear software task | Authorized, verified, review-ready implementation and handoff | [`effective-workflow`](skills/effective-workflow/) with the relevant specialist skills |
| Repository uncertainty | Read-only diagnosis, evidence-backed audit, executable plan, or focused improvement | [`codebase-improvement`](skills/codebase-improvement/) |
| Architecture question | Evidence-led system direction, operability, and evolution path | [`software-architecture`](skills/software-architecture/), [`decision-records`](skills/decision-records/) |
| Software behavior risk | Focused, reliable evidence for a non-frontend regression, invariant, async path, data boundary, or CLI contract | [`software-testing`](skills/software-testing/) |
| Software interface or contributor workflow | Repository-native, verified technical documentation | [`tech-docs`](skills/tech-docs/) |
| Aging or changing system | Researched dependency updates or a behavior-preserving codebase port | [`smart-dependency-updater`](skills/smart-dependency-updater/), [`port-codebases`](skills/port-codebases/) |
| Pull request | Impact-led review, feedback resolution, CI recovery, and delivery follow-through | [`pr-review`](skills/pr-review/) |
| Expertise or offer | Credible consultant positioning and B2B LinkedIn acquisition system | [`consultant-profile`](skills/consultant-profile/), [`linkedin-social-selling`](skills/linkedin-social-selling/) |
| Raw idea or stiff draft | LinkedIn content and natural professional team communication | [`linkedin-posts`](skills/linkedin-posts/), [`metro-english`](skills/metro-english/) |

`effective-workflow` coordinates the path from an unclear software request to a
verified handoff while leaving specialist depth with its first-party owners.
The broadest specialist skill, `effective-web`, routes work across UI/UX, CSS,
React, components, forms, tables, accessibility, internationalization,
interface copy, auth and error states, frontend SEO and AI search, performance,
testing, SVG, motion, textures, print stylesheets, and web-to-print.

## Why Use These Skills

General models can generate plausible answers. Shipping good work requires more:
knowing what evidence is missing, which tradeoff matters, what not to invent,
how far the user's authority extends, and what must be verified before calling
the work done.

These skills are designed around that gap:

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
| [`smart-dependency-updater`](skills/smart-dependency-updater/) | Researched dependency-update portfolios with upstream context, local adaptation, validation, and PR delivery. |
| [`software-architecture`](skills/software-architecture/) | Evidence-led system boundaries, operability, architecture tradeoffs, and evolutionary migration paths. |
| [`software-testing`](skills/software-testing/) | Focused non-frontend test design, implementation, and verification for real software behavior and regressions. |
| [`tech-docs`](skills/tech-docs/) | Repository-native READMEs, guides, API and CLI references, migration notes, code documentation, examples, and verification. |

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
│   └── evals.json # behavioral cases for consequential decisions
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

### Complete team setup with DALO

[DALO](https://dalo.sh) manages skill sources, reviewed selections, versions,
approvals, and installation targets. It is the recommended option for teams,
multiple agent targets, or setups that combine this collection with external
skill catalogs.

Install DALO, then register this repository as the `sebastian` team source:

```sh
curl -fsSL https://dalo.sh/install.sh | sh
dalo init
dalo target link codex
dalo source add sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo status
dalo sync
dalo doctor
```

Unlike `source add-catalog`, `source add` treats this repository as a trusted
team source, so all 19 first-party skills are active together. External
repositories are configured separately as DALO catalogs; they are never copied
or renamed here. See [docs/dalo.md](docs/dalo.md) for the complete setup and the
curated external selection.

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
- Do not vendor external skills; manage them through DALO.

Read [docs/authoring-skills.md](docs/authoring-skills.md) before changing a skill.

## About Sebastian Software

This collection is maintained by
[Sebastian Software](https://oss.sebastian-software.com/), where we build and
support open-source software. We also help teams design, modernize, and ship
ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see [LICENSE](LICENSE).
