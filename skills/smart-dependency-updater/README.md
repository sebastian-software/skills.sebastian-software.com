[← Sebastian Software Skills](../../README.md)

# Smart Dependency Updater — moved

**This skill has moved into [effective-delivery](../effective-delivery/README.md).**

`smart-dependency-updater` is a deprecation stub. It stays installable for one release window so
existing selections keep resolving, then it is removed. It contains no guidance:
the workflow, references, and review scenarios all moved to `effective-delivery`.

**Where it went:** Dependency Updates (references/route-dependencies.md)

See [MIGRATION.md](../../MIGRATION.md) for the complete old-to-new mapping.

## Install the successor

```sh
npx skills add sebastian-software/skills.sebastian-software.com --skill effective-delivery
```

Or follow the [DALO setup guide](../../docs/dalo.md):

```sh
dalo source select sebastian effective-delivery
dalo approve skill sebastian:effective-delivery
dalo sync
```

If you previously selected `smart-dependency-updater`, drop that selection when you add the
successor.

## About Sebastian Software

This skill is maintained by [Sebastian Software](https://oss.sebastian-software.com/),
where we build and support open-source software. We also help teams design,
modernize, and ship ambitious software products through
[our consulting practice](https://sebastian-consulting.com/en).

## License

MIT — see the collection [LICENSE](../../LICENSE).
