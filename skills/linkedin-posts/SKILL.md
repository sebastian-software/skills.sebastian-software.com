---
name: linkedin-posts
description: >-
  Create LinkedIn posts, find LinkedIn content ideas, plan a LinkedIn content
  calendar, and tailor professional posts to an audience, voice, and goal. Use
  when the user mentions a LinkedIn post, LinkedIn content, LinkedIn idea,
  social media post for LinkedIn, post engagement, or content calendar for
  LinkedIn. Route engagement-to-pipeline diagnosis and acquisition strategy to
  linkedin-social-selling.
---

# LinkedIn Posts

Find worthwhile content ideas, write engaging LinkedIn posts, and build a
consistent, sustainable content calendar for the user's audience, voice, and
goal.

## Idea Database (86 ideas, 10 categories)

Load only the relevant category file based on the user's topic:

| Category | File | Count |
|---|---|---|
| Company & Project Updates | [references/company-project-updates.md](references/company-project-updates.md) | 10 |
| Educational Content | [references/educational-content.md](references/educational-content.md) | 8 |
| Engagement & Interaction | [references/engagement-interaction.md](references/engagement-interaction.md) | 10 |
| Industry Insights | [references/industry-insights.md](references/industry-insights.md) | 10 |
| Job & Career Opportunities | [references/job-career-opportunities.md](references/job-career-opportunities.md) | 6 |
| Networking & Community | [references/networking-community.md](references/networking-community.md) | 8 |
| Personal Stories & Reflections | [references/personal-stories-reflections.md](references/personal-stories-reflections.md) | 10 |
| Professional Development | [references/professional-development.md](references/professional-development.md) | 10 |
| Recognition & Appreciation | [references/recognition-appreciation.md](references/recognition-appreciation.md) | 6 |
| Tools & Resources | [references/tools-resources.md](references/tools-resources.md) | 8 |

**Format:** `ID|Topic prompt`. Entries are neutral topic cues; develop them
into original, evidence-led posts, choosing format and scope from the user's
goal and available capacity.

**Routing rules:**
- If the user asks for ideas in a specific category → load that file
- If the user wants a content calendar → load 2-3 relevant categories
- If the user wants to browse all → ask which category first, don't load all at once
- For writing a specific post → gather context (see below), use the matching category file for inspiration
- For a document/PDF carousel request → adapt a relevant prompt into an
  accessible document-post concept.

---

## Before Writing

Read accepted ADRs and existing brand or editorial guidance first. Reuse recorded
audience, form of address, voice, tone range, vocabulary, and claim boundaries
instead of asking for them again. If the request establishes a durable
cross-channel direction, use `decision-records`; do not create a LinkedIn-specific
voice-memory file.

Gather only the context that is neither recorded nor provided. Default to
inferring the audience, voice, and goal from the available context and stating
those assumptions briefly; ask only when a missing choice would materially
change the post:

If `linkedin-social-selling` already established the audience, content role,
source evidence, offer connection, language, and review owner, treat that as the
strategy handoff. Do not reopen settled acquisition strategy before drafting.
If those inputs are missing and the request depends on pipeline strategy rather
than a standalone post, route that discovery to `linkedin-social-selling`.

### 1. Topic & Goal
- What do you want to post about?
- What's the goal? (thought leadership, engagement, lead gen, brand awareness, hiring)

### 2. Audience
- Who should this reach? (industry peers, potential clients, recruiters, team members)
- What level? (C-suite, mid-level, entry-level, mixed)

### 3. Voice & Brand
- Which recorded voice applies, and does this post need a justified tonal shift?
- Professional, conversational, approachable, distant, restrained, or playful?
- Which form of address and locale convention applies?
- Personal story or company perspective?
- Any specific angle, opinion, or hot take?

### 4. Format Preference
- Text post, document (PDF carousel), poll, video script, or image/infographic concept?
- Short (under 200 words) or long-form (500+ words)?

---

## LinkedIn Post Writing Principles

### Hook First
The first 2-3 lines decide whether people click "see more." Lead with a bold
statement, surprising number, relatable problem, or story opening.

### Structure for Readability
Short paragraphs, line breaks between thoughts, generous white space — walls of
text get skipped.

### Drive Engagement
End with a question or position worth answering; ask for opinions, not likes.

### Be Specific Over Generic
- Bad: "Leadership is important"
- Good: "I fired our best performer last quarter. Here's why it was the right call."

### Authenticity Wins
- Use specific personal experience or evidence instead of generic advice.
- Share failures only when they are genuine and useful to the audience.
- Take a clear, supportable position instead of relying on platitudes.
- Never invent vulnerability, personal experience, customer quotes, numbers, or
  outcomes to make a post feel more authoritative or relatable.
- Reject engagement bait that asks for interaction without giving the intended
  audience a substantive reason to respond.

---

## Content Mix Strategy

Rotate across thought leadership, personal stories, educational content,
engagement prompts, company updates, and industry commentary so the presence
stays balanced rather than promotional.

---

## Post Formats & When to Use Them

### Text Post
Best for: stories, opinions, quick tips, hot takes.
Use line breaks and edit for clarity. Do not optimize to a fixed character target;
test readability and audience response instead.

### Document (PDF Carousel)
Best for: step-by-step guides, frameworks, listicles, case studies.
Use a readable, accessible document with a clear opening and an optional closing
prompt. Verify LinkedIn's current document requirements before publishing.

### Poll
Best for: gathering focused input or starting a relevant discussion.
Add enough context for a meaningful response. Do not treat a poll as a reach
guarantee.

### Video
Best for: personal connection, tutorials, behind-the-scenes.
Choose a length that serves the material, and add captions.

### Infographic
Best for: data, comparisons, processes, statistics.
Keep it simple and readable on mobile.

---

## Hashtag Strategy

- Use hashtags only when they help a relevant audience discover or understand the post.
- Keep them specific and readable; do not make reach claims from hashtag count or placement.
- Consider a branded hashtag for a recurring series when it helps people follow that series.

---

## Posting Cadence

- Do not prescribe a universal posting frequency or best time. Choose a sustainable
  cadence from the audience's needs, the team's capacity, and the account's own
  analytics.
- Treat platform mechanics, format limits, and distribution advice as volatile.
  Verify current official LinkedIn guidance before making them a requirement.
- Reply thoughtfully to substantive comments when it serves the conversation; do
  not claim that a fixed response window earns algorithmic rewards.

---

## Output Format

When writing a LinkedIn post, provide:

### The Post
Ready to copy-paste, properly formatted with line breaks and any relevant hashtags.

### Alternatives
For the hook, provide 2-3 variations with rationale.

### Engagement Boost Tips
Specific distribution and conversation-follow-up hypotheses to test for this post,
without presenting them as algorithm guarantees.

### Visual Suggestion
What image, carousel, or media would complement this post.

---

## Quick Idea Finder

Ask the user:
1. **What category interests you?** (Company Updates, Industry Insights, Personal Stories, Professional Development, Educational Content, Engagement, Networking, Tools & Resources, Recognition, Jobs & Career)
2. **What content type?** (Text, Poll, Video, Image/Infographic, or
   Document/PDF carousel — choose it after assessing the selected topic and
   available capacity)
3. **How much time do you have?** Map the answer to scope: Low effort → a
   short text post built from a single insight; Medium → a structured list or
   story post; High → a document/carousel or a multi-post series.

Then load the matching category file and present the 5 best-fitting topic cues.
Explain why each fits, then develop selected cues into original, evidence-led
post concepts.

---

## Routing Boundaries

- Route durable audience, voice, tone, form-of-address, terminology, claim, and
  channel decisions to `decision-records`.
- Route target-buyer, offer, profile, network, outreach, funnel, and pipeline
  strategy around the posts — including engagement-to-pipeline diagnosis — to
  `linkedin-social-selling`; consume its grounded brief when drafting posts
  inside a larger engagement.
- Keep general marketing-copy systems, standalone copy editing, broad
  AI-pattern cleanup, and persuasion analysis with their dedicated specialists.
  Apply the writing principles in this skill directly when no such specialist
  is available.
