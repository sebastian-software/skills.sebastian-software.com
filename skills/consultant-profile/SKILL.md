---
name: consultant-profile
description: This skill should be used when the user asks to create, rewrite, audit, localize, translate, complete, interview for, or improve a consultant profile, consultant CV, freelancer profile, LinkedIn profile, XING profile, project list, case-study list, expert bio, or senior technology-consulting resume. Use it especially when the user mentions missing projects, project gaps, old homepage, LinkedIn recommendations, references, testimonials, interview mode, completeness mode, DACH, EU, German vs English, LinkedIn, profile synchronization, tone, voice, positive framing, marketing psychology, storytelling, professional arc, career narrative, self-presentation, personality, working style, values, boundaries, what they can and cannot do, being opinionated, "Nein-Sager", "people buy from people", "Menschen kaufen von Menschen", anonymous profiles, buyer perspective, interviewer perspective, motivation, what they enjoy, what they want to achieve, design background, visual sense, autodidact, self-learner, On Writing Well, Dan Berlin, project prominence, client logos, achievements, industries, "weitere Projekte", Lebenslauf, Profil, CV, or wants to decide which projects deserve highlight placement.
version: 0.1.0
---

# Consultant Profile

Create consultant profiles that sell a clear professional thesis instead of merely listing a career in reverse chronological order.

The profile's job is to help a buyer, recruiter, partner, or staffing lead quickly understand:

- what this consultant is unusually good at
- which kinds of organizations trust them
- which industries and operating contexts they know
- what level of complexity, responsibility, and impact they have handled
- what they should be hired for next

## First Read

Read these references before making substantive changes:

- `references/profile-principles.md` - research synthesis, project-prominence model, regional/channel strategy, writing formulas, and audit checklist
- `references/language-and-persuasion.md` - tone calibration, positive-but-earned framing, plain-language editing, human voice, and ethical marketing psychology
- `references/narrative-arc.md` - professional storyline, recurring themes, project connections, and "no loose pile of projects" structure
- `references/interview-and-completion.md` - source inventory, gap analysis, interview questions, project completeness, and reference/testimonial mining
- `references/personality-and-boundaries.md` - professional personality, opinionated positioning, limits, working style, design background, and self-learner signals

## Core Workflow

1. Identify the target reader and buying situation.
   - Distinguish between project staffing, direct client acquisition, recruiter screening, partnership, and public website profile.
   - Identify the channel: PDF/CV, website, LinkedIn, XING, marketplace profile, proposal bio, or internal supplier profile.
   - Identify the region and language: DACH/German, EU/international English, US/global English, or bilingual.
   - Read accepted ADRs and brand or editorial guidance for audience
     relationship, form of address, voice, tone, terminology, and channel
     exceptions. Use `decision-records` when this work establishes or changes a
     durable cross-channel communication direction.
   - If the target is unclear, infer the most likely one from the prompt and state the assumption briefly.

2. Extract the consultant's positioning thesis.
   - Reduce the profile to one sharp sentence: "[Role/specialty] who helps [type of organization] achieve [business/technical outcome] in [contexts]."
   - Base this on evidence from projects, clients, industries, scope, and recurring strengths.

3. Build an evidence map before rewriting.
   - List projects, clients, roles, industries, scale, technologies, seniority, outcomes, and notable constraints.
   - Mark each item with evidence types: brand signal, business impact, technical depth, leadership/stakeholder complexity, industry relevance, recency, and uniqueness.

4. Run completeness and interview mode when data is missing or uncertain.
   - Inventory sources such as the current website, old website, LinkedIn profile, LinkedIn recommendations, CVs, project notes, proposals, and testimonials.
   - Separate known facts, plausible inferences, and unknowns.
   - Ask small, prioritized batches of questions instead of trying to solve all gaps at once.
   - Extract project facts and reference signals before rewriting.

5. Find the professional arc.
   - Identify recurring themes across projects: industries returned to, capabilities that deepen, scale that increases, and lessons reused from one context in another.
   - Connect projects where later work clearly builds on earlier experience.
   - Use the arc to explain why the consultant's profile is more than a loose collection of engagements.
   - Keep it concise: create context and momentum, not a biography or a sports-documentary script.

6. Choose project prominence by relevance, not chronology alone.
   - Feature 3-5 "signature projects" or "selected highlights" near the top.
   - Promote older but high-signal work when it proves the desired positioning.
   - Keep a secondary "additional selected projects" list for breadth, not for important work that merely happens to be older.
   - Treat recognizable enterprise names as signal when they support the profile. Examples in this user's context include Heidelberg Materials, Otto Group/Witt, Deutsche Bank, Deutsche Telekom, and 1&1.

7. Rewrite projects as proof points.
   - Prefer Outcome -> Action -> Scope when impact is known.
   - Prefer Challenge -> Role -> Deliverable when outcomes are confidential or unavailable.
   - Name the industry, organization type, scale, and responsibility level where possible.
   - Avoid vague responsibility lists and generic technology stacks without business context.

8. Make the profile scannable.
   - Put the strongest positioning and proof in the first screen/page.
   - Use front-loaded headings, short bullets, and grouped evidence.
   - Avoid walls of text and burying high-signal clients in long chronological lists.

9. Calibrate personality, values, and boundaries.
   - Identify what makes the consultant memorable: working style, professional values, taste, judgment, collaboration style, and recurring stances.
   - Treat personality as a buyer-fit layer, not a decorative sidebar. The reader should understand what kind of person they may hire, what gives them energy, how they think, and what they want to create or improve.
   - Translate raw personality markers into buyer-safe language. For example, "Nein-Sager" may become "constructive dissent", "clear product judgment", "says no when it protects focus, quality, or users", or "brings clear boundaries to ambiguous product work".
   - State relevant boundaries when they clarify fit: what the consultant does well, what they do not pretend to do, which roles they avoid, and where they need complementary specialists.
   - Use background signals when they explain strengths. A design/webdesign origin, visual judgment, layout/color sensitivity, designer collaboration, and autodidactic engineering path can support a bridge positioning between product, design, and software delivery.
   - Include personal motivation and professional ambition when they make the profile more human and commercially relevant. Avoid private biography that does not help the reader decide fit.
   - Keep personality grounded in proof. Do not make the profile quirky for its own sake; show how the stance improves outcomes, collaboration, quality, or focus.

10. Localize the profile instead of translating it literally.
   - For DACH/German profiles, favor precise, credible, evidence-heavy language and avoid exaggerated sales claims.
   - For US/global English profiles, make the value proposition more explicit and outcome-led.
   - For LinkedIn, combine searchable keywords with a human first-person summary, visible proof, recommendations, media, and posts.
   - Keep bilingual variants aligned in facts but adapted in tone, section order, and terminology.

11. Run a language and persuasion pass.
   - Make claims clear, concise, active, and specific.
   - Add positive framing where the evidence supports it; do not leave strong work sounding neutral or accidental.
   - Treat Dan Berlin's coaching heuristic as a useful default: self-presentation is often discounted by readers, so credible strengths may need to be stated more warmly and explicitly than feels natural to the writer.
   - Remove empty hype, generic AI-ish phrasing, and unsupported superlatives.

12. Preserve truthfulness.
   - Do not invent metrics, client claims, leadership scope, or outcomes.
   - If metrics are missing, use bounded qualitative evidence: "enterprise-scale", "regulated banking environment", "multi-brand retail group", "telecommunications customer platform", or similar factual context.
   - Flag claims that need confirmation before publishing.

## Recommended Output

For an audit, return:

1. **Profile Thesis** - one proposed positioning sentence.
2. **Prominence Map** - which projects should be signature, supporting, or archive-level, with rationale.
3. **Source and Gap Inventory** - what is known, missing, inferred, duplicated, or needs permission.
4. **Interview Questions** - prioritized questions that resolve the most important uncertainties.
5. **Narrative Arc** - the through-line that connects projects, capabilities, industries, and recurring strengths.
6. **Personality, Boundaries, and Buyer Fit Strategy** - which values, motivations, stances, strengths, limits, and background signals should be visible, and how to word them professionally.
7. **Channel and Region Strategy** - how the profile should differ for PDF/CV, website, LinkedIn/XING, and German vs English audiences.
8. **Structure** - proposed profile sections in order.
9. **Voice Strategy** - recommended tone for DACH/German, English/international, LinkedIn, and any "more positive" variant.
10. **Rewrite Samples** - improved headline, intro, LinkedIn/About version if relevant, and 3-5 project entries.
11. **Gaps** - missing metrics, facts, client permissions, or platform/API constraints to verify.

For a full rewrite, return a complete profile with:

- headline
- 3-5 line executive summary
- short professional arc / through-line
- optional personal motivation, working-principles, or role-fit block
- capability pillars
- selected highlights or signature projects
- industry/client context
- additional selected projects
- LinkedIn/About and headline variants when a social profile is in scope
- tone variants when useful: restrained DACH, warmer DACH, international English, LinkedIn
- skills/tooling only where it reinforces the thesis

## Quality Bar

Prefer concrete, commercially legible language over career-history narration. A strong output should make the reader think, within 30 seconds: "I understand what this person does, where they have done it, and why they are credible for this kind of work."
