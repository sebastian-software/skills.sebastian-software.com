---
name: s7n-typography
description: |
  UI typography, type hierarchy, readable measure, font stacks, webfont loading, text sizing, line-height, optical sizing, and typographic polish. Use when the user asks about fonts, readability, text hierarchy, font performance, font pairing, or text that feels cramped, weak, oversized, or hard to scan.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Typography

Use this skill for typography in digital interfaces. It covers type choice, hierarchy, rhythm, readable measure, webfont behavior, and the small text decisions that make UI feel professional.

## Workflow

1. Identify the reading mode: scanning UI, dense data, long-form content, marketing copy, or form completion.
2. Choose a restrained type system: usually one family, two or three weights, and a predictable scale.
3. Set body size, line-height, and line length before tuning headings.
4. Ensure labels, buttons, captions, and helper text remain readable at real device sizes.
5. Check fallback fonts, loading behavior, and layout shift.

## Rules

- Do not scale font size directly with viewport width.
- Keep letter spacing at `0` unless using uppercase, small caps, or a deliberate display treatment.
- Avoid thin low-contrast text in UI.
- Reserve hero-scale type for true heroes; compact panels need compact headings.
- Use typographic hierarchy to reduce explanation, not to add decoration.

## References

- [references/typography.md](references/typography.md) - core UI typography rules.
- [references/webfonts.md](references/webfonts.md) - webfont loading, fallbacks, and performance.
- [references/typography-rules.md](references/typography-rules.md) - practical typography implementation rules.
