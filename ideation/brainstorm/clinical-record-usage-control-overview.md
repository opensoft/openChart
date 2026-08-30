# Clinical Record Usage Control Overview — Brainstorm

Status: brainstorm
Kind: reference
Summary: openChart can enforce wallet- and policy-backed medical-record use at its existing versioned API while confidential processing narrows plaintext exposure and external witnesses preserve tamper-evident evidence.
Topics: clinical-record-usage-control, openchart, medical-records, consent, confidential-processing, audit
Repository context: openChart portable medical EMR behavior and Medx composition seam
Captured: 2026-08-29

## Possible feats

- **Purpose-bound clinical record use** — make every protected operation pass
  through one attributable, auditable authority decision.
- **Confidential AI medication review** — process a limited FHIR scope in an
  attested environment and return only a signed summary.

## Motivation

Traditional DRM fails once plaintext reaches an uncontrolled endpoint. A
medical EMR can improve the model by keeping durable keys out of recipients,
evaluating authority at use time, limiting plaintext to a controlled boundary,
and producing evidence for every sensitive attempt. It still must describe the
remaining human, output, side-channel, backup, and legal risks honestly.

## Goals

- Enforce subject, tenant, purpose, role, consent, and grant constraints at the
  openChart service boundary.
- Preserve immutable clinical amendments and attributable use events.
- Minimize plaintext delivery to AI workloads through attested key release.
- Record refused and failed attempts as well as successful use.
- Keep PHI and granular access metadata off public chains.
- Allow openChart to remain independently usable without MedxFactory.

## Non-goals

- Guaranteeing that no authorized human can copy visible information.
- Claiming remote attestation proves safe AI behavior.
- Claiming one key-destruction receipt proves universal data deletion.
- Making blockchain availability a prerequisite for reconstruction or urgent
  patient care.
- Owning billing, claims, reimbursement, or practice retention policy.

## What the system delivers

openChart becomes the authoritative point where a record-use request is
allowed or refused. It can bind wallet authority, consent, role, purpose,
resource scope, session evidence, output, and audit into one clinical-use event
whose opaque commitment is witnessed through the shared evidence chain.

## System model

```text
WALLET + CONSENT + MEDICAL POLICY
                |
                v
        OPENCHART USE GATE
          allow / refuse
                |
        +-------+--------+
        |                |
 human controlled   attested AI session
 disclosure         + KMS key release
        |                |
        +------ use event+
                |
          KASPA WITNESS
                |
     DAILY BITCOIN DURABILITY
```

## Cluster map

- [Synthesis: Controlled Clinical Session](clinical-record-usage-control-synthesis-controlled-session.md)
  — relates authorization, attestation, key release, output restriction,
  revocation, and evidence.

## How it fits

This packet extends openChart's existing authorized and versioned API. It uses
openXwallet-compatible authority without owning wallet contracts, consumes
medical policy through a portable interface, and emits owner-local events for
openxFactory-compatible anchoring. MedxChart can bind exact MedxFactory and
MedxWallet profiles without making the public openChart product depend on them.

## Key decisions and open questions

The first proposed use case is medication review. The app still needs decisions
on session leases, break-glass, attestation technology, model and egress
appraisal, FHIR scope, output schema, revocation latency, and the evidence
required before a key-lifecycle claim is shown to a patient or auditor.

## Document map

### Synthesis documents

- [Controlled Clinical Session](clinical-record-usage-control-synthesis-controlled-session.md)

### Atomic documents

- [Clinical Record-Use Policy Enforcement](clinical-record-usage-control-policy-enforcement.md)
- [Confidential Processing and Cryptographic Erasure](clinical-record-usage-control-confidential-processing.md)
