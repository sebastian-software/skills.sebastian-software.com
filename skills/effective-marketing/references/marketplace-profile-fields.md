# Consultant Marketplace Profile Fields

Use this reference when adapting a consultant profile to a named staffing
intermediary, supplier portal, or expert marketplace. It provides a stable
master model plus dated provider adapters; it is not a claim that every field
is mandatory or public on every platform.

Last verified: **2026-07-24**

Provider forms, ranking logic, membership tiers, and visibility rules change.
Re-check the current portal before completing or automating a real profile.

## Evidence Labels

Keep the source and certainty of every provider field visible:

- **Intake** - visible in a public registration, CV-upload, or application form.
- **Guidance** - recommended in the provider's official help or editorial
  guidance.
- **Buyer filter** - exposed in official search, matching, or transparency
  documentation.
- **Observed profile** - visible on a public provider-hosted profile; it may be
  optional, tier-dependent, or maintained by the provider.

Say "publicly documented", "recommended", or "observed" unless the provider
explicitly calls a field required. A public intake form is not necessarily the
full internal data model.

## Separate Four Field Layers

Do not flatten all portal data into a CV.

1. **Master-profile facts** - reusable consultant-controlled facts such as
   title, summary, skills, languages, projects, certifications, location, and
   delivery preferences.
2. **Application or account data** - private contact details, address, date of
   birth, legal or company data, passwords, uploaded documents, screening
   answers, and assignment-specific rate or availability.
3. **Buyer-facing operational fit** - availability, capacity, location or time
   zone, remote/on-site setup, travel readiness, engagement model, and a rate
   when the channel expects it and the consultant supplied it.
4. **Platform-owned trust signals** - ratings, reviews, badges, on-platform work
   history, earnings, response time, activity, verification, and ranking.
   Treat these as read-only and verifiable. Never invent or silently transfer
   them into a self-authored CV.

## Canonical Master Field Model

Keep one source of truth and map provider terminology onto it.

| Group | Canonical fields | Notes |
| --- | --- | --- |
| Identity | name, public location, country, time zone, public profile URL | Keep private contact, address, birth date, and account data separate. |
| Positioning | professional title, category/discipline, summary, focus areas, services/deliverables | The title should match the role buyers search for, not merely the legal business name. |
| Expertise | top skills, full skills, methods/tools, industries, seniority/years, languages and levels, certifications, education | Preserve which skills are current, evidenced, and most important. |
| Evidence | selected engagements, full project/work history, portfolio, references/recommendations | Project records should hold period, context, role, contribution, deliverables, outcome, and relevant technologies/skills. |
| Availability | available from, capacity, hours or days per week, engagement duration preference | Keep date, percentage, and time-unit semantics explicit. |
| Delivery setup | remote/on-site/hybrid, on-site share, working locations, travel radius, countries, time-zone overlap | "Remote" and "travel ready" are different facts. |
| Commercial setup | engagement type/legal status, hourly or daily rate, currency, rate unit, rate applicability | Never convert hourly and daily rates without an agreed assumption. Preserve whether expenses or VAT are included. |
| Preferences | industries, company size, project duration, sector exclusions, language, location | These may influence matching without belonging in the public CV. |
| Channel metadata | visibility, last updated, external links, CV/documents, permissions | Track client-name and portfolio publication permission per item. |
| Platform signals | ratings, reviews, badges, platform projects/earnings, response metrics | Read-only, source-labelled, and excluded from the master CV unless explicitly verified and relevant. |

## Provider Matrix

This matrix shows what each provider publicly documents, not a universal list
of mandatory fields.

| Provider | Channel model | Publicly documented or observed fields | Profile implication |
| --- | --- | --- | --- |
| Hays | recruiter/intermediary | **Intake:** identity/contact, availability, employment form, expertise area, CV/documents, optional online-profile link. **Guidance:** qualifications, experience, project documents, availability, hourly rate/framework conditions. | Prepare a recruiter-readable CV and a compact operational-fit block. Do not assume the upload form is the complete client-facing schema. |
| GULP / Randstad Professional | searchable expert database plus intermediary | **Buyer filters:** skills, professional focus, project experience, location/radius, rate and currency, available from, capacity, remote option, languages, freelancer/supplier status. **Observed result/profile:** title, top skills, location, availability, on-site regions, project history, optional photo. | Make searchable specialization, top skills, rate semantics, capacity, and deployment geography structured and current. One consultant may maintain differently oriented profile variants where the product supports it. |
| SOLCOM | curated project intermediary | **Intake:** identity/company/account data, documents, external profile links, application text, available from, hourly rate, deployment countries, skills, languages, professional focus. **Guidance:** focus, desired location, availability, alert keywords. | Separate private registration data from shareable consultant evidence. Provide skills, projects, availability, location, and commercial parameters in structured form. |
| freelance.de | open marketplace | **Guidance/buyer filters:** profile title, description, projects/tasks/qualifications, references, up to ten highlighted qualifications, current availability, location, hourly rate, travel, languages, experience duration, CV/documents, sector knowledge, last update. | Treat project records and their skill tags as the evidence source; the platform derives experience signals from them. Keep visibility and document sharing deliberate. |
| freelancermap | open marketplace | **Guidance/observed profile:** title, summary, skills and levels, project history, availability, location, degree, languages, hourly/daily rate, travel/remote setup, portfolio/CV links, profile currency. | Optimize the first-visible title, skills, and rate without letting tags replace project proof. Preserve rate unit and remote/travel distinctions. |
| Malt | searchable marketplace with matching and recommendations | **Required/visibility guidance:** photo, title/category, description, skills/top skills, experience, experience level, language, daily rate, location/workplace preference, availability. **Matching:** industry, company-size and project preferences, response/activity, recommendations. **Portfolio:** work samples and video where the category permits. | Use daily-rate and workplace-preference semantics exactly. Link skills to experience and keep matching preferences outside the general CV unless useful to the buyer. |
| Upwork | global marketplace with proposals and platform work history | **Profile guidance:** photo, title, overview, hourly rate, ordered skills, English proficiency, employment history, education, certifications, portfolio, other experience, video, availability/visibility. **Platform signals:** work history, reviews, Job Success and badges. | Write for search and proposal relevance, but never add off-platform contact data where prohibited or claim platform-owned signals. Upwork removed Specialized Profiles in May 2026; use one primary profile whose relevant evidence is selected dynamically. |
| Toptal | vetted, curated talent network | **Observed public profile:** verified discipline, title, location, bio, expertise, availability, portfolio, years per skill, preferred environment, work/project history, education, certifications, grouped skills. **Screening guidance:** communication, skill review, live screening, test project. | Treat the public profile as evidence of presentation, not proof of a self-service field contract. Rate and matching are not presented like an open marketplace card. |
| Braintrust | vetted talent network and job marketplace | **Guidance:** identity/location, role, links, skills and top "Superpowers", years of experience, bio, work history, projects, certifications, portfolio. **Application/job filters:** hourly rate, availability, resume, role, location, commitment, duration, experience, skills. | Map branded labels such as "Superpowers" to canonical top skills. Keep job-specific rate, availability, and screening answers separate from reusable profile copy. |

## Provider Notes

### Hays

Hays exposes a relatively small public CV-upload intake. Its freelancer
guidance asks for a CV and meaningful project documents containing relevant
qualifications and experience, plus framework conditions such as availability
and hourly rate. This is a recruiter-mediated path: optimize the evidence
package and operational fit, not only the registration form.

### GULP / Randstad Professional

The buyer-search documentation is especially useful because it shows the
fields customers actually filter on. Preserve:

- professional focus and a precise profile title
- top skills plus fuller project-backed skills
- desired rate with currency and unit
- residence and acceptable deployment radius or regions
- available-from date and capacity percentage or hours per month
- remote feasibility and on-site locations
- languages and work status

Do not collapse `available from`, `capacity`, and `remote possible` into one
generic availability sentence.

### SOLCOM

SOLCOM's registration form mixes private account data with market-facing
facts. Date of birth, address, and company data belong to the private intake
layer. Skills, professional focus, languages, project evidence, available-from
date, deployment locations, external professional profiles, and supplied rate
can feed the consultant-facing adapter.

### freelance.de and freelancermap

Both open marketplaces reward current, searchable profiles, but project
evidence remains essential. freelance.de derives some experience displays from
project and qualification entries. freelancermap guidance highlights the
first-visible title, skills, and rate. For both:

- keep the profile title specific
- attach skills to dated project evidence
- distinguish top skills from the long-tail taxonomy
- maintain current availability
- label hourly versus daily rate exactly
- manage contact, document, and profile visibility intentionally

### Malt

Malt's matching documentation makes preference fields unusually explicit:
daily rate, project start and duration, workplace/home-office preference,
location, language, experience, industry, and company size can all affect
matching. Keep those structured in the master data even when they do not
appear in the consultant CV.

Malt Strategy has category-specific visibility and portfolio behavior. Verify
the applicable product area instead of applying the general marketplace rules
blindly.

### Upwork

The overview's opening is prominent in search, and skills are ordered. Use a
specific title, a strong first paragraph, relevant portfolio evidence, and the
consultant's supplied hourly rate. Do not include prohibited contact details
or copy platform work history, ratings, badges, or earnings as if they were
self-authored claims.

Do not recommend multiple Specialized Profiles based on older articles. Upwork
states that these were removed on May 28, 2026 and that the main profile now
surfaces the most relevant work, reviews, portfolio items, and skills for the
client's query or proposal.

### Toptal and Braintrust

These networks combine profile quality with screening or vetting. Toptal's
public expert pages show rich evidence, but not an open self-service rate card.
Braintrust documents a more explicit talent profile and a separate
job-application layer. Keep verified/vetted status, screening outcomes, and
platform activity source-labelled.

## Stable Labels for Reusable Profiles

Use stable master labels in owned documents, then match the provider's exact
taxonomy inside its portal.

| German master label | English master label | Canonical meaning |
| --- | --- | --- |
| Profilbezeichnung | Professional title | Searchable role and specialization |
| Kurzprofil | Professional summary | Buyer-relevant positioning and proof |
| Schwerpunkte | Focus areas / Core services | Problems solved or services delivered |
| Top-Kompetenzen | Top skills | Small ordered set used for matching |
| Weitere Kompetenzen | Additional skills | Broader evidence-backed taxonomy |
| Branchen | Industry expertise | Sector context and domain knowledge |
| Projekterfahrung | Selected engagements / Project experience | Dated evidence with role, contribution, deliverable, and outcome |
| Verfügbar ab | Available from | Earliest realistic start date |
| Kapazität | Capacity | Percentage, hours/week, days/week, or hours/month |
| Einsatzmodell | Delivery setup | Remote, on-site, or hybrid |
| Einsatzorte | Working locations | Cities, regions, countries, or time zones |
| Reisebereitschaft | Travel readiness | Radius, frequency, or on-site share |
| Vertragsmodell | Engagement type | Freelance, contracting, temporary, permanent, supplier employee, or other supported model |
| Stundensatz / Tagessatz | Hourly rate / Daily rate | Amount, currency, unit, and applicability |
| Sprachen | Languages | Language plus supplied proficiency level |
| Referenzen | References / Recommendations | Attributed third-party proof |
| Arbeitsproben | Portfolio / Work samples | Shareable artifacts or case studies |

Do not rename every owned-profile section to provider branding. "Superpowers",
for example, is Braintrust's presentation of top skills, not a universal CV
heading.

## Mapping Workflow

When a named provider is in scope:

1. Identify the provider, country, product area, account type, and whether the
   task concerns registration, public profile, matching, or one application.
2. Re-check the current form or official help page and record the verification
   date.
3. Classify every field as master fact, private/account data, buyer-facing
   operational fit, application-only data, or platform-owned signal.
4. Map known source data to the canonical model. Preserve units, currencies,
   dates, percentages, language levels, and permissions.
5. Map the canonical fields to the provider's current labels. Do not treat an
   observed example field as mandatory without explicit evidence.
6. Report missing required or matching-critical fields instead of inventing
   them. Availability, capacity, rate, travel, language level, legal status,
   and client-name permission commonly require confirmation.
7. Generate the provider-specific version while keeping the master CV and
   other channel variants fact-aligned.

For an audit, a useful provider mapping table contains:

| Provider field | Field layer | Canonical source | Current value | Evidence/status | Action |
| --- | --- | --- | --- | --- | --- |
| exact portal label | master/private/operational/application/platform | canonical field | supplied value or unknown | required/recommended/filter/observed | reuse, rewrite, confirm, omit, or read-only |

## Guardrails

- Do not invent rate, availability, capacity, location flexibility, language
  level, years of experience, vetting, verification, or platform success.
- Do not expose private registration data in public profiles merely because a
  provider collects it.
- Do not infer that a buyer filter must appear as a public CV section.
- Do not transfer provider-owned ratings, earnings, badges, or activity into a
  master profile without a verifiable source and a clear reason.
- Do not automate profile writes until current API access and provider terms
  are verified. Prefer a field map and copy-ready draft.
- Do not treat this dated matrix as an API schema. Current portal behavior wins.

## Sources

### DACH intermediaries and marketplaces

- Hays, [CV upload](https://www.hays.de/personaldienstleister/cv-upload) and
  [finding freelance projects](https://www.hays.de/freelancer/ratgeber/projekte-finden)
- GULP / Randstad Professional,
  [expert-search features](https://www.gulp.de/unternehmen/freelancer-finden/features/experten-suche),
  [freelancing overview](https://www.gulp.de/freelancing), and
  [getting started](https://www.gulp.de/starthilfe)
- SOLCOM,
  [project-portal registration](https://www.solcom.de/projektportal/registrieren)
  and [freelancer project portal](https://www.solcom.de/fuer-freelancer-projektportal)
- freelance.de,
  [profile optimization](https://www.freelance.de/blog/tipps-zur-optimierung-ihres-freelance-de-online-profil/),
  [profile self-marketing](https://www.freelance.de/blog/selbstmarketing-bringen-sie-ihr-profil-aufs-next-level/),
  [buyer search features](https://www.freelance.de/Leistungen-Preise-Personaldienstleister),
  and [profile download](https://support.freelance.de/was-ist-der-profil-download)
- freelancermap,
  [guide to a freelancer profile](https://www.freelancermap.de/blog/der-leitfaden-zum-perfekten-freelancer-profil/)

### International marketplaces

- Malt,
  [complete and update a freelancer profile](https://help.malt.com/hc/en-150/articles/29517405925778-How-do-I-complete-and-update-my-freelancer-profile),
  [profile visibility](https://help.malt.com/hc/en-150/articles/29532973052178-Visibility-of-my-profile),
  [matching transparency](https://www.malt.com/c/transparency), and
  [posting a project](https://help.malt.com/hc/en-150/articles/29580249118354-How-to-post-a-project-on-Malt)
- Upwork,
  [profile completeness](https://support.upwork.com/hc/en-us/articles/211063188-How-do-I-create-a-100-complete-freelancer-profile),
  [profile essentials](https://support.upwork.com/hc/en-us/articles/360016252373-How-to-build-your-freelancer-profile-the-essentials),
  [portfolio and other experience](https://support.upwork.com/hc/en-us/articles/360016144974-How-to-enhance-your-freelancer-profile),
  and [Specialized Profiles removal](https://support.upwork.com/hc/en-us/articles/115013750068-Update-to-Specialized-Profiles-What-to-know)
- Toptal,
  [talent application](https://www.toptal.com/talent/apply),
  [developer network](https://www.toptal.com/developers/all), and an
  [observed public developer profile](https://www.toptal.com/developers/resume/jose-miguel-arreola)
- Braintrust,
  [profile guide](https://support.usebraintrust.com/hc/en-us/articles/14302715197847-Guide-Your-Profile),
  [approved-talent guide](https://support.usebraintrust.com/hc/en-us/articles/14302713002391-Guide-Becoming-Approved-Talent),
  and [getting a job](https://support.usebraintrust.com/hc/en-us/articles/14302783527447-Guide-Getting-a-Job-on-Braintrust)
