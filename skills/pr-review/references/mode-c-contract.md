# Mode C JSON Contract

The operating constraints and exact output contract for Mode C (caller-owned
analysis handoff). SKILL.md defines when Mode C applies; this file defines what
it consumes, what it must not do, and the response shape.

## Operating constraints

The caller supplies:

- resolved repository or change context and the linked intent or scope;
- review items with stable IDs and the available author, location, thread, and
  surrounding-code evidence;
- authority, approval, and delivery ownership;
- allowed and prohibited actions plus delivery requirements.

Analyze only that material. Do not discover or inspect repository, Git, forge,
CI, deployment, or thread state. Do not modify the working tree, commit, push,
rebase, rewrite history, post or resolve feedback, recover CI, or deliver work.
Caller constraints override every autonomous Mode B default.

## Response shape

Return exactly one JSON object without Markdown fences or surrounding prose. Use
this unfenced shape and replace the example values with the caller's values:

    {
      "schema_version": "pr-review-handoff/v1",
      "mode": "caller_owned_analysis",
      "caller_constraints": {
        "authority_owner": "caller",
        "approval_owner": "caller",
        "delivery_owner": "caller",
        "allowed_actions": ["analyze_supplied_context"],
        "prohibited_actions": ["rebase", "force push"],
        "delivery_requirements": ["one new commit if accepted"]
      },
      "missing_inputs": [],
      "items": [
        {
          "id": "preserve-the-caller-id",
          "classification": "valid_in_scope",
          "recommended_action": "caller_fix",
          "rationale": "Evidence-backed reason",
          "proposed_reply": null,
          "missing_evidence": []
        }
      ]
    }

## Field rules

Preserve every item ID exactly. Preserve supplied constraints without silently
broadening authority; use `null` or an empty array for absent constraint values
and name the gap in `missing_inputs`.

Use only these classifications: `valid_in_scope`, `valid_out_of_scope`,
`unsupported`, `question_or_information`, and `needs_evidence`.

Use only these recommended actions: `caller_fix`, `caller_follow_up`,
`caller_reply`, `caller_decline`, `caller_request_evidence`, and `no_action`.

Match them consistently:

- `valid_in_scope` normally uses `caller_fix`;
- `valid_out_of_scope` uses `caller_follow_up` or `no_action`;
- `unsupported` uses `caller_decline` or `caller_reply`;
- `question_or_information` uses `caller_reply` or `no_action`;
- `needs_evidence` uses `caller_request_evidence`.

Use `unsupported` only when supplied evidence supports rejecting a finding,
including a demonstrated misunderstanding of the code or intended behavior.
When context is insufficient, use `needs_evidence`, list the exact missing proof
in `missing_evidence`, and do not invent a decision, code fact, or reply. The
caller decides whether and how to act on every recommendation.
