# Human-Voice Editing and Pattern Audits

Use this reference when a user wants prose to sound less generated, asks for a
minimal voice-preserving edit, or wants concrete signs of formulaic writing
without a rewrite.

## Separate the two jobs

Choose one mode before changing the text:

- **Edit:** Make the smallest set of changes that improves clarity and removes
  formulaic patterns. Return the revised text and a compact note about
  consequential changes.
- **Audit:** Name the observed pattern, quote the smallest useful excerpt,
  explain its reader effect, and suggest a short correction. Do not rewrite
  unless asked.

Never infer who or what wrote a passage. A pattern audit can show that prose
sounds templated, inflated, or mechanically polished; it cannot establish AI
authorship. Do not return an AI probability or confidence score.

## Preserve the writer before removing patterns

Read the complete draft and identify:

- recurring vocabulary and preferred technical terms
- typical sentence and paragraph movement
- bluntness, warmth, humor, uncertainty, or formality
- useful digressions, fragments, and changes in pace
- the current level of polish

Keep those signals unless they obstruct the assignment. Do not make every
paragraph equally tidy, replace characteristic words for variety, or turn a
rough but recognizable voice into generic professional prose.

Apply a minimum-effective-edit rule:

1. Preserve the point, evidence, claim limits, and intended reader action.
2. Fix formulaic framing, unsupported importance, repetition, and genuinely
   tangled sentences.
3. Leave strong sentences alone.
4. Re-read the result for voice drift and accidental over-compression.

## Inspect pattern families

Treat these as diagnostic families, not automatic violations. One isolated
colon, fragment, contrast, list, or em dash may be exactly right. Flag density,
repetition, and mismatch with the writer or channel.

### Manufactured contrast and drama

Look for repeated constructions such as:

- `This is not X. It is Y.`
- `Not X. Not Y. Just Z.`
- several one-line fragments that create importance without adding meaning

State the supported point directly when the contrast is only a delivery
mechanism. Preserve a real distinction, rebuttal, or rhythmic fragment when the
argument depends on it.

### Meta-openers and borrowed authority

Cut setups that delay the claim or manufacture insider status:

- announcements that the writer is about to be honest or clear
- claims about what everyone else misses, skips, or gets wrong
- rhetorical questions immediately answered by the writer

Keep personal setup when it supplies context, tension, vulnerability, or
character. The test is whether removing it costs the reader something besides
ceremony.

### Inflated consequence and empty analysis

Inspect:

- unsupported claims that an event is pivotal, transformative, or proof of a
  broader commitment
- trailing clauses with words such as `highlighting`, `showcasing`, or
  `underscoring` that restate an attitude instead of explaining a consequence
- vague attribution such as `experts agree` or `research shows`
- elaborate verb phrases where `is`, `has`, or one concrete action is clearer

Replace importance with a supplied fact, mechanism, measured effect, or
constraint. Name the actual source for attributed claims; when none is
available, mark the evidence gap instead of inventing support.

### Terminology drift

Do not rotate among near-synonyms merely to avoid repetition. Repeating the
correct term is clearer than renaming the same actor, feature, or concept in
each paragraph.

Preserve deliberate distinctions. Before normalizing terms, check whether they
refer to different roles, states, or technical concepts.

### Scripted reveals and conclusions

Look for:

- a label and colon used to stage an ordinary claim as a reveal
- repeated question-and-answer pairs
- a final metaphor or aphorism that adds drama but changes no conclusion
- a recap ending that repeats what the reader just read

Use colons when they genuinely introduce a list, explanation, quotation, or
label. End on the last concrete consequence, earned implication, decision, or
next step; do not delete closure the reader still needs.

### Decorative structure

Inspect whether headings, bold emphasis, bullets, emoji, punctuation, and very
short sections express real hierarchy or merely decorate thin content.

Turn a list into prose when sequence, comparison, or scanning does not justify
it. Combine tiny sections when the headings interrupt the reading path. Apply
locale and house-style punctuation through `locale-typography`; do not impose a
universal em-dash ban.

### Mechanical rhythm

Read for repeated sentence lengths, identical paragraph shapes, stacked
fragments, symmetrical lists, and the same rhetorical move in every section.
Vary structure only when it improves emphasis or restores the writer's natural
cadence. Random variation is not voice.

## Return an audit people can act on

Group repeated instances of one pattern instead of producing a line-by-line
style lint. Order findings by reader impact.

For each finding, include:

1. **Pattern:** a short descriptive name
2. **Evidence:** the smallest representative quotation
3. **Effect:** what becomes vague, inflated, repetitive, or hard to trust
4. **Direction:** the smallest useful correction

End with a bounded conclusion such as `formulaic in several transitions` or
`mostly specific, with one repeated contrast pattern`. Do not collapse the
report into a binary slop label.

## Verify an edit

Before returning revised prose, check:

- No fact, quotation, statistic, example, opinion, or certainty was invented.
- The writer's recognizable vocabulary, cadence, edge, humor, and uncertainty
  remain.
- The amount of editing is proportional to the observed problems.
- Specific details survived instead of becoming generic claims.
- Sources are named or missing attribution is visible.
- Repetition now serves terminology or rhythm rather than a template.
- Formatting reflects content hierarchy.
- The ending completes the reader's job without a mechanical recap.
- The result sounds natural when read aloud.

## Source note

The audit-without-authorship distinction and several pattern families were
distilled from Peter Yang's
[No AI Slop](https://github.com/petergyang/no-ai-slop), published under the MIT
license. This reference adapts those ideas to this collection's evidence rules,
channel ownership, progressive disclosure, and voice-preservation approach; it
is not a vendored snapshot.
