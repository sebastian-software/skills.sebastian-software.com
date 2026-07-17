[← Sebastian Software Skills](../../README.md)

# Product Design

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Turn product evidence into an understandable system, purposeful environment,
and testable experience.**

This skill connects research, problem framing, interaction modeling,
information architecture, prototyping, and design craft. It chooses artifacts
because they resolve a decision—not because a standard process says every
project needs another workshop or canvas.

## What It Can Deliver

- provisional and evidence-updated design briefs
- research plans, behavioral interview scripts, and synthesis structures
- problem-space, expectation, and mental-model documentation
- problem, empowerment, opportunity, and How Might We framing
- object, relationship, moment, flow, journey, and navigation models
- thumbnail, wireframe, prototype, test, and delivery plans
- purposeful visual-reference studies and in-context character explorations
- autonomy, learnability, motivation, and interaction-risk reviews

## Use It When

Use Product Design when the product direction is sufficiently clear to shape
an experience, but the objects, structure, interaction model, or design
direction are not. It is also useful earlier when research and problem framing
must prevent a team from polishing the wrong solution.

## Example Prompts

```text
Turn these interview observations into a traceable problem-space model and two
distinct design directions without inventing findings.

Model this collaborative product as objects, relationships, permissions,
states, moments, and recoverable actions before we draw screens.

Review this onboarding and reward loop for learnability, autonomy, and
manipulative engagement mechanics.

Choose the smallest prototype that can test our navigation model and the risky
state transition in this workflow.
```

See [SKILL.md](SKILL.md) for the routed workflow, operating principles,
boundaries, and default deliverable.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill product-design
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian product-design
dalo approve skill sebastian:product-design
dalo sync
```

## Related Skills

- [Product Management](../product-management/README.md) decides strategy,
  audience, outcomes, viability, scope, prioritization, and release direction.
- [Effective Web](../effective-web/README.md) specifies and implements the
  browser experience with accessibility, performance, and verification.
- [Decision Records](../decision-records/README.md) preserves durable design
  decisions, tradeoffs, and reopening conditions.
- [Web Legal Compliance](../web-legal-compliance/README.md) handles privacy,
  consent, tracking, and jurisdiction-specific web obligations.

## Scope

This skill shapes experience from supplied or gathered evidence. It does not
manufacture participants, observations, usability results, or product-market
certainty, and it does not replace specialist implementation, legal, or formal
research-operations work.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
