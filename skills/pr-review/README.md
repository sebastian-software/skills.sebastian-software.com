[← Sebastian Software Skills](../../README.md)

# PR Review

[![Maintained by Sebastian Software](https://img.shields.io/badge/Maintained%20by-Sebastian%20Software-0f172a.svg)](https://oss.sebastian-software.com/)

**Review and maintain GitHub pull requests like a trusted teammate: warm,
specific, technically serious, and focused on helping the work land.**

PR Review gives agents an end-to-end workflow for reviewing other people's
pull requests and maintaining their own. It combines branch-aware inspection,
impact-led findings, human feedback, CI diagnosis, author follow-up, and
delivery hygiene without manufacturing friction over taste or nits.

## Operating Modes

- **Reviewing others:** understand the change, inspect earlier feedback, find
  consequential issues, and approve or request changes.
- **Maintaining your own PRs:** act on valid review comments, fix the branch,
  recover CI, keep it current, and close the feedback loop.
- **Caller-owned analysis:** classify review items from context supplied by
  another workflow and return versioned JSON while that caller retains approval,
  implementation, and delivery.

The autonomous modes can run together when a review round reveals work the agent
is authorized to implement. Caller-owned analysis is deliberately read-only and
provider-neutral, so orchestration systems can reuse the review judgment without
adopting this skill's GitHub or delivery policies.

Caller-owned analysis is not a dry run. A dry run reads the real repository and
GitHub state, then previews the actions a direct user could apply. The handoff
uses only supplied context, performs no discovery or mutations, and leaves every
action with the caller.

## What Good Review Looks Like

- start with the actual product and maintenance impact
- recognize what the author did well
- block only on meaningful security, privacy, data, billing, reliability,
  accessibility, or product risk
- keep inline findings few, specific, and actionable
- separate branch regressions from infrastructure failures
- use natural human GitHub replies and verify fixes before resolving threads
- work in isolated worktrees and preserve unrelated local changes

## Example Prompts

```text
Review PR #482, check whether earlier feedback was addressed, and approve or
request changes.

Catch up on my open pull requests, fix valid review findings, and get the
branches ready to merge.

Run a dry review of this PR: show what you would post without changing GitHub.

Classify these supplied review items as a caller-owned handoff. Return the
versioned JSON contract only; I retain approval and delivery.

Diagnose the failing checks on this PR and determine whether the branch caused
them before making changes.
```

See [SKILL.md](SKILL.md) for setup, dry-run behavior, review quality, decision
rules, CI verification, voice, and safety rails.

## Install This Skill

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill pr-review
```

Or follow the [DALO setup guide](../../docs/dalo.md) and select it explicitly:

```sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source select sebastian pr-review
dalo approve skill sebastian:pr-review
dalo sync
```

## Related Skills

- [Effective Workflow](../effective-workflow/README.md) coordinates the wider
  path from request to verified handoff and invokes this skill for PR-scoped
  review, feedback follow-through, CI recovery, and merge judgment.
- [Codebase Improvement](../codebase-improvement/README.md) handles repository
  audits and improvement plans broader than one pull request.
- [Smart Dependency Updater](../smart-dependency-updater/README.md) creates and
  delivers coherent dependency-update pull requests.
- [Metro English](../metro-english/README.md) helps with natural team-facing
  review replies and status updates outside the full PR workflow.
- [Decision Records](../decision-records/README.md) captures durable choices
  discovered during review when the rationale must outlive the PR.

## Scope

Its autonomous workflows are designed around GitHub pull requests and assume
the required repository and GitHub access exists. Its caller-owned analysis
handoff is provider-neutral and cannot read or mutate repository, forge, CI, or
review state. The skill does not turn stylistic preferences into blockers,
overwrite unmanaged work, or publish feedback during a requested dry run.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
