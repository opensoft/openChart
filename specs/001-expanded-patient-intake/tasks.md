# Tasks: Expanded Patient Intake Foundation

Format `[ID] [P?] [tier]` per brief §C. openChart's validator green
before every commit; MedxFactory is never edited; mutation-probe every
check.

## Phase 1: Scaffold
- [x] T001 [opus] App skeleton (pyproject, hooks, modules) + bench-free
      `scripts/validate.py` skeleton + Makefile `validate`.
- [x] T002 [opus] `docker/compose.yaml` (pinned frappe_docker) + site
      bootstrap script + the D7 gate banner helper.
- [x] T003 [opus] Vendor golden intake layer + openchart binding into
      `tests/fixtures/medx/` with provenance headers;
      `contracts/medx-pin.yaml`; drift check (OC-PIN-DRIFT).
- [x] T004 [opus] `contracts/intake-census.yaml` — every golden intake
      field mapped to (doctype, fieldname); census check
      (OC-CENSUS-GAP) fails on unmapped golden fields.

## Phase 2: DocTypes
- [x] T005 [P] [sonnet] OC Patient + OC Patient External Identifier +
      OC Intake Submission DocType JSONs per brief D3/D4/D5.
- [x] T006 [P] [sonnet] OC Medication/Supplement/Condition/Allergy
      Statement DocType JSONs from the census.
- [x] T007 [P] [sonnet] OC Observation/Symptom/Goal/Document Reference
      Statement DocType JSONs from the census.
- [x] T008 [opus] DocType shape checks (OC- prefix, census link,
      submission Link field, assertion_kind default patient_reported,
      unknown-value fields nullable) — OC-DOCTYPE-SHAPE.

## Phase 3: API + lifecycle
- [x] T009 [opus] `open_chart/api/v1.py`: draft/submit/amend/read;
      idempotent submit (D5); succession amendments (D4); subject/
      tenant/purpose/role guards; no direct-table seam (D6).
- [x] T010 [opus] hooks.py events + permission model; the direct-write
      rejection test declaration.
- [x] T011 [opus] Round-trip expectation: golden submission payload
      derived from vendored fixtures + field-for-field comparison spec
      (OC-ROUNDTRIP-LOSS) — executable bench-free against the payload
      builder; live half Docker-gated.
- [x] T012 [P] [sonnet] Negative fixtures: pin-drift, census-gap,
      doctype-shape, roundtrip-loss, duplicate-external-id,
      idempotency-replay-divergence.
- [x] T013 [opus] Harness + arms + probes; ratchet FINAL 6; unfired
      audit (OC-*) at none.

## Phase 4: Polish
- [x] T014 [opus] requirement-coverage.md (closes change verification).
- [x] T015 [P] [sonnet] README updates (status: app exists; quickstart).
- [x] T016 [opus] Coherence pass.
- [ ] T017 [fable] Architect acceptance + change-side records.

Total: 17 tasks (5 sonnet, 11 opus, 1 fable).
