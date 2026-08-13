# CLI Contracts

A command-line interface is a process contract, not just a function call. Test
the narrowest seam that preserves the behavior a script, shell user, or
automation can observe.

## Define the Process Contract

For each focused case, identify the relevant inputs and outputs:

- positional arguments, flags, stdin, environment, current directory, and
  configuration files;
- precedence when the same setting appears in several sources;
- exit status and whether failure is recoverable or usage-related;
- stdout for intended machine or user output and stderr for diagnostics;
- created, changed, or removed files; permissions; paths; and cleanup;
- prompts, non-interactive behavior, network calls, child processes, and
  platform-specific assumptions when they affect the requested behavior.

Do not assert every help string in a regression test unless it is the public
contract at risk. Test the behavior that a caller must distinguish.

## Choose the Seam

Test parsing, configuration resolution, and domain decisions directly when
they are cohesive mechanisms. Add a process-level smoke test when command
startup, real argument parsing, stream separation, exit mapping, or filesystem
wiring is itself the claim. The two layers protect different risks and should
remain small.

Use the project-native command harness when available. Otherwise invoke the
real binary with an explicit working directory, environment, input, and
temporary filesystem area. Never run a destructive production command merely
to create test evidence.

## Make Files and Environment Deterministic

Create a unique temporary workspace per case and clean it through the
repository's normal test lifecycle. Write only the fixtures required for the
claim. Use explicit paths and locale, timezone, environment, and home/config
overrides when those values affect behavior. Avoid relying on a developer's
shell aliases, current repository, credentials, installed global tools, or
leftover files.

For output that contains paths, timestamps, terminal color, or unordered data,
normalize only the incidental variation. Keep stable user-facing wording,
machine-readable fields, and stream placement visible to the test.

## Evidence for Common Risks

- **Configuration precedence:** supply conflicting values at each supported
  layer and assert the winning observable behavior, not merely the resolved
  internal object.
- **Output contract:** capture stdout and stderr separately, assert the exit
  code, and parse structured stdout when automation relies on it.
- **Filesystem side effect:** assert the intended created or changed content
  and the absence of an unwanted write or partial result after failure.
- **Failure recovery:** use a safe failing input or injected local boundary;
  prove the command reports the failure and leaves the documented recoverable
  state.

Run the focused command case first and then the repository's relevant broader
CLI checks. Mark platform- or credential-dependent smoke coverage as opt-in
instead of silently skipping it.
