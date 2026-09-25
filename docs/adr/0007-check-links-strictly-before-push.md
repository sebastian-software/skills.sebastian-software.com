# ADR 0007: Check Links Strictly Before Push and Leniently in CI

- Status: Accepted
- Date: 2026-09-25

## Context

The skills cite primary sources: laws, standards, official spelling rules,
platform documentation, and browser-support data. Those links let maintainers
re-verify the claims that go stale, so every link should keep being checked,
not only the ones a change touches.

The link check ran only on GitHub-hosted runners and failed on any error. Many
hosts answer runners with 403, 503, redirects, or timeouts while serving
people normally, so pull requests failed on links they did not touch. Each
false failure added an entry to `.lycheeignore`, which had grown to 50 entries.
An ignored link is never checked again: a strict run without the list on
2026-09-25 found two genuinely dead links hidden behind it.

The same comparison showed where the failures come from. From a contributor
network, 14 of 1,514 links failed, mostly the same few hosts that fail
everywhere. From runners, nearly every failure was a status or timeout that a
contributor network did not see.

## Decision

1. Every run checks every Markdown and site link.
2. A pre-push hook managed by Lefthook runs the check from the contributor's
   network and fails on any error. `mise install --locked` installs the hook,
   and results are cached for a day so repeated pushes stay fast.
3. CI checks the same links on pull requests and weekly, but fails only when a
   link is gone (404, 410), an anchor is missing, or a host is unreachable. It
   accepts other statuses and timeouts that runners commonly receive.
4. `.lycheeignore` lists only links that no checker can verify from any
   network, each with its reason and date. A host that refuses some
   contributor networks but not CI is excluded from the local check only.
5. Tools are pinned through mise, not npm, so contributors need no Node
   toolchain for hooks or link checks.

## Consequences

- Pull requests fail on dead links, not on runner blocking.
- Blocked or slow hosts are verified from contributor networks before a push,
  so they are no longer excluded permanently.
- The strict check depends on a contributor having installed the hook. Pushes
  without it (other machines, agents, bots) rely on the lenient CI check.
- A temporarily unreachable host can block a push; `LEFTHOOK_EXCLUDE=links`
  skips the job once.

See [contributor checks](../contributor-checks.md) for the workflow.
