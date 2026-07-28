# Forge Access Boundary

Use this reference before reading or changing pull-request or merge-request
state. It keeps provider access separate from review judgment.

## Choose one access path

Select one coherent path per change and keep it for the run:

1. **Connected forge tools.** Prefer host-provided, already authenticated app,
   MCP, or connector tools when they expose the required capabilities. They do
   not depend on a shell sandbox being able to read a local CLI login.
2. **Provider CLI or API.** Use an installed, authenticated provider tool when
   it covers the required capabilities. Examples include `gh` for GitHub,
   `glab` for GitLab, and `tea`, `fj`, or the documented REST API for
   Gitea/Forgejo. Tool presence alone is not proof that review submission,
   threads, checks, or inline anchors are supported.
3. **Caller-supplied review context.** When live access is missing or the caller
   already owns provider integration, accept the complete context below, run
   Mode A's normal inspection ladder, and return a caller-owned review result.

Do not mix adapters merely because one call is awkward. Mixing identities,
timestamps, pagination, and thread IDs can make "since my last action" and
review delivery inconsistent. A local Git checkout may still supply code search
and worktree operations; the selected forge adapter owns remote state.

Never copy tokens, credential files, keychain entries, or login output into a
sandbox to make a CLI work. If a CLI cannot access its stored login or the
network from the shell, treat that path as unavailable: use a connected tool,
an explicitly permitted host execution path, an already injected short-lived
automation token, or caller-supplied context. Do not print or persist tokens.

## Capability contract

A live Mode A adapter must be able to:

- resolve the forge, repository, and exact change;
- resolve the review identity, or accept an explicit caller-supplied identity;
- read metadata, base/head refs and SHAs, commits, the full diff, earlier
  reviews, comments, and unresolved threads;
- read mergeability, behind-base state, checks, deployments when needed, and
  linked intent;
- publish the chosen review outcome and any supported inline or top-level
  comments.

Mode B additionally needs:

- a writable head branch and a safe local fetch/push route;
- thread replies and, when supported, resolution;
- the provider's safe branch-update operation or enough refs for a local merge;
- check-log access and a bounded failed-job retry when CI recovery is requested.

Resolve these capabilities once. If a required read capability is absent, ask
for or report the exact missing evidence; do not silently perform a weaker
review. If publishing or an inline-anchor feature is absent, finish the
judgment and return the exact caller-owned review result instead of pretending
it was posted. Mode B cannot run autonomously without its write capabilities.

## Identity

Use a caller-supplied `reviewer_identity` when present. Otherwise resolve it
through the selected adapter. Keep it distinct from `delivery_actor`:

- `reviewer_identity` identifies earlier actions used for incremental review;
- `delivery_actor` is the user, app, or bot account the provider will attribute
  a new review to.

An app installation or automation token may have no user endpoint. That is not
an authentication failure and must not force a user lookup. The caller can
supply the app or bot identity explicitly. If no earlier-review identity is
available, inspect the full current change and disclose that incremental
"since last review" filtering was not possible.

## Provider selection notes

| Provider | Preferred live path | Fallback |
| --- | --- | --- |
| GitHub | Connected GitHub tool with the required capabilities | `gh` or the documented GitHub API; read [GitHub CLI fallback recipes](gh-recipes.md) only for this path |
| GitLab | Connected GitLab tool | `glab` or the documented GitLab API |
| Forgejo / Gitea | Connected instance-specific tool | `fj`, `tea`, or the documented compatible API after verifying every required capability |
| Other forge | Connected provider tool | Provider CLI/API only when it satisfies the same contract |

Names and command shapes are examples, not dependencies of the skill. Prefer
provider documentation over translating a GitHub command by analogy.

## Caller-supplied full review

This is Mode A with caller-owned provider access, not Mode C's review-item
classifier. The caller supplies equivalent structured fields for:

- `change`: stable ID and URL, title, description, author, draft state, base and
  head refs and SHAs;
- `reviewer_identity` and, when different, `delivery_actor`;
- `intent`: linked ticket or other authoritative scope, plus repository
  guidance relevant to the review;
- `diff`: a unified diff or changed files with patches and stable new-side
  anchors;
- `history`: commits, earlier reviews, comments, unresolved threads, and enough
  timestamps to determine what changed since the supplied identity's last
  action;
- `state`: checks, mergeability, behind-base state, and relevant deployment
  evidence;
- `repository_context`: any unchanged callers, contracts, sibling patterns, or
  files needed to assess impact beyond the diff;
- `authority`: allowed reads and the caller's ownership of publishing,
  implementation, approval, replies, and delivery.

Missing non-critical fields must be named in `missing_evidence`. Missing
critical-boundary evidence must prevent approval. Do not discover live
repository, forge, CI, deployment, or thread state unless the caller explicitly
authorizes a separate access path.

Return exactly one JSON object without Markdown fences or surrounding prose:

    {
      "schema_version": "pr-review-result/v1",
      "mode": "caller_owned_review",
      "change_id": "preserve-the-caller-id",
      "reviewer_identity": "supplied-or-resolved-identity",
      "caller_constraints": {
        "publication_owner": "caller",
        "implementation_owner": "caller",
        "delivery_owner": "caller"
      },
      "decision": "approve",
      "body": "Exact top-level review body",
      "inline_comments": [
        {
          "path": "src/example.ts",
          "line": 42,
          "start_line": null,
          "side": "new",
          "body": "Exact inline comment"
        }
      ],
      "missing_evidence": [],
      "caller_actions": ["publish_review"]
    }

Use only `approve`, `request_changes`, `comment`, or `no_action` for
`decision`. Preserve the caller's change ID. Bodies are publication-ready, not
summaries. `caller_actions` names required provider or delivery actions without
claiming they happened. Use `no_action` only when no new action is warranted,
not as a substitute for naming missing critical evidence.
