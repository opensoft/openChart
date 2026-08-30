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

The repository contains the realized original Frappe v15 application
`open_chart`, built by feature `001-expanded-patient-intake`. It includes the
expanded-intake DocTypes, the guarded versioned `open_chart.api.v1` service
boundary, migrations, synthetic fixtures, and standalone contract coverage.
The pinned support matrix is Frappe v15, Python 3.11, and MariaDB 10.6.

Use the validation commands published in README.md:

- `make validate` runs the bench-free repository checks, simulated golden round
  trip, fixture-safety checks, negative corpus, and guard probes.
- `make validate-docker` runs installation, migrations, and live golden-round-
  trip tests on the pinned Docker matrix; it reports a loud skip when Docker is
  unavailable.

The application and its validation must remain independently usable without a
MedxFactory, MedxEHR, or openPractice application installed. Use only synthetic
or explicitly de-identified test data and preserve the safety and portability
rules above.
