# Agent Instructions

<!-- OPENSPEC-SPECKIT-GLOBAL:START -->
## Shared OpenSpec/Speckit Protocol

This repo uses the user-global OpenSpec/Speckit workflow instead of duplicating
process rules in every repository.

- Global agent entrypoint: `$HOME/.agents/AGENTS.md`
- Workflow protocol: `$HOME/.agents/protocols/openspec-speckit-workflow.md`
- Bootstrap contract: `$HOME/.agents/protocols/project-agent-bootstrap.md`

Repo-local sections below remain authoritative for project-specific commands,
runtime prerequisites, source-of-truth docs, tests, and deployment constraints.
<!-- OPENSPEC-SPECKIT-GLOBAL:END -->

## Repository Role

openChart is the public Frappe-native clinical chart foundation. It must remain
independently usable without MedxFactory, MedxEHR, or openPractice and must not
copy or fork OpenEMR or Marley implementation code.

## Safety and Data

- Never commit real PHI, credentials, decrypted records, wallet secrets, or
  encryption keys.
- Use synthetic or explicitly de-identified fixtures for development and tests.
- Preserve provenance, signing, amendments, record authority, consent, and
  audit behavior in clinical designs.
- Do not enable autonomous clinical actions by default.

## Current Runtime Status

The repository is at governance-scaffold stage. There are no Frappe runtime,
build, migration, or test commands yet. Add those commands here when the first
governed implementation establishes them.
