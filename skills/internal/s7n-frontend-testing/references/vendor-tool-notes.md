# Vendor Tool Notes

Use vendor tools only after the project need is clear. Compare where baselines live, how PR review works, which browsers/devices are covered, how dynamic states are stabilized, and how easy failures are to debug.

## Source-Backed Guidance
### Jest snapshot tools

- Things ID(s): `Ku9oWS7s6CcZKvJUXwAKNE`
- Source: <https://loki.js.org/>
- Decision: `secondary`
- Target: `frontend-testing/vendor`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Treat snapshot and hosted visual-testing tools as vendor options; compare baseline storage, PR review, browsers, and debugging before adopting.

