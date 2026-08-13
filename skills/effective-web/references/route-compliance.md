# Route: Web Legal Compliance

Turn a vague request for an "Impressum" or a "compliant website" into a
jurisdiction-aware, evidence-backed work product. Treat legal text as the
visible result of facts and operational decisions, not as boilerplate.

This is legal information and implementation support, not a legal opinion.

## Workflow

1. Define the requested result: issue inventory, implementation review, page
   map, questionnaire, draft with placeholders, or counsel-ready brief.
2. Read [Scoping and evidence](legal-scoping-and-evidence.md). Establish the
   operator, places of establishment, targeted markets, audience, transactions,
   data flows, marketing channels, publishing model, and regulated activities.
   Mark unknown facts; never invent them.
3. Load every matching regional reference:
   - [European Union and EEA](legal-european-union.md)
   - [United Kingdom](legal-united-kingdom.md)
   - [Canada](legal-canada.md)
   - [United States](legal-united-states.md)
     - [California](legal-united-states-california.md) when California
       residents, transactions, tracking, or business activity are in scope
4. For cookies, tracking, privacy choices, or consent interfaces, also read
   [Consent and tracking](legal-consent-and-tracking.md).
5. Verify current law and regulator guidance from primary official sources.
   Record jurisdiction, applicability trigger, effective date or as-of date,
   obligation, source, and unresolved interpretation. Use secondary sources
   only to find primary authority or explain a disputed point.
6. Build an applicability matrix before drafting. Separate requirements that
   likely apply, conditional requirements, recommendations, and questions for
   counsel. Never merge them into one generic checklist.
7. Inspect the real implementation when available: footer and navigation,
   checkout, forms, analytics and tags, consent state, account flows, email or
   SMS capture, user-generated content, localization, and mobile variants.
8. Read [Deliverables](legal-deliverables.md) and produce the smallest useful
   artifact. Keep entity facts, legal assertions, product copy, and code changes
   separately reviewable.
9. Recheck every draft against the fact inventory, source log, language and
   accessibility needs, link reachability, and mobile presentation. State the
   review date and remaining gaps.

## Operating Rules

- State that the work is legal information and implementation support, not a
  legal opinion. Recommend qualified local counsel where applicability,
  interpretation, risk tolerance, or regulated activity is uncertain.
- Do not call a site "compliant" from a page review alone. Prefer precise
  statements such as "the disclosed facts match the supplied records" or
  "this requirement appears applicable under the cited source."
- Do not treat a domain suffix, visitor IP, translated page, or globally
  accessible site as sufficient proof that a jurisdiction applies. Evaluate
  establishment, intentional targeting, affected people, and activity-specific
  rules.
- Do not assume one strict global template is safest. Extra statements can be
  inaccurate, create commitments, expose unnecessary personal data, or obscure
  locally required information.
- Do not conflate operator identification, privacy notice, consent interface,
  terms, checkout disclosures, accessibility information, and marketing
  disclosures. They may share navigation but have different triggers.
- Prefer live official sources over remembered thresholds, penalty amounts,
  regulator names, required wording, or lists of covered states and provinces.
- Treat geo-routing, privacy signals, consent categories, and fallback behavior
  as explicit Product/Legal policy backed by current sources. Do not silently
  turn a market heuristic into a legal conclusion.
- Preserve a source-backed distinction between mandatory content, conditional
  content, recommended trust information, and optional house style.
- Draft with conspicuous placeholders such as `[LEGAL ENTITY NAME]` and an
  explicit missing-facts list. Never produce plausible-looking fictional
  registration, tax, representative, address, or contact data.

## Cross-links

- Layout, footer navigation, forms, consent UI, accessibility implementation,
  and frontend testing are the matching implementation routes here, after this
  route has established the legal and factual requirements.
- Evidence-backed comparison with supplied creative references, copied identity
  or media, and asset-provenance findings are the Originality route. Copyright,
  trademark, plagiarism, and license clearance still require the appropriate
  qualified specialist.
- The intended audience, position, messaging, supplied proof, launch plan, and
  sales-enablement context belong to `effective-marketing`; return here to
  determine current legal applicability, required qualifications, disclosures,
  consent, and other jurisdiction-specific constraints.
- Locale-specific punctuation, spacing, dates, numbers, and visible prose
  typography belong to `effective-writing`, after counsel-approved wording and
  target locales are known.
- Keep penetration testing, security architecture, records of processing,
  vendor contracting, tax advice, employment law, and corporate filings outside
  this route unless they directly determine a web disclosure.
