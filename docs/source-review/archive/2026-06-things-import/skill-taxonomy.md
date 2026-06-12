# Skill Taxonomy Proposal

Reviewed: 2026-06-10

This document defines the proposed structure for turning the reviewed Things
candidate sources into skill updates. It is intentionally a planning artifact:
do not edit skills directly from the source queue until the relevant section
has gone through a second-pass review.

## Current Source Map

The final Things review produced 221 `Skill Archive Candidate` items. They are
mapped in `candidate-source-map.csv` with these fields:

- `things_id`
- `title`
- `primary_url`
- `other_urls`
- `cluster`
- `topic`
- `proposed_skill`
- `source_type`
- `source_role`
- `quality`
- `actionability`
- `dedupe_group`
- `cluster_reason`
- `second_pass_status`
- `notes`

Initial automatic grouping:

| Proposed skill/reference area | Candidate rows | Intended use                                                                                                    |
| ----------------------------- | -------------: | --------------------------------------------------------------------------------------------------------------- |
| `core-html-a11y`              |             53 | Shared HTML, accessibility, native controls, forms, focus, keyboard, and interaction rules.                     |
| `css-layout-responsive`       |             45 | Layout, responsive behavior, subgrid, viewport units, spacing, container queries, page structure.               |
| `design-system`               |             39 | Design-token foundations: typography, color, icons, images, visual effects, CSS units, placeholders, web fonts. |
| `frontend-testing`            |             26 | Visual regression, Playwright, Vitest Browser Mode, Storybook testing, screenshots, CI baselines.               |
| `react-architecture`          |             21 | RSC, rendering behavior, hooks performance, Suspense/hydration boundaries, server/client tradeoffs.             |
| `motion-interaction`          |             13 | View Transitions, scroll-driven animation, keyframes, transitions, reduced motion.                              |
| `react-component`             |             12 | React component API, composition, interop, custom elements, refs, async/component resilience.                   |
| `s7n-ui-design-core`          |              9 | Higher-level product UI, design-system posture, platform radar, broad UI judgment.                              |
| `build-tooling`               |              2 | Developer terminal habits, TypeScript export style, CSS-in-JS/build-time guidance.                              |
| `agent-knowledge-workflows`   |              1 | Agent/source/archive workflow source material.                                                                  |

Second-pass reviews may retarget sources into additional areas when the
automatic grouping is too broad. For example, HTTP caching sources should move
to `network-performance` because they affect perceived speed, freshness, and
network UX rather than accessibility or security.
Authentication sources such as passkeys/WebAuthn should move to
`auth-security` because they concern threat models, login architecture,
credential safety, and account recovery rather than general form design.

These counts are not final skill boundaries. They are a starting point for the
second-pass review.

## Structural Principles

### 1. Separate Skill Boundaries From Knowledge Layers

Skills should trigger from work the agent is doing, not just from a topic name.
For example, "build a React component" should trigger React-specific guidance,
but that guidance must still inherit HTML and accessibility expectations.

Use two layers:

- **Task skills**: trigger directly from user work, such as building React
  components, testing UI, designing layouts, or implementing motion.
- **Reference layers**: shared rules read by task skills, such as accessible
  HTML, forms, focus management, browser support, typography, and color.

### 2. React Must Not Absorb All UI Guidance

React-specific material should not become a general UI skill. Keep React
concerns focused on:

- component API and composition,
- rendering behavior and state boundaries,
- server/client component boundaries,
- hooks and performance tradeoffs,
- React/library interop.

React task skills should explicitly point to shared UI references for semantic
HTML, accessibility, forms, focus, keyboard behavior, and responsive layout.

### 3. HTML And Accessibility Are Shared Infrastructure

Do not duplicate accessibility rules separately in every framework skill.
Instead, keep one shared reference area and require framework skills to apply
it when they create DOM, interactive widgets, forms, or component APIs.

This avoids two failures:

- React skills becoming visually correct but semantically weak.
- General UI skills becoming too broad and swallowing framework details.

### 4. Prefer Fine-Grained Building Blocks

Do not collapse every UI-adjacent source into `html-accessibility`.
Accessibility is often one lens on a broader workflow. Keep separate reference
or skill areas when the work has its own substantial craft:

- **Forms UX and handling**: validation timing, recovery, copy-paste tolerance,
  field dependencies, error messaging, and submission flows.
- **Component-development know-how**: native control preservation, custom control
  anatomy, state styling, configurable CSS APIs, slots/children, and framework
  portability.
- **UX and interaction patterns**: list navigation, infinite scroll, load-more
  flows, pagination, disclosure patterns, state preservation, and recovery.
- **Typography and editorial UX**: readable type systems, long-form content,
  article semantics, reader-mode resilience, link styling, and content pacing.
- **Internationalization**: language, country, currency, units, locale
  preferences, translation affordances, RTL/layout resilience, and locale-aware
  component testing.
- **HTML/accessibility semantics**: labels, roles, names, focus, keyboard, ARIA
  fallback, and assistive-technology expectations.

React, Web Components, and plain HTML/CSS can all use the same
component-development reference. React-specific guidance should add framework
API details on top, not own the general component craft.

### 5. Source Priority Matters

Use source roles during second-pass review:

| Source role         | Meaning                                                          | How to use                                                                                |
| ------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `primary`           | Official docs, standards-facing docs, working-group explanation. | Can directly shape rules when still current.                                              |
| `secondary`         | High-quality expert article or case study.                       | Use for examples, caveats, and heuristics; pair with primary docs where possible.         |
| `duplicate-support` | Duplicate or near-duplicate source.                              | Use only to confirm strength; do not repeat it in skill references.                       |
| `platform-radar`    | Official or broad roundup.                                       | Use for prioritization and current-feature awareness, not as narrow implementation rules. |
| `background`        | Contextual source.                                               | Keep out of skill bodies unless it clarifies a decision.                                  |

## Proposed Skill/Reference Architecture

### Existing Skill To Keep As Umbrella

#### `s7n-ui-design`

Keep this as the broad UI quality umbrella. It should continue to trigger for
general UI design, CSS, HTML, frontend component code, dashboards, websites,
apps, design systems, and reviews.

Recommended changes later:

- Slim the main `SKILL.md` so it routes to references instead of carrying too
  many detailed rules inline.
- Add clearer "when building components" guidance that points to the shared
  HTML/accessibility references.
- Split dense topics into more precise reference files where needed.

### Shared Reference Layers

#### `references/html-accessibility.md`

Candidate source area: `core-html-a11y`.

Purpose:

- semantic HTML defaults,
- forms, labels, input attributes, autocomplete, validation timing,
- buttons vs links,
- focus and keyboard behavior,
- dialogs, popovers, menus, tabs, tooltips, accordions, selects,
- pointer/touch assumptions,
- ARIA as a fallback rather than a first choice.

Used by:

- `s7n-ui-design`,
- any future React component skill,
- forms/input workflows,
- component-library work,
- UI review/audit prompts.

#### `references/forms-ux.md`

Candidate source area: selected `core-html-a11y` form sources.

Purpose:

- validation timing,
- inline vs late validation,
- copy-paste and input normalization,
- error message behavior,
- recovery paths and overrides,
- field dependency UX,
- submit behavior and progressive disclosure.

Used by:

- `s7n-ui-design`,
- `references/html-accessibility.md`,
- future React or Web Component form/component workflows.

#### `references/component-development.md`

Candidate source area: custom controls and framework-agnostic component
sources from `core-html-a11y`, `react-component`, `css-layout-responsive`, and
`design-system`.

Purpose:

- preserve native controls and semantics where possible,
- design custom control anatomy,
- style state from real DOM/control state,
- expose configurable CSS APIs through custom properties and attributes,
- handle focus, labels, decorative elements, and tap targets,
- keep patterns portable across plain HTML/CSS, React, and Web Components.

Used by:

- `s7n-ui-design`,
- `s7n-react-component`,
- future Web Component guidance,
- component-library review prompts.

#### `references/ux-patterns.md`

Candidate source area: cross-cutting interaction and product UX patterns from
`core-html-a11y`, `s7n-ui-design-core`, `motion-interaction`, and component
sources.

Purpose:

- decide between pagination, load more, infinite scroll, and segmented lists,
- preserve position, URL state, scroll state, and back-button behavior,
- keep navigation, footers, filters, and recovery reachable,
- connect pattern UX to focus, keyboard, announcements, and performance,
- provide component-development requirements for reusable list/feed widgets.

Used by:

- `s7n-ui-design`,
- `references/component-development.md`,
- future app-shell, search, feed, dashboard, and content-browser workflows.

#### `references/i18n.md`

Candidate source area: language, locale, content translation, regional
preferences, RTL, and localization testing from UI, component, design-system,
and testing clusters.

Purpose:

- separate language, country, currency, units, timezone, and shipping choices,
- treat inferred locale as a suggestion, not a forced redirect,
- make global preference selectors discoverable, accessible, and overridable,
- require components and layouts to tolerate translated text and RTL contexts,
- connect locale behavior to UX patterns, forms, component-development, and
  visual regression testing.

Used by:

- `s7n-ui-design`,
- `s7n-react-component`,
- `references/ux-patterns.md`,
- `references/component-development.md`,
- `references/forms-ux.md`,
- frontend testing and visual review workflows.

#### `references/typography.md`

Candidate source area: typography-related sources currently mixed into
`design-system`, `css-layout-responsive`, and `core-html-a11y`.

Purpose:

- define readable font-size, line-height, measure, wrapping, and text spacing,
- codify CSS units for type (`rem`, `em`, `ch`, `cap`, `lh`, `rlh`, `clamp()`),
- handle fluid typography without breaking zoom or user preferences,
- specify link underline and text decoration behavior,
- feed type-related token decisions back into `references/design-system.md`.

Used by:

- `s7n-ui-design`,
- `references/design-system.md`,
- `references/editorial-ux.md`,
- `references/html-accessibility.md`,
- German typography stays separate as `s7n-german-typography`.

#### `references/editorial-ux.md`

Candidate source area: long-form reading, content-heavy layouts, article
semantics, and content presentation sources.

Purpose:

- distinguish article/content layouts from landing pages and application UI,
- preserve comfortable long-form reading through type, spacing, and layout,
- require semantic `main`/`article`/heading structure and skip-link behavior,
- account for reader mode, RSS, email, copied content, and assistive contexts,
- connect editorial images to performance, dark mode, and content focus.

Used by:

- `s7n-ui-design`,
- `references/typography.md`,
- `references/html-accessibility.md`,
- `references/network-performance.md`,
- future content-site or documentation-page workflows.

#### `references/responsive-design.md`

Candidate source area: responsive design sources currently spread across
`css-layout-responsive`, `network-performance`, `design-system`, and retargeted
image/media sources.

Purpose:

- choose responsive behavior from content, viewport, input mode, and device
  constraints rather than screen width alone,
- define responsive media rules for images, art direction, `srcset`, `sizes`,
  `<picture>`, aspect ratios, and source selection,
- connect responsive layout to typography, navigation, forms, tables, and
  content density,
- account for large screens, small screens, dynamic viewport units, safe areas,
  and browser UI changes,
- coordinate with network-performance when responsive choices affect resource
  discovery, bytes, caching, and image CDNs.

Used by:

- `s7n-ui-design`,
- `references/css-layout-responsive.md`,
- `references/network-performance.md`,
- `references/design-system.md`,
- `references/component-development.md`.

#### `references/css-layout-responsive.md`

Candidate source area: `css-layout-responsive`.

Purpose:

- responsive layout strategy,
- container queries and media queries,
- subgrid and CSS grid,
- viewport units and safe areas,
- spacing systems,
- page section layout,
- sticky header and scroll-offset handling,
- tables and content layout.

Used by:

- `s7n-ui-design`,
- future layout-focused skill if the topic becomes large enough,
- React component skill when components own layout behavior.

#### `references/design-system.md`

Candidate source area: `design-system`.

Purpose:

- design-token decisions,
- fluid type,
- units,
- color spaces and color interpolation,
- icons and SVG,
- image placeholders and media loading,
- web fonts,
- visual effects that affect UI clarity.

Used by:

- `s7n-ui-design`,
- German typography stays separate as `s7n-german-typography`,
- possible future visual/media-specific skill.

#### `references/motion-interaction.md`

Candidate source area: `motion-interaction`.

Purpose:

- motion purpose and limits,
- View Transitions,
- scroll-driven animation,
- keyframes and transitions,
- `prefers-reduced-motion`,
- motion as spatial continuity, not decoration.

Used by:

- `s7n-ui-design`,
- future animation/microinteraction skill,
- React component skill when it implements state transitions.

#### `references/baseline.md`

Candidate source area: Baseline, browser-support policy, Web Platform
Dashboard, Interop updates, and platform-radar sources retargeted from broader
frontend clusters.

Purpose:

- decide whether a web-platform feature is safe to use by default,
- prefer Baseline/Web Platform Dashboard over ad hoc browser-support guesses,
- connect feature support to Browserslist, ESLint, Stylelint, IDE, and CI
  feedback where possible,
- classify sources as support-policy/radar vs detailed implementation guidance,
- provide a shared support-status reference for component-development,
  responsive-design, motion-interaction, CSS layout, forms, and design-system
  work.

Used by:

- all frontend skill/reference areas when choosing modern platform APIs,
- component-development for native controls, popovers, dialogs, and anchor
  positioning,
- motion-interaction for View Transitions and scroll-driven features,
- responsive-design and CSS layout for modern viewport/layout APIs.

### React-Specific Task Skills

#### Proposed: `s7n-react-component`

Candidate source areas: `react-component` plus selected `core-html-a11y`,
`css-layout-responsive`, `design-system`, and `motion-interaction`.

Trigger when:

- building or reviewing React components,
- designing component APIs,
- adding component state,
- wiring forms, modals, menus, tabs, tooltips, or custom controls in React,
- creating reusable component-library pieces.

Scope:

- component API and composition,
- props and controlled/uncontrolled state,
- refs and imperative handles,
- async states,
- loading/error/empty/success states,
- portals and layering,
- custom elements interop,
- styling hooks and class APIs,
- accessibility pass-through and semantic DOM requirements.

Required inheritance:

- Always apply `html-accessibility.md` when rendering DOM.
- Apply `css-layout-responsive.md` when the component owns layout.
- Apply `motion-interaction.md` when adding animated state changes.

Non-scope:

- RSC architecture,
- app routing,
- data fetching architecture,
- broad product visual design.

#### Proposed: `s7n-react-architecture`

Candidate source area: `react-architecture`.

Trigger when:

- discussing or implementing React Server Components,
- choosing server/client component boundaries,
- debugging render behavior,
- optimizing hooks or re-renders,
- using Suspense, hydration, streaming, or server actions,
- reasoning about React state architecture.

Scope:

- RSC mental model,
- server/client boundaries,
- rendering and hydration behavior,
- hooks performance,
- memoization tradeoffs,
- Suspense and async UI boundaries,
- framework caveats.

Required inheritance:

- If architecture work creates UI components, also apply
  `s7n-react-component` or the shared UI references.

Non-scope:

- visual design rules,
- HTML/accessibility rules except where architecture affects them,
- package recommendation inventory.

### Testing Skill/Reference Area

#### Proposed: `s7n-frontend-testing`

Candidate source area: `frontend-testing`.

Trigger when:

- writing or reviewing frontend tests,
- setting up visual regression,
- using Playwright screenshots,
- testing Storybook states,
- using Vitest Browser Mode,
- stabilizing screenshot baselines or CI visual tests.

Scope:

- browser-level test strategy,
- visual regression workflows,
- Storybook state coverage,
- screenshot baselines,
- deterministic rendering,
- flake control,
- CI update/review process.

Relationship:

- Can stay separate from `s7n-ui-design`, but UI skills should recommend it
  when the user asks for verification or tests.

### Tooling And Agent Workflow Areas

#### `build-tooling`

Only two candidate sources currently map here. Do not create a new skill yet.
Fold into existing developer workflow docs or defer until more sources exist.

#### `agent-knowledge-workflows`

Only one candidate source currently maps here. Keep as source-review context,
not a new skill.

#### `network-performance`

Candidate source area: retargeted performance/network sources.

Purpose:

- HTTP caching and freshness,
- `stale-while-revalidate`,
- perceived speed and loading UX,
- image placeholder strategies such as blur-up, LQIP, base64 placeholders,
  BlurHash/ThumbHash-style encodings, and calmer visual loading states,
- responsive image delivery, source selection, encoding, and image CDNs,
- network fallback behavior,
- when to use browser cache headers vs service workers.

This is not a security bucket by default. Security sources should only land in
a security area when they actually address threat models, vulnerabilities,
auth, privacy, or hardening.

#### `auth-security`

Candidate source area: authentication, credential handling, login security,
passkeys/WebAuthn, account recovery, and related product UX.

Purpose:

- prefer phishing-resistant authentication patterns where appropriate,
- document passkeys/WebAuthn mental models and browser API boundaries,
- separate credential security from generic forms UX,
- specify login, fallback, recovery, device-sync, and enrollment UX risks,
- cross-reference forms UX only where auth flows expose form-like surfaces.

Used by:

- future security/auth-focused skill or reference,
- `references/forms-ux.md` when implementing login/signup flows,
- component-development only where auth controls expose reusable UI patterns.

#### `web-security`

Candidate source area: application hardening, browser security policies,
HTTP security headers, privacy headers, CSP, transport policy, clickjacking,
MIME sniffing, and security configuration hygiene.

Purpose:

- separate broad web hardening from auth-specific guidance,
- use current OWASP/MDN/security-scanner guidance for concrete rules,
- treat older explanatory articles as context rather than normative policy,
- document when headers are obsolete, replaced, or context-dependent,
- cross-reference network-performance only when caching/transport choices have
  security impact.

Used by:

- future web-security or security-review skill/reference,
- deployment/configuration checklists,
- auth-security where login/session behavior depends on browser policy headers.

## Second-Pass Review Method

Work one proposed area at a time. For each area:

1. Filter `candidate-source-map.csv` by `proposed_skill`.
2. Group by `dedupe_group` and collapse duplicates.
3. Re-score each source:
   - `source_role`: primary, secondary, duplicate-support, platform-radar,
     background.
   - `quality`: high, medium, low.
   - `actionability`: high, medium, low.
   - `currency`: current, check-before-use, stale-risk.
   - `target`: skill body, reference file, source notes, discard.
4. Promote only sources that add a rule, caveat, workflow, or useful example.
5. Draft a skill proposal before editing:
   - trigger description,
   - scope and non-scope,
   - reference files,
   - inherited references,
   - source list,
   - 2-3 evaluation prompts.
6. Edit or create skill files only after the proposal is coherent.

## Recommended Processing Order

1. `core-html-a11y`
   - This becomes shared infrastructure for everything else.
2. `react-component`
   - Uses the shared UI layer and resolves the React-vs-HTML separation.
3. `react-architecture`
   - Keep RSC/rendering separate from component authoring.
4. `css-layout-responsive`
   - Large enough to deserve a focused pass.
5. `design-system`
   - Typography/color/icons/images and token-system foundations; some material may remain under
     `s7n-ui-design` references rather than become a new skill.
6. `motion-interaction`
   - Should be integrated carefully to avoid over-animating product UI.
7. `frontend-testing`
   - Can become a separate practical skill once UI authoring structure is clear.

## Open Design Questions

1. Should `s7n-react-component` become a new internal skill, or should it be a
   reference inside `s7n-ui-design` first?
2. Should `core-html-a11y` be an independent skill or a reference layer only?
   Current recommendation: reference layer first.
3. Should `forms-ux` become its own reference file immediately? Current
   recommendation: yes, because form handling is larger than accessibility and
   needs UX-specific rules.
4. Should `component-development` become a framework-agnostic reference before
   `s7n-react-component`? Current recommendation: yes, so React can inherit
   general component craft instead of owning it.
5. Should broad platform radar sources stay in `s7n-ui-design` or become a
   `web-platform` reference? Current recommendation: keep them in
   `s7n-ui-design` until they become too large.
6. How strict should the skill descriptions be about cross-triggering? Current
   recommendation: React component work should explicitly trigger both React
   component guidance and shared UI/accessibility references.
