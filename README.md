# Sebastian Software Skills

Practice-built skills for agents that need to produce better frontend, product, and content work.

This repository is not a link dump, prompt archive, or loose collection of "nice ideas." It is a curated skill series distilled from real engineering work, design reviews, product decisions, articles, references, and repeated agent sessions. Useful source material gets absorbed into reusable rules, workflows, and checks. The source itself does not become the product.

The ambition is simple: give coding agents sharper taste, stronger technical defaults, and more reliable execution when they build or review real software.

## Why This Exists

General models know a lot, but they often need firmer operating rules to ship consistently good work. They drift into generic UI patterns, overstuffed components, weak accessibility, vague copy, fragile CSS, or performance fixes that sound plausible but miss the actual bottleneck.

These skills turn practical judgment into reusable agent behavior:

- Product interfaces should be clear, accessible, responsive, and hard to misuse.
- Frontend code should be technically solid, not just visually plausible.
- Design rules should be specific enough to change implementation decisions.
- Good references should become working heuristics, not permanent research clutter.
- Skills should stay focused, so the right expert is loaded for the right task.

The result is a first-party skill set for agents that are expected to do production-quality work, not just generate a convincing first draft.

## Positioning

Broad design skills such as Anthropic's `frontend-design` skill and the `impeccable` skill are excellent at pushing agents toward more distinctive, polished, ambitious interfaces. This repository is meant to complement that direction with a more modular operating system for day-to-day software work.

Where broad design skills say "make it exceptional," these S7N skills add sharper specialist judgment:

- `s7n-layout-spacing` handles spacing, grids, responsive structure, and layout stability.
- `s7n-accessibility-html` focuses on semantics, focus behavior, keyboard access, and ARIA restraint.
- `s7n-css-architecture` covers cascade layers, tokens, baseline support, and maintainable styling.
- `s7n-web-performance` keeps performance work tied to browser behavior and measurable bottlenecks.
- `s7n-react-architecture` and `s7n-react-component` guide implementation structure, not just appearance.

The point is not to replace a strong design skill. The point is to make the craft more durable: better defaults, better tradeoffs, better checks, and fewer AI-looking shortcuts.

## What Makes These Skills Different

They come from practice.

The skill set has been shaped by many reviewed sources, real implementation loops, and repeated problems that show up when agents build software: generic card grids, inaccessible controls, fragile responsive layouts, unclear form errors, unbounded typography, weak loading states, overbroad React components, and performance changes that optimize the wrong thing.

They are curated.

When a source is useful, its idea is rewritten as an actionable rule, checklist item, or workflow inside the right skill. When it is not useful enough to improve agent behavior, it is left out. The repository is for skills, not for preserving intake history.

They are granular.

Large composite skills are split into focused experts. A form problem should not load a whole design encyclopedia. A table problem should not pull in SEO guidance. The structure is designed around progressive disclosure: load the smallest useful expert, then consult references only when needed.

They are technical.

The skills aim to produce working output: semantic HTML, stable CSS, accessible interactions, resilient React components, measurable performance improvements, and copy that helps users complete tasks.

## Internal Skills

### UI And Product Craft

- `s7n-ui-design` - broad UI planning, critique, and quality gates.
- `s7n-layout-spacing` - layout structure, spacing systems, grids, responsive behavior.
- `s7n-typography` - UI typography, readable measure, font loading, hierarchy.
- `s7n-color-theming` - color systems, contrast, tokens, theming, dark mode.
- `s7n-component-primitives` - buttons, navigation, dialogs, component states.
- `s7n-forms-ux` - form layout, validation, field states, completion flows.
- `s7n-data-tables` - tables, dense data, comparison views, row actions.
- `s7n-accessibility-html` - semantic HTML, keyboard behavior, focus, ARIA.
- `s7n-motion-interaction` - purposeful motion, transitions, scroll patterns.
- `s7n-error-loading-states` - loading, empty, success, error, and retry states.
- `s7n-i18n-ux` - localization, RTL, text expansion, locale-aware UI.
- `s7n-editorial-ux` - labels, microcopy, empty states, error copy.
- `s7n-auth-security-ux` - auth UX, passkeys, password flows, permission prompts.
- `s7n-frontend-seo` - metadata, structured data, previews, crawlable frontend output.

### Frontend Engineering

- `s7n-react-architecture` - React app structure, data flow, rendering boundaries.
- `s7n-react-component` - component implementation, APIs, state, effects.
- `s7n-css-architecture` - cascade, layers, scoping, custom properties, browser support.
- `s7n-web-performance` - Core Web Vitals, images, preload behavior, caching.
- `s7n-frontend-testing` - frontend test strategy, Playwright, Vitest, selectors.

### Content, Media, And Specialist Output

- `s7n-german-typography` - German punctuation, spacing, quotes, typographic cleanup.
- `s7n-linkedin-posts` - LinkedIn post ideas, hooks, formats, and writing structure.
- `s7n-print-design` - print CSS, paged media, screen-to-print output.
- `s7n-svg-textures` - SVG filters, procedural textures, organic visual effects.

The `s7n-*` prefix is the compact Sebastian Software namespace. It keeps first-party skills distinct after installation.

## Repository Layout

```text
skills/internal/   First-party S7N skills
skills/vendor/     Reviewed external skill snapshots
manifests/         Source and lock manifests for skill-sync
packages/          TypeScript CLI source
docs/              Authoring, sync, review, and publishing workflow notes
```

Each skill is built around progressive disclosure:

```text
skill-name/
├── SKILL.md       Core trigger, workflow, and routing instructions
└── references/    Detailed rules loaded only when useful
```

## Quickstart

```bash
pnpm install
pnpm build
pnpm skill-sync validate
pnpm skill-sync sync --target all
```

Useful commands:

```bash
pnpm skill-sync doctor
pnpm skill-sync build
pnpm skill-sync sync --target all
```

`sync` is managed-only by default. It updates directories that contain a valid `.skill-sync.json` marker and preserves unrelated local skills.

## Contributing

Good contributions are welcome.

The best improvements usually look like one of these:

- A sharper rule that changes how an agent implements something.
- A missing edge case from real project work.
- A better trigger description so the right skill loads at the right time.
- A focused reference that reduces repeated explanation.
- A cleanup that removes duplication or narrows a skill's scope.

Please keep the bar high:

- Do not add article archives, copied source notes, or generic inspiration lists.
- Do not make one skill responsible for unrelated domains.
- Prefer practical rules, examples, and checks over broad advice.
- Keep `SKILL.md` lean and move details to `references/`.
- Validate before opening a pull request.

```bash
pnpm format:check
pnpm lint:oxlint
pnpm skill-sync validate
```

This is an open repository because the work gets better when experienced people bring their own hard-won lessons. If a rule helps agents produce better software in the real world, it belongs here.

## License

See [LICENSE](LICENSE).
