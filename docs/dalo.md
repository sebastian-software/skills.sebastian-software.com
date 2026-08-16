# DALO Setup

DALO can install a reviewed selection from this first-party skill catalog and
link it into one or more agent targets. Composition with other repositories,
team-wide precedence, and cross-catalog routing belong in a separate downstream
agent stack rather than this source collection.

## Install Selected Skills

Register this repository as a catalog:

```sh
curl -fsSL https://dalo.sh/install.sh | sh
dalo init
dalo target link codex
dalo source add-catalog sebastian https://github.com/sebastian-software/skills.sebastian-software.com.git
dalo source inspect sebastian
dalo source select sebastian effective-web
dalo approve skill sebastian:effective-web
dalo sync
dalo doctor
```

Replace `effective-web` with another discipline name — `effective-product`,
`effective-engineering`, `effective-delivery`, `effective-writing`, or
`effective-marketing` — or select several names in one command. Catalog
selections are pinned. New skills in the repository remain inactive until
explicitly selected and approved. Review selected skills before granting the
source-qualified approval.

If you pinned a pre-consolidation slug such as `pr-review` or
`nonfiction-writing`, it no longer exists upstream. DALO preserves the current
catalog pin during `sync`; `dalo source refresh sebastian --check` reports the
selection as `selected_removed` instead of silently advancing it. Re-pin the
selection to the discipline that absorbed it using
[MIGRATION.md](../MIGRATION.md), then sync again.

## Sync and Review

```sh
dalo status
dalo sync
dalo doctor
dalo source refresh sebastian
```

`source refresh` reports upstream drift without advancing catalog pins or
activating new skills. Review changed selections before accepting a future pin.
