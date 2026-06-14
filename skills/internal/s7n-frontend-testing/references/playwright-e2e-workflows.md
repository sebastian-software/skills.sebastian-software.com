# Playwright E2E Workflows

Use Playwright-style E2E tests for high-value integrated user paths. Keep tests user-centered, deterministic, and small enough to debug.

## Working Rules

- Treat codegen output as a draft.
- Prefer locators based on role, label, text, and stable test IDs.
- Remove incidental waits and assertions that only mirror implementation details.
- Control network boundaries when backend state would make the test flaky.
- Use traces, screenshots, and videos as debugging artifacts when CI fails.

## Additional Rules

- Use as historical Playwright E2E architecture and Cypress/Selenium comparison context, not current feature matrix.
- Use Playwright network routing and mocking to make tests deterministic; account for service-worker caveats.
- Use Playwright codegen as a draft workflow; review generated locators, assertions, waits, and scope before committing tests.
- Use Playwright component testing as experimental/current-version caveat guidance.
