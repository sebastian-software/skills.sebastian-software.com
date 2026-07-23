# Responsive Data Tables

Use this module when a real data table must work in constrained space. Start
with the comparison task; a narrower viewport does not automatically make
horizontal scrolling the right answer.

## Choose One Presentation Deliberately

| User need | Preferred presentation |
| --- | --- |
| Compare many columns or scan a wide matrix | Native table in a labelled horizontal scroll container |
| Inspect one record at a time | Cards or a detail view, with equivalent labels and actions |
| Keep a few values visible while secondary values are optional | Priority columns with an explicit way to reveal the rest |
| Adapt a self-contained component to its allocated width | Container-query mode, retaining the semantic table where possible |

## Preserve Meaning and Orientation

- Keep the most important identifier and action visible. Do not hide the value
  needed to understand a row just to avoid overflow.
- Make horizontal overflow discoverable with a visible edge, cue, or short
  instruction; retain keyboard scroll and avoid a nested scroll trap.
- A sticky header or first column is useful only when it maintains orientation
  without covering content, focus targets, or row actions.
- Do not switch table descendants to `display: block` without restoring a
  coherent accessibility model. Prefer the native table when comparison across
  rows and columns remains the job.

## Test the In-Between States

Test continuous widths, zoom, long localized headers, absent columns, screen
reader announcements, keyboard traversal, and an intentional overflow path.

For exact CSS patterns and uncommon comparison layouts, use the [deep table
appendix](tables-data.md).
