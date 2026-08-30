# Clinical Record-Use Policy Enforcement — Brainstorm

Status: brainstorm
Kind: architecture
Summary: openChart could make every sensitive read, amendment, export, disclosure, and AI-processing session pass through its existing subject/tenant/purpose/role boundary with wallet and external contract-state evidence.
Topics: clinical-record-usage-control, policy-enforcement, openchart, medical-records, consent, audit
Repository context: openChart portable EMR authorization and clinical-use event ownership
Captured: 2026-08-29

## Possible feats

- **Clinical record-use gate** — extend the versioned API so protected
  operations require a current authority presentation and produce one signed
  use event.
- **Attempt audit** — record refused, expired, revoked, and malformed attempts
  as well as successful access without publishing granular PHI metadata.

## Focus

This document isolates openChart's role as the enforcement point for clinical
records. A blockchain cannot prevent access to bytes held by an EMR. openChart
must evaluate authority before it reads, writes, exports, discloses, or streams
those bytes.

The existing promoted intake contract already requires authorization by
subject, tenant, purpose, and role and rejects unsupported direct writes. Usage
control should extend that seam rather than create a second data path.

## Proposed model

```text
record-use request
  -> authenticated actor or workload
  -> wallet grant and proof-of-possession
  -> consent and role resolution
  -> fresh external contract/checkpoint state
  -> local openChart policy decision
  -> allow or refuse
  -> signed clinical-use event
  -> asynchronous evidence anchoring
```

The request could distinguish read, amend, export, disclose, reconcile, and
confidential-process operations. The decision binds the exact record-set
selector, purpose, actor, organization, policy versions, grant exercise,
consent basis, emergency state, and result. Public anchoring receives only an
opaque commitment to the signed event.

For frequent interactive reads, policy may issue a short session lease after a
fresh full evaluation. High-impact operations such as export, disclosure,
amendment, bulk query, and model processing should require a new exercise or a
stricter freshness rule.

## Interfaces and boundaries

openChart owns the clinical operation, local permission check, record selector,
allow/refuse decision, use event, and immutable audit relationship. It consumes
wallet authority and Medx or deployment policy through versioned interfaces.
It does not own neutral wallet schemas, public anchor adapters, payer retention
rules, or Medx-specific role definitions.

The external chain state is evidence and policy input. The local gate remains
authoritative for access to openChart's bytes. A network publication outage can
leave an already authorized event `anchor_pending`; inability to evaluate
required authority should fail closed except through an explicitly authorized
break-glass path.

## Alternatives and tensions

- Per-read chain lookups maximize freshness but add latency, availability, and
  metadata exposure. Signed status snapshots or bounded leases reduce that
  dependency.
- Refused-attempt auditing improves accountability but can itself create
  sensitive behavioral data requiring strict off-chain retention.
- Patient revocation governs future discretionary access; treatment,
  regulatory, legal-hold, and emergency bases may require distinct authority
  rather than a silent override.

## Open questions

- Which operations require a new grant exercise versus a session lease?
- What freshness ceiling applies to revocation and contract-state checks?
- Which break-glass roles, reasons, notifications, and retrospective reviews
  are mandatory?
- Can routine care continue while external anchoring is delayed?

## Relationships

Confidential AI and key-release constraints are explored in
[Confidential Processing and Cryptographic Erasure](clinical-record-usage-control-confidential-processing.md).
The end-to-end session is related in
[Synthesis: Controlled Clinical Session](clinical-record-usage-control-synthesis-controlled-session.md).
