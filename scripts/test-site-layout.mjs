import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { chromium } from "playwright-core";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const siteUrl = pathToFileURL(resolve(root, "site", "index.html")).href;
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
  for (const width of viewports) {
    const context = await browser.newContext({
      colorScheme: "light",
      viewport: { width, height: 700 },
    });
    const page = await context.newPage();
    await page.goto(siteUrl, { waitUntil: "load" });
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
        filterScrollable: Boolean(filter && filter.scrollWidth > filter.clientWidth),
        scrollWidth: root.scrollWidth,
        visibleCapabilityPanels: [
          ...document.querySelectorAll("[data-capability-panel]:not([hidden])"),
        ].length,
      };
    });

    assert.ok(
      layout.scrollWidth <= layout.clientWidth,
      `document overflows at ${width}px: ${layout.scrollWidth}px > ${layout.clientWidth}px`
    );
    if (width <= mobileViewportMax) {
      assert.ok(
        layout.filterScrollable,
        `filter bar must remain horizontally scrollable at ${width}px`
      );
    }
    assert.ok(
      layout.codeBlocksContained,
      `installation commands must stay inside their cards at ${width}px`
    );
    assert.ok(
      layout.capabilityExplorerContained,
      `capability explorer must stay inside its frame at ${width}px`
    );
    assert.equal(
      layout.visibleCapabilityPanels,
      1,
      `exactly one capability panel must be visible at ${width}px`
    );

    if (width === viewports[0]) {
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
} finally {
  await browser.close();
}
