# Component API Design

A component's prop surface is its contract. Design it so composition, state,
styling, and semantics stay predictable as the component is reused in contexts
the author never saw. Separate three concerns deliberately: layout (what the
component renders), behavior (what it does), and extension points (how consumers
change it). Mixing them produces props that contradict each other.

## Working Rules

### Prop surface

- Model the smallest prop set that expresses the contract. Keep semantic
  booleans such as `disabled`, `required`, and `loading` when the state is truly
  binary, but resist a boolean per visual mode. Collapse mutually exclusive
  modes into one union prop
  (`variant="primary" | "secondary" | "ghost"`) so impossible combinations
  cannot be typed.
- Name props for intent, not implementation: `tone`, `size`, `loading`,
  `selected` — not `isRed` or `flexDirection`. Names outlive the current CSS.
- Default every optional prop to the safest behavior. A component rendered with
  no props should be accessible and non-destructive.
- Reserve `children` for content the consumer owns. Pass structured data
  (options, columns, items) as typed props, not as parsed children, so the type
  system validates them.
- Forward unknown DOM props (`...rest`) onto the underlying element for one
  primitive root only, after your own props are destructured, so consumers can
  set `id`, `aria-*`, `data-*`, and event handlers without an API change. Never
  spread rest onto multiple elements — the target becomes ambiguous.

### Controlled, uncontrolled, and callbacks

- Decide ownership before writing JSX: fully controlled (`value` + `onChange`),
  uncontrolled (`defaultValue`, internal state), or both. Do not silently switch
  a component between the two across renders — going from `undefined` to a
  defined `value` flips React's mode and warns.
- For dual-mode primitives, treat `value !== undefined` as the controlled
  signal, fall back to internal state otherwise, and always fire the change
  callback in both modes so a controlled parent stays in sync.
- Give callbacks verb-noun names tied to the event (`onSelectionChange`,
  `onOpenChange`), pass the new value as the first argument, and call them after
  internal state updates so consumers read consistent state.

### State provider contracts

- For a composed component whose controls, content, and external siblings share
  behavior, define a small provider contract around `state`, `actions`, and
  optional `meta`. Let UI components consume that contract rather than importing
  one store, form library, router, or data-fetching implementation directly.
- Keep the provider as the only layer that knows whether state is local,
  controlled, URL-owned, form-owned, or backed by an external store. Different
  providers may implement the same contract while the compound UI remains
  unchanged.
- Lift state far enough that sibling controls and custom composition can access
  it, but no farther. Do not use a wide context for high-frequency values merely
  to avoid passing a focused prop.
- Split state and dispatch contexts when consumers that only invoke actions
  should not re-render for every value change. Keep context values referentially
  stable and measure before adding abstraction.
- Use explicit variant components when modes have materially different structure
  or contracts (`CompactDialog`, `ConfirmationDialog`) instead of accumulating
  flags on one monolith. Share internal primitives so variants do not fork
  behavior or accessibility.

### Polymorphism and semantic safety

- Add an `as`/`asChild` prop only when the semantic element legitimately varies
  (a `Button` that is sometimes a link). Do not add it for styling reuse — that
  is what shared classes and tokens are for.
- Constrain a polymorphic `as` to a typed allowlist, not `keyof JSX.IntrinsicElements`.
  Permit `button` and `a`; never permit `div` or `span` as an interactive
  element — a clickable `div` has no role, no keyboard activation, and no focus,
  and breaks the component's accessibility contract.
- When the element changes, change the contract with it: a link variant needs
  `href` and drops `type`/`disabled`/`onClick`-as-submit; a button variant needs
  `type` and real `disabled`. Make these mutually exclusive in the types
  (discriminated union on `as`) so consumers cannot pass `href` to a `button`.
- Prefer Radix-style `asChild` (merge props onto a single child via `Slot`) over
  rendering an extra wrapper element when the goal is to preserve the consumer's
  own semantic node.
- Type the polymorphic ref so `ref` matches the rendered element
  (`HTMLAnchorElement` vs `HTMLButtonElement`); a mistyped ref hides real focus
  and measurement bugs.

### Composition and slots

- Prefer compound components (`Menu`, `Menu.Item`, `Menu.Trigger`) sharing state
  through context over one component with dozens of configuration props. The
  consumer composes the layout; the component owns the behavior.
- Expose named slots as props (`startIcon`, `action`, `header`) when placement is
  fixed, and `children` when the consumer controls order. Render `null`-safe:
  omit the slot's wrapper element entirely when its prop is absent so empty
  containers do not affect layout or screen-reader output.
- Keep extension points additive. Adding a slot or an optional prop must not
  change existing render output; that is what keeps the component reusable.

### Styling hooks

- Let consumers restyle without knowing the internal DOM: accept `className` (and
  `style`) on the root, expose `data-*` state attributes (`data-state="open"`,
  `data-loading`) for state-based styling, and expose CSS custom properties for
  themeable values. Do not require consumers to target generated class names or
  nth-child selectors.
- Merge incoming `className` with internal classes rather than replacing them, so
  a consumer override augments instead of silently deleting base styles.

### Interaction primitives

- When a component adds a gesture (swipe-to-action, drag-to-reorder, long-press),
  ship a non-gesture equivalent in the same API: a visible button for every
  swipe action, a keyboard path for every drag. The gesture is an enhancement,
  never the only route to the behavior.
- Gate motion-based affordances on `prefers-reduced-motion` and make destructive
  gesture actions (swipe-to-delete) recoverable with confirmation or undo, since
  gestures are easy to trigger by accident.

### Preserve semantics through the API

- Render the correct native element underneath regardless of how the component is
  styled: a `Button` is a `<button>`, a toggle is a real `checkbox`/`switch`
  role, a navigation list is a `<nav>` with a list. Styling must never downgrade
  an element to a generic `div`.
- Surface accessibility props in the public API (`aria-label`,
  `aria-labelledby`, `aria-describedby`) so consumers can name a component the
  page-specific way; do not bury the only label in an internal default.

## Review checklist

- Is each prop justified, intent-named, and impossible-combination-proof via
  unions rather than parallel booleans?
- Is controlled vs uncontrolled mode fixed for the component's lifetime, with the
  change callback firing in both modes?
- Is shared state exposed through the smallest stable provider contract without
  coupling UI to one state implementation or broadcasting hot state too widely?
- Are materially different modes explicit variants rather than contradictory
  boolean combinations, while genuine binary semantics remain booleans?
- Is `as`/`asChild` restricted to genuine semantic variation, with a typed
  element allowlist that excludes interactive `div`s and a per-element contract?
- Does the polymorphic `ref` type match the rendered element?
- Can a consumer restyle and rename via `className`, `data-*`, CSS variables, and
  `aria-*` without touching internal DOM?
- Does every gesture have a keyboard/button equivalent, reduced-motion handling,
  and undo for destructive actions?
- Does the rendered native element keep its correct role under every variant?
