# DALO Setup

DALO is the only source manager and installer for this repository. The
first-party collection is one trusted team source; public repositories are
separate, selectively pinned catalogs.

## First-Party Source and Targets

```sh
dalo init
dalo target link codex
dalo target link generic ~/.agents/skills
dalo source add sebastian git@github.com:sebastian-software/skills.sebastian-software.com.git
```

Run `dalo target detect` first when setting up a different machine, and link only
the targets used there.

## External Catalogs

Register the repositories without activating their full inventories:

```sh
dalo source add-catalog marketingskills https://github.com/coreyhaines31/marketingskills.git
dalo source add-catalog antfu-skills https://github.com/antfu/skills.git
dalo source inspect marketingskills
dalo source inspect antfu-skills
```

Select exactly the reviewed set:

```sh
dalo source select marketingskills \
  copy-editing \
  copywriting \
  product-marketing \
  marketing-plan \
  launch \
  pricing \
  customer-research \
  competitor-profiling \
  competitors \
  content-strategy \
  analytics \
  cro \
  seo-audit \
  ai-seo \
  marketing-ideas \
  marketing-psychology

dalo source select antfu-skills vitest
```

Catalogs start untrusted. After reviewing the selected content, grant
source-scoped approvals through DALO:

```sh
dalo approve source marketingskills
dalo approve source antfu-skills
dalo approve list
```

The catalog selection remains the activation gate. A source approval does not
select newly discovered skills.

## Sync and Review

```sh
dalo status
dalo sync
dalo doctor
dalo source refresh marketingskills
dalo source refresh antfu-skills
```

`source refresh` reports upstream drift without advancing catalog pins or
activating new skills. Review changed selections before accepting a future pin.

External skills keep their upstream slot names. For example, `copywriting` and
`vitest` replace the former repository-local names `marketingskills-copywriting`
and `antfu-vitest`.
