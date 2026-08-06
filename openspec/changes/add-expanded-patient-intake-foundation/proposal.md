code_surface: openChart (the original open_chart Frappe application: app package and site-install path, Patient / Patient External Identifier / Intake Submission / typed statement DocTypes, migrations, permissions, audit, the versioned idempotent intake API, supported MedxEHR extension seams, synthetic fixtures and contract tests against the pinned MedxFactory golden intake layer; bench-dependent checks Docker-gated; no clinician workflows, no billing, no external-EHR adapters, no reconciliation decisions)
target_release: intake foundation v1 — archives on a landed, validator-green open_chart application whose golden-patient intake round-trip passes STANDALONE (no Medx application installed), with the accepted MedxFactory one-patient-integration-contracts intake and identity surfaces pinned by digest and the supported extension surfaces published for MedxEHR and HealthLinc
Status: ratified
Ratified by: Brett Heap's direction to start p4 ("build the Frappe foundation") on 2026-08-05 at the Spec Kit handoff (feature `001-expanded-patient-intake`). The proposal predated the front-matter convention; this stamp adds it. design.md's three open questions (Frappe/Python support matrix, synchronous terminology scope, child-table vs DocType split) carry to the feature's clarify round together with the toolchain question (no local bench; Docker present) and do not block the ratified requirement set.

## Why

OpenEMR does not represent the complete patient-reported medication,
supplement, adherence, symptom, and goal context MedxFactory needs. openChart
requires a small, independently useful Frappe foundation that can accept this
expanded intake without depending on MedxFactory or copying another EHR.

## What Changes

- Bootstrap the original openChart Frappe application and its governed runtime,
  migration, permission, test, and audit conventions.
- Add general Patient and Patient External Identifier records required by the
  first clinical profile.
- Add immutable or versioned Intake Submission records and structured patient-
  reported medication, OTC, supplement, condition, allergy, observation,
  symptom, goal, and document-reference statements.
- Preserve original wording, product and ingredient detail, formulation, dose,
  timing, indication, adherence, provenance, confidence, amendments, and raw-
  submission reference where supplied.
- Add a versioned, idempotent intake API plus producer and consumer contract
  tests against the accepted golden-patient fixture.
- Add the supported hooks and APIs MedxEHR needs to reference openChart records
  without direct table coupling.
- Exclude clinician ordering, full encounters, billing, Medx reasoning,
  external-EHR adapters, reconciliation decisions, and autonomous action.

## Capabilities

### New Capabilities

- `expanded-patient-intake`: Defines openChart's standalone patient identity,
  versioned expanded intake, patient-reported clinical statements, provenance,
  permissions, and supported API behavior.

### Modified Capabilities

None.

## Impact

- **openChart:** first Frappe runtime and general clinical data models, APIs,
  migrations, permissions, audit behavior, tests, and contributor commands.
- **Dependencies:** pins the accepted MedxFactory
  `one-patient-integration-contracts` intake and identity contract versions but
  remains usable without a running MedxFactory deployment.
- **Consumers:** HealthLinc submits the intake contract; MedxEHR references the
  patient and statement records through supported extension surfaces.
- **Safety:** synthetic-only fixtures, explicit patient-report provenance, no
  real PHI in the repository, and no treatment or writeback authority.

Architecture context: MedxFactory's `one-patient-intake-vertical-slice` and
`openchart-openpractice-medxehr` brainstorm packets.

