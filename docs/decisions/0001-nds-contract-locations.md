---
status: accepted
date: '2026-10-24'
adaptation:
  standard:
    id: std-0001
  rules:
  - R-0018
  paths:
  - config
  - module.yaml
  - modules
  - standarts.lock
  reason: The owner-approved repository README decision (2026-10-24) and NDS system ADR 0013 keep
    NDS-owned material at fixed top-level locations in this repository.
  result: '`config`: Synthetic self-hosting values and exact public server Gitlink owned by this example.
    `module.yaml`: NDS module descriptor owned by the product standards corpus. `modules`: Synthetic self-hosting
    values and exact public server Gitlink owned by this example. `standarts.lock`: NDS contract lock
    pinning the standards source.'
  verification: Review against the repository README decision and ADR 0013; the root catalog check validates
    NDS descriptors and locks, and the repository's own checks exercise the remaining paths.
---
# NDS contract locations

The owner approved the [repository README decision](../../README.md) and NDS system [ADR 0013](https://github.com/NDDev-Technocracy-OpenNetwork-NDS/nddev-device-sync/blob/main/standarts/decisions/0013-estate-hygiene-and-standards-adoption.md), which keep NDS-owned material at
deliberate top-level locations in this repository. This record scopes
those decisions to this repository under std-0001 R-0037 and replaces the
earlier manifest variations without changing them.

- `config` (infrastructure): Synthetic self-hosting values and exact public server Gitlink owned by this example.
- `module.yaml` (manifest): NDS module descriptor owned by the product standards corpus.
- `modules` (infrastructure): Synthetic self-hosting values and exact public server Gitlink owned by this example.
- `standarts.lock` (lock): NDS contract lock pinning the standards source.
