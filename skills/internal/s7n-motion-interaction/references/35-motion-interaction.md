# Motion Interaction

Use motion to explain state change, spatial continuity, feedback, and progress. Avoid decorative motion that delays task completion or makes layout harder to understand.

## Working Rules

- Respect `prefers-reduced-motion` and provide a useful non-motion baseline.
- Keep product UI transitions short and tied to user intent.
- Use View Transitions, scroll-driven animations, keyframes, and entry/exit animations only after support and fallback behavior are clear.
- Preserve focus, scroll position, URL state, and semantic navigation when adding page or component transitions.

## Additional Rules

- View Transition API overview for same-document SPA transitions via document.startViewTransition() and cross-document MPA transitions via @view-transition navigation:auto; use for spatial continuity in navigation, filtering/reordering, list-to-detail, and persistent UI, while enforcing prefers-reduced-motion, performance, focus/scroll context, and semantic navigation checks.
- Use color-shifting animation as a motion/effects example; require reduced-motion and readability checks.
- Use CSS `@starting-style` as entry-transition guidance with support and fallback checks.
- Use scroll-driven animation material as rule for scroll-linked motion with progressive enhancement.
- Use partial keyframes as animation craft guidance; keep motion purposeful and bounded.
- Use GSAP-to-native scroll animation migration as implementation example, not as blanket replacement rule.
- Use CSS scroll animation as support/context for native scroll-driven motion.
- Use scroll timelines for scroll-driven animation patterns and caveats.
- Use shared-element transition discussion as SPA/MPA motion tradeoff context.
- Use View Transitions implementation as practical companion to docs.
- Use auto-height transition for entry/size animation caveats and support checks.
- Use as scroll-driven animation companion guidance; prefer docs for API details.
