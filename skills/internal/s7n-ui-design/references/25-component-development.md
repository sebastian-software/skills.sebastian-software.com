# Component Development

Build components as durable interface primitives: semantic DOM first, clear state surfaces, predictable layout ownership, resilient focus behavior, and configurable CSS APIs.

## Working Rules

- Preserve native controls and semantics whenever possible.
- Separate component internals from parent layout; component internals may use `gap`, while outer layout owns spacing between components.
- Expose state through real DOM state, attributes, data attributes, and custom properties instead of hidden implementation details.
- Define disabled, loading, empty, error, success, hover, focus, active, reduced-motion, high-contrast, and translated-text behavior.
- Keep component APIs portable across plain HTML/CSS, React, and Web Components unless framework specifics are required.

## Source-Backed Guidance

### Build a fully-responsive, progressively enhanced burger menu - Picca

- Things ID(s): `AXsJMeRBGH82pzPNZYg7ng`
- Source: <https://piccalil.li/blog/build-a-fully-responsive-progressively-enhanced-burger-menu>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://piccalil.li/blog/build-a-fully-responsive-progressively-enhanced-burger-menu/
- Guidance: Primary for framework-agnostic component-development: progressive responsive navigation/disclosure, semantic nav baseline, skip links, focus flow, minimum viable experience, and JS as enhancement rather than replacement.

### Building Low Level Components the Radix Way | Alex Kondov - Software

- Things ID(s): `96XkrXULWNjnRvUThPRtxW`
- Source: <https://alexkondov.com/building-low-level-components-the-radix-way/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F+This+Week+In+React+%23160%3A+Remix%2C+Next.js%2C+Expo+API+Routes%2C+Ladle%2C+MDXEditor%2C+Sonner%2C+Docusaurus%2C+AbortController%2C+Query+String%2C+Menubar%2C+VisionCamera%2C+Victory+Native+XL%2C+Bun%2C+ESLint%2C+TC39...%20-%2011844219>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for framework-agnostic component-development: low-level primitives, composable APIs, unstyled accessible components, DOM/data-attribute state, controlled/uncontrolled state, and maintainable layering; not React-specific.

### Designing better target sizes

- Things ID(s): `4Vm7AWykJqnAWxAcSfg5Tb`
- Source: <https://ishadeed.com/article/target-size>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200, redirects to https://ishadeed.com/article/target-size/
- Guidance: Primary for component-development with html-accessibility and ux-patterns cross-references: target size, hit area vs visual size, spacing between targets, Fitts law, multi-input/touch contexts, labels as target areas, icon buttons, navigation, pagination, and target-size testing.

### Designing The Perfect Accordion - Smashing Magazine

- Things ID(s): `QZwsfzjQmjciUPm5WbwrZV`
- Source: <https://www.smashingmagazine.com/2017/06/designing-perfect-accordion-checklist/>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development: durable accordion/disclosure interaction rules, icon semantics and position, whole-row target behavior, 44x44 touch target, link vs expand recovery, avoid forced auto-scroll, multi-open vs single-open state, and navigation/FAQ/table-detail variants; cross-reference ux-patterns and html-accessibility.

### Exklusives Akkordeon | CSS and UI | Chrome for Developers

- Things ID(s): `9p2RqJ1yNp1DAqKmCvEQea`
- Source: <https://developer.chrome.com/docs/css-ui/exclusive-accordion?hl=de>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary as technical companion to the Smashing accordion pattern source: use native <details name> for exclusive accordion behavior when only one panel should be open, prefer browser semantics over custom state logic, note browser-support/polyfill considerations, and keep the UX caveat that exclusive accordions can hurt comparison/scanning.

### Focus Trap

- Things ID(s): `X9zy2neGFJotVMNt1neCNi`
- Source: <https://css-tricks.com/there-is-no-need-to-trap-focus-on-a-dialog-element/>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development: prefer native <dialog> with showModal() where appropriate, understand built-in inertness/focus behavior, avoid reflexive custom JS focus traps, but still specify/test initial focus, focus return, close/Escape behavior, background content not receiving page focus, iframe/browser edge cases, and the caveat that this does not mean focus management is optional.

### Gap is the new Margin - Frontend Masters Boost

- Things ID(s): `CyyuZUhVNNfkz7RXcrhpJV`
- Source: <https://frontendmasters.com/blog/gap-is-the-new-margin/>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development with design-system/css-layout-responsive cross-references: component internals should avoid leaking external margins; parent layouts should own inter-component spacing through gap/stack/grid utilities, while margin remains a deliberate content-flow tool.

### Handling The Indentation of a Treeview Component

- Things ID(s): `3rQzahG5KHnXKhJufrcC45`
- Source: <https://ishadeed.com/article/tree-view-css-indent/>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development with css-layout-responsive/i18n cross-references: treeview indentation is component layout logic; reserve affordance/toggle space, calculate nesting per item, support LTR/RTL, and prefer robust CSS variables/math over fragile parent-child selector chains.

### How I build a button component

- Things ID(s): `9xPV5LuXs2FaoCAzNAKvsd`
- Source: <https://piccalil.li/blog/how-i-build-a-button-component/?ref=main-rss-feed>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development: framework-agnostic button component craft, preserve native <button> semantics, type/state/disabled/focus handling, inline-flex/icon gap/padding/border/radius structure, explicit hover/contrast colors, custom properties as configurable CSS API, and controlled variant complexity; cross-reference design-system, html-accessibility, and forms-ux.

### Making content-aware components using CSS :has(), grid, and quantity

- Things ID(s): `D345npubf7a86csT1rb61q`
- Source: <https://piccalil.li/blog/making-content-aware-components-using-css-has-grid-and-quantity-queries/?ref=main-rss-feed>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development with css-layout-responsive/design-system/i18n cross-references: components should adapt to content count, container width, and language length using :has(), quantity queries, Grid, container queries, @supports fallbacks, logical properties, and explicit magic-number caveats.

