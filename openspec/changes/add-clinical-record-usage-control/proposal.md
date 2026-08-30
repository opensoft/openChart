Status: draft

## Why

openChart's versioned API identifies subject, tenant, purpose, and role, but it
does not yet define portable use-time authority, evidence for refused attempts,
or a bounded confidential-processing path. Clinical record use needs one local
enforcement contract that remains independently deployable while making its
security and deletion claims precise.

## What Changes

- **BREAKING**: Require protected `read`, `amend`, `export`, `disclose`,
  `reconcile`, and `confidential-process` operations at the existing versioned
  API to present current portable authority and policy inputs; requests that
  cannot be evaluated fail closed except through explicit break-glass.
- Distinguish short-lived leases for routine eligible access from fresh
  exercises required for each sensitive operation.
- Record owner-local, attributable allow and refuse use events, including
  malformed, expired, revoked, failed-attestation, and abnormal attempts.
- Make the local decision, owner-local use event, and local mutation atomic
  where possible; route external effects through an idempotent outbox and expose
  indeterminate reconciliation states instead of reporting false success.
- Define explicit break-glass authority, reason, notification, expiry, and
  retrospective-review evidence rather than silently bypassing policy.
- Add a confidential-processing flow in which a governed verifier appraises TEE
  evidence, a KMS independently enforces release for the bound session, and
  only structured, bounded output classes are accepted.
- Treat provider key-event statements as scoped evidence, never proof of
  universal deletion of plaintext, derived data, replicas, or other key paths.
- Keep evidence anchoring asynchronous with an `anchor_pending` state. Public
  payloads conform exactly to one selected, version-pinned neutral public-
  envelope profile, contain no PHI or stable correlatable identifiers, and have
  no openChart-defined public superset; detailed association remains local.
- Consume versioned wallet, authority, consent, and deployment-policy inputs
  through portable interfaces without a direct MedxFactory or MedxEHR runtime
  dependency.
- Require unconditional owner ratification in a durable record before creating
  the single Speckit feature, and require separate project-constitution adoption
  plus a meaningful Constitution Check before that feature advances to plan.

## Capabilities

### New Capabilities

- `clinical-record-usage-control`: Defines portable use-time policy
  enforcement, leases and exercises, break-glass, owner-local evidence,
  confidential processing, bounded outputs, key-event claims, and private
  asynchronous anchoring for clinical record operations.

### Modified Capabilities

- `expanded-patient-intake`: Strengthens the existing versioned API requirement
  so protected reads and amendments use the clinical record-use gate while
  preserving standalone operation and the supported extension boundary.

## Impact

- **Versioned API:** protected operations gain authority, policy, exercise or
  lease, break-glass, decision, output, and anchoring contracts at the existing
  service boundary.
- **Clinical records and audit:** owner-local use events become part of the
  immutable audit relationship for successful and unsuccessful attempts, with
  atomic local persistence and explicit reconciliation for uncertain external
  effects.
- **External interfaces:** portable authority/policy providers, governed TEE
  verifier, KMS/HSM, and asynchronous anchor adapters are consumed through
  versioned contracts; no Medx application is required for standalone use.
- **Security and privacy:** required authority evaluation fails closed,
  structured outputs are bounded, and public evidence excludes PHI and granular
  access metadata while conforming to one pinned neutral envelope profile.
- **Implementation handoff:** this OpenSpec change governs exactly one Speckit
  feature for specification, planning, implementation, and verification after
  durable owner ratification; constitution adoption remains separate project
  governance.
