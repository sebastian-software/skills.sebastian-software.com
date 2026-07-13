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

The collection is deliberately granular. A form problem should load a form
expert, not a complete design encyclopedia. Detailed material lives in
`references/` and is loaded only when useful.

## Skills

### UI and frontend

| Skill | Focus |
| --- | --- |
| `s7n-ui-design` | Broad UI planning, critique, direction, and quality gates. |
| `s7n-layout-spacing` | Layout, spacing, grids, responsive behavior, and safe areas. |
| `s7n-typography` | Type hierarchy, readable measure, font loading, and text rhythm. |
| `s7n-color-theming` | Color systems, contrast, semantic tokens, and dark mode. |
| `s7n-component-primitives` | Buttons, navigation, dialogs, menus, and reusable states. |
| `s7n-forms-ux` | Form layout, labels, validation, and completion flows. |
| `s7n-data-tables` | Tables, dense data, sorting, filtering, and row actions. |
| `s7n-accessibility-html` | Semantics, focus, keyboard access, and ARIA restraint. |
| `s7n-motion-interaction` | Motion, transitions, scroll patterns, and reduced motion. |
| `s7n-error-loading-states` | Loading, empty, success, error, and retry states. |
| `s7n-i18n-ux` | Localization, RTL, text expansion, and locale-aware UI. |
| `s7n-editorial-ux` | Labels, microcopy, errors, empty states, and product writing. |
| `s7n-auth-security-ux` | Login, passkeys, recovery, permissions, and security UX. |
| `s7n-frontend-seo` | Metadata, structured data, previews, and crawlable output. |
| `s7n-react-architecture` | React rendering boundaries, state, data flow, and hydration. |
| `s7n-react-component` | Component APIs, composition, forms, refs, and interop. |
| `s7n-css-architecture` | Cascade, scoping, tokens, browser support, and CSS tooling. |
| `s7n-web-performance` | Core Web Vitals, images, caching, and resource loading. |
| `s7n-frontend-testing` | Playwright, Vitest, Storybook, E2E, and visual testing. |

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
| `s7n-svg-textures` | SVG filters, procedural textures, and surface effects. |

The `s7n-*` prefix is the compact Sebastian Software namespace. Other names are
kept where a skill has an established first-party identity.

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
- Do not make one skill responsible for unrelated domains.
- Prefer practical rules, examples, and checks over broad advice.
- Keep `SKILL.md` lean and move detail into `references/`.
- Do not vendor external skills; manage them through DALO.

Read [docs/authoring-skills.md](docs/authoring-skills.md) before changing a skill.

## License

See [LICENSE](LICENSE).
