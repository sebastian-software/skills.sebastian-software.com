# Sebastian Software Skills

Practice-built skills for agents that need to produce better frontend, product,
engineering, and content work.

This repository is the first-party source for Sebastian Software agent skills.
It contains the skills themselves and no installer, vendored third-party
snapshots, generated distribution tree, or dependency lockfiles. Installation
is handled by an Agent Skills-compatible manager such as
[DALO](https://dalo.sh) or Vercel's [skills CLI](https://skills.sh/docs).

## Why This Exists

General models know a lot, but they often need firmer operating rules to ship
consistently good work. These skills turn practical judgment from engineering,
design review, product work, and repeated agent sessions into focused workflows
and checks.

The collection is deliberately routed. Cohesive domains can expose one memorable
skill while keeping specialized workflows in `references/`, so a form problem
loads form guidance without exposing a long menu of overlapping skill names.

## Skills

### Web design and engineering

| Skill | Focus |
| --- | --- |
| `effective-web` | Routed web design and engineering guidance: UI/UX, CSS, React, accessibility, SEO, performance, testing, SVG textures, and web-to-print. |

### Engineering workflows

| Skill | Focus |
| --- | --- |
| `port-codebases` | Resource-aware, behavior-preserving ports across languages, runtimes, frameworks, platforms, and major APIs. |

### Marketing and sales

| Skill | Focus |
| --- | --- |
| `linkedin-social-selling` | Evidence-led B2B LinkedIn positioning, profile, network, content, conversations, lead magnets, funnels, and measurement. |
| `linkedin-posts` | LinkedIn ideas, formats, calendars, and post writing. |

### Content and specialist work

| Skill | Focus |
| --- | --- |
| `consultant-profile` | Consultant profiles, CVs, case studies, and positioning. |
| `github-pr-auto-review` | GitHub PR review, maintenance, feedback, and CI recovery. |
| `metro-english` | Natural metropolitan US team English for professional writing. |
| `smart-dependency-updater` | Researched dependency-update portfolios and PR delivery. |
| `locale-typography` | Locale-aware punctuation, spacing, quotes, dashes, and formatting guidance for 26 European and North American locales. |
| `web-legal-compliance` | Evidence-backed website legal disclosures and consent surfaces across the EU/EEA, UK, Canada, and the United States. |

The broad web domain uses the memorable `effective-web` identity. Specialist
skills use descriptive, portable names without a repository-specific prefix.

## Repository Interface

Every public skill lives directly below `skills/`:

```text
skills/<name>/
├── SKILL.md
├── references/   # optional progressive-disclosure material
├── scripts/      # optional deterministic helpers
├── assets/       # optional output resources
└── examples/     # optional complete examples
```

`SKILL.md` is the public interface. Its YAML frontmatter must contain a unique,
portable `name` and a useful `description`.

## Installation

### Managed setup with DALO

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

DALO treats this repository as a trusted team source, so all first-party skills
are active together. External repositories are configured separately as DALO
catalogs; they are never copied or renamed here. See [docs/dalo.md](docs/dalo.md)
for the complete setup and the curated external selection.

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

## License

See [LICENSE](LICENSE).
