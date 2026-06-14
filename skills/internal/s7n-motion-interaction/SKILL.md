---
name: s7n-motion-interaction
description: |
  UI motion, transitions, micro-interactions, scroll patterns, animation timing, spatial continuity, reduced-motion support, and avoiding jank. Use when adding, reviewing, or fixing animations, page transitions, scroll-driven effects, hover effects, or motion in product UI.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Motion & Interaction

Use this skill for motion that clarifies state, continuity, feedback, and progress without slowing users down.

## Workflow

1. Identify the purpose of motion: feedback, state change, orientation, hierarchy, or continuity.
2. Remove decorative motion that competes with task completion.
3. Animate compositor-friendly properties where possible.
4. Keep product transitions short and predictable.
5. Respect `prefers-reduced-motion` and provide equivalent state clarity without animation.

## Rules

- Motion should never hide latency or force users to wait for choreography.
- Avoid layout-property animation in task surfaces.
- Do not make content available only through hover or scroll tricks.
- Use scroll effects only when they improve comprehension or orientation.
- Preserve stable layout during transitions.

## References

- [references/14-scroll-patterns.md](references/14-scroll-patterns.md) - scroll interaction patterns and risks.
- [references/35-motion-interaction.md](references/35-motion-interaction.md) - motion principles, timing, and reduced-motion rules.
