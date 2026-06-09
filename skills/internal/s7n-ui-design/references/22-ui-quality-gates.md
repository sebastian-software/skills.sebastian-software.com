# UI Quality Gates

Use these gates before calling UI implementation complete. They are not design
scores. Scores hide severity and reward improving a number instead of fixing the
right issue. Mark each category as `blocked`, `risky`, or `acceptable`.

## Measurable UI Gate

| Category | Blocked | Risky | Acceptable |
|----------|---------|-------|------------|
| Accessibility | WCAG AA blocker, keyboard trap, missing labels on critical controls, unreadable contrast | Minor ARIA gaps, weak focus styling, unclear alt text | Keyboard, semantics, labels, focus, contrast, target size, and announcements are covered |
| Responsive layout | Horizontal overflow, unusable mobile layout, clipped primary action, text that cannot fit | Awkward spacing, density, or ordering at one breakpoint | Mobile, tablet, desktop, zoom, long text, and touch input work |
| Performance | Implementation choice likely breaks LCP, INP, CLS, or interaction responsiveness | Heavy assets, expensive animation, or unbounded rendering need verification | Critical assets, layout stability, and interaction cost are handled |
| Theming | Hard-coded colours break tokens, dark mode, contrast, or semantic state colours | Some one-off values need token consolidation | Tokens and semantic colours are used consistently |
| State coverage | Missing empty, loading, error, success, disabled, or permission state for the core flow | Secondary states exist but need clearer copy or interaction detail | All states required by the brief are implemented in the real components |
| Resilience | Perfect-data-only UI breaks with long text, empty values, permissions, offline/errors, or localisation | Some edge cases are known but bounded | Long text, missing data, error recovery, permission states, and i18n expansion are handled |

## Interpretation

- Any `blocked`: do not call the UI done.
- Any `risky`: either fix now or explicitly name the follow-up risk.
- All `acceptable`: the implementation can ship from a measurable-quality
  perspective.

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

Do not use this pass to change the design register, invent a new visual
direction, or add decoration. If the pass reveals that the direction itself is
wrong, return to the Design Readiness Check and revise the brief.

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

Do not treat a clean automated check as proof of visual quality. Automated
checks catch measurable defects; rendered inspection catches whether the UI
actually matches the brief.

## Use With Judgment

This gate covers measurable quality. It does not replace design judgment. A UI
can pass every measurable gate and still have the wrong register, weak
hierarchy, or unclear primary action. Use the Design Readiness Check before
implementation and this gate before completion.
