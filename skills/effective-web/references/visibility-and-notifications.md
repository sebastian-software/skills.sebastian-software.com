# Visibility, Discoverability, and Notifications

Hidden is not one state. Decide independently whether content should be
painted, occupy layout, appear in the accessibility tree, receive focus,
accept interaction, and remain discoverable through find-in-page. Then choose a
mechanism whose behavior matches all of those decisions.

## Start with the intended state

Before hiding or disabling anything, answer:

- Should sighted users see it now?
- Should screen-reader users encounter it now?
- Should keyboard or pointer users operate it now?
- Should it occupy layout or preserve a transition surface?
- Should browser find-in-page be able to reveal it?
- Is it temporarily unavailable, permanently irrelevant, or merely visually
  de-emphasized?

Do not compensate for a mismatched mechanism by stacking `aria-hidden`,
`tabindex`, `pointer-events`, and off-screen CSS until one tested path appears to
work. Align visual, accessibility-tree, focus, and interaction state at the
component boundary.

## Choose a mechanism by behavior

| Mechanism | Visual/layout effect | Accessibility and interaction effect | Use and caution |
| --- | --- | --- | --- |
| `hidden` or `display: none` | Not painted; no layout box | Removed from accessibility tree and sequential focus | Use for content that is unavailable to everyone. It also prevents normal find-in-page discovery. |
| `visibility: hidden` | Not painted; layout space remains | Normally removed from accessibility tree and focus | Useful when layout must remain stable; verify transitions do not expose descendants early. |
| `opacity: 0` | Invisible; layout remains | Still exposed and operable unless separately controlled | Never use alone to hide controls. Invisible focus targets remain reachable. |
| Visually-hidden CSS | Not visibly painted in normal layout | Remains available to assistive tech | Use for real labels or instructions that should be nonvisual, not for content that sighted keyboard users also need. Reveal focusable skip links on focus. |
| `inert` | No inherent visual change | Removes a subtree from focus and interaction and, in current implementations, the accessibility tree | Use for inactive page regions such as the background behind a modal. Pair it with the intended visual treatment and restore it atomically. |
| Native `disabled` | Browser-dependent disabled styling | Prevents activation and usually removes form controls from sequential focus and submission | Use for genuinely unavailable native controls. Explain why when the reason is not obvious; do not disable a submit button merely to avoid showing validation. |
| `aria-disabled="true"` | No inherent visual change | Announces disabled but does not prevent focus or activation | Use when a discoverable, focusable unavailable control is intentional. Suppress its action and style it consistently. |
| `tabindex="-1"` | No visual change | Removes an element from sequential focus but still permits programmatic focus | Use for focus destinations, not as a general hiding tool. It does not remove semantics or pointer operation. |
| `aria-hidden="true"` | No visual change | Removes a subtree from the accessibility tree | Use only for redundant or decorative content with no focusable descendants. Never place it on an ancestor of the focused element. |
| `role="none"` / `presentation` | No visual change | Removes an element's semantic role, not its content; required owned elements (table rows/cells, list items) also become presentational | Use only when the wrapper's native semantics are genuinely unwanted. It does not hide content. |
| `hidden="until-found"` | Hidden until browser search or fragment navigation reveals it | Support and accessibility exposure vary by platform | Consider for searchable collapsed content only after support and fallback testing; synchronize the component's visible and ARIA state when `beforematch` fires. |

CSS clipping recipes for visually hidden text must remain robust at zoom and in
forced-colors modes. Prefer the project's established utility, and test any
focusable use in the rendered page rather than copying a snippet blindly.

## Disclosures, drawers, and modal surfaces

- A non-modal disclosure keeps the rest of the page interactive. Hide its closed
  content consistently and update the trigger's `aria-expanded` state.
- A modal dialog or navigation drawer blocks the background. Move focus into
  the surface, keep focus within it while modal, make a visible close action
  available, close on Escape, make the background inert, and return focus to
  the opener.
- Do not call a drawer modal while leaving page controls focusable behind it.
- When responsive CSS changes a mobile drawer into persistent desktop
  navigation, clear obsolete inline hidden, inert, scroll-lock, and
  `aria-expanded` state. Test the breakpoint transition while the drawer is
  open.
- Preserve a no-JavaScript path for essential site navigation. If script creates
  the disclosure behavior, the underlying link list should remain available
  when enhancement fails.

## Searchable collapsed content

Collapsed FAQs, accordions, and long navigation trees can make browser
find-in-page report no match even though the page contains the answer. Treat
searchability as a product requirement, not an incidental browser behavior.

- Prefer native `details`/`summary` when its interaction and styling fit.
- If matching content must open automatically, evaluate `hidden="until-found"`
  and `beforematch` against the real support matrix. On reveal, update the
  disclosure state and expose the same visual result as a user activation.
- Provide a coherent fallback for browsers without the feature, such as keeping
  important reference content expanded or offering a page-level search that
  opens the matching section.
- Test fragment links, browser find, screen-reader navigation, printing, and
  restored history state. Each can reveal a different stale-state bug.

## Prefer state and focus before announcements

Dynamic UI does not automatically need a live region. First ask whether the
change is already conveyed by:

- focus moving to the new content;
- the focused control's native or ARIA state changing;
- normal document content the user will encounter next; or
- a semantic element such as `progress`, a dialog heading, or an inline error.

Add an announcement when users would otherwise miss an important asynchronous
change. Examples include a background save result, changed search-result count,
expired session warning, or error that appears away from focus.

## Build live regions conservatively

- Keep a small number of stable live-region containers in the initial DOM, then
  update their text. Creating a region and its populated content together is
  unreliable.
- Use `role="status"` or `aria-live="polite"` for non-urgent updates. Use
  `role="alert"` or assertive announcements only for time-sensitive failures or
  hazards that justify interruption.
- Announce one short, actionable message. Coalesce rapid updates such as stream
  tokens, progress ticks, search keystrokes, or repeated saves.
- Keep controls, links, headings, lists, and rich recovery UI outside a live
  region. Announce a concise result, then move focus or provide normal DOM
  structure for interaction.
- Use `aria-atomic="true"` only when the whole message must be spoken after each
  change. Use `aria-relevant` sparingly; broad settings can create duplicate or
  verbose output.
- Mark a changing region `aria-busy="true"` only while its update is incomplete,
  then clear it. Do not leave a subtree permanently busy.
- Preserve the page language and avoid duplicate narration from overlapping
  alerts, descriptions, focus changes, and live regions.
- Do not clear a message so quickly that users cannot review it visually or in
  assistive-technology history.

## Verify the real state matrix

Test open, closed, loading, error, disabled, and responsive-transition states
with:

1. CSS disabled or failed when progressive enhancement matters.
2. Keyboard navigation and visible focus.
3. The accessibility tree, including hidden descendants and current state.
4. Browser find-in-page and fragment navigation when content is collapsible.
5. At least one representative screen-reader/browser pairing for live regions
   and modal focus.
6. Zoom, text resize, forced colors, and reduced motion where hiding or
   transitions affect comprehension.
