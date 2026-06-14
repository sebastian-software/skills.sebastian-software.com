# Component Development

Build components as durable interface primitives: semantic DOM first, clear state surfaces, predictable layout ownership, resilient focus behavior, and configurable CSS APIs.

## Working Rules

- Preserve native controls and semantics whenever possible.
- Separate component internals from parent layout; component internals may use `gap`, while outer layout owns spacing between components.
- Expose state through real DOM state, attributes, data attributes, and custom properties instead of hidden implementation details.
- Define disabled, loading, empty, error, success, hover, focus, active, reduced-motion, high-contrast, and translated-text behavior.
- Keep component APIs portable across plain HTML/CSS, React, and Web Components unless framework specifics are required.
- Use low-level primitives for behavior and composition; keep visual styling and app-specific policy layered above them.
- Prefer configurable CSS APIs over prop explosions: custom properties, data attributes, parts/slots, and semantic child structure scale better than many one-off visual props.
- Derive parent/container styling from real child state with `:has()`, `:focus-visible`, `:checked`, `aria-expanded`, data attributes, or form validity instead of replacing semantic children with fake wrappers.
- For floating UI, separate three decisions: trigger semantics, positioning/collision strategy, and dismissal/focus behavior. Anchor positioning can solve placement, but it does not solve accessibility by itself.
- Before building custom select, switch, accordion, dialog, tooltip, menu, tabs, or navigation, check whether current native elements plus progressive enhancement meet the requirement.
- Preserve structural affordances in high contrast mode. Hide optional borders with transparent colors rather than deleting borders/outlines that carry layout or recognizability.

## Component Pattern Rules

- **Buttons and links:** choose by outcome, not appearance. Buttons mutate state; links navigate. Keep `type="button"` explicit for non-submit buttons inside forms.
- **Switches and checkboxes:** keep the real input in the DOM, associate a visible label, and style from checked/focus/disabled state.
- **Accordions/disclosures:** use `details`/`summary` where the interaction model fits; consider `details name` for exclusive sections, but avoid exclusive accordions when users need comparison.
- **Dialogs:** prefer native `dialog.showModal()` when suitable; still specify initial focus, focus return, Escape/close affordance, scroll locking, and background interaction behavior.
- **Tooltips/popovers:** use `aria-describedby` or popover semantics intentionally; support keyboard/touch dismissal and test collision, overflow, reduced motion, and viewport edges.
- **Selects/comboboxes:** evaluate customizable native `select` before custom comboboxes; test mobile picker behavior, fallback parsing, width, option content, and form submission.
- **Navigation:** keep a semantic nav baseline with reachable links before adding disclosure, priority-plus, or burger behavior. JS enhances organization; it should not create the only path.
- **Treeviews and nested lists:** reserve affordance space, calculate indentation through CSS variables/logical properties, and support LTR/RTL without fragile selector chains.

## Review Checklist

- Does the component still work with no JavaScript or with delayed JavaScript where that is reasonable?
- Are visual states connected to real semantic state rather than duplicate hidden state?
- Can the component be translated, zoomed, used with touch, used with keyboard, and used in forced-colors mode?
- Does the parent layout control external spacing while the component controls only its internal rhythm?
- Are optional visual effects, animation, and masking removable without losing meaning?
- Are the component's escape hatches documented: slots, `className`, CSS variables, data attributes, refs, and event callbacks?

## Additional Rules

- Progressive responsive navigation/disclosure, semantic nav baseline, skip links, focus flow, minimum viable experience, and JS as enhancement rather than replacement.
- Low-level primitives, composable APIs, unstyled accessible components, DOM/data-attribute state, controlled/uncontrolled state, and maintainable layering; not React-specific.
- Target size, hit area vs visual size, spacing between targets, Fitts law, multi-input/touch contexts, labels as target areas, icon buttons, navigation, pagination, and target-size testing.
- Accordion/disclosure interaction rules, icon semantics and position, whole-row target behavior, 44x44 touch target, link vs expand recovery, avoid forced auto-scroll, multi-open vs single-open state, and navigation/FAQ/table-detail variants; connect to ux-patterns and html-accessibility.
- Use native <details name> for exclusive accordion behavior when only one panel should be open, prefer browser semantics over custom state logic, note browser-support/polyfill considerations, and keep the UX caveat that exclusive accordions can hurt comparison/scanning.
- Prefer native <dialog> with showModal() where appropriate, understand built-in inertness/focus behavior, avoid reflexive custom JS focus traps, but still specify/test initial focus, focus return, close/Escape behavior, background content not receiving page focus, iframe/browser edge cases, and the caveat that this does not mean focus management is optional.
- Component internals should avoid leaking external margins; parent layouts should own inter-component spacing through gap/stack/grid utilities, while margin remains a deliberate content-flow tool.
- Treeview indentation is component layout logic; reserve affordance/toggle space, calculate nesting per item, support LTR/RTL, and prefer robust CSS variables/math over fragile parent-child selector chains.
- Framework-agnostic button component craft, preserve native <button> semantics, type/state/disabled/focus handling, inline-flex/icon gap/padding/border/radius structure, explicit hover/contrast colors, custom properties as configurable CSS API, and controlled variant complexity; connect to design-system, html-accessibility, and forms-ux.
- Components should adapt to content count, container width, and language length using :has(), quantity queries, Grid, container queries, @supports fallbacks, logical properties, and explicit magic-number caveats.
- Modern CSS Anchor Positioning tooltip/floating-ui positioning pattern using anchor-name, position-anchor, position-area, position-try-fallbacks, flip-block, and anchor(); browser support has improved to Baseline Newly available in 2026, so treat as preferred native positioning approach for suitable tooltips/popovers while still testing fallback/collision behavior and adding separate semantics, trigger, dismissal, keyboard/touch, and accessibility rules.
- Pattern guidance for accessible dropdowns/modals/controls, prefer semantic elements such as button triggers and structured option lists, use ARIA like aria-expanded/aria-controls as support rather than replacement, and ensure keyboard, screen reader, focus, and assistive-technology usability are part of component APIs and review checklists.
- Visible focus indicators are required for interactive components; standardize outline, outline-offset, size/color/style custom properties, currentColor, max(2px, 0.08em), :focus-visible with :focus fallback, high-contrast and dark-mode considerations, and component-specific adjustments for buttons, links, inputs, textareas, and summary.
- Before building a custom combobox/select, evaluate native customizable select via appearance: base-select, ::picker(select), top-layer picker, anchor positioning, rich option content, internal parts/states, and unchanged JS interfaces; preserve form semantics while testing support, parsing changes, mobile OS picker tradeoffs, width behavior, and fallback strategy.
- Has() companion: broad parent/context/state styling tool, use :has(button:focus-visible) and other child-state selectors to keep semantic markup while styling parent containers, use @supports selector(:has(*)) fallbacks, derive UI state from focus/active/checked/data-state, update CSS variables from child state, and avoid replacing semantic children with fake interactive wrapper elements; connect to css-layout-responsive, design-system, and html-accessibility.
- Preserve structural border/outline affordances for interactive controls by using border-color: transparent or outline-color: transparent instead of border: none/outline: none when hiding visual borders; supports Forced Colors/High Contrast mode, control recognizability, layout stability, and focus/hover state robustness.
- Expressive styling example for native <dialog>, ::backdrop, backdrop-filter, animations, SVG/image backgrounds, and :has(input:valid) state styling; use only as visual/design-system supplement after stronger dialog semantics, focus, close, labels, and reduced-motion rules.
- Important modal/dialog problem space around preventing background/root scroll, preserving scroll position, avoiding scrollbar reflow, allowing internal modal scroll, and testing iOS Safari/touch leakage; concrete 2019 workaround should be treated as historical/caveat material and paired with current <dialog>, overscroll-behavior, scrollbar-gutter, and browser-support checks.
- Strong CSS shape/API craft for tooltip and speech-bubble visuals using clip-path, border-image, gradients, min()/max(), custom properties, tail position/shape, border-radius corrections, and edge-case clamping; not sufficient as tooltip guidance because real tooltip components also need semantics, trigger behavior, dismissal, keyboard/touch support, aria-describedby, popover/anchor positioning, overflow and collision handling.
- Real-world anchor-positioning onboarding/callout pattern, but native anchor positioning is already covered by stronger sources and onboarding-specific UX/focus/dismissal rules need separate sources.
- Progressive-enhancement pattern using details/summary, name, CSS Grid, Subgrid, and ::details-content for tab-like content organization without JS; keep as caveat/alternative because this is native disclosure behavior, not automatically a full ARIA tabs pattern with expected roles and keyboard interaction; connect to css-layout-responsive and html-accessibility.
- @scope/donut-scope explainer for limiting parent component styles before nested content boundaries, but keep as support/context guidance and pair with current @scope docs before codifying rules.
- Spacing-primitive argument for component architectures and optical alignment, but React-specific and partially outdated around flex gap support; use as caveat/companion to the gap-vs-margin guidance.
- Historical/practical SSR caveat guidance for Web Components in Next or similar frameworks, but framework behavior and web component SSR options have shifted enough that rules need current sources before codification.
- Use built-in-elements-with-web-components for progressive enhancement and platform component caveats.
- Use no-UI-framework as component/platform decision context.
