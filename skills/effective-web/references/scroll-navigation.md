# Scroll and Navigation

Use this module for anchor navigation, horizontal sequences, sticky headers, or
scroll snap. Scrolling must preserve orientation and user control.

## Anchor and Sticky Offsets

- Set `scroll-padding` on the scrolling container or `scroll-margin` on targets
  so a sticky header does not obscure an anchor or focused element.
- Keep browser history, focus, and semantic links working. Smooth scrolling is
  an enhancement; guard it for reduced motion and never use it to hijack normal
  navigation.

## Horizontal Sequences

- Use scroll snap only when discrete items are genuinely sequential and a
  partially visible neighboring item helps discoverability. Do not trap users in
  a carousel-like interaction that hides content or resists normal scrolling.
- Preserve keyboard access, visible focus, and a clear affordance for horizontal
  overflow. A hidden scrollbar needs another reliable cue.
- Use `scrollbar-gutter: stable` when changing scrollbar presence would shift
  layout, and style scrollbars only as a progressive enhancement.

For range syntax, browser support, and detailed snap patterns, consult the
[deep scroll appendix](scroll-patterns.md).
