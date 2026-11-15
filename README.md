# openChart

openChart is a Frappe-native, open-source clinical charting and electronic
medical records platform.

## Status

openChart is an ORIGINAL Frappe v15 application (`open_chart`) — it is not a
fork of OpenEMR or Marley/Frappe Healthcare. The application now EXISTS, in
the code leg at `code/open_chart`: it was built by feature
`001-expanded-patient-intake` under OpenSpec change
`add-expanded-patient-intake-foundation`.

## Product boundary

openChart owns general clinical records and workflows, including patients,
encounters, conditions, allergies, medications, supplements, observations,
results, orders, care plans, documents, provenance, and clinical
interoperability surfaces.

It does not own billing, claims, revenue cycle, or general practice
operations; those belong to [openPractice](https://github.com/opensoft/openPractice).
Medx-specific scenario, evidence, authority, and decision workflows belong to
[MedxEHR](https://github.com/opensoft/MedxEHR), which will extend openChart.

## Original implementation

openChart is an original Frappe application. OpenEMR, Marley/Frappe Healthcare,
other EHR products, and healthcare standards may guide requirements and
interoperability behavior, but their code is not an implementation base for
this project. openChart is not an OpenEMR or Marley fork.

## What exists

Feature 001 delivers the expanded patient intake foundation:

- **11 `OC`-prefixed DocTypes**: OC Patient, OC Patient External Identifier,
  OC Intake Submission, and eight statement DocTypes — OC Medication
  Statement, OC Supplement Statement, OC Condition Statement, OC Allergy
  Statement, OC Observation Statement, OC Symptom Statement, OC Goal
  Statement, and OC Document Reference Statement.
- **A versioned API**, `open_chart.api.v1` (`code/open_chart/api/v1.py`), as
  the only supported write surface: `submit`, `amend`, `read_submission`
  (submission read-back), and `register_external_identifier`. Submit is
  idempotent on repeat calls with identical content; amendments are
  succession-based (never in-place edits of an accepted submission); an
  identity conflict routes to review — it is never silently merged.
- **Guarded controllers**: DocType controllers reject direct table writes
  that bypass the API's guard flag, so `open_chart.api.v1` remains the one
  path into clinical data.

## Support matrix

Pinned (widening is a reviewed change): Frappe v15, Python 3.11, MariaDB 10.6.

## Quickstart

Clone this assembly root with both legs, then bootstrap, and run every
`make` target from this root:

```sh
git clone --recurse-submodules https://github.com/opensoft/openChart.git
cd openChart
make bootstrap
```

`make bootstrap` puts each leg on its tracking branch at its pinned commit, or
says why it did not, then runs the validators and prints a review-authority
readout (its `authority is not wallet-carried in this org` line is a report,
not a fault).

Two validation tiers:

- **Bench-free repo checks** — `make validate`, the gate. It runs
  `make validate-content`, then the shape's naming, manifest, and lockstep-pin
  validators. `make validate-content` is the content checks alone:
  `code/scripts/validate.py` (vendored-fixture pin drift, intake census
  coverage, DocType shape, a simulated golden round trip, and fixture
  safety), `code/scripts/harness.py` (the negative corpus with neutralization
  probes, planted-safety probes, and the guard probe), and the
  `test_live_runner*.py` unit tests for the live QA runner. `make pins` runs
  the lockstep pin validator alone. Needs Python 3.11 or later with PyYAML;
  no bench or Docker required.
- **Docker-gated bench suite** — `make validate-docker`. Runs site install,
  migrations, and the live golden round-trip tests on the pinned matrix via
  the `frappe/bench:v5.31.0` and `mariadb:10.6.27` images
  (`code/docker/compose.yaml`). It pulls images and builds a bench, so it is
  slow; the bench run reports `OC-DOCKER-RESULT: PASS` or `FAIL at step ...`.
  The target has no skip of its own and fails without Docker. The loud skip
  banner is printed by `code/scripts/validate.py` during `make validate` and
  `make validate-content`: a `SKIP bench-dependent checks` banner when Docker
  is absent, a NOTE that the Docker-gated checks did not run when it is
  present.
- **Installing into an existing bench**: the Frappe app is the code leg, not
  this root. `bench get-app https://github.com/opensoft/openChart-code`, then
  `bench --site <site> install-app open_chart`. The app reads the intake
  census from the spec leg's contracts: from a `contracts/` directory in the
  app, if there is one, otherwise from the directory named by the
  `CONTRACTS_DIR` environment variable, so point `CONTRACTS_DIR` at
  `spec/contracts` from a checkout of
  [openChart-spec](https://github.com/opensoft/openChart-spec).

## Contract pin

Vendored MedxFactory surfaces under `code/tests/fixtures/medx/` are pinned by
digest in `spec/contracts/medx-pin.yaml` (bundle
`one-patient-integration-contracts` 1.4.0). The intake field census — every
golden intake field mapped to its DocType field — lives in
`spec/contracts/intake-census.yaml`. Gate `G2` (intake fidelity) is co-owned
with p6/HealthLinc; this repo's acceptance is standalone conformance — the
golden round trip passing with no Medx application installed.

## Safety

All fixtures are synthetic (`SYN-` discipline); no real PHI or credentials
are committed. Statements record the patient's reported wording as
`patient_reported` assertions — never prescriptions, diagnoses, or orders.

## Spec-driven development

Product and architecture changes use OpenSpec for governance and Spec Kit for
feature specification, planning, implementation, and verification. Specs and
code live in separate repositories — the spec leg (`spec/`) and the code leg
(`code/`) — and this assembly root pins the commit of each, so each
implementation commit remains traceable to its requirements and tests.

See [AGENTS.md](AGENTS.md) for the shared workflow and repository
constraints, and [AGENTS-shape.md](AGENTS-shape.md) for the rules of the
layout.

## Doc index

- `spec/contracts/medx-pin.yaml` — the MedxFactory contract pin and vendored
  fixture digests.
- `spec/contracts/intake-census.yaml` — the golden intake field census.
- `contracts/spec-pin.yaml`, `contracts/code-pin.yaml`, and
  `contracts/shape-pin.yaml` — this root's own pins: the commit of each leg,
  and the openRepoShape revision with the digests of the files copied from it.
  The product contracts above are in the spec leg, not in this root's
  `contracts/`.
- `spec/specs/001-expanded-patient-intake/` — spec, architect brief, plan, and
  tasks for this feature.
- `spec/openspec/specs/expanded-patient-intake/spec.md` — the promoted
  capability specification.
- `spec/openspec/changes/archive/2026-08-05-add-expanded-patient-intake-foundation/`
  — the governing OpenSpec change record (archived on landing).

## License

Licensed under the [Apache License 2.0](LICENSE).

Never commit real patient information, credentials, decrypted clinical
records, wallet secrets, or encryption keys to this repository.

## Recovered live QA tools

[Persistent synthetic QA procedure](code/docker/QA.md) and
[historical p4 scenario record](spec/specs/001-expanded-patient-intake/scenario-live-half.md).
The August 2026 evidence is retained as captured; recovery is not a new live
acceptance result. From this root, run
`uv run code/scripts/run_p4_live.py --self-test` offline.

## Triad development

Clone with `git clone --recurse-submodules` and run `make bootstrap`, then
`make validate`.
The assembly pins [openChart-spec](https://github.com/opensoft/openChart-spec)
at `spec/` and [openChart-code](https://github.com/opensoft/openChart-code)
at `code/`:

- This root holds the manifest (`project.yaml`), the pins (`contracts/`), the
  gate (`Makefile`, `shape/Makefile`, and the shape's validators in
  `scripts/`), the assistant instructions, and this front door. It holds no
  product code.
- The spec leg (`spec/`) holds the requirements and decisions: feature specs
  in `spec/specs/`, OpenSpec changes and capability specs in `spec/openspec/`,
  `spec/ideation/`, and the contracts in `spec/contracts/`.
- The code leg (`code/`) holds the implementation and its tests: the Frappe
  app in `code/open_chart/`, plus `code/scripts/`, `code/tests/`, and
  `code/docker/`.

Contracts live in `spec/contracts/`. The root exports
`CONTRACTS_DIR` for code validation. Live evidence is written under `spec/specs/`.

The maintained shape targets are included from `shape/Makefile`.
`make validate` runs shape checks and the content suite.
`make validate-docker` runs the Frappe integration environment.

See [the adoption proposal](spec/openspec/changes/adopt-openchart-triad/proposal.md)
and [implementation tasks](spec/specs/002-triad-adoption/tasks.md).
Historical single-repository worktrees retain their original commits.

## The lockstep invariant

Advancing a leg is ONE commit in this repository, made after the change is
committed and pushed in the leg. It moves three things together: the gitlink
recorded at the leg's path (`spec` or `code`), `commit:` (with its tree digest)
in `contracts/spec-pin.yaml` or `contracts/code-pin.yaml`, and every
`.github/workflows/*.yml` `@<sha>` reference naming that leg. A bare
`git submodule update` moves the gitlink alone and leaves the pin behind.
`make pins` (`scripts/validate-pins.py`, also run by `make validate` and by the
`validate` pull-request workflow) refuses when the three disagree. See
[AGENTS-shape.md](AGENTS-shape.md) for the full rule.
