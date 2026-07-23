---
name: metro-english
description: >-
  Rewrite text into relaxed US metropolitan team English: the kind of natural,
  direct, human voice used in Slack threads, GitHub or Linear issue comments, PR
  notes, async updates, and internal team communication. Use this skill whenever
  the user asks to make writing sound casual, less formal, less AI-generated,
  more human, more Slack-like, more startup/team-like, or closer to everyday New
  York, San Francisco, or Silicon Valley professional English. Also use it when
  the user provides German or stiff English and wants it turned into natural
  English for team communication.
---

# Metro English

Rewrite text so it sounds like a smart teammate wrote it quickly but carefully:
clear, direct, warm enough, and a little loose. The target voice is polished
casual with a bit of startup Slack energy, not corporate copy and not internet
slang.

This skill borrows the stance of `humanizer` from the separately managed DALO
`marketingskills` catalog: remove obvious AI writing patterns, then add human
rhythm and judgment. The point is not to make the text fancy. The point is to
make it sound like a real person communicating with a real team.

## Decision Context

Read accepted ADRs and house-style guidance when the text belongs to a project
with a recorded audience relationship, voice, formality, terminology, or
channel rule. Apply the Metro English treatment inside those constraints rather
than replacing the organization's voice with a generic startup persona.

An explicit user request may intentionally override the recorded style for one
artifact; surface the divergence when it could create cross-channel drift. Use
`decision-records` when the work establishes or changes a durable communication
direction instead of creating a Metro-English-specific memory file.

## What this skill does

Use this for:

- Slack or chat messages
- GitHub, GitLab, Linear, Jira, and issue comments
- PR review comments and handoff notes
- Async project updates
- Short internal announcements
- Quick feedback, nudges, and status replies
- German-to-English rewrites for team communication
- Stiff English that needs to sound more natural

When the user gives German source text, translate the meaning into natural team
English instead of translating word by word.

## Voice target

Aim for:

- Everyday US professional English, closer to NYC/SF/Silicon Valley team chat
  than to corporate comms.
- Shorter sentences with natural variation.
- Contractions where they sound normal: "I'm", "we're", "that's", "doesn't".
- Plain verbs: "fix", "ship", "check", "move", "cut", "keep", "drop",
  "split", "follow up".
- Light personality: "I think", "feels like", "this part is a bit off",
  "nice catch", "I'd keep this simpler".
- Direct asks and clear next steps.
- Respectful confidence. Be candid without sounding harsh.

The text should feel written in the flow of work. It can be a little imperfect,
but it should not be careless.

## Rewrite rules

1. Preserve the user's intent, facts, names, constraints, and decision.
2. Make the message shorter unless the user asked for detail.
3. Replace formal scaffolding with natural phrasing.
4. Remove generic praise and chatbot politeness.
5. Use first person when it helps: "I'd", "I think", "I don't think we need".
6. Keep technical language when it carries meaning, but drop padded wording
   around it.
7. Make the ask obvious: what should happen, who is blocked, or what decision is
   needed.
8. Keep a human rhythm. Mix one-line sentences with slightly longer ones.
9. If the source is tense or critical, make it calmer without hiding the point.
10. If the source is too blunt, add a little warmth without adding fluff.

## Avoid

Do not add fake local flavor. No forced NYC, SF, or Silicon Valley stereotypes.
No "bro", "hustle", "move fast", "10x", "vibes", or VC-speak unless the user
clearly wants that.

Avoid AI and corporate patterns:

- "delve", "crucial", "pivotal", "robust", "seamless", "leverage"
- "underscores", "showcases", "serves as a testament"
- "I hope this helps", "certainly", "great question", "you're absolutely right"
- "not only... but also..."
- forced rule-of-three lists
- title-case mini headers in short comments
- bolded label bullets like "**Issue:**"
- em dash-heavy prose
- generic upbeat endings like "exciting times ahead"

Avoid sounding:

- overly polished
- performatively casual
- passive-aggressive
- sycophantic
- like a press release
- like a chatbot explaining its own work

## Context presets

### Slack or team chat

Keep it compact. One short paragraph is usually enough. If there are actions,
use 2-4 bullets. Use "quick" only when it actually fits.

Good patterns:

- "Quick heads-up: ..."
- "I think we can keep this simple: ..."
- "I'm blocked on ..."
- "Can someone sanity-check ..."
- "I'll take the first pass and post an update here."

### Issue comments

Be specific about the current state, the problem, and the next step. Avoid long
setup. If the issue is not ready, say what is missing.

Good patterns:

- "I can reproduce this with ..."
- "This looks like ..."
- "I think the fix should live in ..."
- "Let's split this from ..."
- "I don't think this is part of this ticket."

### PR review comments

Sound like a teammate reviewing code, not a compliance bot. Be clear about
severity. If it is blocking, say so plainly. If it is a suggestion, keep it
light.

Good patterns:

- "This looks good overall. One thing I'd change before merging: ..."
- "Small suggestion, non-blocking: ..."
- "I think this should be a request-change. The current path can ..."
- "Nice cleanup. The part I'm less sure about is ..."

### Async updates

Lead with the actual status. Then add the blocker, decision, or next step. Do not
bury the point under context.

Good patterns:

- "Status: ..."
- "What's done: ..."
- "What's left: ..."
- "The decision we need is ..."
- "I'll follow up once ..."

### Docs-adjacent notes

Stay natural, but be a little more durable than Slack. Keep contractions if they
sound right. Avoid jokes or throwaway phrasing that will age badly.

Good patterns:

- "This doc is the source of truth for ..."
- "Keep this section focused on ..."
- "If this changes, update ..."
- "This is intentionally out of scope for now."

## Examples

### Formal PR review comment

Input:
> The implementation appears to be largely correct. However, it is important to
> note that the error handling path could potentially lead to confusing behavior
> for users in the event that the request fails.

Output:
> This mostly looks right. I'd tighten the error path before merging, though. If
> the request fails, users can end up with a pretty confusing state.

### Stiff Slack update

Input:
> I would like to provide a brief update regarding the current status of the
> migration effort. We have completed the initial investigation and are now
> proceeding with implementation.

Output:
> Quick update on the migration: the initial investigation is done, and we're
> moving into implementation now.

### AI-ish issue comment

Input:
> This issue highlights a crucial gap in the current validation landscape and
> underscores the need for a more robust approach to handling malformed input.

Output:
> This looks like a validation gap. We should handle malformed input earlier, so
> the downstream code never sees this shape.

### German team note

Input:
> Ich glaube, wir sollten das nicht in diesem PR machen. Das ist eigentlich ein
> separates Thema und macht den Review nur unnoetig gross.

Output:
> I don't think we should do this in this PR. It's a separate thread, and adding
> it here will just make the review harder than it needs to be.

### Too blunt

Input:
> This is wrong. Please redo it.

Output:
> I don't think this is the right path yet. Can you take another pass and align it
> with the approach in the existing flow?

## Output format

By default, return only the rewritten text.

Only include notes, alternatives, or an explanation when the user asks for them.
If the user asks for options, provide two:

1. A polished casual version.
2. A slightly looser Slack-style version.

If the original has important ambiguity, preserve it or ask a short question
before rewriting. Do not invent facts, decisions, approvals, deadlines, or blame.

## Routing Boundaries

- Route technical, legal, product, and documentation correctness to the skill
  that owns the underlying work; this skill improves language, not substance.
- Route locale-specific typography and punctuation to `locale-typography`.
