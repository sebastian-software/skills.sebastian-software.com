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

function writeBatchScript(outputDir, batch, batchNumber) {
  const lines = [
    "set matchedCount to 0",
    "set mismatchCount to 0",
    "set missingCount to 0",
    "set detailText to \"\"",
    "tell application \"Things3\"",
  ];

  for (const assignment of batch) {
    lines.push("try");
    lines.push(`set targetToDo to to do id ${appleString(assignment.id)}`);
    lines.push("set actualProject to \"\"");
    lines.push("try");
    lines.push("set actualProject to name of project of targetToDo");
    lines.push("end try");
    lines.push(`if actualProject is ${appleString(assignment.proposedProject)} then`);
    lines.push("set matchedCount to matchedCount + 1");
    lines.push("else");
    lines.push("set mismatchCount to mismatchCount + 1");
    lines.push(
      `set detailText to detailText & ${appleString(assignment.id)} & tab & ${appleString(assignment.proposedProject)} & tab & actualProject & linefeed`,
    );
    lines.push("end if");
    lines.push("on error errMsg number errNum");
    lines.push("set missingCount to missingCount + 1");
    lines.push(`set detailText to detailText & ${appleString(assignment.id)} & tab & "MISSING" & tab & errNum & tab & errMsg & linefeed`);
    lines.push("end try");
  }

  lines.push("end tell");
  lines.push('return "matched=" & matchedCount & " mismatches=" & mismatchCount & " missing=" & missingCount & linefeed & detailText');

  const scriptPath = path.join(outputDir, `verify-${String(batchNumber).padStart(3, "0")}.applescript`);
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
  const batchSize = Number(process.argv[4] || 50);

  if (!inputPath || !outputDir) {
    throw new Error("Usage: node scripts/verify-things-assignments.mjs <assignments.json> <output-dir> [batch-size]");
  }

  const payload = JSON.parse(fs.readFileSync(inputPath, "utf8"));
  const assignments = (payload.assignments || payload).filter((assignment) => assignment.confidence !== "low");

  fs.mkdirSync(outputDir, { recursive: true });
  const runLogPath = path.join(outputDir, "verify.log");
  fs.writeFileSync(runLogPath, "");

  let totalMatched = 0;
  let totalMismatches = 0;
  let totalMissing = 0;

  for (const [index, batch] of chunk(assignments, batchSize).entries()) {
    const scriptPath = writeBatchScript(outputDir, batch, index + 1);
    console.log(`${new Date().toISOString()} verify batch ${index + 1}/${Math.ceil(assignments.length / batchSize)} ${scriptPath}`);
    const result = runOsascript(scriptPath);
    fs.appendFileSync(runLogPath, `\n## batch ${index + 1}: ${scriptPath}\nexit=${result.status}\nstdout:\n${result.stdout}\nstderr:\n${result.stderr}\n`);
    if (result.status !== 0) {
      throw new Error(`verify batch ${index + 1} failed; see ${runLogPath}`);
    }

    const match = result.stdout.match(/matched=(\d+) mismatches=(\d+) missing=(\d+)/);
    if (match) {
      totalMatched += Number(match[1]);
      totalMismatches += Number(match[2]);
      totalMissing += Number(match[3]);
    }
  }

  const manifest = {
    generatedAt: new Date().toISOString(),
    inputPath,
    assignments: assignments.length,
    totalMatched,
    totalMismatches,
    totalMissing,
    outputDir,
  };
  fs.writeFileSync(path.join(outputDir, "manifest.json"), JSON.stringify(manifest, null, 2));
  console.log(JSON.stringify(manifest, null, 2));
}

main();
