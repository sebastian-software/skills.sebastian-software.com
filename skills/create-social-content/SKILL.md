---
name: create-social-content
description: >-
  Create, rewrite, review, and adapt evidence-led social media content across
  X or Twitter, Threads, Bluesky, Instagram, Mastodon, and unspecified or
  multiple social platforms. Use for posts, replies, quote posts, threads,
  captions, resource shares, product or project updates, social content ideas,
  series or calendars, cross-platform repurposing, matching an authorized voice
  from authored examples, or checking whether an angle repeats recent content.
  Route LinkedIn-only post work to linkedin-posts and LinkedIn acquisition
  strategy to linkedin-social-selling.
---

# Create Social Content

Turn a real idea, source, experience, or result into platform-native social
content without inventing authority or flattening every channel into the same
post.

## Workflow

1. Define the assignment:
   - mode: ideas, draft, rewrite, critique, reply, adaptation, series, or plan
   - speaker, audience, relationship, purpose, language, and desired response
   - target platform or platforms, format, media, length pressure, and deadline
   - supplied notes, source material, approved claims, and publication state

   Infer low-risk missing context and state the assumption briefly. Ask only
   when a missing choice would materially change the content. Route a
   LinkedIn-only post request to `linkedin-posts`; keep this skill when the
   platform is unspecified, non-LinkedIn, or the assignment spans channels.
2. Establish the evidence boundary. Read accepted ADRs and existing brand,
   editorial, terminology, and claim guidance before defining a new voice.
   Read [Source, voice, and content history](references/source-and-voice.md)
   when the task depends on personal or product context, voice matching,
   published-content history, or a freshness claim.
3. Choose the content unit and format. Reduce the piece to one useful claim,
   observation, story, result, resource, question, or invitation. Identify
   whether it is an original post, reply, quote or resource share, thread,
   product or project post, educational post, announcement, or visual caption.
   Read [Formats and remixing](references/formats-and-remixing.md) when the
   direction is open, the source is being repurposed, or several versions are
   requested.
4. Choose the platform treatment. Read
   [Platform adaptation](references/platform-adaptation.md) for a named
   non-LinkedIn platform, a multi-platform deliverable, or any request that
   depends on current platform behavior or exact limits. Treat platform
   mechanics as volatile and verify current official guidance before making an
   exact requirement consequential.
5. Search available content history before claiming novelty. Search narrowly
   for the subject, hook, claim, anecdote, proof point, resource combination,
   and ending. A repeated belief is acceptable only when the new piece adds
   current proof, a different mechanism, a meaningful update, or a new
   perspective. If no usable history is available, do not claim the angle is
   fresh or unprecedented.
6. Draft from the strongest grounded material:
   - preserve the user's strongest natural line when it already carries the
     thought;
   - make every sentence add context, reason, mechanism, proof, contrast,
     consequence, question, or conclusion;
   - keep authored statements separate from quoted or linked source material;
   - use personal experience, metrics, customer language, product behavior,
     and outcomes only when the available evidence supports them;
   - make a commercial connection explicit and proportionate instead of
     disguising a pitch as neutral advice.
7. Vary direction only when it helps the decision. When the angle remains open,
   return three materially different finished options and put the strongest
   first. Vary intent, structure, evidence, rhythm, or perspective rather than
   producing surface paraphrases. When the user requests one version or the
   evidence clearly supports one direction, deliver one polished version.
8. Adapt, do not merely truncate. Preserve the idea, facts, terminology, and
   claim limits across platforms, then rebuild the opening, pacing, context,
   interaction, media role, and ending for each channel.
9. Review before returning:
   - factual support, attribution, confidentiality, and permission
   - voice fit without manufactured quirks or copied distinctive phrases
   - editorial duplication and actual new value
   - platform fit, readability, media accessibility, and link context
   - proportionate call to action, disclosure, and commercial intent

## Operating Rules

- Treat supplied wording and verified authored examples as voice evidence, not
  text to splice together.
- Never invent vulnerability, biography, usage, customers, quotations,
  endorsements, metrics, team behavior, product capabilities, or results.
- Prefer a concrete mechanism or example over a generic hook. Do not add
  outrage, false certainty, fake urgency, or engagement bait to compensate for
  thin source material.
- Keep replies and comments proportional to the conversation. Do not turn every
  response into a miniature essay or unsolicited pitch.
- Use calls to action only when the reader has an earned, relevant next step.
  A useful ending may instead be a consequence, question, invitation, or clean
  stop.
- Preserve exact technical and product terms where changing them would weaken
  accuracy. Explain only what the selected audience needs.
- Suggest captions, alt text, transcripts, or visual structure when media is
  part of the deliverable. Do not treat accessibility as optional decoration.
- Do not create a private voice-memory folder, content ledger, or project
  schema unless the user asks to persist the system. Follow the project's
  existing editorial and decision conventions when persistence is authorized.
- Drafting does not authorize publishing, scheduling, liking, following,
  messaging, or other account mutations. Perform an external action only when
  the user explicitly requests it and the connected tool supports the required
  review and authorization.

## Default Deliverable

Return the finished copy first, grouped by platform when necessary. Add only
the assumptions, material alternatives, evidence gaps, or media notes the user
needs to judge or publish it. Do not bury ready-to-use content beneath a long
strategy explanation.

## Routing Boundaries

- Use `linkedin-posts` for LinkedIn-only ideas, calendars, formats, and
  drafting. For a multi-platform assignment that includes LinkedIn, keep the
  shared idea, evidence, and voice brief here and hand the LinkedIn expression
  to `linkedin-posts` without reopening settled choices.
- Use `linkedin-social-selling` for LinkedIn positioning, target buyers,
  profiles, networks, conversations, lead magnets, funnels, and pipeline
  strategy; consume its approved audience, offer, proof, and content role.
- Use `nonfiction-writing` for the standalone article, essay, newsletter, case
  study, or other long-form source; return here to turn it into social content.
- Use `product-marketing` to establish cross-channel positioning, messaging,
  proof, launches, and market-facing claim boundaries before expressing them
  socially.
- Use `consultant-profile` to establish professional positioning, career
  evidence, project facts, and permission-sensitive client context before
  turning them into public posts.
- Use `decision-records` for durable cross-channel choices about audience
  relationship, voice, tone, terminology, claims, and channel exceptions.
- Use `locale-typography` for locale-specific visible prose after the message,
  platform treatment, and target locale are known.
- Use `web-legal-compliance` when current advertising, endorsement,
  testimonial, promotion, privacy, or jurisdiction-specific disclosure
  requirements materially constrain the content. Treat its output as legal
  information and implementation support, not a legal opinion.
