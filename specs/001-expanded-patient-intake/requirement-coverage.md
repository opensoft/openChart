# Requirement Coverage — Feature 001 (T014)

Status: accepted with T017 (2026-08-05)
Closes: `add-expanded-patient-intake-foundation` verification task (change
task 3.x); every FR and SC below names its executable check and where its
firing was WATCHED — a check nobody has seen fail is not evidence.

Conventions: `validate` = `scripts/validate.py`; `harness` =
`scripts/harness.py` (negative corpus + neutralization probes + planted
safety + guard probe + unfired audit); `guard probe` =
`scripts/guard_probe.py` (frappe-stub, subprocess arm of the harness);
`bench suite` = `open_chart/tests/test_intake_api.py` inside
`make validate-docker`. All checks run on every `make validate` except
the bench suite, which is Docker-gated with a loud banner (ruling Q4).

## Functional requirements

| FR | Check(s) | Watched firing |
|----|----------|----------------|
| FR-001 standalone install | `docker/run-checks.sh` (bench init → new site → `install-app open_chart` with no Medx app anywhere → migrate → tests); pinned images in `docker/compose.yaml` | Docker suite run 2026-08-05 (this feature's acceptance run); each step names itself on failure (`fail()` per step) |
| FR-002 identity, conflict → review | `core.identity_decision` (pure); `GuardedIdentifier.validate`; `v1.register_external_identifier` | harness `duplicate-external-id` fixture (decision = identity_review) + input-sensitivity probe (same-patient flip → register); bench `test_identity_conflict_enters_review` |
| FR-003 submission envelope | `oc_intake_submission.json` (12 fields incl. idempotency_key, predecessor, amendment_reason); `v1.submit` | shape checks over the DocType (OC-DOCTYPE-SHAPE branches watched via the doctype-shape fixture); bench round-trip test |
| FR-004 idempotent submit | `core.idempotency_decision`; `v1.submit` replay/diverged branches | harness `idempotency-replay-divergence` fixture (decision = diverged) + input-sensitivity probe (same-hash flip → replay); guard probe fired OC-IDEMPOTENCY-DIVERGED through the real `v1.submit` path; bench `test_idempotent_replay_returns_existing`, `test_divergent_replay_refused` |
| FR-005 census preservation | `census_errors` (OC-CENSUS-GAP: every golden leaf mapped; OC-DOCTYPE-SHAPE: every mapped field present); census as data (`contracts/intake-census.yaml`, brief D9) | harness `census-gap` fixture + neutralization probe; missing-DocType branches watched red during construction (first validate run, 2026-08-05, 8 findings before T005-T007 landed) |
| FR-006 succession amendments | `core.successor_fields` (refuses empty reason); `GuardedSubmission` (OC-ACCEPTED-IMMUTABLE); `v1.amend` | guard probe: tamper fired, legal amend transition passed, transition-without-flag fired; core shakedown: empty-reason ValueError watched; bench `test_amend_creates_successor`, `test_accepted_submission_immutable` |
| FR-007 versioned API, no table writes | `v1._require_context` (OC-CONTEXT-REQUIRED); `GuardedDocument` (OC-DIRECT-WRITE); whitelisted `open_chart.api.v1.*` only | guard probe: both context refusals fired, full context passed; direct write fired, API-flagged write passed; bench `test_direct_table_write_rejected` |
| FR-008 assertion_kind, no clinical actions | `doctype_shape_errors` assertion-default branch; `assertion_kind` read_only in all 8 statement DocTypes; `emit_submission_event` pointer-only payload | doctype-shape fixture `expect_all` branch "assertion_kind must default to patient_reported"; event payload reviewed at T016 coherence (carries name/state/patient only) |
| FR-009 golden round trip | `roundtrip_errors` → `core.simulated_roundtrip_errors` (bench-free half); bench `test_golden_roundtrip_zero_loss` (live half) | harness `roundtrip-loss` fixture (census mapping dropped → loss fired) + neutralization probe; core shakedown watched planted loss AND planted fabrication fire; live half in Docker suite |
| FR-010 pin record + drift | `contracts/medx-pin.yaml`; `pin_drift_errors` (OC-PIN-DRIFT, both digests recomputed every run) | harness `pin-drift` fixture (one appended byte) + neutralization probe |
| FR-011 bench-free vs Docker-gated | `validate.py` runs bench-free (no frappe import anywhere in its path); `docker_gate()` two-branch banner | docker-absent banner text asserted by construction; docker-present note prints on every local validate (observed); a silent branch does not exist |
| FR-012 no real PHI/credentials | `fixture_safety_errors` (key material + synthetic marker) over all fixture YAML | harness planted arms: assembled key-material string fired; missing `synthetic: true` fired |

## Success criteria

| SC | Evidence |
|----|----------|
| SC-001 | `make validate` green bench-free (every commit); Docker suite result recorded in the acceptance record (T017) |
| SC-002 | Simulated round trip green on every validate; live round trip in the Docker suite; zero-loss comparison is bidirectional (loss AND fabrication) |
| SC-003 | Bench suite: replay, divergence, amendment lineage, identity review; decision cores additionally probed bench-free every validate |
| SC-004 | `census_errors` walks every golden entry leaf of every family fixture; unmapped leaf fails (watched) |
| SC-005 | `pin_drift_errors`: pinned digest vs recomputed digest, two computed values per vendored file per run |
| SC-006 | Harness: 6-fixture corpus == `RESULT_CLASSES` == `NEGATIVE_RATCHET` (ratchet self-probed); neutralization probes on all four validate-arm classes; unfired audit over all OC- codes in executable Python (10/10 fired); harness itself meta-probed (wrong `expect` watched failing 2026-08-05) |

## Known boundaries (honest, by design)

- G2 gate evidence is NOT claimed: co-owned with p6 (unbuilt); this
  feature's claim is standalone conformance only (spec Contract Pin).
- The Docker suite's step lines (`docker/run-checks.sh`) are shell, not
  Python — outside the unfired audit's universe; the gate exercises them.
- `emit_submission_event` fires only under bench (realtime transport);
  its no-clinical-content property is enforced by payload construction
  and reviewed, not probed.
