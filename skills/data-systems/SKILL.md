---
name: data-systems
description: >-
  Design, review, and evolve reliable data models, datastores, transactions,
  consistency contracts, replication, partitioning, batch or streaming flows,
  and data migrations. Use for database or event-model decisions, read and
  write guarantees, concurrent updates, dual-write risks, replication lag,
  sharding or partition-key choices, data-pipeline semantics, schema evolution,
  backfills, cutovers, and recovery planning. Start from observed access
  patterns, invariants, load, failure consequences, and operational capability;
  do not introduce distribution, polyglot persistence, or event sourcing
  without a concrete driver.
---

# Data Systems (superseded)

This skill is superseded by `effective-engineering`. It remains installable for one
release window so existing selections keep resolving, and it carries no
guidance of its own.

Load `effective-engineering` and take the route that absorbed this work:

> Data Systems (references/route-data.md)

Every reference that lived here moved with it, unchanged.

Install the successor:

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-engineering
```

## Routing Boundaries

- Route every request that previously landed here to `effective-engineering`.
- Do not answer from this stub. It states the handoff and nothing else.
