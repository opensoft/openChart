## MODIFIED Requirements

### Requirement: APIs and extension hooks are authorized and versioned
openChart SHALL expose authenticated versioned commands and reads for patient context, draft, submit, amendment and statement retrieval plus supported hooks or events for MedxEHR. Authorization MUST enforce subject, tenant, purpose and role. Protected reads and amendments MUST invoke the clinical record-use gate with current portable authority and policy inputs; routine eligible reads MAY use a bounded lease, while each amendment MUST use a fresh operation-bound exercise. Extensions MUST NOT require or receive a direct unversioned table-write or protected-read path, and standalone conformance MUST NOT require a Medx application.

#### Scenario: HealthLinc submits a conformant intake
- **WHEN** an authorized HealthLinc client sends the pinned contract and verified subject context
- **THEN** openChart validates, persists and returns stable submission and statement references

#### Scenario: MedxEHR uses an unsupported direct write
- **WHEN** an extension attempts to mutate an intake table outside the supported service boundary
- **THEN** permissions or compatibility tests reject the operation

#### Scenario: Authorized statement read uses a routine lease
- **WHEN** an authenticated client reads intake statements within every bound of a current eligible lease
- **THEN** openChart authorizes the read through the clinical record-use gate and links its owner-local use event to that lease

#### Scenario: Amendment lacks a fresh exercise
- **WHEN** a client requests an intake amendment with only a routine lease or a consumed, expired, stale, revoked, or mismatched exercise
- **THEN** openChart refuses the amendment without changing the accepted submission history

#### Scenario: Amendment audit cannot commit
- **WHEN** an allowed intake amendment cannot atomically persist its decision, owner-local use event, amended submission version, and required outbox entry
- **THEN** openChart rolls back the local unit, preserves the prior accepted history, and reports no success

#### Scenario: Standalone extension uses portable inputs
- **WHEN** a non-Medx extension supplies conformant authority and policy inputs through the versioned API
- **THEN** openChart evaluates the protected operation without any Medx application installed
