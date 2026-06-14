# Vendor Tool Notes

Use vendor tools only after the project need is clear. Compare where baselines live, how PR review works, which browsers/devices are covered, how dynamic states are stabilized, and how easy failures are to debug.

## Additional Rules

- Treat snapshot and hosted visual-testing tools as vendor options; compare baseline storage, PR review, browsers, and debugging before adopting.
- Treat Cypress homepage as vendor-context only; do not use it as direct implementation guidance.
