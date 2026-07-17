[← Sebastian Software Skills](../../README.md)

# Decision Records

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Keep important project reasoning understandable after the meeting, the pull
request, and the agent session are over.**

Decision Records helps agents create, review, update, supersede, and audit
Architecture Decision Records without inventing a private memory system. It
uses repository-owned Markdown for durable technical, product, design, content,
marketing, security, operational, and communication choices.

## What It Can Deliver

- proposed or accepted ADRs that follow the repository's convention
- clear context, decision drivers, considered options, and consequences
- supersession that preserves accepted history
- an opt-in living-record lifecycle for repositories where one mutable file is
  intentionally the current decision
- reviews for stale rationale or implementation drift
- decision indexes and a minimal default convention when none exists
- explicit review triggers for choices that may need to change later

## Use It When

Record a decision when it is durable, cross-cutting, expensive to reverse, or
needs to coordinate several people, tools, channels, or future sessions. The
skill first discovers existing ADR conventions and related accepted records so
the new artifact belongs to the project rather than to one agent.

## Example Prompts

```text
Write an ADR for choosing server-rendered React over a client-only application,
including the rejected options and review triggers.

Review our accepted ADRs against the current code and identify meaningful
decision drift.

Supersede this branding decision without rewriting the historical record.

Update our living project-setup ADR in place, preserving its localized status
vocabulary and its intentionally owned configuration table.

Decide whether this local refactor deserves an ADR or should remain in the pull
request explanation.
```

See [SKILL.md](SKILL.md) for the lifecycle, default convention, and operating
rules.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill decision-records
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian decision-records
dalo approve skill sebastian:decision-records
dalo sync
```

## Related Skills

- [Product Management](../product-management/README.md) develops the product
  decision before its durable rationale is recorded.
- [Effective Web](../effective-web/README.md) implements and verifies frontend
  decisions against the accepted direction.
- [Codebase Improvement](../codebase-improvement/README.md) separates audit
  findings and delivery plans from long-lived decisions.
- [Product Naming](../product-naming/README.md) produces a naming recommendation
  whose rationale may warrant a decision record.

## Scope

An ADR is not a task log, implementation plan, audit finding, or changelog.
Exact configuration values stay in their owning artifacts unless the repository
explicitly declares a narrowly scoped living setup record as their source of
truth. The skill preserves established conventions and keeps immutable records
as the conservative default instead of silently rewriting old decisions.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
