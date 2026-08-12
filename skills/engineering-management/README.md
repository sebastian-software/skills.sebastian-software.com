[← Sebastian Software Skills](../../README.md)

# Engineering Management

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Design a clearer, healthier management system for product, design, and
engineering work.**

This skill helps agents diagnose ownership, delegation, coaching, decision
paths, meetings, team boundaries, and cognitive load before proposing a
management intervention. It keeps product outcomes, operating constraints, and
human consequences visible together.

## What It Can Deliver

- responsibility and decision-right maps
- management-system and meeting audits
- coordination-medium choices for asynchronous, synchronous, paired, workshop,
  and in-person work
- one-to-one, coaching, feedback, and delegation plans
- team-boundary and cognitive-load diagnoses
- product-design-engineering working agreements
- evidence-led transitions to AI-assisted work with explicit human decisions,
  bounded pilots, safeguards, and request-to-operation measures
- small, reversible organizational experiments with safeguards
- review plans that combine delivery, quality, and human signals

## Use It When

Use Engineering Management when ownership is unclear, leaders are bottlenecks,
teams are overloaded, decisions stall between disciplines, one-to-ones lack
purpose, or someone proposes a reorganization without evidence about the work.

## Example Prompts

```text
Our head of engineering approves every technical decision. Diagnose the system
and design the smallest delegation change that preserves necessary control.

Review our recurring meetings and decision paths. Keep the governance we
actually need, but remove delay and duplicated attendance.

Our remote team has recurring tacit-knowledge and trust problems. Decide which
work needs documents, calls, pairing, workshops, or in-person collaboration
without imposing a universal office or meetup cadence.

Two teams share three specialists and both miss commitments. Determine whether
the problem is team boundaries, cognitive load, capacity, or unclear priority
before recommending a reorganization.

Clarify how product, design, engineering management, and technical leadership
should collaborate on discovery and delivery without creating a feature
factory.

Help this engineering team adopt AI agents without turning generated output
into a productivity quota or leaving architecture and acceptance decisions
unowned.
```

See [SKILL.md](SKILL.md) for the evidence model, workflow, safeguards, routing
boundaries, and default deliverable.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill engineering-management
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian engineering-management
dalo approve skill sebastian:engineering-management
dalo sync
```

## Related Skills

- [Product Management](../product-management/README.md) owns product strategy,
  outcomes, customer evidence, and roadmap choices.
- [Product Design](../product-design/README.md) owns product research,
  interaction design, and prototype evidence.
- [Software Architecture](../software-architecture/README.md) owns system
  boundaries and evolutionary technical decisions.
- [Decision Records](../decision-records/README.md) preserves durable
  cross-functional choices and their review triggers.
- [Effective Workflow](../effective-workflow/README.md) takes an authorized
  software change through implementation and verification.

## Scope

This skill supports professional management judgment. It does not replace
qualified People/HR, employment-law, compensation, occupational-health,
security, or crisis expertise, and it does not infer private employee intent or
performance from weak proxies.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
