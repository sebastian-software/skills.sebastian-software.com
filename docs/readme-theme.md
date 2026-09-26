# Maintaining the README

The root README is a short entry point: purpose, a compact skill overview, one
installation example, and links for users and contributors. The homepage owns
detailed use cases, positioning, and inventory counts; `docs/dalo.md` owns the
managed setup guide. Link to these owners instead of repeating their content.

Edit `README.md.src`; `README.md` is committed output.
Sebastian-Theme supplies the company badge in
the existing badge row and a compact footer. Project content stays in this repo.

## Set up the contributor tool

Follow the one-time [contributor setup](contributor-checks.md#set-up-once-per-clone),
then run:

```sh
mise run readme:write
mise run readme:check
```

The CLI version belongs to this project in `mise.toml`; `mise.lock` records
release checksums for Linux, macOS, and Windows. README tasks require the
installed pin and never install a missing tool or fall back to a system binary.
This is contributor tooling; people using the project do not need mdtheme.

Edit prose and project badges in `README.md.src`. Keep one ordered pair of
`mdtheme:badges` markers. Do not copy the Sebastian badge or footer into the
source. Review and commit both source and generated output. CI runs the same
read-only check on every pull request and push to the default branch.

## Before pushing

The pre-push hook runs `mise run readme:check` when a push changes
`README.md.src`, `README.md`, or `mdtheme.yaml`. On a failure, run
`mise run readme:write`, review the output, and commit it yourself. The hook
never stages, commits, or pushes. See [contributor checks](contributor-checks.md)
for the hook setup.

## Update the tool or theme

Update the CLI version in `mise.toml`, then run:

```sh
mise lock --platform linux-arm64,linux-x64,macos-arm64,macos-x64,windows-x64
mise install --locked
mise run readme:write
mise run readme:check
```

Review the lockfile and output together. The theme is pinned separately in
`mdtheme.yaml`. Change its `ref` to a reviewed commit to update branding.
Branches and tags also work; `main` follows branding changes on every run.
Generation and checking need Git access to the theme repository even when the
CLI is already installed. Theme files are data; mdtheme does not execute them.

The [README ownership decision](adr/0006-compose-readme-with-mdtheme.md) records this contract.
