# Route: Consultant Profile — Thesis, Prominence, and Structure

Create consultant profiles that sell a clear professional thesis instead of
merely listing a career in reverse chronological order.

The profile's job is to help a buyer, recruiter, partner, or staffing lead
quickly understand:

- what this consultant is unusually good at
- which kinds of organizations trust them
- which industries and operating contexts they know
- what level of complexity, responsibility, and impact they have handled
- what they should be hired for next

## Read

- [Profile principles](profile-principles.md) — research synthesis,
  project-prominence model, regional and channel strategy, writing formulas,
  and audit checklist
- [Narrative arc](narrative-arc.md) — professional storyline, recurring themes,
  project connections, and the "no loose pile of projects" structure

## Workflow

1. Identify the target reader and buying situation.
   - Distinguish between project staffing, direct client acquisition, recruiter
     screening, partnership, and public website profile.
   - Identify the channel: PDF/CV, website, LinkedIn, XING, marketplace
     profile, proposal bio, or internal supplier profile.
   - Identify the country/market and language: Germany, Austria, Switzerland,
     EU/international English, US/global English, or bilingual.
   - Combine country with buying channel before applying format conventions.
     Germany, Austria, and Switzerland share some credibility-first
     expectations, but they are not one fixed CV format; direct-buyer profiles,
     staffing CVs, and marketplace cards also solve different jobs.
   - Read accepted ADRs and brand or editorial guidance for audience
     relationship, form of address, voice, tone, terminology, and channel
     exceptions. Record a durable cross-channel communication direction as an
     ADR through `effective-product`.
   - If the target is unclear, infer the most likely one from the prompt and
     state the assumption briefly.
   - A controlled-language request made only because the subject is technical is
     a profile mismatch, not a governing contract: state the channel tradeoff,
     use natural language for this artifact, and switch only when an existing
     artifact contract governs it or the user reconfirms after that tradeoff.
     Include that correction with the first-pass rewrite rather than silently
     adopting the requested controlled rhythm.

2. Extract the consultant's positioning thesis.
   - Reduce the profile to one sharp sentence: "[Role/specialty] who helps
     [type of organization] achieve [business/technical outcome] in [contexts]."
   - Base this on evidence from projects, clients, industries, scope, and
     recurring strengths.

3. Build an evidence map before rewriting.
   - List projects, clients, roles, industries, scale, technologies, seniority,
     outcomes, and notable constraints.
   - Mark each item with evidence types: brand signal, business impact,
     technical depth, leadership/stakeholder complexity, industry relevance,
     recency, and uniqueness.
   - Treat recommendations and testimonials as attributed external evidence.
     Preserve author, relationship, role/company at the time, date, original
     language/text, source locator, known reuse restrictions or sensitivities,
     selected excerpts, translations, and the claims they support.
   - When an opportunity brief or project request exists, separate explicit
     requirements, useful signals, and contextual preferences. Map each one to
     supplied evidence, and leave unsupported or unknown criteria unresolved
     instead of inferring a match or inventing a percentage score.

4. Find the professional arc.
   - Identify recurring themes across projects: industries returned to,
     capabilities that deepen, scale that increases, and lessons reused from one
     context in another.
   - Connect projects where later work clearly builds on earlier experience.
   - Use the arc to explain why the consultant's profile is more than a loose
     collection of engagements.
   - Keep it concise: create context and momentum, not a biography or a
     sports-documentary script.

5. Choose project prominence by relevance, not chronology alone.
   - Feature 3-5 "signature projects" or "selected highlights" near the top.
   - Promote older but high-signal work when it proves the desired positioning.
   - Keep a secondary "additional selected projects" list for breadth, not for
     important work that merely happens to be older.
   - Treat recognizable client names as signal only when the supplied evidence,
     target audience, and publication permissions support using them.

6. Rewrite projects as proof points.
   - Prefer Outcome -> Action -> Scope when impact is known.
   - Prefer Challenge -> Role -> Deliverable when outcomes are confidential or
     unavailable.
   - Name the industry, organization type, scale, and responsibility level where
     possible.
   - Avoid vague responsibility lists and generic technology stacks without
     business context.

7. Make the profile scannable.
   - Put the strongest positioning and proof in the first screen/page.
   - Use front-loaded headings, short bullets, and grouped evidence.
   - Avoid walls of text and burying high-signal clients in long chronological
     lists.
   - Let every section earn its place by helping the target reader perceive
     relevant fit; design should reinforce hierarchy rather than decorate the
     document.

8. Preserve truthfulness.
   - Do not invent metrics, client claims, leadership scope, or outcomes.
   - If metrics are missing, use bounded qualitative evidence:
     "enterprise-scale", "regulated banking environment", "multi-brand retail
     group", "telecommunications customer platform", or similar factual context.
   - Flag claims that need confirmation before publishing.

## Recommended Output

For an audit, return:

1. **Profile Thesis** — one proposed positioning sentence.
2. **Prominence Map** — which projects should be signature, supporting, or
   archive-level, with rationale.
3. **Source and Gap Inventory** — what is known, missing, inferred, duplicated,
   or needs permission.
4. **Interview Questions** — prioritized questions that resolve the most
   important uncertainties.
5. **Narrative Arc** — the through-line that connects projects, capabilities,
   industries, and recurring strengths.
6. **Personality, Boundaries, and Buyer Fit Strategy** — which values,
   motivations, stances, strengths, limits, and background signals should be
   visible, and how to word them professionally.
7. **External Proof Strategy** — which recommendations should become direct
   quotes, claim support, working-style evidence, or source-only material;
   include attribution, reuse sensitivity, translation, and source-link
   handling.
8. **Channel and Market Strategy** — how the profile should differ for direct
   buyers, staffing/supplier channels, marketplaces, PDF/CV, website,
   LinkedIn/XING, and Germany, Austria, Switzerland, EU/international, or US
   audiences.
9. **Provider Field Mapping** — when a named intermediary or marketplace is in
   scope, map its current documented fields to the stable master model and label
   each as reusable, private/account, operational/application, or
   platform-owned.
10. **Structure** — proposed profile sections in order.
11. **Voice Strategy** — recommended German-language credibility-first tone,
    country/channel adaptations, English/international tone, LinkedIn tone, and
    any "more positive" variant.
12. **Rewrite Samples** — improved headline, intro, LinkedIn/About version if
    relevant, and 3-5 project entries.
13. **Gaps** — missing metrics, facts, known quote restrictions, client
    permissions, provider-field volatility, or platform/API constraints to
    verify.

For a full rewrite, return a complete profile with:

- headline
- 3-5 line executive summary
- short professional arc / through-line
- optional personal motivation, working-principles, or role-fit block
- capability pillars
- selected highlights or signature projects
- industry/client context
- optional selected-recommendations or "voices from collaboration" block with
  local attribution and visibly labelled translations
- optional operational-fit block for staffing, supplier, or marketplace channels
- optional provider field map when a named intermediary or marketplace is in
  scope
- additional selected projects
- LinkedIn/About and headline variants when a social profile is in scope
- tone variants when useful: restrained or warmer German-language copy,
  country/channel adaptations, international English, LinkedIn
- skills/tooling only where it reinforces the thesis

## Quality Bar

Prefer concrete, commercially legible language over career-history narration. A
strong output should make the reader think, within 30 seconds: "I understand
what this person does, where they have done it, and why they are credible for
this kind of work."

## Cross-links

- Personality, boundaries, localization, and the language-and-persuasion pass
  are the Profile Voice route.
- Source inventory, gap analysis, interview mode, and marketplace field mapping
  are the Profile Evidence route.
- The acquisition overlay — target-buyer path, network, conversation, content,
  and pipeline strategy for a completed profile — is the LinkedIn Selling route.
  Keep professional evidence and field-level profile content here.
- Public posts derived from approved positioning, project evidence, and
  permission-sensitive client context are the Social Content route.
- Standalone technical articles and thought leadership belong to
  `effective-writing`; repository-derived behavior and controlled-language
  verification belong to `effective-delivery`. Keep profile positioning, career
  evidence, and buyer-facing interpretation here.
