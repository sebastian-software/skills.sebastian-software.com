# Playwright E2E Workflows

Use Playwright-style E2E tests for high-value integrated user paths. Keep tests user-centered, deterministic, and small enough to debug.

## Working Rules

- Treat codegen output as a draft.
- Prefer locators based on role, label, text, and stable test IDs.
- Remove incidental waits and assertions that only mirror implementation details.
- Control network boundaries when backend state would make the test flaky.
- Use traces, screenshots, and videos as debugging artifacts when CI fails.

## Source-Backed Guidance
### E2E-Testing mit Playwright: Der Weg der Mitte

- Things ID(s): `8gEgkCSpcPb9mbkafEUxfA`
- Source: <https://www.heise.de/hintergrund/E2E-Testing-mit-Playwright-Der-Weg-der-Mitte-7310444.html?wt_mc=rss.red.ho.ho.atom.beitrag.beitrag>
- Decision: `secondary`
- Target: `frontend-testing/playwright`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use as historical Playwright E2E architecture and Cypress/Selenium comparison context, not current feature matrix.
### Network | Playwright

- Things ID(s): `RaQYW8s5DFcmoWypkrRs3E`
- Source: <https://playwright.dev/docs/network#record-and-replay-requests>
- Decision: `primary`
- Target: `frontend-testing/playwright`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Playwright network routing and mocking to make tests deterministic; account for service-worker caveats.
### Test generator | Playwright

- Things ID(s): `X22tAQxZX3Mja2UJ4Wrm4Y`
- Source: <https://playwright.dev/docs/codegen>
- Decision: `primary`
- Target: `frontend-testing/playwright`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Playwright codegen as a draft workflow; review generated locators, assertions, waits, and scope before committing tests.
### Experimental: components | Playwright

- Things ID(s): `3mPdXbVm2UMorhjirRL7XR`
- Source: <https://playwright.dev/docs/test-components>
- Decision: `secondary`
- Target: `frontend-testing`
- URL recheck: 2026-06-13, HTTP 200
- Guidance: Use Playwright component testing as experimental/current-version caveat source.

