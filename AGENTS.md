Read AGENTS-shape.md first -- the rules of this repository shape.

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

The code leg (`code/`) holds the realized Frappe v15 application `open_chart`,
at `code/open_chart`, built by feature `001-expanded-patient-intake`. It
contains the `OC`-prefixed DocTypes (patient, external identifier, intake
submission, and the clinical statement families), the guarded versioned
`open_chart.api.v1` service boundary, synthetic fixtures and MedxFactory
contract fixtures (digest-pinned by `spec/contracts/medx-pin.yaml`) under
`code/tests/fixtures/`, and a bench test suite. There are no patch scripts:
`bench migrate` syncs the DocType JSON. The pinned support matrix is Frappe
v15, Python 3.11, and MariaDB 10.6. Requirements and contracts live in the spec
leg (`spec/`).

Run these commands from this assembly root:

- `make bootstrap` is the first command after `git clone --recurse-submodules`.
  It puts each leg on its tracking branch at its pinned commit, or says why it
  did not, then runs the validators.
- `make validate` is the gate; the `validate` and `content` pull-request
  workflows together cover it. It runs `make validate-content`, then the
  shape's naming, manifest, and lockstep-pin validators. It needs Python 3.11
  or later with PyYAML, and neither a bench nor Docker.
- `make validate-content` runs the content checks alone:
  `code/scripts/validate.py` (vendored-fixture pin drift, intake census
  coverage, DocType shape, a simulated golden round trip, and fixture safety),
  `code/scripts/harness.py` (the negative corpus with neutralization probes,
  planted-safety probes, and the guard probe), and the `test_live_runner*.py`
  unit tests for the live QA runner.
- `make pins` runs the lockstep pin validator alone.
- `make validate-docker` runs what needs a bench, on the pinned matrix, through
  `code/docker/compose.yaml` (`frappe/bench:v5.31.0`, `mariadb:10.6.27`): a
  clean Frappe version-15 bench on Python 3.11, a site with `open_chart`
  installed alone, `bench migrate`, and the app's bench tests, including the
  live golden round trip. It pulls images and builds a bench, so it is slow,
  and it ends with `OC-DOCKER-RESULT: PASS` or `FAIL at step ...`. The target
  has no skip of its own and fails without Docker. The loud skip banner is
  printed by `code/scripts/validate.py`, so `make validate` reports that the
  Docker-gated checks did not run: a `SKIP bench-dependent checks` banner when
  Docker is absent, a NOTE when it is present.

The application and its validation must remain independently usable without a
MedxFactory, MedxEHR, or openPractice application installed (the Docker gate
installs `open_chart` alone). Use only synthetic or explicitly de-identified
test data, as in Safety and Data above.

## Triad layout

Specifications and contracts are in spec/. Implementation and tests are in code/.
Run make validate from this assembly root. Live evidence is written under spec/specs/.
