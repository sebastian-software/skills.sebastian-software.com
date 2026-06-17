# HTML and Accessibility

Accessibility is a structural property of the markup, not a layer added at the
end. Native semantics carry role, name, state, and a keyboard model for free;
ARIA only patches what the platform cannot express. Decide structure, focus
behavior, and announcements deliberately, the same way the rendered design is
decided.

## Semantic structure first

- Reach for the native element that already has the correct role, name, state,
  keyboard model, and form behavior before building anything custom: `button`,
  `a[href]`, `label`, `input`, `select`, `textarea`, `details`/`summary`,
  `dialog`, `table`, `fieldset`/`legend`, `ul`/`ol`/`li`.
- Use `button` for actions and `a[href]` for navigation. A `button` is reachable
  by Tab, fires on Enter and Space, and exposes a button role. A clickable `div`
  or `span` has none of this; recreating it needs `tabindex="0"`, `role`,
  keydown handlers for Enter and Space, and a disabled story — so use the native
  element instead.
- Provide exactly one `h1` per page or view, and nest headings without skipping
  levels (`h1` → `h2` → `h3`). Headings are the primary screen-reader navigation
  map; do not pick a level for its font size — style with CSS instead.
- Wrap regions in landmarks: one `main`, plus `header`/`banner`, `nav`,
  `aside`/`complementary`, `footer`/`contentinfo`. Give multiple landmarks of the
  same type distinct accessible names (`aria-label` or `aria-labelledby`) so "two
  navigations" become "primary" and "footer" in the landmark list.
- Use real lists for grouped items and `table` with `th`, `scope`, `caption`,
  and `thead`/`tbody` for tabular data. Never use a table for layout, and never
  fake rows with stacked `div`s when the data is genuinely tabular.
- Provide a "skip to main content" link as the first focusable element so
  keyboard users bypass repeated navigation.

## ARIA as a repair layer

- Treat ARIA as the patch for gaps native HTML cannot express, never as a
  substitute for the right element. The first rule of ARIA: do not use ARIA if a
  native element or attribute already provides the semantics.
- Do not change an element's native role without rebuilding everything that role
  implied (keyboard interaction, states, focus management). `role="button"` on a
  `div` still needs every behavior a real `button` gave for free.
- Never put interactive roles or `tabindex` on elements inside a `button` or
  `a`; nested interactive content is invalid and unreliable in assistive tech.
- Keep ARIA state in sync with reality: toggle `aria-expanded` on disclosure and
  menu triggers, `aria-pressed` on toggle buttons, `aria-checked` on custom
  checkboxes, `aria-selected` on tabs/options, and `aria-current="page"` on the
  active nav link. A stale ARIA attribute is worse than none.
- Reference only existing, rendered ids from `aria-labelledby`,
  `aria-describedby`, and `aria-controls`. An id that points at nothing yields
  silence.
- Use `aria-hidden="true"` only on content that is also unreachable by keyboard;
  never hide a focusable element from the accessibility tree, or a keyboard user
  lands on something a screen reader cannot describe.

## Accessible names

- Give every control a stable, meaningful accessible name. Prefer a visible
  `label` associated by `for`/`id`, or wrap the control in the `label`. Fall
  back to `aria-label`/`aria-labelledby` only when no visible text exists.
- Make link and button text describe the action or destination on its own. Avoid
  "click here" and bare "read more"; if the visible text must stay short, extend
  it with `aria-label` or visually hidden text that names the target.
- Give icon-only controls an explicit name (`aria-label`) and mark the decorative
  icon `aria-hidden="true"`. An `svg` used as an image needs `role="img"` and a
  `title`/`aria-label`; a purely decorative `svg` should be hidden.
- Always provide meaningful `alt` for informative images, and `alt=""` for
  decorative ones so they are skipped. Do not start `alt` with "image of".
- When a visible label and the accessible name differ, keep the visible text as
  the start of the accessible name so speech-input users can activate the control
  by saying what they see.

## Forms and labels

- Pair every field with a programmatically associated `label`. Group related
  controls (radios, related checkboxes, address blocks) in a `fieldset` with a
  `legend`. Placeholder text is not a label and disappears on input.
- Mark required fields with the native `required` attribute (optionally
  `aria-required="true"`), and do not rely on color or a bare asterisk alone to
  signal "required".
- Associate help text and error text with the field via `aria-describedby`, and
  set `aria-invalid="true"` on a field that fails validation so the error is
  announced and reachable, not merely shown in red.
- Preserve browser assistance: set accurate `type`, `name`, and `autocomplete`
  tokens (`email`, `username`, `current-password`, `new-password`, `one-time-code`,
  `tel`, `postal-code`, `name`) so autofill and password managers work. Do not
  disable autocomplete or block paste unless the value is genuinely one-time or
  sensitive.
- Drive the right mobile keyboard and submit action with `inputmode`
  (`numeric`, `decimal`, `tel`, `email`, `url`, `search`) and `enterkeyhint`
  (`search`, `send`, `go`, `next`, `done`). Use these to refine the on-screen
  keyboard; never use them as a replacement for the correct `type`, which also
  governs validation and parsing.
- Delay validation until the user has had a fair chance to answer. Prefer the
  `:user-valid` / `:user-invalid` pseudo-classes (which apply only after
  interaction) over `:valid` / `:invalid`, and prefer validating on blur or
  submit over flashing errors on every keystroke. On failure, keep the entered
  values, move focus to the first invalid field or an error summary, and give
  concrete recovery copy that states how to fix the problem.
- Never convey a field's state by color alone; pair color with an icon, text, or
  border change so it survives low vision and color-vision differences.

## Phone numbers and contact links

- Mark a callable phone number with an explicit `a[href="tel:..."]` rather than
  leaving it as plain text for the platform to auto-detect. Put the E.164 form in
  the `href` (`tel:+14155550100`) and a human-formatted number in the visible
  text.
- Disable platform telephone auto-detection (`<meta name="format-detection"
  content="telephone=no">`) only when intentional `tel:` markup and styling are
  provided in its place, so numbers are still callable but render consistently and
  are not mangled by the OS heuristic.
- Apply the same explicit-link approach to `mailto:` and `sms:` actions, and
  give each an accessible name that states the action ("Call sales", "Email
  support") rather than reading out raw digits.

## Focus management

- Keep focus visible at all times. Style `:focus-visible` (not just `:focus`) so
  the indicator shows for keyboard and not for mouse clicks, and never remove the
  outline without replacing it with an equally clear indicator.
- Treat the focus indicator as a design token: standardize outline color, width,
  and `outline-offset` across links, buttons, inputs, `summary`, and custom
  triggers. Note that `outline: currentColor` follows text color, which can fail
  on colored backgrounds — set an explicit, sufficiently contrasting color
  instead and verify it in both light and dark themes.
- Never rely on color alone for the focus state; ensure the indicator is visible
  against every background it can sit on and meets contrast against adjacent
  colors.
- On opening a modal `dialog`, move focus into it (the first control or a
  sensible heading), trap Tab within it, close it on Escape, and return focus to
  the element that opened it. The native `<dialog>` element with `showModal()`
  provides the top layer, Escape handling, and inert background; reach for it
  before a hand-rolled overlay. The `popover` attribute gives light-dismiss and
  top-layer behavior for non-modal popovers.
- After a client-side route change in a single-page app, move focus to the new
  view's heading or `main` and announce the new page; otherwise focus stays on a
  link that no longer exists and screen-reader users are not told the page
  changed.
- Manage focus through disclosures and async UI: when revealed content should
  receive attention, send focus to it; when content the user was on is removed,
  move focus to a stable nearby element rather than letting it reset to the top.
- Maintain a logical DOM order that matches the visual order so the Tab sequence
  is predictable. Reserve `tabindex="-1"` for programmatic focus targets, and
  avoid positive `tabindex` values, which fight the natural order.

## Announcements and live regions

- Announce dynamic changes the user did not directly trigger through a live
  region. Use `aria-live="polite"` (or `role="status"`) for non-urgent updates
  such as "saved" or search-result counts, and `aria-live="assertive"` (or
  `role="alert"`) only for errors that must interrupt.
- Render the live-region container in the DOM before the message arrives, then
  inject text into it; a region added together with its content may not be
  announced.
- Announce only what helps. Do not wire up live regions for changes the user
  caused and can see, or the interface becomes noisy and users disable speech.
- For long or background operations, communicate progress with a native
  `progress` element or `role="progressbar"` with `aria-valuenow`/min/max so the
  state is conveyed rather than implied by a spinner.

## Composite widgets and custom controls

- Before building a custom widget, exhaust native options. When a custom
  control is unavoidable, implement the full anatomy the role implies: role,
  accessible name, current value/state, and the complete keyboard model from the
  WAI-ARIA Authoring Practices for that pattern (tabs, menu, combobox, listbox,
  disclosure, slider, etc.).
- Preserve the underlying semantic input when styling. Build a custom-looking
  checkbox, radio, or select on top of the real form control (visually hiding the
  native input, not deleting it) so submitted values, autofill, and assistive-tech
  semantics survive the restyle.
- Make components configurable through CSS custom properties and state-driven
  selectors rather than swapping markup per variant, so a single accessible
  structure serves every visual theme.
- Test every custom or composite widget with keyboard only and with a screen
  reader before considering it done; visual correctness does not prove the role,
  name, and keyboard model are right.

## Semantic and state-driven styling

- Drive presentation from semantics and state, not from extra wrapper markup.
  Style from the element's own state (`:checked`, `:disabled`, `:user-invalid`,
  `[aria-expanded="true"]`, `[aria-current]`) so the visual state cannot drift
  from the accessibility state.
- Use parent-context selectors (`:has()`) to react to a child's state — for
  example `form:has(:user-invalid)` or `label:has(:checked)` — instead of
  toggling presentational classes from JavaScript. This keeps a single source of
  truth (the real control's state) and removes class-sync bugs that leave the
  visual and accessible states disagreeing.
- Keep these patterns general: child-, content-, focus-, error-, and
  state-driven parent styling is a structural CSS technique, with accessibility
  as one beneficiary; prefer it wherever a class would otherwise mirror DOM state.

## Visual accessibility and user preferences

- Meet WCAG contrast minimums: 4.5:1 for normal text, 3:1 for large text and for
  the visual boundaries of UI components and meaningful graphics. Verify focus and
  state indicators against every background they appear on.
- Make interactive targets large enough for touch and imprecise pointers; treat
  roughly 24x24 CSS pixels as a floor and a larger size as the comfortable target,
  with adequate spacing between adjacent hit areas.
- Do not infer input capability from viewport width. Use pointer media queries
  (`@media (pointer: coarse)` / `(hover: none)`) to adapt target sizes and hover
  affordances to the actual device, since a narrow window on a desktop still has a
  fine pointer and a wide tablet does not.
- Honor `@media (prefers-reduced-motion: reduce)`: remove or substantially reduce
  non-essential animation, parallax, and auto-playing motion, and never gate
  required information behind a motion the user has opted out of.
- Support `@media (forced-colors: active)` (Windows High Contrast): rely on
  system color keywords, avoid conveying meaning through removed backgrounds or
  box-shadows, use `forced-color-adjust` deliberately, and keep focus indicators
  visible since custom colors are overridden by the user's palette.
- Ensure content reflows without loss at 200% zoom and 400% on small viewports,
  and survives users overriding text size and spacing; size text and containers in
  relative units (`rem`/`em`) and avoid fixed pixel heights that clip enlarged
  text.
- Hide content consistently. Visually hidden but screen-reader-available text uses
  a clip/offscreen technique (not `display:none`); content meant to be gone must be
  removed from the visual, keyboard, and accessibility trees together, so nothing
  is reachable by Tab yet invisible, or visible yet missing from speech.

## Review checklist

- Is each job solved by a native element (`button`, `a`, `label`, `input`,
  `select`, `details`, `dialog`, `table`, landmark) before any custom role?
- Is there one `h1`, a logical heading outline, landmark regions, and a skip
  link?
- Does every control and link have a meaningful, stable accessible name, and do
  icon-only controls carry an explicit name with the icon hidden?
- Is every field labelled, with errors associated via `aria-describedby` +
  `aria-invalid`, correct `autocomplete`/`type`/`inputmode`, and late validation
  that preserves input and moves focus to the first error?
- Do `tel:`/`mailto:` links use explicit markup with action-naming text rather
  than relying on auto-detection?
- Does focus stay visible (`:focus-visible` token, not color alone), move into
  and out of dialogs/popovers correctly, and reset to the heading or `main` on SPA
  route changes?
- Are dynamic, user-unprompted changes announced via an appropriate live region,
  and silent when announcement would only add noise?
- Does each custom or composite widget implement the full role, name, value,
  state, and keyboard model, with the native input preserved underneath?
- Do contrast, target size, pointer media queries, `prefers-reduced-motion`,
  `forced-colors`, and 200%/400% zoom all pass?
- Have keyboard-only and screen-reader passes been run for every interactive
  pattern?
