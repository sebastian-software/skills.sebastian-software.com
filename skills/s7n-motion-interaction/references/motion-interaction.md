# Motion Interaction

Use motion to explain state change, spatial continuity, feedback, and progress. Every animation must carry meaning: where something came from, where it went, what changed, or that the system is working. Remove decorative motion that delays task completion or makes layout harder to understand.

## Reduced Motion First

- Treat `prefers-reduced-motion: reduce` as the baseline, not an afterthought. Author the static, non-animated experience first, then add motion inside `@media (prefers-reduced-motion: no-preference)`.
- Never remove information when motion is disabled. A reduced-motion fallback must still show the final state, the new content, and any feedback — replace movement with an instant change or a subtle opacity cross-fade, not with nothing.
- Mirror the CSS check in JavaScript with `window.matchMedia('(prefers-reduced-motion: reduce)').matches` before triggering `scrollIntoView`, `animate()`, or library-driven motion, and listen for changes so the preference can flip at runtime.
- Distinguish essential from non-essential motion. Motion that conveys state (a spinner, a progress bar) may continue under reduced motion; large translational, parallax, zoom, and auto-playing motion must be suppressed because it triggers vestibular discomfort.

## Performance-Safe Properties

- Animate only `transform` and `opacity` for movement, scaling, and fades. These run on the compositor and avoid layout and paint on every frame.
- Never animate layout-affecting properties (`width`, `height`, `top`, `left`, `margin`, `padding`) in task surfaces — they force synchronous layout (layout thrash) and drop frames. Use `transform: translate()` / `scale()` instead.
- Promote an element to its own layer with `will-change: transform` only for the duration of an animation, then remove it; leaving `will-change` set permanently wastes memory.
- Read layout values (`offsetWidth`, `getBoundingClientRect`) before writing styles within a frame, never interleaved, to avoid forced reflow. Batch reads and writes (or use `requestAnimationFrame`) when measuring for JS-driven motion.
- Keep product UI transitions short — roughly 150–250ms for state changes and micro-interactions; reserve longer durations only for large spatial moves. Motion must never make the user wait for choreography or hide real latency.
- Use ease-out curves for elements entering and responding to user input (fast start, gentle settle) and ease-in for elements leaving. Reserve spring or overshoot easing for playful, non-blocking accents; never apply bouncy springs to functional, frequently repeated transitions.

## Transitions vs Animations

- Prefer CSS `transition` for simple, reversible state changes driven by a class, attribute, or pseudo-class (`:hover`, `[data-open]`, `[aria-expanded]`). Transitions are naturally interruptible — the browser retargets smoothly when the state flips mid-flight.
- Use CSS `@keyframes` animations for multi-step, looping, or self-starting motion (loaders, attention pulses, entry sequences). Omit intermediate keyframes you do not need — partial keyframes (only `from`/`to`, or a single `50%`) keep motion bounded and let the browser interpolate the rest.
- Make every animation interruptible. User input must be able to cancel, reverse, or retarget an in-progress animation; never block interaction while motion plays. For JS-driven motion, hold the `Animation` object so it can be `cancel()`ed or reversed.

## Entry and Exit Animations

- Animate elements entering the top layer (dialogs, popovers, `[popover]`, `details`) from a hidden or `display: none` state using `@starting-style` together with `transition`, which defines the styles to transition *from* on first render. Support is recent (Chrome/Edge 117+, Safari 17.5+, Firefox 129+); the transition is simply skipped where unsupported, so treat it as progressive enhancement.
- Transition an element to or from `display: none` by including `display` and `overlay` in the `transition-property` list and using `transition-behavior: allow-discrete`, so the element stays visible through its exit animation before being removed.
- Animate height to or from `auto` only with the modern intrinsic-size sizing keywords (`interpolate-size: allow-keywords` on a root, or `calc-size()`); this is Chromium-only at present, so provide a fixed-height or cross-fade fallback elsewhere. Do not fake auto-height growth by animating `max-height` to a guessed pixel value — it produces eased delays and clipping.

## View Transitions

- Use the View Transitions API for spatial continuity across state changes: list-to-detail, filtering and reordering, and persistent UI that should appear to stay put. For same-document (SPA) transitions, wrap the DOM update in `document.startViewTransition(updateCallback)`; for cross-document (MPA) transitions, opt in with `@view-transition { navigation: auto; }` in CSS on both pages.
- Tag elements that should animate between states with a unique `view-transition-name` (or `view-transition-class` for groups). Two elements sharing a name in the old and new state are matched and tweened as one — this is how a thumbnail expands into a hero image.
- Always guard view transitions with reduced motion: wrap the snapshot pseudo-element animations in `@media (prefers-reduced-motion: no-preference)`, or skip `startViewTransition` and apply the DOM change directly when the user prefers reduced motion. Without a guard the default cross-fade still animates.
- View Transitions support is uneven (same-document is broadly available in Chromium and Safari; cross-document and Firefox lag). Feature-detect with `if (document.startViewTransition)` and fall back to an instant, un-animated update — the content change must work without the transition.
- Customise the snapshot animation via the `::view-transition-group()`, `::view-transition-old()`, and `::view-transition-new()` pseudo-elements rather than animating real DOM nodes; the snapshots run on the compositor.

## Scroll-Driven and Spatial Motion

- Prefer native CSS scroll-driven animations (`animation-timeline: scroll()` / `view()`) over JavaScript scroll listeners; they run off the main thread and cannot jank. See [scroll-patterns.md](scroll-patterns.md) for ranges, the `animation`-shorthand ordering rule, and required `@supports` / reduced-motion guards.
- Reach for a JavaScript animation library (GSAP, Motion) only when a behaviour genuinely exceeds CSS — coordinated timelines, physics, or FLIP measurements. Do not adopt a library as a blanket replacement for transitions or scroll-driven animations that the platform already handles.
- When animating color (state, theme, or accent shifts), keep text and its background within contrast requirements at every frame, not only at the endpoints, and suppress purely decorative color cycling under reduced motion.

## State Continuity

- Preserve focus, scroll position, URL state, and semantic navigation when adding page or component transitions. A transition must never strand keyboard focus, reset the scroll position unexpectedly, or replace a real navigation with a non-semantic animation.
- Do not gate content behind hover or scroll: information must be reachable without a pointer hover and without triggering a scroll effect, so keyboard, touch, and assistive-technology users get the same content.

## Review Checklist

- Does every animation convey meaning (feedback, state, orientation, continuity), and would removing it lose nothing for the user's task?
- Is there a `prefers-reduced-motion: reduce` path that still shows the final state and all feedback without large or translational motion?
- Are only `transform` and `opacity` animated on hot paths, with no layout-property animation causing reflow?
- Are durations short (≈150–250ms for UI state) and the easing appropriate (ease-out in, ease-in out)?
- Can every in-progress animation be interrupted, reversed, or cancelled by user input?
- Are View Transitions and scroll-driven animations feature-detected, reduced-motion-guarded, and functional when unsupported?
- Do transitions preserve focus, scroll position, URL state, and semantic navigation?
