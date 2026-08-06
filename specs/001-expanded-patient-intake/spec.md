# Feature Specification: Expanded Patient Intake Foundation

**Feature Branch**: `001-expanded-patient-intake`
**Created**: 2026-08-05
**Status**: Clarified 2026-08-05 — ready for plan
**Input**: OpenSpec change `add-expanded-patient-intake-foundation`
(ratified 2026-08-05), its design.md, and the MedxFactory one-patient
program's accepted intake surfaces.

## Change Linkage *(immutable)*

- **Governing change**: `add-expanded-patient-intake-foundation`
  (ratified 2026-08-05; eight ADDED requirements, twelve scenarios).
- **This feature**: `specs/001-expanded-patient-intake/` on branch
  `001-expanded-patient-intake` (worktree
  `../openChart-worktrees/001-expanded-patient-intake`).
- The change's task 1.x entry is the change→feature link; this block is
  the feature→change link. Neither may be repointed after acceptance.

## Contract Pin *(binding)*

- **Component**: `p4-expanded-patient-intake-foundation` (the MedxFactory
  one-patient gate registry's roster entry; home repository openChart).
- **Pinned MedxFactory surfaces** (by digest, vendored where consumed):
  `one-patient-integration-contracts` bundle 1.4.0
  (tag `one-patient-contracts/v1.4.0`, manifest sha256
  `30cf554de3422796db63da3078f44fbb0b5891db03bb00bd66685183f11ed167`);
  the golden `20-intake-raw` layer (the intake round-trip fixture);
  `binding-03-openchart` (the identity surface: namespace `openchart`).
- **Gate obligation**: G2 (`intake fidelity`) is co-owned p4 + p6.
  p6 (HealthLinc) is unbuilt: conformant G2 evidence requires both
  owners and therefore lands only when p6 exists — the program's
  established dual-owner rule. p4 is built and accepted STANDALONE; its
  acceptance surface is the golden round-trip passing with no Medx
  application installed.
- openChart remains independently useful: nothing at runtime reads a
  MedxFactory path; pinned surfaces are vendored copies with provenance.

## Clarifications

### Session 2026-08-05 (architect rulings; full options in clarify-questions.md)

- **Q1 — support matrix**: Frappe v15 + Python 3.11 + MariaDB 10.6 (the
  Frappe v15 defaults), pinned in the app manifest and exercised via the
  official frappe_docker images. One matrix in v1; widening is a
  reviewed change.
- **Q2 — synchronous terminology**: none in v1. Statements store the
  patient's reported wording and any supplied codes VERBATIM; enrichment
  is a later change (mirrors the MedxFactory program's terminology
  deferral).
- **Q3 — statement records**: independent DocTypes for every statement
  family — medication (Rx/OTC), supplement, condition, allergy,
  observation, symptom, goal, document reference — because
  reconciliation, amendment, and per-family permissions need stable
  identities (the design's own rationale). Child tables only for true
  composition (e.g. ingredient lists).
- **Q4 — toolchain**: the app tree and DocType JSON are authored as REPO
  CONTENT and validated by openChart's own repo validator without a
  running bench; bench-dependent checks (site install, migrations, the
  live round trip) run inside the official frappe_docker compose and are
  Docker-gated with a loud skip banner — the D9 pattern from the
  MedxFactory program.
- **Q5 — contract vendoring**: the golden intake fixture and the
  openchart binding are VENDORED into openChart's test fixtures with a
  provenance header and the bundle digest pin; a drift check compares
  the vendored copies' digests against the pin record.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - The installable original app (Priority: P1)

An operator installs `open_chart` on a clean supported Frappe site;
migrations complete; the golden-patient intake tests pass with no Medx
application installed. Nothing is forked from OpenEMR or Marley.

### User Story 2 - Identity and the versioned intake lifecycle (Priority: P1)

A patient record carries a local identifier plus namespaced external
identifiers (Medx, HealthLinc) that never replace it or silently merge
patients. An intake draft is saved, resumed, and submitted as ONE
accepted version with full provenance; a retried submit with the same
idempotency key returns the existing submission; an amendment creates a
successor with predecessor, actor, reason, and time while the prior
version stays auditable.

### User Story 3 - Faithful statements and the service boundary (Priority: P2)

Every statement family preserves reported detail — original wording,
product/ingredients, formulation, dose, route, frequency, timing,
indication, adherence, source, confidence, verification state —
with unknown values explicitly unknown. Consumers reach records only
through versioned commands and supported hooks; a direct table write
from an extension is rejected; no statement ever reads as a
prescription, diagnosis, or order.

### Edge Cases

- A dose explicitly marked unknown (accepted; never inferred).
- The same external identifier active on two patients (identity-review
  state, never a merge).
- A submit retry racing a first submit (one logical submission).
- An amendment of an amendment (chain of successors, all auditable).
- A statement family absent from a submission (legal; the manifest says
  which families were submitted).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The `open_chart` Frappe app SHALL install standalone on the
  pinned matrix with repeatable migrations, fixtures, and contributor
  commands; no Medx application is required for any test.
- **FR-002**: `OC Patient` and versioned `OC Patient External Identifier`
  DocTypes SHALL carry issuer/source endpoint, namespace, value, status,
  effective interval, and provenance; an active (issuer, value) pair on
  another patient refuses or enters identity review — never a merge.
- **FR-003**: `OC Intake Submission` SHALL carry patient, contract
  version, submission version, lifecycle state, submitter context,
  purpose/consent reference, timestamps, provenance, client idempotency
  key, and predecessor when amended; accepted content is immutable.
- **FR-004**: Submit SHALL be idempotent on (patient, idempotency key):
  a replay returns the existing accepted submission and creates nothing.
- **FR-005**: Eight statement DocTypes (ruling Q3) SHALL preserve the
  full reported detail census of the golden intake layer; unknown
  optional values persist as explicitly unknown.
- **FR-006**: Amendments SHALL create successor versions referencing
  predecessor, actor, reason, and time; prior accepted content remains
  readable to authorized audit; silent overwrite is structurally
  impossible through the supported surfaces.
- **FR-007**: The versioned intake API (draft, submit, amend, read) SHALL
  enforce subject, tenant, purpose, and role; supported MedxEHR hooks and
  events expose records without direct table writes.
- **FR-008**: Every statement carries `assertion_kind: patient_reported`
  and no API response or event creates a prescription, diagnosis, order,
  administration, recommendation, or autonomous action.
- **FR-009**: The vendored golden intake fixture SHALL round-trip: submit
  through the API, read back, and compare field-for-field against the
  vendored source with zero loss (G2's fidelity claim, exercised
  standalone).
- **FR-010**: A pin record SHALL carry the MedxFactory bundle tag and
  manifest digest plus the vendored files' digests; a drift check
  recomputes both sides on every validator run.
- **FR-011**: Repo-content checks (DocType JSON shape, fixture safety,
  pin drift, census coverage) SHALL run without bench; bench-dependent
  checks Docker-gate with a loud skip banner (ruling Q4).
- **FR-012**: No real PHI, credentials, or production keys; fixtures are
  synthetic (`SYN-` discipline inherited from the program).

### Key Entities

- **OC Patient / OC Patient External Identifier** — local identity plus
  namespaced external references.
- **OC Intake Submission** — the versioned, idempotent lifecycle
  envelope.
- **Statement DocTypes (8)** — medication, supplement, condition,
  allergy, observation, symptom, goal, document reference.
- **Pin record** — the vendored-contract digest ledger.

## Success Criteria *(mandatory)*

- **SC-001**: The repo validator is green with no bench; the Docker-gated
  suite installs the app on a clean site and passes migrations.
- **SC-002**: The golden round-trip compares field-for-field with zero
  loss, standalone.
- **SC-003**: Idempotent replay and amendment lineage proven by tests;
  identity conflict enters review, never merge.
- **SC-004**: The census check maps every golden intake field to a
  DocType field; a missing field fails.
- **SC-005**: Pin drift as two computed values on every validator run.
- **SC-006**: Every check mutation-probed; negative fixtures fire with
  declared classes; coverage table closes the change's verification
  task.

## Assumptions

- The MedxFactory program surfaces are frozen inputs, vendored by digest;
  defects escalate to the architect.
- G2 evidence waits for p6 (dual-owner rule); p4's acceptance is
  standalone conformance.
- MedxEHR extends openChart later through the supported seams only.
