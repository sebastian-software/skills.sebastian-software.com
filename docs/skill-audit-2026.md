# 2026 Web Skill Audit Notes

This note records the implementation priorities from the June 2026 external review of the internal web/frontend skills.

## Priorities Applied

1. **Baseline policy became operational.** `s7n-css-architecture` now distinguishes Widely available, Newly available, Limited availability, and radar-only features, and ties adoption to Browserslist, product analytics, fallbacks, and CI.
2. **Native UI guidance now separates platform support from accessibility.** Popover, dialog, anchor positioning, command/invoker attributes, customizable select, interest-triggered popovers, and CSS carousel features have separate guidance rather than one broad "native UI" rule.
3. **WCAG 2.2 rules were made concrete.** Accessibility guidance now calls out Focus Not Obscured, Dragging Movements, Target Size Minimum, Consistent Help, Redundant Entry, and Accessible Authentication.
4. **Target-size guidance was corrected.** Web UI references now distinguish WCAG's 24 x 24 CSS px minimum and the 44-48 CSS px comfort target for common touch controls.
5. **Performance guidance now reflects current tooling.** The Web Vitals extension is no longer treated as a live recommendation; DevTools Performance panel, field data, and lab/field distinctions are emphasized.
6. **React architecture guidance now reflects React 19.** Server Components, Server Actions, form Actions, `useActionState`, `useFormStatus`, `useOptimistic`, `use`, hydration diagnostics, and framework-boundary caveats are represented.
7. **Thin split-skill references were made actionable.** Forms, responsive design, frontend testing, visual baselines, i18n, auth/security UX, and CSS build tooling gained decision rules and checklists.
8. **Frontend SEO gained an AI/GEO and distribution layer.** `s7n-frontend-seo` now covers AI search eligibility, entity clarity, business profile consistency, Merchant Center/Business Profile distribution, LLM crawler access, optional `llms.txt`/Markdown/API surfaces, and practitioner GEO heuristics without treating speculative tactics as ranking rules.

## External Source Classes Used

- Official platform and compatibility references: web.dev Baseline, MDN Baseline/browser compatibility, WebDX/Web Platform Dashboard.
- Accessibility standards and support references: W3C WCAG 2.2, WAI APG, assistive-technology support data.
- Performance references: web.dev Core Web Vitals, Chrome DevTools/Web Vitals tooling notes, preload scanner guidance.
- Framework references: React 19 release notes and React RSC documentation.
- Search and AI-discovery references: Google Search Central AI features and generative AI optimization guidance, Google Business Profile API, schema.org, IndexNow, OpenAI crawler documentation, Anthropic crawler documentation.
- Practitioner radar: modern CSS and native UI articles were treated as trend/radar input only unless confirmed by current official support data.
- SEO/GEO practitioner radar: Aleyda Solis, Mike King/iPullRank, Lily Ray, Kevin Indig, Cindy Krum, Jason Barnard/Kalicube, Brodie Clark, Glenn Gabe, Marie Haynes, Crystal Carter, and Jono Alderson were treated as sources of heuristics and review questions, not direct ranking guarantees.

## Review Rule For Future Updates

When a new article suggests a rule, classify it before editing a skill:

- **Normative:** official spec, standard, or stable framework/platform documentation.
- **Compatibility:** Baseline, MDN browser-compat data, Web Platform Dashboard, Can I Use.
- **Practice:** article with durable implementation reasoning.
- **Radar:** single-browser demo, proposal, release note, conference recap, or experimental API.

Only normative and compatibility sources should directly change default rules. Practice sources can improve workflows and examples. Radar sources should remain explicitly support-gated.
