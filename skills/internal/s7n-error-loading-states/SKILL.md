---
name: s7n-error-loading-states
description: |
  Loading states, skeletons, progress UI, empty states, error pages, 404/500 pages, retry flows, success states, partial failure, and resilient frontend states. Use when designing or implementing non-happy-path UI or making async states stable and clear.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Error & Loading States

Use this skill for the states users see while work is pending, unavailable, failed, empty, partial, or complete.

## Workflow

1. List every state: initial, loading, empty, partial, success, validation error, network error, permission error, not found, fatal.
2. Preserve layout stability across states.
3. Give users honest progress and a recovery path when recovery is possible.
4. Keep state copy specific and close to the affected region.
5. Verify retry, refresh, back navigation, and offline behavior where relevant.

## Rules

- Skeletons must match final layout closely enough to prevent reorientation.
- Spinners are acceptable only for short, uncertain waits or compact controls.
- Errors need cause, impact, and next step at the right level of detail.
- Empty states should not blame the user or over-explain the product.
- Success states should confirm meaningful completion, not celebrate routine clicks.

## References

- [references/loading-states.md](references/loading-states.md) - loading, progress, and skeleton patterns.
- [references/error-pages.md](references/error-pages.md) - error page and recovery patterns.
