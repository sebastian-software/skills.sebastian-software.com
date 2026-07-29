# Source, Voice, and Content History

Ground social content in project-owned evidence and authorized authored
material. Keep durable communication direction, exact editorial guidance,
source facts, and published content in the artifacts that own them.

## Discover the Available Sources

Inspect only what the current task needs:

1. current user instructions and raw wording
2. accepted ADRs and project instructions
3. editorial or brand guidance such as `STYLE.md`
4. supplied notes, transcripts, articles, release notes, project evidence, and
   approved claims
5. a project-owned source map, content index, or published-content ledger
6. current product documentation, repository behavior, analytics, or primary
   sources when a claim may have changed
7. authorized authored examples, prioritizing recent examples of the same
   format
8. prior generated drafts only when continuity is useful

Do not treat generated copy, scraped third-party prose, quoted-source text, or
an unattributed draft as evidence of the speaker's voice.

## Build a Focused Evidence Register

For each consequential statement, distinguish:

- **verified fact:** directly supported by a supplied or inspected source
- **authored interpretation:** the speaker's supported judgment or conclusion
- **opinion or hypothesis:** legitimate when labelled or clearly framed as such
- **unknown:** needs confirmation, qualification, omission, or a placeholder
- **restricted:** confidential, private, unapproved, or unsafe to publish

Preserve dates and material conditions for metrics, product behavior, customer
outcomes, rankings, prices, availability, and other volatile claims. If current
verification is unavailable, remove the unstable detail or expose the gap
instead of smoothing it into certainty.

## Use a Source Map When the Project Has One

A compact source map can point drafting work to the right evidence without
copying complete documents:

| Context | Primary source | Safe use | Check before claiming |
| --- | --- | --- | --- |
| Identity and voice | Accepted ADR and editorial guide | Stable relationship, tone, vocabulary | Whether current guidance supersedes it |
| Product or project | Repository, release notes, approved case evidence | Verified behavior and constraints | Current release state, permission, measured result |
| Personal experience | Authored notes, transcript, published post | Supported first-person perspective | Relevance, privacy, and exact detail |
| Customer evidence | Approved case study, attributed quote, research record | Claims within the approved scope | Consent, attribution, date, and confidentiality |
| Market or platform | Current primary source | Dated fact or requirement | Whether it has changed |

Treat this as a project-owned editorial artifact, not a required filename or a
skill-private memory format. Create or update it only when the user authorizes
persistent content-system work.

## Derive Voice from Evidence

Separate stable voice from format-specific expression.

Stable voice can include:

- who is speaking to whom and from which relationship
- recurring qualities such as direct, calm, candid, warm, technical, curious,
  restrained, or opinionated
- preferred nouns, verbs, terminology, level of explanation, and form of
  address
- how confidently claims are made and how uncertainty is exposed
- the acceptable range for humor, emotion, commercial intent, and calls to
  action

Format-specific evidence teaches different things:

- **Replies and comments:** conversational vocabulary, capitalization,
  curiosity, gratitude, disagreement, and brevity
- **Original posts:** openings, pacing, paragraph shape, proof, argument,
  stories, and endings
- **Quote or resource shares:** how the speaker adds a reason, mechanism,
  application, question, or related source
- **Threads and series:** sequencing, continuity, transitions, and how much
  context each part can carry
- **Product or project posts:** proof, tradeoffs, constraints, demonstrations,
  and the boundary between explanation and promotion

Infer a voice rule only from a repeated, meaningful pattern. Keep an isolated
rough edge as evidence of one draft, not a permanent persona rule. Preserve
natural directness, fragments, contractions, or lower-case phrasing when they
fit, but never manufacture mistakes to simulate authenticity.

When a durable voice choice needs to survive channels and sessions, route the
decision through `decision-records` and keep detailed examples in the project's
editorial guide.

## Search Content History Without Loading It All

When a project maintains published content, search only the current subject and
likely repeated elements. Useful fields include:

- canonical ID or URL
- publication date and platform
- format and publication status
- exact authored text
- quoted or linked source text stored separately
- topic, claim, anecdote, proof point, resource, and intended audience
- campaign, product, or source reference when relevant

Use focused repository search such as:

```sh
rg -n -i "<topic|hook|claim|anecdote|proof|resource|ending>" <content-paths>
```

Do not claim corpus-level freshness when only a small or unknown sample was
available.

Check two kinds of duplication:

1. **Record duplication:** the same ID, canonical URL, or normalized authored
   text appears more than once.
2. **Editorial duplication:** the same distinctive hook, claim, anecdote, proof
   point, resource bundle, structure, or ending is being reused with surface
   changes.

A recurring belief remains usable when the new content adds a current event,
new proof, a changed conclusion, a different mechanism, a meaningful
counterexample, or a useful application for another audience.

Use this freshness test:

- What happened or changed?
- Which artifact, observation, or result proves it?
- What mechanism or tradeoff is newly visible?
- What can the reader understand or do differently now?

If none of those changed, prefer another angle instead of paraphrasing the old
post.

## Protect Authorship, Privacy, and Permission

- Store or quote only material the user supplied, authored, or authorized for
  the task.
- Keep quoted-source wording separate from the speaker's authored text.
- Preserve attribution and do not turn another person's phrase into house
  voice.
- Do not infer private biography, family details, client identity, travel,
  internal team behavior, or confidential outcomes from weak context.
- Treat old public content as evidence that something was said, not automatic
  permission to reuse every detail in a new context.
- Report a missing permission or evidence gap instead of inventing a safe
  substitute.
