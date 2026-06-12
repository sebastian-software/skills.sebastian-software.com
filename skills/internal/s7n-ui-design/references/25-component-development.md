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

### Perfectly Pointed Tooltips: A Foundation - Frontend Masters Blog

- Things ID(s): `H2vSAorpXj9royWFZTMqfZ`
- Source: <https://frontendmasters.com/blog/perfectly-pointed-tooltips-a-foundation/>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development: modern CSS Anchor Positioning tooltip/floating-ui positioning pattern using anchor-name, position-anchor, position-area, position-try-fallbacks, flip-block, and anchor(); browser support has improved to Baseline Newly available in 2026, so treat as preferred native positioning approach for suitable tooltips/popovers while still testing fallback/collision behavior and adding separate semantics, trigger, dismissal, keyboard/touch, and accessibility rules.

### Practical Accessibility Tips You Can Apply Today

- Things ID(s): `C8Z8ZDF6UyDgoymLZ5tnn6`
- Source: <https://piccalil.li/blog/practical-accessibility-tips-you-can-apply-today/?ref=main-rss-feed>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development with html-accessibility cross-reference: practical pattern guidance for accessible dropdowns/modals/controls, prefer semantic elements such as button triggers and structured option lists, use ARIA like aria-expanded/aria-controls as support rather than replacement, and ensure keyboard, screen reader, focus, and assistive-technology usability are part of component APIs and review checklists.

### Standardizing Focus Styles With CSS Custom Properties | CSS-Tricks

- Things ID(s): `PnctxHQnx7iW6p4LZBQixJ`
- Source: <https://css-tricks.com/standardizing-focus-styles-with-css-custom-properties/>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development with html-accessibility and design-system cross-references: visible focus indicators are required for interactive components; standardize outline, outline-offset, size/color/style custom properties, currentColor, max(2px, 0.08em), :focus-visible with :focus fallback, high-contrast and dark-mode considerations, and component-specific adjustments for buttons, links, inputs, textareas, and summary.

### The <select> element can now be customized with CSS | Blog | Chrome

- Things ID(s): `WMo2RNEEwqdKHFQaSvzz38`
- Source: <https://developer.chrome.com/blog/a-customizable-select?hl=en>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development with forms-ux, html-accessibility, design-system, and responsive-design cross-references: before building a custom combobox/select, evaluate native customizable select via appearance: base-select, ::picker(select), top-layer picker, anchor positioning, rich option content, internal parts/states, and unchanged JS interfaces; preserve form semantics while testing support, parsing changes, mobile OS picker tradeoffs, width behavior, and fallback strategy.

### The Undeniable Utility Of CSS :has • Josh W. Comeau

- Things ID(s): `6hP6h8HiTHQmQD7GyCmryk`
- Source: <https://www.joshwcomeau.com/css/has/?ck_subscriber_id=1866528194&utm_source=convertkit&utm_medium=email&utm_campaign=%E2%9A%9B%EF%B8%8F%20This%20Week%20In%20React%20#200:%20Remix,%20React%20Universe,%20Next.js%20dynamicIO,%20:has,%20Redwood,%20MDX,%20Atomic-CRM,%20NewArch,%20Fusebox,%20Hermes,%20Gesture%20Handler,%20TypedGPU,%20Firebase,%20Vite,%20Express,%20TypeScript,%20Rsbuild...%20-%2014977938>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development, linked to source 2 as practical :has() companion: broad parent/context/state styling tool, use :has(button:focus-visible) and other child-state selectors to keep semantic markup while styling parent containers, use @supports selector(:has(*)) fallbacks, derive UI state from focus/active/checked/data-state, update CSS variables from child state, and avoid replacing semantic children with fake interactive wrapper elements; cross-reference css-layout-responsive, design-system, and html-accessibility.

### You Want border-color: transparent, Not border: none - Frontend Mast

- Things ID(s): `NLbxB8eHs8dnQXE6hhaLUa`
- Source: <https://frontendmasters.com/blog/you-want-border-color-transparent-not-border-none/>
- Decision: `primary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Primary for component-development with html-accessibility and design-system cross-references: preserve structural border/outline affordances for interactive controls by using border-color: transparent or outline-color: transparent instead of border: none/outline: none when hiding visual borders; supports Forced Colors/High Contrast mode, control recognizability, layout stability, and focus/hover state robustness.

### Getting Creative With HTML Dialog | CSS-Tricks

- Things ID(s): `2j6fXQTkFTQk14JKU8fvQZ`
- Source: <https://css-tricks.com/getting-creative-with-html-dialog/>
- Decision: `secondary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for component-development: useful expressive styling example for native <dialog>, ::backdrop, backdrop-filter, animations, SVG/image backgrounds, and :has(input:valid) state styling; use only as visual/design-system supplement after stronger dialog semantics, focus, close, labels, and reduced-motion rules.

### Modals: Prevent Root Scrolling

- Things ID(s): `3QzcLphZTBT9z63RiEvdCG`
- Source: <https://css-tricks.com/prevent-page-scrolling-when-a-modal-is-open/>
- Decision: `secondary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for component-development: important modal/dialog problem space around preventing background/root scroll, preserving scroll position, avoiding scrollbar reflow, allowing internal modal scroll, and testing iOS Safari/touch leakage; concrete 2019 workaround should be treated as historical/caveat material and paired with current <dialog>, overscroll-behavior, scrollbar-gutter, and browser-support checks.

### Modern CSS Tooltips And Speech Bubbles (Part 1) - Smashing Magazine

- Things ID(s): `9uHi7h8Gqa9v41wbr9VvY3`
- Source: <https://www.smashingmagazine.com/2024/03/modern-css-tooltips-speech-bubbles-part1/?utm_source=CSS-Weekly&utm_medium=newsletter&utm_campaign=issue-581-march-08-2024>
- Decision: `secondary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for component-development: strong CSS shape/API craft for tooltip and speech-bubble visuals using clip-path, border-image, gradients, min()/max(), custom properties, tail position/shape, border-radius corrections, and edge-case clamping; not sufficient as primary tooltip guidance because real tooltip components also need semantics, trigger behavior, dismissal, keyboard/touch support, aria-describedby, popover/anchor positioning, overflow and collision handling.

### Onboarding mit CSS anchor

- Things ID(s): `8ssGUJ4p7WstyFjgfNKtRE`
- Source: <https://piccalil.li/links/one-of-those-onboarding-uis-with-anchor-positioning/?ref=main-rss-feed>
- Decision: `secondary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for component-development with ux-patterns/baseline cross-references: useful real-world anchor-positioning onboarding/callout pattern, but native anchor positioning is already covered by stronger primary sources and onboarding-specific UX/focus/dismissal rules need separate sources.

### Pure CSS Tabs With Details, Grid, and Subgrid | CSS-Tricks

- Things ID(s): `YazxJrDcieJVYmHyRDzrbe`
- Source: <https://css-tricks.com/pure-css-tabs-with-details-grid-and-subgrid/?ref=labnotes.org>
- Decision: `secondary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for component-development: useful progressive-enhancement pattern using details/summary, name, CSS Grid, Subgrid, and ::details-content for tab-like content organization without JS; keep as caveat/alternative because this is native disclosure behavior, not automatically a full ARIA tabs pattern with expected roles and keyboard interaction; cross-reference css-layout-responsive and html-accessibility.

### Solved by CSS: Donuts Scopes

- Things ID(s): `XMJfCxTrF3tjRU6wiLTNb9`
- Source: <https://css-tricks.com/solved-by-css-donuts-scopes/>
- Decision: `secondary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for component-development with design-system/baseline cross-references: useful @scope/donut-scope explainer for limiting parent component styles before nested content boundaries, but keep as support/context source and pair with current @scope docs before codifying rules.

### Spacer gifs

- Things ID(s): `SBC11yteQ19ob6PX9re3S5`
- Source: <https://www.joshwcomeau.com/react/modern-spacer-gif/>
- Decision: `secondary`
- Target: `component-development`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Secondary for component-development with design-system cross-reference: useful spacing-primitive argument for component architectures and optical alignment, but React-specific and partially outdated around flex gap support; use as caveat/companion to the primary gap-vs-margin source.

