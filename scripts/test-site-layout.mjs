import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { chromium } from "playwright-core";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const pageUrl = (name) => pathToFileURL(resolve(root, "site", name)).href;
const pages = [
  { name: "index.html", url: pageUrl("index.html"), hasCapabilityExplorer: true },
  { name: "comparisons.html", url: pageUrl("comparisons.html"), hasCapabilityExplorer: false },
];
const mobileViewportMax = 400;
const viewports = [320, 360, 375, 400, 768, 1024, 1440];
const chromeCandidates = [
  process.env.CHROME_BIN,
  "/usr/bin/google-chrome",
  "/usr/bin/google-chrome-stable",
  "/usr/bin/chromium",
  "/usr/bin/chromium-browser",
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
].filter(Boolean);
const executablePath = chromeCandidates.find(existsSync);

assert.ok(
  executablePath,
  "Chrome was not found; set CHROME_BIN to run the viewport regression test"
);

const browser = await chromium.launch({ executablePath, headless: true });

try {
  for (const site of pages) {
    for (const width of viewports) {
      const context = await browser.newContext({
        colorScheme: "light",
        viewport: { width, height: 700 },
      });
      const page = await context.newPage();
      await page.goto(site.url, { waitUntil: "load" });
      const layout = await page.evaluate(() => {
        const root = document.documentElement;
        const filter = document.querySelector(".filter-bar");
        const capabilityExplorer = document.querySelector(".capability-explorer");
        const codeBlocks = [...document.querySelectorAll(".code-block")];
        return {
          capabilityExplorerContained: Boolean(
            capabilityExplorer &&
              capabilityExplorer.scrollWidth <= capabilityExplorer.clientWidth
          ),
          clientWidth: root.clientWidth,
          codeBlocksContained: codeBlocks.every(
            (block) => block.scrollWidth <= block.clientWidth
          ),
          hasFilter: Boolean(filter),
          filterOverflowX: filter
            ? getComputedStyle(filter).overflowX
            : null,
          scrollWidth: root.scrollWidth,
          visibleCapabilityPanels: [
            ...document.querySelectorAll("[data-capability-panel]:not([hidden])"),
          ].length,
        };
      });

      assert.ok(
        layout.scrollWidth <= layout.clientWidth,
        `${site.name} document overflows at ${width}px: ${layout.scrollWidth}px > ${layout.clientWidth}px`
      );
      if (layout.hasFilter && width <= mobileViewportMax) {
        assert.ok(
          ["auto", "scroll"].includes(layout.filterOverflowX),
          `${site.name} filter bar must be a horizontal scroll container (overflow-x auto/scroll) at ${width}px, got ${layout.filterOverflowX}`
        );
      }
      assert.ok(
        layout.codeBlocksContained,
        `${site.name} installation commands must stay inside their cards at ${width}px`
      );
      if (site.hasCapabilityExplorer) {
        assert.ok(
          layout.capabilityExplorerContained,
          `${site.name} capability explorer must stay inside its frame at ${width}px`
        );
        assert.equal(
          layout.visibleCapabilityPanels,
          1,
          `exactly one capability panel must be visible on ${site.name} at ${width}px`
        );
      }

      if (site.hasCapabilityExplorer && width === viewports[0]) {
        await page.click('[data-capability-tab="claim"]');
        const selectedCapability = await page.evaluate(() => ({
          claimSelected:
            document
              .querySelector('[data-capability-tab="claim"]')
              ?.getAttribute("aria-selected") === "true",
          claimVisible: !document
            .querySelector('[data-capability-panel="claim"]')
            ?.hasAttribute("hidden"),
          decisionHidden: document
            .querySelector('[data-capability-panel="decision"]')
            ?.hasAttribute("hidden"),
        }));

        assert.deepEqual(selectedCapability, {
          claimSelected: true,
          claimVisible: true,
          decisionHidden: true,
        });
      }

      await context.close();
    }
  }
} finally {
  await browser.close();
}
