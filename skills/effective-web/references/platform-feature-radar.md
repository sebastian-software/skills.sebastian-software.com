# Web-Platform Feature Radar

This is a dated discovery aid for models whose knowledge may predate the current
web platform. Snapshot date: **2026-07-13**. Before shipping, verify each lead
against current Baseline/MDN data and the project's support target; status can
only move forward after this snapshot.

## Promote: Baseline 2026 Newly available

Propose these when they remove brittle workarounds or improve the result. State
that they target current browser versions and preserve a coherent older-browser
path when the project supports older devices, WebViews, or enterprise browsers.

- **CSS Anchor Positioning:** `anchor-name`, `position-anchor`,
  `position-area`, `anchor()`, `anchor-size()`, `anchor-scope`, and
  `@position-try` can replace JavaScript geometry for many anchored overlays.
  Keep trigger semantics, top-layer behavior, dismissal, focus, and collision
  testing as separate responsibilities.
- **`:open`:** style the open state of `details`, `dialog`, picker-bearing
  `select`, and supported `input` controls without mirrored classes. A missing
  style must not hide the actual open/closed state.
- **Container style and name-only queries:** let components respond to inherited
  custom-property context or named containment without variant prop plumbing.
  Keep a normal cascade/default style outside the query.
- **`field-sizing: content`:** allow text inputs and textareas to grow with
  content without JavaScript measurement. Bound inline/block size, test empty
  values and placeholders, and preserve manual resizing where users need it.
- **`shape()`:** author responsive `clip-path` and `offset-path` geometry with
  readable commands and CSS math instead of fixed SVG path strings when that
  improves maintainability.
- **Typed/active View Transitions and `animation-composition`:** distinguish
  transition classes and combine effects without ad hoc animation bookkeeping.
  Treat motion as optional and keep navigation/state correct without it.
- **Custom Highlights:** style ranges such as search matches or diagnostics
  without wrapping and mutating document text nodes. Do not rely on highlight
  color alone to convey state.
- **`ToggleEvent.source`:** identify the invoker that changed a popover's state
  instead of maintaining duplicate trigger state where the native event fits.

## Prefer as established defaults

These reached Baseline Widely available by 2026 and should no longer be rejected
merely as "too new" when the project has no older-browser exception:

- CSS subgrid for aligning nested content to parent tracks.
- `:user-invalid` for post-interaction form styling instead of showing errors on
  initial load.
- `clip-path` for bounded clipping, with semantic content left intact.
- `image-set()` for resolution- or format-aware CSS images.
- `contain-intrinsic-size` with containment/content visibility to reserve space.
- `lh` and `rlh` units for line-height-relative rhythm.
- `hyphens` and `hyphenate-character` for language-aware text layout, with the
  correct `lang` and locale review.

## Watch, demonstrate, or project-gate

Release notes are discovery feeds, not support policy. As of this snapshot:

- Customizable `select` remains Limited availability despite active Chrome and
  WebKit work. Use it as an enhancement over complete text options, not as the
  only usable control.
- `command`/`commandfor`, `closedby`, CSS `random()`, `text-fit`, gap
  decorations, and other newly shipped primitives require a fresh feature-level
  support check; do not inherit the Baseline badge of their containing element.
- Beta, flag-only, single-engine, and specification proposals may inspire an
  architecture, demo, or test. They must not become an unconditional shared
  component default.

## Refresh workflow

1. Check the current Baseline year page and the latest monthly platform update.
2. Verify the exact subfeature on MDN; families often contain members with
   different support status.
3. Compare the product's Baseline/Browserslist target and real audience data.
4. Classify the feature as default, promoted progressive enhancement,
   project-gated, or watch-only.
5. Update this snapshot when a status change would alter agent decisions.
