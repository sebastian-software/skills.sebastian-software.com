# Architecture Decision Records

This directory contains durable decisions for the skills collection.

## Convention

- Use zero-padded filenames: `NNNN-kebab-case-title.md`.
- Use `proposed`, `accepted`, `rejected`, `deprecated`, or `superseded` status
  values.
- Accepted records are immutable. Change a decision through a new record and
  link supersession in both directions.
- Keep exact implementation values in their owning code or configuration.
- Add every record to the index below.

## Index

| ADR | Status | Decision |
| --- | --- | --- |
| [ADR-0001](0001-distill-effective-flow-and-retire-the-standalone-system.md) | accepted | Distill independently valuable Effective Flow capabilities and retire the standalone system in stages. |
