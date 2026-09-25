# ADR 0008: Merge the Service Growth System and Dual-License the Collection

- Status: Accepted
- Date: 2026-09-25
- Amends: [ADR 0004](0004-effective-disciplines.md)

## Context

The Service Growth System was published separately under Apache-2.0 as one
routed skill for service businesses. It covers offers, pilots, messaging,
content, outbound, conversations, consultative sales, funnels, paid campaigns,
CRM, and operations.

About half of it overlapped existing disciplines: positioning, messaging,
copywriting, social content, LinkedIn conversations, lead magnets, and pricing.
When both were installed, one request such as "position my offer" or "turn this
DM into a call" activated both skills. The agent then had to reconcile two
frameworks for the same decision: an offer card next to a positioning brief and
a commercial thesis, and a six-step chat-to-meeting path next to an eight-step
one. ADR 0004 had consolidated the collection to remove exactly this kind of
trigger competition.

The other half filled real gaps. No discipline covered outbound prospecting,
consultative sales, paid lead campaigns, CRM design, or an end-to-end
bottleneck view for a service business.

A prompt audit of the standalone skill found no dated emphasis or scaffolding.
Its structural defects were a second routing layer (`routes/*.md`) that
restated the leaf checklists and had already drifted from them, and one
authority rule repeated in seven places with different thresholds.

The collection was MIT-licensed, while the growth system was Apache-2.0. Both
have the same copyright holder.

## Decision

1. Merge the growth system into the existing disciplines instead of adding a
   seventh skill. Its gaps become five `effective-marketing` routes: Service
   Business Growth, Outbound Prospecting, Consultative Sales, Paid Campaigns,
   and CRM and Sales Operations.
2. Its overlaps become focused references on existing routes: service offer
   (Positioning), positioning thesis (Messaging), service landing page
   (Copywriting), video and audio content and the content journey (Social).
   Service pricing and service pilots go to `effective-product` (Pricing and
   Discovery).
3. Drop the intermediate routing layer. Keep the authority rule at the level of
   each discipline's `SKILL.md`, where it applies once.
4. License the whole collection as `MIT OR Apache-2.0` at the user's option
   (`LICENSE-MIT`, `LICENSE-APACHE`). Contributions are dual-licensed the same
   way unless stated otherwise.

## Alternatives Considered

### Keep the growth system as a separate skill

Rejected. It fails the ADR 0004 test for a new discipline: most of its outcomes
already have an owner, and its description competes with `effective-marketing`
and `effective-product` for the same requests. Its main strength, the
end-to-end bottleneck view, is preserved as the Service Business Growth route.

### Add it as a seventh `effective-` discipline

Rejected for the same reason. Sales and CRM take a verified offer to market and
belong with the discipline that already owns launch and sales enablement.

### Relicense only the merged files

Rejected. File-level license mixing is hard to explain in installs that select
one discipline, and a collection-wide dual license gives every user the same
choice.

## Consequences

- `effective-marketing` grows from 12 to 17 routes. Its description now names
  prospecting, sales, paid campaigns, CRM, and service-business growth, so the
  blind routing review must cover the new boundaries: sales versus launch
  enablement, CRM configuration versus application data models, and service
  pricing versus the sales conversation.
- Growth-system users map old commands to routes through
  [MIGRATION.md](../../MIGRATION.md).
- Skill READMEs carry the dual-license notice, and the README validator
  enforces it.
