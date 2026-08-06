## ADDED Requirements

### Requirement: openChart provides an original standalone Frappe application
openChart SHALL provide an installable original Frappe application with declared framework and Python compatibility, repeatable migrations, synthetic fixtures, permissions, audit behavior, backup guidance, tests and contributor commands. The application MUST operate without MedxFactory, MedxEHR or openPractice and MUST NOT copy or fork OpenEMR or Marley implementation code.

#### Scenario: Standalone site installs
- **WHEN** the app is installed on a clean supported Frappe site
- **THEN** migrations complete and the golden-patient intake tests run without any Medx application installed

### Requirement: Patient identity records retain external namespaces
openChart SHALL define a Patient and versioned Patient External Identifier records carrying issuer or source endpoint, namespace, value, status, effective interval and provenance. An external identifier MUST NOT replace the openChart patient identifier or silently merge patients.

#### Scenario: Golden patient is created
- **WHEN** the fixture creates its openChart patient
- **THEN** the patient receives a local identifier and the declared Medx and HealthLinc references remain namespaced external identifiers

#### Scenario: External identifier conflicts
- **WHEN** an active issuer and value already belong to another patient
- **THEN** creation fails or enters an explicit identity-review state without merging records

### Requirement: Intake submissions are versioned, auditable and idempotent
An Intake Submission SHALL carry patient, contract version, submission version, lifecycle state, submitter context, purpose or consent reference, created and submitted times, provenance, client idempotency key and predecessor when amended. Replaying the same accepted command and key MUST return the existing logical submission rather than create another.

#### Scenario: Draft is resumed and submitted
- **WHEN** an authorized patient saves, resumes, reviews and submits a valid draft
- **THEN** one accepted submission version retains its draft history, submitter and provenance

#### Scenario: Submit is retried
- **WHEN** a client retries the same submit command with its idempotency key
- **THEN** openChart returns the existing accepted version and creates no duplicate statements

### Requirement: Medication and supplement statements preserve reported detail
openChart SHALL store patient-reported Rx, OTC and supplement statements with assertion kind, original wording, product or ingredients when known, formulation, dose and units, route, frequency, start and end dates when known, indication, adherence, source, confidence, verification state and submission provenance. Unknown optional values MUST remain unknown rather than being inferred.

#### Scenario: Detailed supplement is submitted
- **WHEN** the golden patient reports a supplement with product wording, formulation, dose, frequency, indication and adherence
- **THEN** every supplied value and its original wording remain available on the accepted statement

#### Scenario: Patient does not know a dose
- **WHEN** a patient explicitly marks the dose unknown
- **THEN** validation accepts the statement under the contract and does not invent a dose

### Requirement: Expanded intake supports other required patient statements
The accepted profile SHALL support patient-reported conditions, allergies or intolerances, selected observations, symptoms, goals and clinical document references with statement identity, original wording, applicable structured values and timing, source, verification and submission provenance.

#### Scenario: Mixed intake is accepted
- **WHEN** the golden submission includes every required statement family
- **THEN** each statement is addressable and linked to the same accepted submission version

### Requirement: Amendments preserve accepted history
An accepted submission or statement MUST NOT be silently overwritten. A patient correction SHALL create a new version or amendment with predecessor, actor, reason and time while prior accepted content remains auditable.

#### Scenario: Patient corrects supplement frequency
- **WHEN** the patient amends an accepted supplement statement
- **THEN** the new version references the prior version and both remain available to authorized audit

### Requirement: APIs and extension hooks are authorized and versioned
openChart SHALL expose authenticated versioned commands and reads for patient context, draft, submit, amendment and statement retrieval plus supported hooks or events for MedxEHR. Authorization MUST enforce subject, tenant, purpose and role, and extensions MUST NOT require direct unversioned table writes.

#### Scenario: HealthLinc submits a conformant intake
- **WHEN** an authorized HealthLinc client sends the pinned contract and verified subject context
- **THEN** openChart validates, persists and returns stable submission and statement references

#### Scenario: MedxEHR uses an unsupported direct write
- **WHEN** an extension attempts to mutate an intake table outside the supported service boundary
- **THEN** permissions or compatibility tests reject the operation

### Requirement: Intake does not confer clinician or autonomous authority
Patient statements SHALL remain visibly patient-reported until an authorized clinical workflow records another assertion. No intake, supplement statement, API response or extension event SHALL create a prescription, diagnosis, order, administration, treatment recommendation or autonomous action.

#### Scenario: Submitted medication is treated as prescription
- **WHEN** a consumer attempts to interpret a patient medication statement as a signed prescription
- **THEN** the assertion kind and authorization boundary prevent that interpretation

