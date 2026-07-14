# SVG Graphics

Use this route for SVG icons, logos, diagrams, charts, illustrations, paths,
sprites, and vector micro-interactions. Keep general vector craft separate from
procedural SVG filter textures.

## Workflow

1. Identify the graphic's job: decorative, informative, interactive, data-rich,
   branded, or animated.
2. Choose delivery deliberately: external image for static content, inline SVG
   for DOM styling and interaction, or a component/sprite system for repeated
   icons.
3. Establish the coordinate system and sizing contract with a correct `viewBox`,
   intrinsic ratio, and responsive CSS.
4. Preserve semantics and accessible naming before adding styling or motion.
5. Prefer simple shapes and readable paths; optimize only after the source is
   correct and maintainable.
6. Verify scaling, theme/forced-colors behavior, keyboard use, reduced motion,
   browser support, and rendering cost.

## Rules

- Never remove or fabricate a `viewBox` without checking the artwork bounds; it
  defines the internal coordinate system, not the rendered CSS size.
- Use inline SVG only when CSS, JavaScript, theming, or internal animation needs
  access to its nodes. Prefer `<img>` for cacheable static artwork.
- Hide decorative graphics from assistive technology. Give informative graphics
  a concise accessible name and provide nearby text or a longer description for
  charts and complex diagrams.
- Put interaction semantics on a native HTML control or link that contains the
  SVG. Do not turn the SVG itself into a simulated button.
- Use `currentColor`, semantic custom properties, and deliberate presentation
  attributes so icons inherit component states without internal selector hacks.
- Keep path data readable in source. Prefer shapes over paths when they express
  the geometry clearly, and use `pathLength` when normalized stroke progress is
  more useful than measured path units.
- Treat path morphing and advanced SVG animation as progressive enhancements.
  Match hover with focus/activation, respect reduced motion, and provide a
  coherent static result.
- Keep filters, masks, clipping, nested groups, and path complexity proportional
  to the visible result. Measure large or repeated effects on low-end hardware.

## References

- [svg-graphics.md](svg-graphics.md) - delivery, coordinate systems, paths,
  accessibility, styling, animation, optimization, and review checks.
- [design-system-rules.md](design-system-rules.md) - reusable icon systems,
  tokens, masks, and visual effects.
- [motion-interaction.md](motion-interaction.md) - timing, execution models,
  earned delight, and reduced-motion behavior.
- [html-accessibility.md](html-accessibility.md) - names, roles, focus, keyboard,
  forced colors, and non-visual alternatives.

## Boundaries

Read [SVG Textures](route-textures.md) for `feTurbulence`, filter chains, grain,
paper, clouds, and organic surfaces. Read [Data Tables](route-tables.md) or the
relevant visualization workflow when the primary problem is data interpretation
rather than SVG implementation.
