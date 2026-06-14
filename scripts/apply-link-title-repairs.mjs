import childProcess from "node:child_process";
import fs from "node:fs";
import path from "node:path";

function appleString(value) {
  return `"${String(value || "")
    .replace(/\\/g, "\\\\")
    .replace(/"/g, '\\"')
    .replace(/\r?\n/g, "\\n")}"`;
}

function compact(value) {
  return String(value || "").replace(/\s+/g, " ").trim();
}

function titleForThings(value) {
  const title = compact(value);
  return title.length > 220 ? `${title.slice(0, 219)}…` : title;
}

function isGenericTitle(result) {
  const title = compact(result.metadata?.title);
  if (!title || title === "Instagram" || title === "Post") {
    return true;
  }
  if (/\(@[^)]+.\) on X$/.test(title) && result.metadata?.source !== "twitter-oembed") {
    return true;
  }
  if (/^[^:]+:\s*https:\/\/t\.co\/\S+$/i.test(title)) {
    return true;
  }
  return false;
}

function makeNotes(currentNotes, url) {
  const notes = String(currentNotes || "").trim();
  if (!url) {
    return currentNotes || "";
  }
  if (notes.includes(url)) {
    return currentNotes || "";
  }
  if (!notes || /^https?:\/\/\S+\s*$/i.test(notes)) {
    return url;
  }
  return `${currentNotes.replace(/\s+$/g, "")}\n\n${url}`;
}

function chunk(items, size) {
  const chunks = [];
  for (let index = 0; index < items.length; index += size) {
    chunks.push(items.slice(index, index + size));
  }
  return chunks;
}

function writeBatchScript(outputDir, batch, index) {
  const lines = [
    "set appliedCount to 0",
    "set failureCount to 0",
    "set failureText to \"\"",
    "tell application \"Things3\"",
  ];

  for (const repair of batch) {
    lines.push("try");
    lines.push(`set targetToDo to to do id ${appleString(repair.id)}`);
    lines.push(`set name of targetToDo to ${appleString(repair.newName)}`);
    lines.push(`set notes of targetToDo to ${appleString(repair.newNotes)}`);
    lines.push("set appliedCount to appliedCount + 1");
    lines.push("on error errMsg number errNum");
    lines.push("set failureCount to failureCount + 1");
    lines.push(`set failureText to failureText & ${appleString(repair.id)} & tab & errNum & tab & errMsg & linefeed`);
    lines.push("end try");
  }

  lines.push("end tell");
  lines.push("return \"applied=\" & appliedCount & \" failures=\" & failureCount & linefeed & failureText");

  const scriptPath = path.join(outputDir, `title-repair-${String(index).padStart(3, "0")}.applescript`);
  fs.writeFileSync(scriptPath, `${lines.join("\n")}\n`);
  return scriptPath;
}

function runOsascript(scriptPath) {
  return childProcess.spawnSync("osascript", [scriptPath], {
    encoding: "utf8",
    maxBuffer: 1024 * 1024 * 20,
  });
}

function main() {
  const inputPath = process.argv[2];
  const outputDir = process.argv[3];
  const apply = process.argv.includes("--apply");
  const batchSizeArg = process.argv.find((arg) => arg.startsWith("--batch-size="));
  const batchSize = batchSizeArg ? Number(batchSizeArg.slice("--batch-size=".length)) : 50;

  if (!inputPath || !outputDir) {
    throw new Error("Usage: node scripts/apply-link-title-repairs.mjs <metadata.json> <output-dir> --apply [--batch-size=50]");
  }
  if (!apply) {
    throw new Error("Refusing to mutate Things without --apply");
  }

  const metadata = JSON.parse(fs.readFileSync(inputPath, "utf8"));
  const repairs = metadata.results
    .filter((result) => result.shouldRename)
    .filter((result) => result.metadata?.ok && result.metadata?.title)
    .filter((result) => !isGenericTitle(result))
    .map((result) => ({
      id: result.id,
      url: result.url,
      oldName: result.currentName,
      newName: titleForThings(result.metadata.title),
      oldNotes: result.currentNotes || "",
      newNotes: makeNotes(result.currentNotes || "", result.url),
      source: result.metadata.source,
      domain: result.domain,
    }))
    .filter((repair) => repair.newName && repair.newName !== compact(repair.oldName));

  fs.mkdirSync(outputDir, { recursive: true });
  const manifest = {
    generatedAt: new Date().toISOString(),
    inputPath,
    repairs: repairs.length,
    batchSize,
  };
  fs.writeFileSync(path.join(outputDir, "manifest.json"), JSON.stringify(manifest, null, 2));
  fs.writeFileSync(path.join(outputDir, "repairs.json"), JSON.stringify(repairs, null, 2));

  const runLogPath = path.join(outputDir, "run.log");
  fs.writeFileSync(runLogPath, "");

  let totalApplied = 0;
  let totalFailures = 0;
  for (const [index, batch] of chunk(repairs, batchSize).entries()) {
    const scriptPath = writeBatchScript(outputDir, batch, index + 1);
    console.log(`${new Date().toISOString()} title batch ${index + 1}/${Math.ceil(repairs.length / batchSize)} ${scriptPath}`);
    const result = runOsascript(scriptPath);
    fs.appendFileSync(runLogPath, `\n## batch ${index + 1}: ${scriptPath}\nexit=${result.status}\nstdout:\n${result.stdout}\nstderr:\n${result.stderr}\n`);
    if (result.status !== 0) {
      throw new Error(`batch ${index + 1} failed; see ${runLogPath}`);
    }
    const match = result.stdout.match(/applied=(\d+) failures=(\d+)/);
    if (match) {
      totalApplied += Number(match[1]);
      totalFailures += Number(match[2]);
    }
  }

  console.log(JSON.stringify({ ...manifest, totalApplied, totalFailures, outputDir }, null, 2));
}

main();
