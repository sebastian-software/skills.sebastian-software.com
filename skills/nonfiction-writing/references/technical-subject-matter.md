# Technical Subject-Matter Writing

Use this reference for engineering blog posts, technical articles, explainers,
technical case studies, and long-form homepage prose for technical products or
projects. Preserve technical integrity without making editorial or
market-facing prose sound like a manual.

## Select the writing contract

Choose the narrowest contract that fits the artifact:

| Contract | Use |
| --- | --- |
| Technical editorial prose | Explain, argue, teach, or demonstrate through an article, blog post, case study, or public project page. |
| Technical marketing prose | Explain a verified capability, mechanism, constraint, or differentiator in a product or service page. |
| Technical documentation | Help a user operate, configure, integrate, migrate, or troubleshoot a product through `tech-docs`. |
| Controlled technical language | Apply ASD-STE100, a tekom-based project profile, or another named standard through `tech-docs` only when it governs the artifact. |

Do not infer a controlled-language requirement from a general request for
clarity. For public German prose, prefer precise, natural technical German
rather than Einfache Sprache. For public English prose, prefer natural
editorial English rather than internal-team Metro English.

Treat controlled language as an artifact contract, not as a synonym for
technical clarity. A controlled-language request made only because the subject
is technical is a profile mismatch, not a governing contract: state the channel
tradeoff, use natural language for this artifact, and switch only when an
existing artifact contract governs it or the user reconfirms after that
tradeoff. A publication, customer, regulatory, or project requirement is such a
contract; the shortcut in the initial request is not.

On the first pass, correct the profile mismatch briefly and provide the
channel-appropriate technical editorial version; offer the controlled variant
when it remains a meaningful choice. If the user still prioritizes that profile,
route its language-level authoring or review through `tech-docs`.

Do not describe German prose as ASD-STE100 compliant: ASD-STE100 controls
English. State that mismatch before drafting when the requested assurance is
invalid. Do not describe prose as universally tekom-compliant: a project adopts
specific rules from a named guide and editorial profile.

## Establish the source and ownership chain

Keep these layers separately reviewable:

```text
engineering truth -> approved terminology -> claim and proof
                  -> editorial explanation -> channel presentation
```

- Derive product behavior, values, limits, compatibility, and failure modes
  from current engineering or approved product sources.
- Use `tech-docs` when repository inspection, executable examples, a public
  interface, or a controlled-language contract owns correctness.
- Use `product-marketing` to establish market position, supported claims,
  proof, audience, and desired action.
- Keep the article, explanation, narrative, and long-form page prose in this
  skill.
- Use `effective-web` for page hierarchy, interface copy, accessibility,
  implementation, and browser verification.

Do not use polished prose as evidence that a technical or commercial claim is
true. Mark unresolved behavior, measurements, permissions, and comparisons
before drafting around them.

## Preserve the technical proposition

Extract the proposition before revising its language:

- actor or owning system
- action or mechanism
- object or affected surface
- prerequisites and conditions
- limits, versions, scale, or environment
- result, side effect, and likely failure
- evidence and uncertainty

Keep qualifications next to the claim they constrain. Do not turn `can`,
`supports`, `typically`, or `under these conditions` into an unconditional
promise for a cleaner sentence or stronger hook.

Preserve literal code, commands, API names, configuration keys, UI labels,
protocol names, identifiers, and quoted output. Route uncertain implementation
details back to their technical source instead of smoothing over them.

## Control terminology without flattening the prose

- Use one preferred term for each important technical concept.
- Preserve official product, protocol, framework, and interface names.
- Define an unfamiliar term at its first useful occurrence when the audience
  needs it; do not interrupt specialists with definitions of shared basics.
- Expand an abbreviation on first use unless the audience and channel make it
  reliably familiar.
- Vary surrounding language, examples, and sentence construction rather than
  rotating synonyms for a core concept.
- Distinguish adjacent concepts that readers may otherwise collapse, such as
  authentication and authorization, latency and throughput, or backup and
  replication.
- Reuse an accepted glossary, terminology database, or editorial decision
  instead of creating a parallel vocabulary inside one article.

Treat stable terminology as a comprehension aid, not as a ban on voice,
metaphor, or normal lexical variety.

## Explain for the selected audience

Start from what the reader already recognizes, then add only the technical
depth needed for the piece's governing idea.

- Connect mechanism to consequence: explain what the system does, why that
  behavior matters, and under which conditions.
- Introduce a concrete example before a large abstraction when it reduces the
  reader's cognitive load.
- Use an analogy only when its mapping is accurate. Name where it stops being
  accurate when readers could otherwise carry the wrong model forward.
- Separate the supported path from alternatives and edge cases.
- Use diagrams, code, or tables only when they explain a relationship more
  efficiently than prose.
- Let specialist readers keep useful complexity. Do not replace precise domain
  language with broad everyday words that change the meaning.

Write for competent readers who may lack this specific context. Do not confuse
accessibility with condescension or remove the qualification that makes an
expert statement true.

## Preserve editorial movement

Technical editorial prose may use:

- a governing argument or narrative arc
- varied sentence and paragraph length
- first person, judgment, and professional experience when sourced
- examples, comparisons, restrained humor, and accurate metaphors
- tension, curiosity, and a point of view that the body repays
- a conclusion or call to action appropriate to the reader relationship

Do not mechanically apply one action per sentence, one sentence per paragraph,
an approved-word dictionary, imperative syntax, or other controlled-language
constraints. Use those rules only when a named documentation contract governs
the artifact.

For a tutorial embedded in an article, separate the editorial frame from the
operational instructions. Apply documentation discipline to commands,
prerequisites, steps, expected results, and recovery while allowing the
surrounding article to retain its voice.

## Write technical homepage prose

Keep the first screen understandable without pretending every reader needs the
same level of depth:

1. State the recognizable situation or result.
2. Name the relevant capability or mechanism.
3. Supply proof and material constraints.
4. Offer deeper technical detail for readers who need to validate fit.

Do not use terms such as `secure`, `scalable`, `real-time`, `open`, `automated`,
or `AI-powered` as self-proving benefits. Explain the relevant mechanism,
boundary, comparison, or evidence.

Keep product positioning and technical explanation distinct. A headline may
express buyer relevance; the supporting copy must still preserve the behavior
and conditions that make the claim true.

## Adapt without losing the contract

### German

- Prefer natural, precise technical German with useful subordinate clauses and
  normal paragraph rhythm.
- Reduce heavy nominal constructions, ambiguous references, and unnecessary
  internal jargon.
- Keep established Fachbegriffe when they are accurate and useful.
- Treat tekom-derived clarity rules as an editorial influence unless a
  project-specific rule set explicitly governs the artifact.
- Do not default to Einfache Sprache or Leichte Sprache.

### English

- Prefer direct, idiomatic editorial English appropriate to the audience and
  author.
- Keep technical terms stable while allowing contractions, narrative rhythm,
  and personality when the channel supports them.
- Do not claim ASD-STE100 conformance or apply its dictionary and rule set
  unless the artifact is explicitly governed by it.
- Use `metro-english` for internal team communication about the work, not as
  the default voice for a public technical article or homepage.

## Review in passes

1. **Technical integrity** - Verify behavior, conditions, limits, examples, and
   comparisons against their owning sources.
2. **Terminology** - Check preferred terms, literal identifiers, abbreviations,
   and distinctions between adjacent concepts.
3. **Audience path** - Confirm that context, mechanism, consequence, and depth
   arrive in the order the selected reader needs.
4. **Claim and proof** - Keep every consequential technical and commercial
   claim within the supplied evidence.
5. **Voice and movement** - Restore rhythm, personality, examples, and
   transitions where precision editing made the prose mechanical.
6. **Channel fit** - Check the title, lead, page hierarchy, call to action, and
   handoffs without changing the technical proposition.

Report a controlled-language conformance level only through the governing
technical-documentation workflow. For editorial prose, describe the result as
technically reviewed, terminology-aligned, or informed by rule-based technical
writing only when the performed review supports that statement.
