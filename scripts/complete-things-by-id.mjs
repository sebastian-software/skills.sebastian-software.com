import childProcess from "node:child_process";
import fs from "node:fs";
import path from "node:path";

function appleString(value) {
  return `"${String(value || "")
    .replace(/\\/g, "\\\\")
    .replace(/"/g, '\\"')
    .replace(/\r?\n/g, "\\n")}"`;
}

function chunk(items, size) {
  const chunks = [];
  for (let index = 0; index < items.length; index += size) {
    chunks.push(items.slice(index, index + size));
  }
  return chunks;
}

function normalizeInput(payload) {
  if (Array.isArray(payload)) {
    return payload.map(String);
  }
  if (Array.isArray(payload.ids)) {
    return payload.ids.map(String);
  }
  if (Array.isArray(payload.assignments)) {
    return payload.assignments.map((item) => String(item.id));
  }
  throw new Error("Input must be an array, { ids: [...] }, or { assignments: [{ id }] }");
}

function writeBatchScript(outputDir, ids, batchNumber) {
  const lines = [
    "set completedCount to 0",
    "set alreadyCount to 0",
    "set missingCount to 0",
    "set failureCount to 0",
    "set detailText to \"\"",
    "tell application \"Things3\"",
  ];

  for (const id of ids) {
    lines.push("try");
    lines.push(`set targetToDo to to do id ${appleString(id)}`);
    lines.push("if status of targetToDo is completed then");
    lines.push("set alreadyCount to alreadyCount + 1");
    lines.push("else");
    lines.push("set status of targetToDo to completed");
    lines.push("set completedCount to completedCount + 1");
    lines.push("end if");
    lines.push("on error errMsg number errNum");
    lines.push("if errNum is -1728 then");
    lines.push("set missingCount to missingCount + 1");
    lines.push(`set detailText to detailText & ${appleString(id)} & tab & "missing" & tab & errNum & tab & errMsg & linefeed`);
    lines.push("else");
    lines.push("set failureCount to failureCount + 1");
    lines.push(`set detailText to detailText & ${appleString(id)} & tab & "failure" & tab & errNum & tab & errMsg & linefeed`);
    lines.push("end if");
    lines.push("end try");
  }

  lines.push("end tell");
  lines.push(
    'return "completed=" & completedCount & " already=" & alreadyCount & " missing=" & missingCount & " failures=" & failureCount & linefeed & detailText',
  );

  const scriptPath = path.join(outputDir, `complete-${String(batchNumber).padStart(3, "0")}.applescript`);
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
    throw new Error("Usage: node scripts/complete-things-by-id.mjs <ids.json> <output-dir> --apply [--batch-size=50]");
  }
  if (!apply) {
    throw new Error("Refusing to mutate Things without --apply");
  }

  const payload = JSON.parse(fs.readFileSync(inputPath, "utf8"));
  const ids = [...new Set(normalizeInput(payload))].sort();

  fs.mkdirSync(outputDir, { recursive: true });
  const manifest = {
    generatedAt: new Date().toISOString(),
    inputPath,
    ids: ids.length,
    batchSize,
  };
  fs.writeFileSync(path.join(outputDir, "manifest.json"), JSON.stringify(manifest, null, 2));
  fs.writeFileSync(path.join(outputDir, "ids.json"), JSON.stringify(ids, null, 2));

  const runLogPath = path.join(outputDir, "run.log");
  fs.writeFileSync(runLogPath, "");

  let totalCompleted = 0;
  let totalAlready = 0;
  let totalMissing = 0;
  let totalFailures = 0;

  for (const [index, batch] of chunk(ids, batchSize).entries()) {
    const scriptPath = writeBatchScript(outputDir, batch, index + 1);
    console.log(`${new Date().toISOString()} complete batch ${index + 1}/${Math.ceil(ids.length / batchSize)} ${scriptPath}`);
    const result = runOsascript(scriptPath);
    fs.appendFileSync(runLogPath, `\n## batch ${index + 1}: ${scriptPath}\nexit=${result.status}\nstdout:\n${result.stdout}\nstderr:\n${result.stderr}\n`);
    if (result.status !== 0) {
      throw new Error(`complete batch ${index + 1} failed; see ${runLogPath}`);
    }

    const match = result.stdout.match(/completed=(\d+) already=(\d+) missing=(\d+) failures=(\d+)/);
    if (match) {
      totalCompleted += Number(match[1]);
      totalAlready += Number(match[2]);
      totalMissing += Number(match[3]);
      totalFailures += Number(match[4]);
    }
  }

  const finalManifest = {
    ...manifest,
    totalCompleted,
    totalAlready,
    totalMissing,
    totalFailures,
    outputDir,
  };
  fs.writeFileSync(path.join(outputDir, "manifest.json"), JSON.stringify(finalManifest, null, 2));
  console.log(JSON.stringify(finalManifest, null, 2));
}

main();
