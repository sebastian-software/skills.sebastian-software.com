# Communication Decisions

Use this reference for durable language, brand voice, content, marketing, sales,
support, documentation, and interface-copy decisions. Store the decision in the
same ADR corpus as technical and design decisions; do not invent a separate
voice-memory format.

## Decision Dimensions

Record only dimensions that materially constrain future work:

- **Audience relationship:** peer, guide, expert, partner, host, authority, or
  service provider; name who is speaking to whom.
- **Form of address:** `du`, `Sie`, first name, title, second person, or an
  equivalent locale-specific convention. State capitalization and exceptions.
- **Voice:** the stable character across channels, expressed in concrete
  qualities such as precise, direct, calm, candid, warm, opinionated, or formal.
- **Tone range:** how the voice adapts for marketing, product UI, support,
  errors, legal or security messages, recruiting, and executive communication.
- **Formality and proximity:** professional versus casual, approachable versus
  distant, restrained versus expressive. Avoid vague labels without behavioral
  implications.
- **Information density:** terse, concise, explanatory, or exhaustive; define
  how much context, rationale, repetition, and sequencing each channel needs.
  Treat density as independent from warmth and formality. Concise can remain
  friendly; exhaustive can remain direct.
- **Vocabulary:** preferred product nouns and verbs, technical depth, jargon
  policy, contractions, anglicisms, inclusive-language choices, and terms to
  avoid.
- **Evidence and claims:** how confidently the organization speaks, which claims
  require proof, and where uncertainty or limitations must be explicit.
- **Humor and emotion:** where they are welcome, where they are risky, and which
  situations must remain sober.
- **Channel and locale differences:** which parts stay invariant and which adapt
  by channel, market, language, or regulatory context.

## Example Decision

```md
## Decision

German owned channels address customers with "du" and use a direct,
professional, approachable voice. We write as an experienced peer: specific
and candid, without slang, forced jokes, or inflated claims.

- Product UI: concise and task-led; errors explain recovery without humor.
- Marketing: more explanatory and narrative where context builds trust, but
  every outcome claim needs evidence and each section still earns its length.
- Support: calm, accountable, and explicit about ownership and next steps.
- Legal and security: complete, precise, and sober; brevity never removes
  obligations, uncertainty, sequence, scope, or risk.
- English: preserve the peer relationship rather than translating German
  informality mechanically.
```

Include short examples and non-examples only when they make the boundary easier
to apply. Do not turn the ADR into a complete style guide.

## Information-Density Guidance

Record density only when it will guide repeated work across authors, tools, or
channels. Define what readers must be able to understand or do, not a universal
word count.

- **Product UI:** prefer the shortest language that preserves action, state,
  consequence, and recovery. Keep exact identifiers, commands, values, and
  technical terms intact.
- **Marketing and editorial:** allow context, evidence, examples, and narrative
  when they help the audience decide or trust. Remove throat-clearing,
  duplicated claims, and decorative explanation.
- **Sales:** match detail to buying stage and stakeholder risk. A first message
  and a procurement proposal should not have the same density.
- **Support:** lead with the outcome, ownership, and next step; add diagnostic
  detail users need to proceed or understand impact.
- **Documentation:** optimize for successful execution and future discovery.
  Preserve prerequisites, order, edge cases, and exact code or commands rather
  than compressing them into ambiguous fragments.
- **Legal, security, incident, payment, and irreversible actions:** expand when
  compression could hide scope, ordering, uncertainty, consequences, required
  action, or recovery. Clarity outranks stylistic brevity.

Do not adopt intentionally broken grammar, invented abbreviations, or a persona
solely to reduce tokens. Match the audience's language and reading context.

## Drift Checks

- Do interface labels, website copy, social posts, profiles, sales messages, and
  support responses express the same underlying relationship?
- Does the form of address change without a documented channel or locale reason?
- Are professional and approachable being treated as opposites when the chosen
  voice intentionally combines them?
- Do error, legal, security, or crisis messages become playful where sobriety is
  required?
- Have new markets, audiences, channels, or brand positioning invalidated the
  original decision?
- Are examples and terminology in editorial guides still aligned with the ADR?
- Has a concise channel started omitting consequences or recovery, or has an
  explanatory channel accumulated filler and repeated claims?
- Do high-risk messages expand enough to preserve exact sequence, uncertainty,
  obligations, and technical identifiers?
