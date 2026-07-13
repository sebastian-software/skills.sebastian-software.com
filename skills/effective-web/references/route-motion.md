# Motion and Interaction

Use this skill for motion that clarifies state, continuity, feedback, and progress without slowing users down.

## Workflow

1. Identify the purpose of motion: feedback, state change, orientation, hierarchy, or continuity.
2. Remove decorative motion that competes with task completion.
3. Animate compositor-friendly properties where possible.
4. Keep product transitions short and predictable.
5. Respect `prefers-reduced-motion` and provide equivalent state clarity without animation.

## Rules

- Author the static, reduced-motion experience first; layer motion inside `@media (prefers-reduced-motion: no-preference)` and never lose information when motion is off.
- Animate only `transform` and `opacity` on hot paths; never animate layout properties (`width`, `height`, `top`, `left`, `margin`) in task surfaces.
- Keep UI transitions short (≈150–250ms) and make every animation interruptible by user input.
- Motion should never hide latency or force users to wait for choreography.
- Do not make content available only through hover or scroll tricks.
- Use scroll effects only when they improve comprehension or orientation.
- Feature-detect and reduced-motion-guard View Transitions and scroll-driven animations; the content change must work when they are unsupported.
- Preserve focus, scroll position, URL state, and stable layout during transitions.

## References

- [scroll-patterns.md](scroll-patterns.md) - scroll interaction patterns and risks.
- [motion-interaction.md](motion-interaction.md) - motion principles, timing, and reduced-motion rules.
