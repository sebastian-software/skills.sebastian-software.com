# Interface Copy

Use this skill for words inside product UI: labels, helper text, empty states, headings, button text, status messages, and short-form explanation.

## Workflow

1. Read accepted ADRs and editorial guidance for audience relationship, form of
   address, stable voice, vocabulary, claim boundaries, and channel exceptions.
2. Identify the user's question at that moment: what is this, why does it matter, what happens next?
3. Remove copy that explains the interface instead of making the interface clearer.
4. Make labels concrete and action text outcome-oriented.
5. Match tone to consequence without changing the recorded voice: calm for
   errors, direct for actions, sparse for repeated workflows.
6. When copy feels generic or generated, use [UI anti-patterns](ui-antipatterns.md)
   to check repeated cadence, manufactured contrast, unsupported claims, and
   redundant language without banning individual words or punctuation.
7. Check text expansion, localization, accessibility names, and cross-channel
   consistency. Use `decision-records` when the work changes a durable
   communication direction.

## Rules

- Button labels should usually be verb plus object.
- Error copy should name the problem and the recovery path.
- Empty states should help users take the next useful action.
- Avoid marketing language inside task surfaces.
- Prefer specific nouns over clever phrasing.

## References

- [copywriting.md](copywriting.md) - concise interface and product copy rules.
- [editorial-ux.md](editorial-ux.md) - editorial UX patterns and wording checks.
- [ui-antipatterns.md](ui-antipatterns.md) - contextual generated-copy and
  marketing tells plus exception handling.
