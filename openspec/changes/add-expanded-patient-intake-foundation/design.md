## Context

openChart is a governance scaffold with no Frappe runtime. Its first capability
must establish an original, standalone clinical application while providing
the expanded patient-reported intake required by the one-patient program. It
must learn from existing EHRs without copying OpenEMR or Marley code.

## Goals / Non-Goals

**Goals:**

- Establish the openChart Frappe app, migrations, permissions, audit and tests.
- Persist one patient and versioned expanded-intake submissions.
- Represent medications, OTC products, supplements and other patient reports
  with original wording and provenance.
- Expose an idempotent API and supported MedxEHR extension seams.
- Remain independently useful without MedxFactory.

**Non-Goals:**

- Full EHR parity, clinician orders, prescribing, complete encounters,
  billing, external-EHR connectors, reconciliation decisions or autonomy.

## Decisions

### 1. Build an original Frappe app with a declared minimum profile

The feature establishes the package, site installation, migrations, test
fixtures and contributor commands needed for the intake profile only. It does
not fork or depend on GPL healthcare applications.

### 2. Store submission versions and typed patient statements

`Intake Submission` is the provenance and lifecycle envelope. Typed child or
linked records represent medication, supplement, condition, allergy,
observation, symptom, goal and document-reference statements. This is
preferred over a single opaque JSON document because permissions,
reconciliation, amendment and queries require stable identities.

### 3. Preserve raw patient wording beside normalized fields

Normalization may enrich terminology asynchronously, but the submitted text,
product detail and provenance are immutable for an accepted version. Unknown
values remain explicit rather than guessed.

### 4. Use idempotent versioned intake commands

Clients submit a verified subject context, schema version and idempotency key.
Draft updates and accepted submissions have explicit state and optimistic
version behavior. Retries do not create a second logical submission.

### 5. Expose supported services and hooks, not table coupling

MedxEHR references patient and statement records through public APIs, DocType
contracts and events. Co-installation on one Frappe site does not permit direct
unversioned writes to internal tables.

## Risks / Trade-offs

- **[First feature becomes a full EHR rewrite]** → Enforce the minimum intake
  profile and defer clinician workflows to later changes.
- **[Typed records slow early delivery]** → Limit statement families while
  keeping raw submission custody and public extension points.
- **[Patient reports appear clinician-verified]** → Carry assertion kind,
  submitter, verification and provenance in every statement.
- **[Hidden Medx coupling]** → Run standalone tests with no MedxFactory or
  MedxEHR installed.

## Migration Plan

1. Pin the accepted intake and identity contracts.
2. Create the Frappe package, site installation path and synthetic fixture.
3. Add Patient, external identifier, submission and statement migrations.
4. Add APIs, permissions, audit, events and contract tests.
5. Publish the passing openChart revision and compatibility range.

Rollback uninstalls the candidate app from disposable sites or migrates back
before real PHI is permitted. Accepted synthetic submissions remain exportable
for test evidence.

## Open Questions

- Which Frappe and Python versions define the first support matrix?
- Which terminology enrichment is synchronous in version one?
- Which statement records are child tables versus independent DocTypes?

