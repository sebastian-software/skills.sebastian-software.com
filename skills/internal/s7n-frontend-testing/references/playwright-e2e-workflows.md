# Playwright E2E Workflows

Use Playwright-style E2E tests for high-value integrated user paths. Keep tests user-centered, deterministic, and small enough to debug.

## Working Rules

- Treat codegen output as a draft.
- Prefer locators based on role, label, text, and stable test IDs.
- Remove incidental waits and assertions that only mirror implementation details.
- Control network boundaries when backend state would make the test flaky.
- Use traces, screenshots, and videos as debugging artifacts when CI fails.

## Source-Backed Guidance

