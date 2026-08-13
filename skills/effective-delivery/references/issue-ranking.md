# Ranking contract

Normalize tracker records before calling `scripts/rank_issues.py`. The script
provides consistent grouping and a recency bias; the agent remains responsible for
truthful issue interpretation.

## Input

Pass a JSON array, or an object with an `issues` array. Each issue supports:

| Field | Required | Meaning |
| --- | --- | --- |
| `id`, `title`, `created_at` | yes | Stable tracker ID, title, ISO-8601 creation time |
| `updated_at`, `url` | no | Last activity and canonical link |
| `priority` | no | `urgent`, `high`, `medium`, `low`, `none`, `0`–`4`, `p0`–`p4` |
| `labels` | no | Array of label names |
| `assignees` | no | Array of current tracker assignees |
| `ownership` | no | Precomputed `self` or `unassigned`; exclude `other` before ranking |
| `impact` | no | 0–5 user/business/data impact assessment |
| `urgency` | no | 0–5 time sensitivity assessment |
| `relevance` | no | 0–5 fit for the current repository/project |
| `blocked` | no | Whether an external decision/dependency prevents work |
| `blocks_others` | no | Whether resolving it unlocks other work |
| `linked_pr` | no | Existing implementation PR URL/identifier |

Use UTC timestamps. Keep assessments evidence-based:

- `impact`: breadth and consequence if left unfixed;
- `urgency`: how quickly harm or blocking grows;
- `relevance`: confidence that this repository and current project own the fix.

Apply the ownership gate in `SKILL.md` before writing this file. Ownership is an
eligibility rule, not score weight: a high-scoring ticket assigned only to another
active human must not enter the automatic queue.

## Ordering

The script combines explicit tracker priority, recognized risk labels, the three
assessments, dependency-unblocking value, creation recency, and recent activity.
Creation recency receives the stronger time boost. Explicit critical risk always
outweighs cosmetic novelty.

Output groups:

1. `Immediate`
2. `Urgent`
3. `Next`
4. `Later`
5. `Blocked`

Within a group, sort by descending score, then newer creation time, newer update
time, and stable ID. Human-provided ordering always takes precedence.

## Example

```json
{
  "issues": [
    {
      "id": "3DE-2104",
      "title": "Prevent stale concurrent migrations",
      "created_at": "2026-07-27T09:00:00Z",
      "updated_at": "2026-07-28T08:30:00Z",
      "priority": "high",
      "labels": ["bug", "data-integrity"],
      "impact": 5,
      "urgency": 4,
      "relevance": 5,
      "blocks_others": true,
      "url": "https://linear.app/example/issue/3DE-2104"
    }
  ]
}
```

Use `--now 2026-07-28T12:00:00Z` for reproducible snapshots and `--format json`
when another tool will consume the result.
