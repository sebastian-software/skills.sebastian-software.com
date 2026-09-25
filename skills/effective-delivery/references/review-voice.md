# PR Review Voice

## General prose owner

Use repository conventions and the requested register for ordinary comments.
Load `effective-writing` and its Metro English route only when a rewrite,
translation, or unresolved voice problem needs that depth and the register fits.
Do not maintain a second general prose blacklist here.

Repository language and communication conventions override the Metro English
default. When `effective-writing` is unavailable or does not match the
repository, use its established conventions and fall back to concise,
professional prose. Match the user's language in the private status summary.

## PR-specific semantics

Delivery retains the review decision and the meaning carried by the comment:

- **Inline, no label prefixes.** Put a finding on the relevant changed line
  when a stable anchor exists. Do not prefix it with `nit:`, `issue:`,
  `suggestion:`, severity codes, confidence scores, or emoji. State the
  severity through the consequence and required action.
- **Blocking is explicit.** A request-changes review names what must change and
  why the current behavior cannot merge. Natural wording must not soften a
  material risk into an optional suggestion.
- **Optional means optional.** Taste, naming alternatives, formatting, and
  speculative refactors are explicitly skippable or omitted. They never appear
  as required work in a request-changes review.
- **Bot and human replies differ.** Replies to reviewers ending in `[bot]` and
  repository-known review bots are short and technical: decision plus reason.
  Human replies can carry a little more context and warmth. The technical
  decision does not change with the audience.
- **Praise does not carry severity.** Recognize a concrete strength when it is
  useful, but do not use a praise sandwich, hide a blocker behind compliments,
  or manufacture praise for every finding.

Use the specialized [review examples](review-voice-examples.md) when a severity
or tone question remains. They are optional calibration, not a pre-read for
every comment.
