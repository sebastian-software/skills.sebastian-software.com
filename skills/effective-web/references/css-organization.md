# CSS Organization

Use this module when deciding where authored CSS belongs and how it reaches the
browser. Keep the source easy to inspect after build tooling, theming, and
third-party styles have been added.

## Organize by Ownership

- Keep global reset and base styles small. Place reusable layout primitives in a
  stable layer and component styles with the component or its documented style
  boundary.
- Prefer a simple entry point that declares layer order and imports intentional
  groups. Avoid a folder taxonomy that hides which file owns a visual rule.
- Isolate third-party CSS and application overrides so upgrades and removal do
  not become a specificity hunt.
- Extract an abstraction after repeated evidence: the same behavior, ownership,
  and variation need must recur. Do not turn a one-screen implementation detail
  into a global utility merely because it looks reusable.

## Check Before Shipping

Review generated output, unused CSS, import order, code-splitting boundaries,
and the browser-support promise. Measure render-blocking and selector work only
when the page's actual performance evidence calls for it.

For file-tree examples, methodology trade-offs, and performance details,
consult the [deep CSS architecture appendix](css-architecture.md).
