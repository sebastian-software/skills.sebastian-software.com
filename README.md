# Sebastian Software Skills

Practice-built skills for agents that need to produce better frontend, product,
engineering, and content work.

This repository is the first-party source for Sebastian Software agent skills.
It contains the skills themselves and no installer, vendored third-party
snapshots, generated distribution tree, or dependency lockfiles. [DALO](https://dalo.sh)
handles source tracking, resolution, selection, and installation.

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
| `effective-web` | Routed web design and engineering guidance: UI/UX, CSS, React, accessibility, SEO, performance, testing, and SVG textures. |

### Content and specialist work

| Skill | Focus |
| --- | --- |
| `consultant-profile` | Consultant profiles, CVs, case studies, and positioning. |
| `github-pr-auto-review` | GitHub PR review, maintenance, feedback, and CI recovery. |
| `metro-english` | Natural metropolitan US team English for professional writing. |
| `smart-dependency-updater` | Researched dependency-update portfolios and PR delivery. |
| `s7n-german-typography` | German punctuation, spacing, quotes, and dashes. |
| `s7n-linkedin-posts` | LinkedIn ideas, formats, calendars, and post writing. |
| `s7n-print-design` | Print CSS, paged media, and printable documents. |

The broad web domain uses the memorable `effective-web` identity. Existing
specialist names stay stable until their domains warrant a similar consolidation.

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

## Install With DALO

```sh
dalo init
dalo target link codex
dalo source add s7n git@github.com:sebastian-software/skills.sebastian-software.com.git
dalo status
dalo sync
dalo doctor
```

DALO treats this repository as a trusted team source, so all first-party skills
are active together. External repositories are configured separately as DALO
catalogs; they are never copied or renamed here. See [docs/dalo.md](docs/dalo.md)
for the complete setup and the curated external selection.

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
