# Animation Runtime Performance

Use this reference when motion, canvas, WebGL, physics, media, timers, or
observers create jank, sustained CPU or GPU load, memory growth, battery drain,
or route-lifecycle leaks. Measure the running experience; screenshots and a
successful build cannot prove that background work stopped.

## Establish the Runtime Baseline

1. Open the exact route and state that exhibits the problem.
2. Sample the top, middle, and lower page plus a representative narrow viewport
   when layout changes which effects exist.
3. Separate the work by execution model:
   - CSS transitions, keyframes, and animated pseudo-elements;
   - Web Animations or library timelines;
   - `requestAnimationFrame` loops for canvas, WebGL, or simulation;
   - timers, observers, media, workers, and asynchronous loaders.
4. Record visible and offscreen activity separately. A paused CSS animation
   says nothing about a JavaScript render loop.
5. For suspected leaks, take a bounded idle sample and repeat the shortest
   meaningful route or mount/unmount cycle. Record DOM, canvas, image, iframe,
   listener, observer, and exposed heap evidence when the environment supports
   it. Treat unavailable heap data as unknown, not as proof of safety.

Keep probes bounded. A crashed tab is evidence of overload, but it does not
identify the cause without a smaller reproduction.

## Stop Work at the Owning Lifecycle

- Pause decorative CSS animation when its owning region is offscreen. Include
  animated `::before` and `::after` content when relevant.
- Gate canvas, WebGL, and simulation loops directly. Cancel the active frame
  offscreen or on unmount, resume deliberately on re-entry, and cap elapsed
  frame time so a resumed simulation does not process one oversized step.
- Pause nonessential work while the document is hidden. Preserve essential
  progress and state semantics rather than freezing user-visible completion.
- Clear every timer created by the owner. Disconnect `IntersectionObserver`,
  `ResizeObserver`, `MutationObserver`, subscriptions, and global listeners
  with the same references used to register them.
- Kill owned library timelines and tweens. Dispose WebGL textures, materials,
  geometries, renderers, framebuffers, and media streams when their lifecycle
  ends.
- Guard asynchronous loaders so a late result cannot recreate or retain
  resources after disposal.
- Keep visibility state outside hot React render paths. Prefer lifecycle-local
  mutable control for per-frame work over component state updates on every
  frame.

Do not apply one page-level pause selector blindly. Long sections, repeated
cards, skeletons, marquees, and nested canvases may need different owners.

## Verify the Same Surface Afterward

Repeat the baseline under the same route, positions, viewport, and interaction:

- no nonessential offscreen animation or render loop remains active;
- visible effects start or resume without a jump, oversized physics step, or
  lost state;
- repeated route or mount cycles return observable resource counts to the
  expected baseline;
- reduced-motion mode preserves the final state and disables nonessential
  movement;
- normal search, filtering, navigation, or dynamic insertion still works;
- the console has no new lifecycle, context-loss, or hydration errors.

Report measured runtime evidence separately from source-audit risks. Say
“measured lower” only for before/after measurements; otherwise describe the
specific work that was removed or bounded without claiming a performance gain.

## Avoid False Fixes

- Do not remove all motion merely to make a probe green.
- Do not assume `animation-play-state` pauses RAF, WebGL, video, or timers.
- Do not leave permanent `will-change` promotion as a generic performance fix.
- Do not infer leak freedom from one short page load or one unavailable metric.
- Do not optimize invisible implementation details before identifying the
  measured user or device cost.
