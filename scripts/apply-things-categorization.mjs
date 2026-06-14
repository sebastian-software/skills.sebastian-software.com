import childProcess from "node:child_process";
import fs from "node:fs";
import path from "node:path";

function parseArgs(argv) {
  const args = {
    dryRunPath: argv[2],
    outputDir: argv[3],
    apply: false,
    batchSize: 100,
    limit: 0,
  };

  for (const arg of argv.slice(4)) {
    if (arg === "--apply") {
      args.apply = true;
    } else if (arg.startsWith("--batch-size=")) {
      args.batchSize = Number(arg.slice("--batch-size=".length));
    } else if (arg.startsWith("--limit=")) {
      args.limit = Number(arg.slice("--limit=".length));
    }
  }

  if (!args.dryRunPath || !args.outputDir) {
    throw new Error("Usage: node scripts/apply-things-categorization.mjs <dry-run.json> <output-dir> --apply [--batch-size=100] [--limit=N]");
  }

  if (!Number.isFinite(args.batchSize) || args.batchSize < 1) {
    throw new Error("--batch-size must be a positive number");
  }

  return args;
}

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

function runOsascript(scriptPath) {
  return childProcess.spawnSync("osascript", [scriptPath], {
    encoding: "utf8",
    maxBuffer: 1024 * 1024 * 20,
  });
}

function writeSetupScript(outputDir, areas, projects) {
  const lines = ["tell application \"Things3\""];

  for (const area of areas) {
    lines.push(`if not (exists area ${appleString(area)}) then`);
    lines.push(`make new area with properties {name:${appleString(area)}}`);
    lines.push("end if");
  }

  for (const { area, project } of projects) {
    lines.push(`if not (exists project ${appleString(project)}) then`);
    lines.push(`set targetProject to make new project with properties {name:${appleString(project)}}`);
    lines.push("else");
    lines.push(`set targetProject to project ${appleString(project)}`);
    lines.push("end if");
    lines.push(`set area of targetProject to area ${appleString(area)}`);
  }

  lines.push("end tell");
  lines.push(`return "setup areas=${areas.length} projects=${projects.length}"`);

  const scriptPath = path.join(outputDir, "setup.applescript");
  fs.writeFileSync(scriptPath, `${lines.join("\n")}\n`);
  return scriptPath;
}

function writeBatchScript(outputDir, batch, batchNumber) {
  const lines = [
    "set appliedCount to 0",
    "set failureCount to 0",
    "set failureText to \"\"",
    "tell application \"Things3\"",
  ];

  for (const assignment of batch) {
    lines.push("try");
    lines.push(`set targetToDo to to do id ${appleString(assignment.id)}`);
    lines.push(`set targetProject to project ${appleString(assignment.proposedProject)}`);
    lines.push("set project of targetToDo to targetProject");
    lines.push("set appliedCount to appliedCount + 1");
    lines.push("on error errMsg number errNum");
    lines.push("set failureCount to failureCount + 1");
    lines.push(
      `set failureText to failureText & ${appleString(assignment.id)} & tab & ${appleString(assignment.proposedArea)} & tab & ${appleString(assignment.proposedProject)} & tab & errNum & tab & errMsg & linefeed`,
    );
    lines.push("end try");
  }

  lines.push("end tell");
  lines.push("return \"applied=\" & appliedCount & \" failures=\" & failureCount & linefeed & failureText");

  const scriptPath = path.join(outputDir, `batch-${String(batchNumber).padStart(3, "0")}.applescript`);
  fs.writeFileSync(scriptPath, `${lines.join("\n")}\n`);
  return scriptPath;
}

function main() {
  const args = parseArgs(process.argv);
  if (!args.apply) {
    throw new Error("Refusing to mutate Things without --apply");
  }

  const dryRun = JSON.parse(fs.readFileSync(args.dryRunPath, "utf8"));
  let assignments = dryRun.assignments.filter((assignment) => assignment.confidence !== "low");
  if (args.limit > 0) {
    assignments = assignments.slice(0, args.limit);
  }

  const areas = [...new Set(assignments.map((assignment) => assignment.proposedArea))].sort((a, b) => a.localeCompare(b, "de"));
  const projectByName = new Map();
  for (const assignment of assignments) {
    const existingArea = projectByName.get(assignment.proposedProject);
    if (existingArea && existingArea !== assignment.proposedArea) {
      throw new Error(`Project name conflict: ${assignment.proposedProject} is assigned to both ${existingArea} and ${assignment.proposedArea}`);
    }
    projectByName.set(assignment.proposedProject, assignment.proposedArea);
  }

  const projects = [...projectByName.entries()]
    .map(([project, area]) => ({ area, project }))
    .sort((a, b) => a.area.localeCompare(b.area, "de") || a.project.localeCompare(b.project, "de"));

  fs.mkdirSync(args.outputDir, { recursive: true });
  const manifest = {
    generatedAt: new Date().toISOString(),
    dryRunPath: args.dryRunPath,
    applyMode: args.limit > 0 ? `limited:${args.limit}` : "full",
    batchSize: args.batchSize,
    assignments: assignments.length,
    targetAreas: areas.length,
    targetProjects: projects.length,
    lowConfidenceSkipped: dryRun.assignments.filter((assignment) => assignment.confidence === "low").length,
  };
  fs.writeFileSync(path.join(args.outputDir, "manifest.json"), JSON.stringify(manifest, null, 2));
  fs.writeFileSync(path.join(args.outputDir, "assignments.json"), JSON.stringify(assignments, null, 2));

  const scriptPaths = [writeSetupScript(args.outputDir, areas, projects)];
  for (const [index, batch] of chunk(assignments, args.batchSize).entries()) {
    scriptPaths.push(writeBatchScript(args.outputDir, batch, index + 1));
  }

  const runLogPath = path.join(args.outputDir, "run.log");
  fs.writeFileSync(runLogPath, "");

  let totalFailures = 0;
  for (const [index, scriptPath] of scriptPaths.entries()) {
    const label = index === 0 ? "setup" : `batch ${index}/${scriptPaths.length - 1}`;
    console.log(`${new Date().toISOString()} ${label} ${scriptPath}`);
    const result = runOsascript(scriptPath);
    fs.appendFileSync(runLogPath, `\n## ${label}: ${scriptPath}\nexit=${result.status}\nstdout:\n${result.stdout}\nstderr:\n${result.stderr}\n`);

    if (result.status !== 0) {
      throw new Error(`${label} failed; see ${runLogPath}`);
    }

    const failureMatch = result.stdout.match(/failures=(\d+)/);
    if (failureMatch) {
      totalFailures += Number(failureMatch[1]);
    }
  }

  console.log(JSON.stringify({ ...manifest, totalFailures, outputDir: args.outputDir }, null, 2));
}

main();
