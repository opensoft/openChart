## ADDED Requirements

### Requirement: Protected clinical operations use one local enforcement gate
openChart SHALL authorize every protected `read`, `amend`, `export`, `disclose`, `reconcile`, and `confidential-process` operation at its existing versioned API before selecting, mutating, exporting, disclosing, reconciling, or streaming clinical records. The decision MUST bind the authenticated actor or workload, subject, tenant, purpose, role, operation, record-set selector, authority and policy versions, and requested output class. Required inputs that are missing, stale, invalid, or unavailable MUST fail closed, and no extension or internal data path MAY bypass the gate.

#### Scenario: Protected operation is allowed
- **WHEN** a protected request presents current authority and policy inputs whose bound subject, tenant, purpose, role, operation, selector, and output class permit the request
- **THEN** openChart records an allow decision before performing only the bound clinical operation

#### Scenario: Required authority cannot be evaluated
- **WHEN** a required authority or policy input is missing, stale, invalid, or unavailable
- **THEN** openChart refuses the operation without selecting, mutating, exporting, disclosing, reconciling, or streaming the protected records

#### Scenario: Extension attempts to bypass the gate
- **WHEN** an extension invokes a protected clinical data path without a use-gate decision
- **THEN** openChart rejects the operation and records the refused attempt

### Requirement: Authority and policy inputs are portable
openChart SHALL consume versioned, provider-neutral authority, consent, status, proof-of-possession, and policy inputs through configured trust adapters. Each accepted input MUST identify its issuer, contract version, scope, validity or freshness bounds, and verifiable provenance. The capability MUST operate with conformant local or external providers and MUST NOT require MedxFactory, MedxEHR, a Medx-specific role model, or a public-chain lookup.

#### Scenario: Standalone provider authorizes use
- **WHEN** a standalone openChart deployment supplies conformant authority and policy inputs from configured non-Medx providers
- **THEN** the gate evaluates the request without any Medx application installed

#### Scenario: Medx profile is supplied portably
- **WHEN** a Medx deployment maps its authority and policy profile to the published provider-neutral contracts
- **THEN** openChart evaluates the normalized inputs without importing or directly calling Medx runtime objects

### Requirement: Routine leases and sensitive exercises are distinct
openChart MAY issue a short-lived lease only after a full evaluation for routine eligible reads, and the lease MUST remain bounded to its actor, subject, tenant, purpose, role, selector, policy versions, expiry, and revocation-freshness ceiling. Bulk reads and every `amend`, `export`, `disclose`, `reconcile`, and `confidential-process` operation MUST require a fresh single-operation exercise that cannot be replayed. A lease or exercise MUST NOT widen its original scope and MUST be refused when expired, revoked, stale, consumed, or mismatched.

#### Scenario: Routine read reuses a valid lease
- **WHEN** a routine read remains within every bound of a current eligible lease
- **THEN** openChart may authorize that read under the lease and links the use event to it

#### Scenario: Sensitive operation presents only a lease
- **WHEN** an actor presents a routine lease for an amendment, export, disclosure, reconciliation, confidential process, or bulk read
- **THEN** openChart refuses the request until a fresh operation-bound exercise is presented

#### Scenario: Exercise is replayed
- **WHEN** a consumed exercise is presented for another attempt
- **THEN** openChart refuses the attempt and records the replay reason

### Requirement: Break-glass is explicit and reviewable
openChart SHALL treat break-glass as a distinct configured authority path, not as an implicit fallback or a representation of patient consent. A break-glass request MUST bind an authenticated eligible actor, allowed operation, record scope, coded basis, human reason, start and expiry, notification obligations, and retrospective-review obligation. openChart MUST record the exercise, resulting decision, notifications, and review outcome as linked owner-local events.

#### Scenario: Ordinary policy evaluation fails
- **WHEN** ordinary authority cannot be evaluated and no valid break-glass authority is explicitly exercised
- **THEN** openChart refuses the protected operation without activating break-glass

#### Scenario: Eligible actor exercises break-glass
- **WHEN** an authenticated eligible actor explicitly supplies all configured break-glass fields for an allowed bounded operation
- **THEN** openChart evaluates that exceptional authority, marks any allow as break-glass, and schedules the required notification and retrospective review

#### Scenario: Break-glass review is completed
- **WHEN** an authorized reviewer records the retrospective outcome
- **THEN** openChart preserves it as a linked event without rewriting the original decision

### Requirement: Every protected attempt produces owner-local evidence
openChart SHALL create an immutable, owner-local, signed clinical-use event for every protected attempt, including allowed, refused, malformed, expired, revoked, replayed, failed-appraisal, failed-key-release, and abnormally terminated attempts. The event MUST bind a stable attempt identifier, operation, decision or failure state, bounded reason code, actor or attributable ingress context, subject and tenant references, purpose, policy and authority versions when available, lease or exercise reference when available, time, and privacy-minimized commitment to the requested scope. Untrusted free text MUST NOT be copied into public evidence.

#### Scenario: Malformed request is refused before record access
- **WHEN** a protected request is attributable at ingress but malformed before authority evaluation completes
- **THEN** openChart records a privacy-minimized refused-attempt event and does not access protected records

#### Scenario: Authorized operation completes
- **WHEN** an allowed protected operation completes
- **THEN** its use event links the decision, exact operation result state, authority or exercise, and local audit relationship

#### Scenario: Allowed operation terminates abnormally
- **WHEN** an allowed protected operation fails or terminates after its decision
- **THEN** openChart records the abnormal result as linked evidence without changing the original allow decision

### Requirement: Local state is atomic and external effects are reconcilable
openChart SHALL commit the local decision, owner-local use event, local clinical mutation, and required outbox entry in one transaction wherever they share a transactional storage boundary. Failure to persist any required member MUST roll back that local unit and MUST NOT return success. Every external effect MUST be initiated through a durably persisted idempotent outbox operation. If an external effect may have succeeded but its acknowledgement, result event, or corresponding local status cannot be persisted, openChart MUST expose an explicit `indeterminate` state, MUST NOT report success, and SHALL reconcile idempotently to a durable terminal result.

#### Scenario: Amendment and event commit atomically
- **WHEN** an authorized amendment, its decision, use event, and required outbox entry can share one local transaction
- **THEN** openChart commits all required records together before reporting success

#### Scenario: Local event persistence fails
- **WHEN** a protected local mutation succeeds in memory but its required decision, use event, mutation, or outbox write cannot commit
- **THEN** openChart rolls back the local unit and does not report the operation as successful

#### Scenario: External acknowledgement is lost
- **WHEN** an idempotently dispatched external effect may have succeeded but openChart cannot durably record its acknowledgement
- **THEN** openChart records or returns `indeterminate`, reports no false success, and reconciles with the same idempotency key

#### Scenario: Reconciliation confirms the effect
- **WHEN** reconciliation obtains authoritative evidence for an indeterminate external effect
- **THEN** openChart records one durable terminal result without duplicating the effect or rewriting the original decision

### Requirement: Confidential processing separates decision, appraisal, and release
openChart SHALL authorize a `confidential-process` operation before any protected record is streamed, but its allow decision MUST NOT itself release decryption material. The confidential-computing provider SHALL emit signed TEE evidence. A governed verifier and policy service SHALL appraise that evidence against versioned policy and bind the appraisal to the measured workload, session public key, allowed egress, requested record scope, purpose, and output class. The KMS/HSM MUST NOT appraise TEE evidence and SHALL independently enforce key release or unwrap only when the current openChart decision and governed verifier appraisal match the same authorized session.

#### Scenario: Appraised session receives scoped release
- **WHEN** an allowed confidential-process decision and a current successful verifier appraisal match the same session and release policy
- **THEN** the KMS/HSM may release or unwrap only the scoped material bound to that session public key

#### Scenario: TEE evidence fails appraisal
- **WHEN** the governed verifier refuses or cannot validate the TEE evidence
- **THEN** the KMS/HSM releases no usable key material and openChart records the failed attempt

#### Scenario: Provider emits TEE evidence
- **WHEN** a confidential-computing provider presents signed evidence for a candidate session
- **THEN** the governed verifier and policy service, not the KMS/HSM, appraise that evidence before any release decision is enforced

#### Scenario: Decision and appraisal bindings differ
- **WHEN** the decision, attestation appraisal, session key, purpose, scope, egress, or output-class bindings do not match
- **THEN** key release and confidential processing are refused

### Requirement: Confidential outputs are structured and bounded
Each confidential-processing policy SHALL identify an allowed versioned output schema and explicit field, cardinality, size, rate, destination, and provenance bounds. openChart MUST accept or release only output signed by the authorized session, bound to its decision and exercise, and valid against every configured bound. Raw, extra-schema, oversized, excessive-rate, unsigned, or misdirected output MUST be refused and evidenced.

#### Scenario: Bounded signed output is returned
- **WHEN** an authorized session returns output that matches its schema and every bound
- **THEN** openChart validates the signature and bindings and returns or persists only the approved structured fields with provenance

#### Scenario: Session emits extra content
- **WHEN** a session returns raw records, undeclared fields, excessive cardinality or size, or an unapproved destination
- **THEN** openChart refuses the output and records the bounded failure reason

### Requirement: Key-event statements make only scoped claims
openChart SHALL represent a provider key event as a signed statement about a named provider, key or wrapper, operation, session or grant binding, result, and time. APIs, user interfaces, exports, and audit views MUST NOT interpret one key event as proof that source records, plaintext, derived outputs, caches, replicas, backups, snapshots, exported keys, equivalent wrappers, or unknown copies were universally deleted.

#### Scenario: Provider reports wrapper destruction
- **WHEN** a configured provider signs a successful destruction statement for one named wrapper
- **THEN** openChart reports that scoped provider statement and its binding without claiming universal deletion

#### Scenario: Equivalent access path is not covered
- **WHEN** a key event does not name another wrapper, replica, output, or plaintext copy
- **THEN** openChart leaves the unmentioned object's deletion state unknown

### Requirement: Evidence anchoring uses one exact neutral public envelope
Every anchor-eligible owner-local event SHALL create a local idempotent outbox record in `anchor_pending`. openChart SHALL select and pin exactly one provider-neutral public-envelope profile and version, and every public anchor payload MUST conform exactly to that profile. openChart MUST NOT define a local public superset or append custom public fields. A public payload MAY contain only profile-permitted opaque one-use commitments and non-PHI values and MUST NOT contain PHI, patient identifiers, record selectors, purposes, human reasons, output content, granular access metadata, or identifiers reused across events, subjects, actors, tenants, purposes, or distinct publications. Event, outbox, retry, dispatch, and receipt associations SHALL remain owner-local. Anchor delay or outage MUST NOT reverse a completed authorized operation or make public-chain availability a prerequisite for urgent care or record reconstruction.

#### Scenario: Anchor service is unavailable
- **WHEN** a locally recorded event cannot be submitted to the configured anchor service
- **THEN** its local outbox association remains immutable and `anchor_pending` for idempotent retry while authorized local clinical behavior does not depend on publication

#### Scenario: Event is anchored
- **WHEN** an asynchronous adapter obtains a valid receipt for an event commitment
- **THEN** openChart links the receipt owner-locally without publishing the event association, PHI, granular metadata, or a stable correlatable identifier

#### Scenario: Candidate payload extends the neutral profile
- **WHEN** a candidate public payload adds an openChart field or otherwise exceeds the selected pinned neutral profile
- **THEN** openChart refuses publication instead of defining a local public-envelope superset

#### Scenario: Candidate payload contains a stable correlation identifier
- **WHEN** a candidate public payload contains an identifier reused across events, subjects, actors, tenants, purposes, or distinct publications
- **THEN** openChart refuses that payload and keeps retry, dispatch, and receipt association owner-local

#### Scenario: Public payload contains sensitive data
- **WHEN** a candidate anchor payload contains PHI, a patient identifier, record selector, purpose, human reason, output content, or granular access metadata
- **THEN** openChart refuses publication and records the local anchoring failure
