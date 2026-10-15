## Context

openChart already owns versioned clinical reads and amendments and rejects
unsupported direct writes. Its promoted intake contract authorizes by subject,
tenant, purpose, and role, but it does not define how portable external
authority and policy become a use-time decision, how sensitive attempts are
evidenced, or how a confidential workload receives keys and returns output.

The design must remain portable: openChart owns access to its clinical bytes and
its audit record, while wallet issuers, deployment policy providers, governed
attestation verifiers, KMS/HSM services, and anchor adapters remain replaceable.
Medx deployments can bind their profiles through those interfaces, but the
public application cannot require a Medx runtime. Patients, clinical users,
auditors, operators, and confidential-workload owners all rely on the resulting
decision and evidence boundaries.

## Goals / Non-Goals

**Goals:**

- Put every protected operation through one versioned openChart use gate.
- Accept provider-neutral authority and policy inputs with explicit versions,
  trust, freshness, scope, and proof-of-possession.
- Separate routine leases from per-sensitive-operation exercises.
- Make break-glass an explicit, bounded, reviewable authority path.
- Retain owner-local evidence for allowed, refused, and failed attempts.
- Commit local decisions, use events, and mutations atomically where possible,
  and never report uncertain external effects as successful.
- Keep policy decision, TEE appraisal, and KMS release as independent checks.
- Accept only structured, bounded confidential-processing outputs.
- Describe key and anchoring evidence without overstating deletion, exposing
  PHI, defining an openChart public-envelope superset, or publishing stable
  correlatable identifiers.

**Non-Goals:**

- Prevent an authorized human from copying information they can perceive.
- Make a TEE measurement proof of workload correctness or non-exfiltration.
- Make a key-event statement proof that every plaintext or key copy is gone.
- Put PHI, record selectors, purposes, or granular access metadata on a public
  chain.
- Make public-anchor availability a prerequisite for record reconstruction or
  urgent care.
- Define a local public-envelope variant or add openChart public fields beyond
  the selected neutral profile.
- Define Medx-specific roles, grants, retention rules, or decision workflows.
- Add billing, claims, autonomous clinical action, or a second clinical data
  access path.

## Decisions

### 1. Extend the existing versioned service boundary with one use gate

`read`, `amend`, `export`, `disclose`, `reconcile`, and
`confidential-process` enter the same gate before openChart selects, mutates, or
streams protected records. The gate binds actor or workload, subject, tenant,
purpose, operation, record-set selector, authority and policy versions, and the
requested output class to one decision. Internal or extension paths cannot
skip it.

This extends the current API rather than introducing a parallel secure API,
because parallel paths would drift and leave bypasses. The behavior is breaking
for protected callers that cannot supply the new contract.

### 2. Normalize portable authority and policy at adapters

Trusted adapters validate issuer signatures, proof-of-possession, status,
freshness, scope, and policy provenance, then supply versioned provider-neutral
inputs to the local decision engine. The decision records both the normalized
claims and opaque references or digests needed to verify their source. A
deployment can use local, wallet-compatible, or remote policy providers without
changing clinical operation semantics.

Direct Medx object imports and mandatory chain lookups were rejected because
they would make standalone openChart unavailable when another product or public
network is absent. Unavailable or stale required inputs produce a refusal, not
an optimistic allow.

### 3. Use bounded leases only for routine eligible reads

A full evaluation can issue a short-lived lease for routine reads whose actor,
subject, tenant, purpose, selector bounds, policy versions, and revocation
freshness ceiling remain unchanged. Bulk reads and every `amend`, `export`,
`disclose`, `reconcile`, and `confidential-process` request require a fresh,
single-operation exercise. An exercise cannot be replayed for a second
operation, and a lease cannot widen its original scope.

Per-read external lookups were rejected as the only mode because they create an
availability and latency dependency. Unbounded sessions were rejected because
they weaken revocation and purpose enforcement.

### 4. Model break-glass as explicit authority, never an implicit override

Break-glass requires an authenticated eligible actor, a configured operation
and record scope, a bounded duration, a coded basis plus human reason, and the
deployment's notification and retrospective-review obligations. Its decision
and later review are linked owner-local events. Failure to evaluate ordinary
authority does not itself activate break-glass.

This keeps emergency and other exceptional legal bases inspectable instead of
misrepresenting them as patient consent or silently bypassing refusal.

### 5. Sign one privacy-minimized owner-local event for every attempt

openChart records immutable events for allow, refuse, malformed input, expiry,
revocation, failed appraisal, failed key release, abnormal termination, and
break-glass review outcomes. Events use bounded reason and state codes and
locally protected references or commitments; untrusted free text, PHI, and
granular selectors are not copied into public evidence. Event persistence is
part of the protected operation's fail-closed boundary where required to retain
an attributable decision.

Only the owner-local event is the detailed audit source. Public-envelope
construction is governed separately by the exact pinned neutral profile in
Decision 10.

### 6. Make local state atomic and external effects reconcilable

The local decision, immutable owner-local use event, any clinical mutation, and
any required outbox entry commit in one database transaction where the storage
boundary permits. A failed event or mutation write rolls back the local unit and
cannot produce a success response. Reads and other operations without a
clinical mutation still durably record their decision and use event before a
success is reported whenever the operation can remain inside that transaction.

External disclosure, export delivery, key release request, notification, and
anchor submission cannot share the local transaction. They therefore use a
durably recorded idempotency key and outbox entry, retry without duplicating the
effect, and record acknowledgement separately. If an external effect may have
succeeded but its acknowledgement, result event, or corresponding local status
cannot be persisted, openChart records or returns `indeterminate`, blocks a
false success, and requires idempotent reconciliation to a terminal result.

Best-effort audit after performing the effect was rejected because a crash can
create an unaudited mutation or disclosure. Treating a timeout as failure was
also rejected because retrying a completed external effect can duplicate it.

### 7. Separate evidence emission, appraisal, and key release

An allow decision can request confidential processing, but cannot release a
key. The confidential-computing provider emits signed TEE evidence. A governed
verifier and policy service appraise that evidence against versioned policy for
the measured workload, model and prompt package, session public key, allowed
egress, and output class. The KMS does not appraise TEE evidence; it independently
enforces release by requiring the bound openChart decision and current governed
appraisal before releasing or unwrapping key material only for that session key.

Raw attestation self-evaluation inside openChart and application-directed KMS
release were rejected because they collapse independent trust boundaries. A
failed or stale appraisal, mismatched binding, or failed KMS enforcement emits
a refused attempt and releases no usable key material.

### 8. Treat confidential output as a constrained protocol

Each policy-approved output class names a versioned schema and bounds fields,
cardinality, size, rate, destination, and provenance. openChart accepts only a
signed output bound to the decision and session, validates it before release or
persistence, and refuses raw or extra-schema output.

A prompt-only instruction to avoid excessive output was rejected because it is
not an enforceable boundary.

### 9. Keep key-event claims narrowly scoped

A key event identifies the provider, operation, named key or wrapper, session or
grant binding, result, time, and statement signature. User-facing and auditor
representations state only what that provider attested for that object. They do
not claim deletion of source records, outputs, caches, replicas, backups,
snapshots, exported keys, or unknown plaintext copies.

### 10. Anchor through one exact neutral public-envelope profile

New events and their idempotent local outbox entries start in `anchor_pending`.
The implementation selects and pins exactly one provider-neutral public-
envelope profile and version. Every public payload conforms exactly to that
profile: openChart neither defines a local public superset nor appends custom
public fields. Payloads contain only profile-permitted opaque one-use
commitments and non-PHI values and contain no identifier reused across events,
subjects, actors, tenants, purposes, or distinct publications. Retries retain
their idempotency and association only in the owner-local outbox. Detailed
event-to-outbox-to-receipt association stays owner-local.

An asynchronous adapter can later attach a receipt or terminal failure state
without changing the original event or decision. Lost or uncertain
acknowledgement follows Decision 6 and remains indeterminate until idempotent
reconciliation. Anchor delay or outage does not invalidate a completed
authorized operation or block care, while inability to persist the local event
and outbox follows the atomic failure boundary.

Synchronous public anchoring was rejected because it would expose timing
signals and make clinical availability depend on an external network.

### 11. Gate the implementation feature with ratification and constitution

The owner must unconditionally ratify this exact OpenSpec change before any
Speckit feature is created. The durable ratification record identifies the
owner, unconditional decision, change name and revision or digest, and time.
Automated OpenSpec validity or apply readiness does not substitute for that
record.

The repository constitution is adopted through separate project governance,
not authored or amended inside the implementation feature. After ratification,
exactly one Speckit feature may be created for this change. Before its plan
phase advances, the project must have an adopted constitution and the feature
must record a meaningful Constitution Check against its actual security,
privacy, portability, atomicity, testing, and governance constraints. A
boilerplate or unconditional pass is insufficient.

## Risks / Trade-offs

- **[Portable adapters normalize claims differently]** → Publish canonical
  input schemas, conformance fixtures, signature rules, and decision vectors.
- **[Short leases permit access briefly after revocation]** → Bind a declared
  freshness ceiling, prohibit scope widening, and require fresh exercises for
  sensitive operations.
- **[Attempt evidence becomes sensitive behavioral data]** → Keep detailed
  events owner-local, use bounded codes, minimize selectors, and apply local
  retention and access policy.
- **[External timeout is reported incorrectly]** → Use transactional outbox,
  durable idempotency, explicit indeterminate state, and reconciliation before
  any terminal success.
- **[Break-glass is abused]** → Require explicit eligibility, narrow scope,
  notification, expiry, and linked retrospective review.
- **[TEE evidence is mistaken for safe behavior]** → Keep appraisal policy,
  egress controls, output validation, and KMS enforcement separate and state
  the residual side-channel and workload risks.
- **[KMS or verifier outage blocks confidential processing]** → Fail that
  operation closed and preserve ordinary authorized clinical access paths.
- **[Async anchors accumulate or become correlatable]** → Retain association
  locally, reconcile idempotently, use one-use public commitments, and validate
  exact conformance to the pinned neutral profile with no custom public fields.
- **[Existing protected clients are refused after activation]** → Publish the
  versioned contract and migrate clients before enforcing the new requirement.

## Migration Plan

1. Obtain unconditional owner ratification and persist its durable record for
   this exact change revision before creating any implementation feature.
2. Create exactly one linked Speckit feature after ratification; adopt the
   project constitution separately and complete a meaningful Constitution Check
   before the feature plan advances.
3. Define canonical authority, policy, decision, event, lease, exercise,
   break-glass, appraisal, key-event, output, and anchor contracts with
   standalone conformance fixtures, selecting and pinning one exact neutral
   public-envelope profile and version.
4. Add transactional owner-local persistence and migrations for immutable
   decisions, events, mutations, idempotent outbox records, leases, exercises,
   sessions, reviews, indeterminate reconciliation, and asynchronous anchor
   state.
5. Route protected versioned API operations through the gate, then add verifier,
   KMS, output, and anchor adapters behind deny-by-default configuration.
6. Migrate supported clients to the published inputs and activate enforcement
   only after standalone and compatibility suites pass with no Medx app
   installed.

Rollback disables new session initiation and keeps protected operations fail
closed rather than restoring an ungoverned path. Persisted events and clinical
amendments remain auditable; adapter and API activation can be rolled back only
to a security-supported version that preserves their interpretation.

This change is archived only after the single linked feature's implementation
is merged into its intended base and all required validation and acceptance
evidence is durable.

## Open Questions

None block the Speckit handoff. Concrete freshness durations, eligible
break-glass roles, verifier technologies, KMS products, and first output schemas
remain deployment/profile choices constrained by the contracts above.
