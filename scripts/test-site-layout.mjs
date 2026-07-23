import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import { chromium } from "playwright-core";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const siteUrl = pathToFileURL(resolve(root, "site", "index.html")).href;
const viewports = [320, 360, 375, 400];
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
      const codeBlocks = [...document.querySelectorAll(".code-block")];
      return {
        clientWidth: root.clientWidth,
        codeBlocksContained: codeBlocks.every(
          (block) => block.scrollWidth <= block.clientWidth
        ),
        filterScrollable: Boolean(filter && filter.scrollWidth > filter.clientWidth),
        scrollWidth: root.scrollWidth,
      };
    });

    assert.ok(
      layout.scrollWidth <= layout.clientWidth,
      `document overflows at ${width}px: ${layout.scrollWidth}px > ${layout.clientWidth}px`
    );
    assert.ok(
      layout.filterScrollable,
      `filter bar must remain horizontally scrollable at ${width}px`
    );
    assert.ok(
      layout.codeBlocksContained,
      `installation commands must stay inside their cards at ${width}px`
    );
    await context.close();
  }
} finally {
  await browser.close();
}
