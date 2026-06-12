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

