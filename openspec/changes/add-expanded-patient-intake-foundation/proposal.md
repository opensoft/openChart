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

