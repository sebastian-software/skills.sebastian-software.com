---
name: s7n-data-tables
description: |
  Tables, dense data views, comparison grids, sortable columns, filtering, responsive data layouts, financial or operational dashboards, and row-level actions. Use when the user asks about table UX, data density, comparison views, dashboards, or making tabular information usable on desktop and mobile.
license: MIT
metadata:
  author: sebastian-software
  version: "1.0"
---

# S7N Data Tables

Use this skill when the primary UI problem is understanding, comparing, filtering, or acting on structured data.

## Workflow

1. Identify the user's comparison task and the few columns that matter most.
2. Decide whether the data should be a table, list, card set, matrix, or chart.
3. Set column priority, alignment, sorting, filtering, pagination, and row actions.
4. Design empty, loading, partial, overflow, and error states with stable dimensions.
5. Verify keyboard navigation and small-screen behavior.

## Rules

- Align numbers by decimal or right edge; align text by left edge.
- Keep actions close to the row or selection they affect.
- Do not hide essential data behind hover.
- Sticky headers and columns are useful only when they preserve orientation without covering content.
- Responsive tables need an explicit strategy, not horizontal overflow by default.

## References

- [references/12-tables-data.md](references/12-tables-data.md) - table structure, dense data, and responsive data patterns.
