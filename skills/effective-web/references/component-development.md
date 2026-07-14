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
- Derive parent/container styling from real child state with `:has()`, `:focus-visible`, `:checked`, `aria-expanded`, data attributes, or form validity instead of replacing semantic children with fake wrappers. Guard `:has()` usage with `@supports selector(:has(*))` where a fallback matters.
- Treat ARIA as support for missing semantics, not a replacement for it. Reach for `button` triggers, real option lists, and native controls first; add `aria-expanded`, `aria-controls`, and `aria-describedby` to convey state that the markup cannot, and keep keyboard, focus, and screen-reader behavior part of the component API and its review checklist.
- For floating UI, separate three decisions: trigger semantics, positioning/collision strategy, and dismissal/focus behavior. Anchor positioning can solve placement, but it does not solve accessibility by itself.
- Before building custom select, switch, accordion, dialog, tooltip, menu, tabs, or navigation, check whether current native elements plus progressive enhancement meet the requirement. Ship a usable baseline (semantic markup, reachable links, skip links, sensible focus flow) that works before JavaScript loads, and let JavaScript enhance organization rather than create the only path.
- Reach for native platform primitives that preserve semantics and replace hand-written state code, but never treat a native visual API as an accessibility shortcut. Use command/invoker attributes (`command`/`commandfor`) to cut glue JavaScript only where target browsers support them, and keep the same actions reachable through ordinary controls where support is mixed. Treat experimental primitives such as interest-triggered popovers and CSS carousels as not-yet-shippable unless the product is explicitly browser-gated; build critical hovercards and carousels with tested input, focus, and fallback behavior.
- Give interactive controls a target of at least 44x44 CSS pixels with adequate spacing between adjacent targets, independent of the visual size. Extend the hit area past small visual bounds (icon buttons, pagination, toggles), make the whole label or row part of the target, and apply Fitts's law by placing frequent actions where they are easy to reach. Expanded targets must not overlap adjacent interactive targets. Verify target sizes under touch and pointer input.
- Require a visible focus indicator on every interactive component. Standardize it through custom properties for size, color, and style; draw it with `outline` plus `outline-offset` using `currentColor` and a minimum thickness such as `max(2px, 0.08em)`; key it on `:focus-visible` with a `:focus` fallback; and verify it holds up in dark mode and forced-colors mode, adjusting per control type (button, link, input, textarea, `summary`).
- Make components adapt to content count, container width, and language length using container queries, quantity queries (`:has()` over child counts), Grid, and logical properties, with `@supports` fallbacks. Prefer these over hard-coded breakpoints, and document any remaining magic numbers as deliberate.
- Keep layout stable when overlays or state changes appear: reserve space with `scrollbar-gutter`, prevent scroll chaining with `overscroll-behavior`, and avoid layout shift from appearing/disappearing chrome rather than relying on fixed pixel offsets.
- Preserve structural affordances in high contrast mode. Hide optional borders with transparent colors (`border-color: transparent`, `outline-color: transparent`) rather than `border: none` or `outline: none`, so forced-colors mode, control recognizability, layout stability, and focus/hover states survive.
- Keep tightly nested rounded surfaces concentric when they visually form one
  shell: derive the outer radius from the inner radius plus the intervening
  inset. Apply the geometry only when spacing is even and the curves are meant
  to share a center; choose radii independently for asymmetric or clearly
  separate surfaces.
- Prefer optical alignment when mathematically centered text or icons still
  look unbalanced. Correct the source SVG `viewBox` or path when possible;
  otherwise use a small, documented local adjustment and verify it across icon
  variants, writing directions, and zoom levels.

## Component Pattern Rules

- **Buttons and links:** choose by outcome, not appearance. Buttons mutate state; links navigate. Keep `type="button"` explicit for non-submit buttons inside forms.
- **Switches and checkboxes:** keep the real input in the DOM, associate a visible label, and style from checked/focus/disabled state.
- **Accordions/disclosures:** use `details`/`summary` where the interaction model fits, and prefer this native disclosure behavior over custom open/close state. Use the shared `name` attribute on `details` for exclusive (one-open) sections, but avoid exclusive accordions when users need to compare panels. Make the whole `summary` row a target, and do not force the page to auto-scroll when a panel opens. Native disclosure plus `::details-content` and Grid can organize tab-like content without JavaScript, but it is not an ARIA tabs pattern; only add `role="tablist"` with full roving-focus keyboard behavior when those tab semantics are actually required.
- **Dialogs:** prefer native `dialog.showModal()` when suitable and rely on its built-in inertness and focus handling instead of building reflexive custom focus traps. This does not make focus management optional: still specify initial focus, focus return, Escape/close affordance, scroll locking, and the fact that background content must not receive focus, and test iframe and browser edge cases.
- **Tooltips/popovers:** use `aria-describedby` or popover semantics intentionally; support keyboard/touch dismissal and test collision, overflow, reduced motion, and viewport edges. For placement, prefer CSS Anchor Positioning (`anchor-name`, `position-anchor`, `position-area`, `position-try-fallbacks`, `anchor()`) where browser support allows, with a fallback positioning strategy; positioning is a separate concern from the trigger, dismissal, and accessibility semantics, which still must be specified.
- **Non-modal top-layer UI:** reach for the native Popover API (`popover`, `popovertarget`) for menus, teaching bubbles, and lightweight disclosures whose semantics fit, rather than hand-built top-layer state; pair it with a `button` trigger, explicit dismissal rules, and keyboard/touch checks. Use it for non-modal surfaces and keep `dialog.showModal()` for modal ones.
- **Selects/comboboxes:** evaluate the customizable native `select` (`appearance: base-select`, `::picker(select)`, rich option content) before building a custom combobox, keeping the existing form semantics and JS interface. Treat it as Limited availability until current Baseline data says otherwise, and opt in with a support-gated enhancement. Keep real text in every option; icons, swatches, and images may add meaning but must not replace the label, because unsupported browsers reduce the control to its standard text options. Test mobile OS picker behavior, fallback parsing, accessible value, width behavior, option content, hydration, and form submission.
- **Navigation:** keep a semantic nav baseline with reachable links before adding disclosure, priority-plus, or burger behavior. JS enhances organization; it should not create the only path.
- **Treeviews and nested lists:** reserve affordance space, calculate indentation through CSS variables/logical properties, and support LTR/RTL without fragile selector chains.

## Review Checklist

- Does the component still work with no JavaScript or with delayed JavaScript where that is reasonable?
- Are visual states connected to real semantic state rather than duplicate hidden state?
- Can the component be translated, zoomed, used with touch, used with keyboard, and used in forced-colors mode?
- Does the parent layout control external spacing while the component controls only its internal rhythm?
- Do tightly nested radii remain concentric where the surfaces form one shell,
  and are asymmetric surfaces allowed to use independent geometry?
- Are visibly asymmetric icons optically aligned at the source or through a
  small documented adjustment that survives variants and RTL?
- Are optional visual effects, animation, and masking removable without losing meaning?
- Do interactive targets meet the 44x44 pixel minimum without overlap and with adequate spacing, and does every focusable element show a visible `:focus-visible` indicator in light, dark, and forced-colors modes?
- Are the component's escape hatches documented: slots, `className`, CSS variables, data attributes, refs, and event callbacks?
