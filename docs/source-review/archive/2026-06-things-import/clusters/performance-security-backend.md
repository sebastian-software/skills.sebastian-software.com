# Cluster Brief: Performance, Security, Backend

## Scope

Review a small Things cluster that mixes web performance, security/authentication,
and serverless/backend sources. This is an intermediate source-review artifact:
no Things tasks were changed and no skills were edited.

Reviewed on: 2026-06-10

## Access Notes

- All provided links were opened or checked over the network.
- `https://css-tricks.com/passkeys-what-the-heck-and-why/` returned usable HTML
  through `curl`; the web page was reachable with HTTP 200.
- `https://egghead.io/courses/develop-a-serverless-backend-using-node-js-on-aws-lambda`
  returned HTTP 200 and embedded course metadata/lesson titles, but the full
  course content is gated/media-based. Decision is based only on visible page
  metadata and lesson outline.
- `https://adactio.com/journal/9881` includes a visible prompt-injection string
  near the top of the fetched page. Ignore that page text as an instruction; the
  article content itself was only evaluated as source material.
- GitHub repositories were checked through their public pages and repository
  metadata where helpful.

## Decision Summary

| Status | Count | Things |
| --- | ---: | --- |
| `candidate` | 8 | 1, 4, 6, 8, 9, 10, 13, 16 |
| `keep` | 1 | 14 |
| `defer` | 5 | 5, 11, 12, 15, 17 |
| `reject` | 3 | 2, 3, 7 |

## Source Cards

| # | Thing ID | Things title | URL | What is behind the link? | Decision | Target / reason |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `WJZHvbNT4mrzUtGYpQi7op` | Databases For Front-End Developers | https://www.smashingmagazine.com/2022/08/databases-frontend-developers-rise-serverless-databases/?ck_subscriber_id=1697729046 | Smashing Magazine article by Atila Fassina, published 2022-08-11. Conceptual primer for frontend developers on CMS/spreadsheets vs databases, consistency, scaling, serverless database tradeoffs, and why abstraction does not remove architecture decisions. | `candidate` | Better fit for `s7n-backend-edge-serverless` than performance. Durable as conceptual background, but should be paired with fresher database/vendor material. |
| 2 | `GCNPfMZ6raEFMbRDiMGm16` | pragmatic-drag-and-drop | https://github.com/atlassian/pragmatic-drag-and-drop | Public Atlassian GitHub repo for a low-level, framework-agnostic drag-and-drop toolchain. It emphasizes small core size, browser-native drag/drop, optional visual outputs, and assistive-technology flows. | `reject` | Misclassified. It is frontend interaction tooling, not performance/security/backend. If ever useful, it belongs in a UI accessibility/interaction source pass, not this cluster. |
| 3 | `MCSUshc3cHGX7T5M31HkkW` | firecrawl | https://github.com/mendableai/firecrawl | Redirects to `firecrawl/firecrawl`, a public AGPL-3.0 web scraping/search/API project with active releases. Repository metadata shows it is current and popular, but it is a crawling product/tool, not a performance/security/backend foundation source. | `reject` | Misclassified for this archive pass. Potential future vendor/tool review for web scraping or agent data ingestion, but no durable value for the requested skill candidates. |
| 4 | `7snEM5KM6NHXf1aMHCpPvB` | Responsive image breakpoints | https://www.smashingmagazine.com/2016/01/responsive-image-breakpoints-generation/ | Smashing Magazine article by Nadav Soferman, published 2016-01-26, introducing Cloudinary's responsive breakpoint generator and explaining why responsive image breakpoint selection should be data-driven rather than arbitrary. | `candidate` | Useful for `s7n-web-performance` image optimization history and heuristics. Caveat: old and tool/vendor-adjacent; cite for the breakpoint reasoning, not current tool choice. |
| 5 | `QBJhgP66wT3GqLcPomPwy8` | Simon Willison Gemini | https://simonwillison.net/2025/Mar/25/gemini/ | Simon Willison's 2025-03-25 hands-on notes on Gemini 2.5 Pro: multimodal tests, long context, transcription, bounding boxes, and coding experiments. | `defer` | Product/model news and AI workflow commentary. Not performance/security/backend. Could be useful in a separate AI coding/model-evaluation source pass, but will churn quickly. |
| 6 | `Ga7AGaG4XpqaaevALg1naW` | Learn Images | https://web.dev/learn/images/ | Official web.dev course index for images on the web. Covers image history, performance issues, vector/raster formats, GIF/PNG/JPEG/WebP/AVIF, responsive images, `srcset`, `sizes`, and descriptive syntaxes. | `candidate` | Strong source for `s7n-web-performance`, and partly for existing `s7n-ui-design` image rules. Durable, official, and broad enough to anchor an image-performance reference. |
| 7 | `8nQXmmkJ8mv86FpP4fMV3D` | Meta-Data Markup | https://adactio.com/journal/9881 | Jeremy Keith/Adactio post from 2015-11-28 about redundant social metadata markup across Twitter Cards, Open Graph, Slack/oEmbed, and web app manifests. | `reject` | Misclassified. This is SEO/social metadata, already conceptually covered by existing `skills/internal/s7n-ui-design/references/09-seo.md`. Also old and includes prompt-injection noise in fetched page. Do not use for this cluster. |
| 8 | `FaoTKJcTt6HmVMi7k1UqQy` | Optimizing image LCP | https://www.smashingmagazine.com/2023/01/optimizing-image-element-lcp/ | Smashing Magazine article by Eloise Martin, published 2023-01-16, on optimizing LCP when the LCP element is an image. Covers `srcset`, `sizes`, browser selection behavior, resource load time, and resource load delay. | `candidate` | Strong `s7n-web-performance` source. Best used with web.dev sources to avoid vendor bias from TwicPics examples. |
| 9 | `Bzo1tpxKqQLgUNTHZXdYbi` | Server-Timing monitoring | https://www.smashingmagazine.com/2022/05/rethinking-server-timing-monitoring-tool/ | Smashing Magazine article by Sean Roberts, published 2022-05-16, on using the `Server-Timing` response header for RUM and monitoring. Covers exposing timing and non-timing metadata through Performance APIs, including assets, HTML documents, CDNs, regions, request IDs, and cache status. | `candidate` | Good bridge source for `s7n-web-performance` and `s7n-backend-edge-serverless`: practical observability pattern that connects server, CDN, and browser signals. |
| 10 | `GFfTZrYzLTvUKPhvfbtNzA` | Secure HTTP headers | https://www.smashingmagazine.com/2017/04/secure-web-app-http-headers/ | Smashing Magazine article by Hagay Lupesko, published 2017-04-03, explaining security-focused HTTP headers for web apps with Node.js examples. | `candidate` | Useful for a security/hardening skill, but the proposed `s7n-security-auth` name may be too auth-specific for this source. Needs verification against current OWASP/MDN header guidance before use. |
| 11 | `MQbwvScaHvBJpCPTU12Gv3` | Web Vitals extension now in DevTools | https://developer.chrome.com/blog/web-vitals-extension | Chrome Developers post by Rick Viscomi and Addy Osmani, published 2024-09-24, announcing Web Vitals extension features moving into Chrome DevTools and ending extension support on 2025-01-07. | `defer` | Tooling lifecycle/news. It may become a short `s7n-web-performance` tooling note: prefer DevTools Performance panel over the retired extension. Not enough durable content for a skill source by itself. |
| 12 | `4nTGvxSAsLRj3kTCQMAAH3` | Lighthouse 10 | https://developer.chrome.com/blog/lighthouse-10-0/ | Chrome Developers post last updated 2023-02-09 about Lighthouse 10. Key durable point: TTI removed from scoring and CLS weight increased; also includes Lighthouse 10 audit/type changes. | `defer` | Version-specific tooling change. Useful only as historical context if a performance skill includes Lighthouse scoring caveats; do not anchor a skill on this. |
| 13 | `EQSwrzoCqtcV3cNsDbwiJy` | Passkeys explainer | https://www.smashingmagazine.com/2023/10/passkeys-explainer-future-password-less-authentication/ | Smashing Magazine article by Neal Fennimore, published 2023-10-30, explaining passkeys, public/private key pairs, WebAuthn concepts, attestation/assertion, challenge generation, browser APIs, and phishing/database-leak benefits. | `candidate` | Strong basis for `s7n-security-auth`, especially an auth-design reference on passkeys/WebAuthn. Must be paired with current passkeys.dev, MDN, W3C/FIDO, and platform support sources. |
| 14 | `FDLiaaQoUdiKS77TGNSrv6` | Passkeys CSS-Tricks | https://css-tricks.com/passkeys-what-the-heck-and-why/ | CSS-Tricks article by Neal Fennimore, published 2023-04-12 and modified 2025-10-30. Explains passkeys/WebAuthn terminology, public-key challenge flow, browser APIs, platform support caveats, and demos. | `keep` | Keep as secondary source, deduped under #13. Same author and similar topic; use only when it adds wording/UX framing not present in the later Smashing article. |
| 15 | `8zB4NKN5f2EZ8gZTZY6mtD` | State of Databases for Serverless & Edge | https://leerob.io/blog/backend | Lee Robinson/Substack post, discussion visible around 2023-01-30, surveying serverless and edge database vendors and themes: autoscaling vectors, global data, Firebase, MongoDB, PlanetScale, Aurora, CockroachDB, Upstash, Convex, Neon, Supabase, Xata, and others. | `defer` | Vendor landscape snapshot. Some framing is useful for `s7n-backend-edge-serverless`, but the provider statuses are stale and need a fresh 2026 vendor review before skill use. |
| 16 | `DWqqDGNbSA1PTRD5W38Pw1` | serverless-express | https://github.com/vendia/serverless-express | Redirects to `CodeGenieApp/serverless-express`, a public Apache-2.0 repo for running Express/Koa/Hapi/Sails-style Node.js apps on AWS Lambda/API Gateway, Lambda@Edge, Azure Functions, and related event sources. README shows v5 with Node.js 24 support and basic Lambda/Azure wrappers. | `candidate` | Narrow but useful for `s7n-backend-edge-serverless` as a migration pattern: wrap existing Node frameworks for Lambda when a rewrite is not justified. Treat as vendor/tool reference, not general serverless architecture guidance. |
| 17 | `6GdRk4oB2MqYgvmtv9dDfR` | Egghead serverless backend course | https://egghead.io/courses/develop-a-serverless-backend-using-node-js-on-aws-lambda | Egghead course page for building a serverless Node.js backend on AWS Lambda. Visible metadata says it covers an HTTP endpoint, a Todo REST API, DynamoDB, AWS CLI, and Serverless Framework deployment. | `defer` | Course/tutorial material with likely version drift and limited accessible content. Could inform an eval prompt for backend setup, but current AWS/Serverless Framework docs should be primary. |

## Dedupe And Misclassification

- #13 and #14 are near-duplicates: same author, same passkeys/WebAuthn topic,
  different publishers and dates. Keep #13 as primary, #14 as secondary.
- #1 and #15 overlap on serverless databases, but #1 is conceptual and #15 is a
  vendor landscape snapshot. Do not treat them as duplicate sources.
- #4, #6, and #8 form the strongest subcluster: responsive images and LCP image
  performance.
- #11 and #12 are Chrome tooling/version notes, not durable performance
  methodology.
- #2 is frontend interaction/accessibility tooling, not this cluster.
- #3 is scraping/agent data-ingestion tooling, not this cluster.
- #5 is AI model release/experimentation commentary, not this cluster.
- #7 is SEO/social metadata. It belongs, if anywhere, in an existing
  `s7n-ui-design` SEO reference pass.

## Proposed Outcome

Decision: `new skill` plus `existing skill update candidates`

Target skill or proposed skill names:

- `s7n-web-performance` looks justified from #4, #6, #8, #9, with #11 and #12
  only as optional tooling notes.
- `s7n-security-auth` is plausible but thin from this cluster alone: #13/#14
  support passkeys/WebAuthn, while #10 is broader web hardening. Consider
  either narrowing the skill to auth/passkeys or renaming the future scope to
  cover web app security hardening.
- `s7n-backend-edge-serverless` is plausible but not ready from this cluster
  alone: #1 and #16 are useful, #9 bridges observability, while #15 and #17 need
  current replacement/verification before they can anchor a durable skill.

Existing-skill candidates:

- `skills/internal/s7n-ui-design/` already mentions Core Web Vitals,
  responsive images, LCP image priority, and SEO metadata. Sources #4, #6, #8,
  and maybe #7 could inform a future reference update, but that is outside this
  task.
- `skills/vendor/convex-performance-audit/` is Convex-specific and should not
  absorb general web performance or broad serverless database sources.

## Skill Boundary

Use `s7n-web-performance` when the user asks to:

- diagnose or improve Core Web Vitals, especially LCP/CLS/INP
- optimize image loading, responsive image markup, image formats, `srcset`, and
  `sizes`
- add browser-visible performance instrumentation such as `Server-Timing`
- decide which browser tooling to use for local performance debugging

Do not use `s7n-web-performance` when:

- the task is purely visual UI design with no measured performance concern
- the task is Convex-specific performance work; use the existing Convex skill
- the request is only SEO metadata or social sharing markup

Use `s7n-security-auth` when the user asks to:

- explain or design passkeys/WebAuthn login flows
- compare passwords, MFA, WebAuthn, and passkeys at the product/security level
- review auth flows for challenge/origin/public-key verification risks

Do not use `s7n-security-auth` when:

- the request is a general code security audit with no auth focus
- the request is only HTTP header hardening, unless the future skill scope is
  intentionally broader than auth

Use `s7n-backend-edge-serverless` when the user asks to:

- choose backend/data architecture for frontend-heavy or serverless apps
- evaluate serverless database tradeoffs conceptually
- migrate or wrap existing Node/Express-style apps for Lambda/API Gateway
- connect frontend RUM signals to server/CDN/backend timing metadata

Do not use `s7n-backend-edge-serverless` when:

- the request needs current cloud-provider pricing or product status without a
  fresh verification pass
- the request is vendor-specific Convex setup/performance/migration already
  covered by existing Convex skills

## Proposed Structure

```text
skills/internal/s7n-web-performance/
├── SKILL.md
├── README.md
├── SOURCE.md
├── references/
│   ├── core-web-vitals.md
│   ├── responsive-images.md
│   ├── image-lcp.md
│   ├── server-timing-rum.md
│   └── tooling.md
└── evals/
```

```text
skills/internal/s7n-security-auth/
├── SKILL.md
├── README.md
├── SOURCE.md
├── references/
│   ├── passkeys-webauthn.md
│   ├── auth-flow-review.md
│   └── http-security-headers.md
└── evals/
```

```text
skills/internal/s7n-backend-edge-serverless/
├── SKILL.md
├── README.md
├── SOURCE.md
├── references/
│   ├── architecture-tradeoffs.md
│   ├── serverless-databases.md
│   ├── express-on-lambda.md
│   └── edge-observability.md
└── evals/
```

## Reference Plan

- `s7n-web-performance/references/responsive-images.md` -- use #4, #6, #8.
  Prefer web.dev as primary; use Smashing articles for practical examples and
  historical breakpoint reasoning.
- `s7n-web-performance/references/image-lcp.md` -- use #8 and current web.dev
  LCP docs. Capture rules: identify actual LCP element, do not lazy-load LCP
  image, supply correct `srcset`/`sizes`, avoid resource-load delay.
- `s7n-web-performance/references/server-timing-rum.md` -- use #9. Capture
  `Server-Timing` + Performance API pattern, cross-origin `Timing-Allow-Origin`,
  and CDN/origin correlation examples.
- `s7n-web-performance/references/tooling.md` -- use #11/#12 only as a dated
  note: Web Vitals extension support ended 2025-01-07; Lighthouse 10 removed TTI
  from score weighting.
- `s7n-security-auth/references/passkeys-webauthn.md` -- use #13 as primary and
  #14 as secondary; add current MDN, passkeys.dev, W3C WebAuthn, and FIDO
  sources before writing.
- `s7n-security-auth/references/http-security-headers.md` -- #10 can seed the
  outline, but update against current OWASP Secure Headers Project, MDN, and
  framework/platform defaults before any skill change.
- `s7n-backend-edge-serverless/references/architecture-tradeoffs.md` -- use #1
  for concepts and add fresher primary docs/sources.
- `s7n-backend-edge-serverless/references/serverless-databases.md` -- do not use
  #15 as authoritative without a new 2026 vendor review.
- `s7n-backend-edge-serverless/references/express-on-lambda.md` -- use #16 as a
  vendor/tool reference and compare with `serverless-http`, native Lambda
  handlers, and platform-native adapters.

## Eval Ideas

- Prompt: "Audit this product page for image-related LCP problems."
  Expected behavior: identify LCP image, check eager loading/fetch priority,
  dimensions/aspect ratio, `srcset`/`sizes`, format choices, and verification
  steps in DevTools.
- Prompt: "Add `Server-Timing` to this Next.js route so RUM can correlate CDN,
  origin, cache, and request ID data."
  Expected behavior: propose a minimal header format, note privacy/cross-origin
  caveats, and show how the browser reads it from Performance APIs.
- Prompt: "Explain whether we should add passkeys to this SaaS login flow."
  Expected behavior: explain relying party, authenticator, challenges,
  attestation/assertion, account recovery, platform support, and fallback
  strategy without overselling passkeys.
- Prompt: "We have an Express API and want to run it on Lambda."
  Expected behavior: compare adapter wrapping with a native Lambda rewrite,
  identify cold-start/bootstrap implications, event-source mapping, local test
  approach, and deployment constraints.

## Open Questions

- Should `s7n-security-auth` stay auth-only, or should this become a broader
  `s7n-web-security`/`s7n-app-hardening` skill that can own HTTP security
  headers?
- Is `s7n-web-performance` meant to be standalone, or should image performance
  remain inside `s7n-ui-design` with only a smaller reference expansion?
- Should `s7n-backend-edge-serverless` include vendor selection, or only durable
  architecture and migration workflows? Vendor selection requires recurring
  freshness checks.
- Do we want a separate future intake for AI/model/tooling sources so #5 and
  similar links do not pollute technical web/backend clusters?

## Things Actions

| Things ID | Decision | Final tag | Complete? | Reason |
| --- | --- | --- | --- | --- |
| `WJZHvbNT4mrzUtGYpQi7op` | candidate | `Skill Archive Candidate` | yes | Durable serverless database concepts; route to `s7n-backend-edge-serverless`, not performance. |
| `GCNPfMZ6raEFMbRDiMGm16` | rejected | `Skill Archive Rejected` | yes | Misclassified frontend drag-and-drop tooling; no performance/security/backend archive value. |
| `MCSUshc3cHGX7T5M31HkkW` | rejected | `Skill Archive Rejected` | yes | Misclassified web scraping/API product; possible future vendor review, not this cluster. |
| `7snEM5KM6NHXf1aMHCpPvB` | candidate | `Skill Archive Candidate` | yes | Useful responsive-image breakpoint reasoning for `s7n-web-performance`; old/tool-adjacent caveat documented. |
| `QBJhgP66wT3GqLcPomPwy8` | deferred | `Skill Archive Deferred` | yes | AI model/product experiment; not this cluster and high churn. |
| `Ga7AGaG4XpqaaevALg1naW` | candidate | `Skill Archive Candidate` | yes | Official broad image-performance course; strong `s7n-web-performance` source. |
| `8nQXmmkJ8mv86FpP4fMV3D` | rejected | `Skill Archive Rejected` | yes | SEO/social metadata source; existing `s7n-ui-design` route noted, but false for this cluster. |
| `FaoTKJcTt6HmVMi7k1UqQy` | candidate | `Skill Archive Candidate` | yes | Practical image LCP source for `s7n-web-performance`. |
| `Bzo1tpxKqQLgUNTHZXdYbi` | candidate | `Skill Archive Candidate` | yes | Server-Timing observability bridges frontend RUM and backend/CDN signals. |
| `GFfTZrYzLTvUKPhvfbtNzA` | candidate | `Skill Archive Candidate` | yes | Security header hardening source; requires current OWASP/MDN verification before skill use. |
| `MQbwvScaHvBJpCPTU12Gv3` | deferred | `Skill Archive Deferred` | yes | Chrome tooling lifecycle note; standalone Web Vitals extension support ended 2025-01-07. |
| `4nTGvxSAsLRj3kTCQMAAH3` | deferred | `Skill Archive Deferred` | yes | Lighthouse 10 scoring/version note; useful only as dated tooling caveat. |
| `EQSwrzoCqtcV3cNsDbwiJy` | candidate | `Skill Archive Candidate` | yes | Primary passkeys/WebAuthn explainer for possible `s7n-security-auth`. |
| `FDLiaaQoUdiKS77TGNSrv6` | candidate | `Skill Archive Candidate` | yes | Secondary passkeys/WebAuthn source deduped under the later Smashing article. |
| `8zB4NKN5f2EZ8gZTZY6mtD` | deferred | `Skill Archive Deferred` | yes | Serverless/edge database vendor snapshot is stale; needs fresh 2026 review. |
| `DWqqDGNbSA1PTRD5W38Pw1` | candidate | `Skill Archive Candidate` | yes | Narrow but useful Express-on-Lambda migration reference for `s7n-backend-edge-serverless`. |
| `6GdRk4oB2MqYgvmtv9dDfR` | deferred | `Skill Archive Deferred` | yes | Tutorial/course outline visible, but likely version drift and limited accessible content. |
