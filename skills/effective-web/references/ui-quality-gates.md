# UI Quality Gates

Use these gates before calling UI implementation complete. They are not design
scores. Scores hide severity and reward improving a number instead of fixing the
right issue. Mark each category as `blocked`, `risky`, or `acceptable`.

## Measurable UI Gate

| Category | Blocked | Risky | Acceptable |
|----------|---------|-------|------------|
| Accessibility | WCAG AA blocker, keyboard trap, missing labels on critical controls, unreadable contrast | Minor ARIA gaps, weak focus styling, unclear alt text | Keyboard, semantics, labels, focus, contrast, target size, and announcements are covered |
| Responsive layout | Horizontal overflow, unusable mobile layout, clipped primary action, text that cannot fit | Awkward spacing, density, or ordering at one breakpoint | Continuous resize, short and narrow viewports, zoom, long text, and touch input work |
| Performance | Implementation choice likely breaks LCP, INP, CLS, or interaction responsiveness | Heavy assets, expensive animation, or unbounded rendering need verification | Critical assets, layout stability, and interaction cost are handled |
| Theming | Hard-coded colours break tokens, dark mode, contrast, or semantic state colours | Some one-off values need token consolidation | Tokens and semantic colours are used consistently |
| State coverage | Missing empty, loading, error, success, disabled, or permission state for the core flow | Secondary states exist but need clearer copy or interaction detail | All states required by the brief are implemented in the real components |
| Resilience | Perfect-data-only UI breaks with long text, empty values, permissions, offline/errors, or localisation | Some edge cases are known but bounded | Long text, missing data, error recovery, permission states, and i18n expansion are handled |
| Specificity | The UI could belong to any product in the category, or uses obvious generated-output patterns | Some details are specific but the main layout, media, or interaction model is still generic | The dominant design decisions follow the brief, audience, content, and register |

## Interpretation

- Any `blocked`: do not call the UI done.
- Any `risky`: either fix now or explicitly name the follow-up risk.
- All `acceptable`: the implementation can ship from a measurable-quality
  perspective.

## Accessibility as an operating capability

Do not postpone accessibility to a final audit. Make it part of the delivery
system at the cheapest useful layer:

- Put semantic, keyboard, focus, contrast, motion, target-size, and naming
  requirements in component acceptance criteria and design-system contracts.
- Give accessibility defects owners and severity. A blocked primary task cannot
  become acceptable because an automated scan is green or the release is late.
- Run static and component-level checks during development, browser checks in CI,
  and manual keyboard and assistive-technology review for consequential flows.
- Include disabled people and representative assistive setups in usability work
  when the product risk or audience warrants it.
- Track regressions and recurring root causes across releases. Fix the shared
  primitive or process when the same defect appears in multiple features.
- Keep a release-time audit as a verification layer, not the first time the team
  considers accessibility.

## Core and Enhancement Gate

Build and verify the semantic, usable core before adding decorative overlap,
sticky behavior, advanced typography, motion, or another optional enhancement.
The core must preserve the primary task, content, source order, focus order, and
readable fallback when the enhancement is removed or unsupported.

Before starting the enhancement pass, verify the core with:

- Feature erasure and delayed or unavailable JavaScript where relevant.
- Continuous resizing instead of a few named breakpoints, including shallow
  landscape viewports and mobile browser chrome.
- Keyboard navigation, visible and unobscured focus, zoom, touch, pointer, text
  selection, and hash-target navigation.
- Minimum, typical, maximum, empty, long, and localized content.
- Representative browsers from the project's support policy.

Keep flair optional. Suspend sticky, overlapping, clipped, or animated treatment
when it obscures focused content or blocks the primary task. If the enhancement
requires compound conditions, undo chains, duplicated content, opaque math, or
repeated exception selectors, revisit the underlying design and layout model
before adding another patch.

## Reusable UI Fixtures

Create a fixture in the same implementation task when changing global CSS,
reusable components, or stateful layout and interaction behavior:

- For global CSS, maintain a semantic kitchen sink with headings, prose, lists,
  forms, tables, media, selection, focus, hash targets, and uncommon elements.
- For reusable components, use the project's Storybook or pattern library and
  cover representative content, states, themes, locale, and interaction.
- For sticky, overlapping, scrolling, focus-dependent, or container-dependent
  behavior, provide enough surrounding height, width, items, and controls to
  reproduce the behavior while resizing and navigating by keyboard.
- If no component workshop exists, use a small isolated local route or example.
  Keep fixture-only styles and data out of production behavior.
- For a simple one-off page region, verify the real page instead of creating a
  parallel fixture without reuse value.

## Final Execution Pass

Use this pass after implementation, not as an open-ended polish loop. Its job is
to catch execution mistakes in an otherwise correct direction.

Check:

- **Design-system fit:** no one-off colours, spacing, shadows, radius, icons, or
  controls where project tokens/components already exist.
- **Alignment and spacing:** related elements align, gaps follow the project
  scale, and optical adjustments are intentional.
- **State completeness:** loading, empty, error, success, disabled, focus, and
  hover states are present where the component needs them.
- **Copy consistency:** labels use the same nouns and verbs as the surrounding
  product, button text says what happens, and errors explain recovery.
- **Responsive execution:** long text, narrow viewports, touch targets, zoom,
  and reduced motion are handled in the real UI.
- **Layout stability:** images, embeds, loading indicators, and async content do
  not shift the page unexpectedly.
- **Web code details:** focus is not obscured by sticky UI, async updates are
  announced when needed, form fields expose meaningful browser hints, and
  stateful UI can be deep-linked when users need to share or return to it.

Do not use this pass to change the design register, invent a new visual
direction, or add decoration. If the pass reveals that the direction itself is
wrong, return to the Design Readiness Check and revise the brief.

## Generic Output Gate

Use this gate to catch templated AI output without turning design into a
polishing loop. Classify suspected patterns with
[UI anti-patterns](ui-antipatterns.md): objective defects can block, individual
style tells are advisory, and clusters indicate a likely direction problem.

Ask:

- Would this screen still make sense if the brand name and colours were removed?
  If yes, what product-specific structure, content, media, or interaction is
  missing?
- Does the layout come from the brief, or from a common category template such
  as hero plus metrics plus repeated cards?
- Is the memorable part useful to the user, or merely decorative?
- Does the interface show real evidence when users need to inspect a product,
  place, person, object, state, screenshot, diagram, or outcome?
- Is restraint doing real work, or is it hiding an absent point of view?
- Is boldness doing real work, or is it compensating for weak hierarchy and
  content?
- For product UI, does navigation, data presentation, or workflow structure
  reflect the product domain, or could the same shell fit any dashboard?

Product UI can pass this gate by being extremely clear and quiet. Brand UI can
pass by being memorable. Content-heavy UI can pass by being unusually readable
and trustworthy. The standard is specificity, not intensity.

## Performance Design Check

Performance is part of the user experience. Do not optimise random details, but
do make performance-sensitive design choices explicit before shipping.

Check:

- The LCP element is known, not lazy-loaded, and has appropriate priority.
- Images are sized for their display context and have width/height or
  `aspect-ratio` to prevent layout shift.
- Heavy visual effects are bounded to small areas and do not animate layout
  properties.
- Long lists, large tables, feeds, and search results have a pagination,
  virtualisation, or progressive loading strategy.
- Non-critical media, scripts, and visual flourishes are lazy-loaded or omitted
  when they do not serve the primary action.
- Font choices do not require unnecessary weights, families, or blocking loads.
- The interface remains usable on slower mobile devices and weaker connections.
- Large client-rendered lists, tables, feeds, or search results are virtualised,
  paginated, or progressively loaded before they threaten scroll or input
  responsiveness.

If performance risk is visible in the design itself, fix the design decision.
If performance risk depends on implementation details, measure before and after
the change.

## Visual Verification

Inspect the rendered UI before calling it complete. Source review alone misses
layout, colour, overflow, and interaction problems.

Verify:

- Desktop and mobile viewports.
- The primary interaction path.
- Long text, empty data, loading, error, and success states.
- Keyboard focus order and visible focus rings.
- Dark/light theme if the project supports both.
- Motion behaviour with `prefers-reduced-motion`.
- Screenshots or browser inspection when a dev server or static preview is
  available.

For a code audit, group findings by file and report the actionable issue at a
clickable `file:line` location. Explain only the non-obvious tradeoff or fix;
do not bury concrete defects under a generic score or long preamble.

## Code-Level Web Checks

Run these checks when reviewing implementation code, especially React, Next.js,
Vue, Svelte, or plain HTML/CSS:

- Use `<button>` for actions and `<a>`/router links for navigation. Do not use
  clickable `<div>`/`span` elements for primary interaction.
- Icon-only controls have accessible names; decorative icons are hidden from
  assistive technology.
- Form inputs have `label`, meaningful `name`, appropriate `type`,
  `autocomplete`, and `inputmode`. Do not block paste.
- Global form and prose fixtures include wrapped labels, disabled explanations,
  hidden or generated fields, long localized words, URLs, code overflow,
  selection contrast, disclosure widgets, and real fragment navigation beneath
  persistent UI.
- Disable spellcheck for email addresses, usernames, invitation codes, and
  machine identifiers when spelling suggestions would corrupt or distract from
  the value. Do not disable it for normal prose fields.
- Async validation, save status, background work, and toast messages use local
  feedback and `aria-live` when screen reader users need the update.
- Text containers handle long content with wrapping, `min-width: 0` in flex/grid
  children, or deliberate truncation with a path to the full value.
- Dates, times, numbers, and currencies use `Intl.*` APIs rather than hardcoded
  formatting.
- Animations list properties explicitly; avoid `transition: all`, layout
  animation, and non-interruptible effects.
- URL state reflects tabs, filters, pagination, selected records, and expanded
  panels when users need shareable or restorable UI state.
- Warn before route change, reload, or close only when users would lose genuine
  unsaved work; remove the guard immediately after save or discard.
- Dark themes set `color-scheme`; browser UI such as form controls and
  scrollbars should not fight the theme.
- Keep browser chrome coherent by updating `theme-color` when the top-level
  surface changes materially, including supported light and dark modes.
- Mark stable brand names, code tokens, product identifiers, and commands with
  `translate="no"` when automatic translation would corrupt them; keep surrounding
  explanatory prose translatable.

Do not treat a clean automated check as proof of visual quality. Automated
checks catch measurable defects; rendered inspection catches whether the UI
actually matches the brief.

## Use With Judgment

This gate covers measurable quality. It does not replace design judgment. A UI
can pass every measurable gate and still have the wrong register, weak
hierarchy, or unclear primary action. Use the Design Readiness Check before
implementation and this gate before completion.
