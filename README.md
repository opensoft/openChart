# openChart

openChart is a Frappe-native, open-source clinical charting and electronic
medical records platform.

## Status

openChart is an ORIGINAL Frappe v15 application (`open_chart`) — it is not a
fork of OpenEMR or Marley/Frappe Healthcare. The application now EXISTS: it
was built by feature `001-expanded-patient-intake` under OpenSpec change
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
- **A versioned API**, `open_chart.api.v1`, as the only supported write
  surface: `submit`, `amend`, `read` (submission read-back), and
  `register_external_identifier`. Submit is idempotent on repeat calls with
  identical content; amendments are succession-based (never in-place edits
  of an accepted submission); an identity conflict routes to review — it is
  never silently merged.
- **Guarded controllers**: DocType controllers reject direct table writes
  that bypass the API's guard flag, so `open_chart.api.v1` remains the one
  path into clinical data.

## Support matrix

Pinned (widening is a reviewed change): Frappe v15, Python 3.11, MariaDB 10.6.

## Quickstart

Two validation tiers:

- **Bench-free repo checks** — `make validate`. Runs `scripts/validate.py`
  and `scripts/harness.py`: pin drift, census coverage, DocType shape, a
  simulated golden round trip, fixture safety, the negative corpus, and
  guard probes. No bench or Docker required.
- **Docker-gated bench suite** — `make validate-docker`. Runs site install,
  migrations, and the live golden round-trip tests on the pinned matrix via
  the `frappe/bench` and `mariadb:10.6` images (`docker/compose.yaml`).
  Shows a loud skip banner when Docker is unavailable.
- **Installing into an existing bench**: `bench get-app <this repo>`, then
  `bench --site <site> install-app open_chart`.

## Contract pin

Vendored MedxFactory surfaces under `tests/fixtures/medx/` are pinned by
digest in `contracts/medx-pin.yaml` (bundle `one-patient-integration-contracts`
1.4.0). The intake field census — every golden intake field mapped to its
DocType field — lives in `contracts/intake-census.yaml`. Gate `G2` (intake
fidelity) is co-owned with p6/HealthLinc; this repo's acceptance is standalone
conformance — the golden round trip passing with no Medx application
installed.

## Safety

All fixtures are synthetic (`SYN-` discipline); no real PHI or credentials
are committed. Statements record the patient's reported wording as
`patient_reported` assertions — never prescriptions, diagnoses, or orders.

## Spec-driven development

Product and architecture changes use OpenSpec for governance and Spec Kit for
feature specification, planning, implementation, and verification. Specs and
code live together in this repository so each implementation commit remains
traceable to its requirements and tests.

See [AGENTS.md](AGENTS.md) for the shared workflow and repository constraints.

## Doc index

- `contracts/medx-pin.yaml` — the MedxFactory contract pin and vendored
  fixture digests.
- `contracts/intake-census.yaml` — the golden intake field census.
- `specs/001-expanded-patient-intake/` — spec, architect brief, plan, and
  tasks for this feature.
- `openspec/specs/expanded-patient-intake/spec.md` — the promoted
  capability specification.
- `openspec/changes/archive/2026-08-05-add-expanded-patient-intake-foundation/`
  — the governing OpenSpec change record (archived on landing).

## License

Licensed under the [Apache License 2.0](LICENSE).

Never commit real patient information, credentials, decrypted clinical
records, wallet secrets, or encryption keys to this repository.
