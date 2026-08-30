# Synthesis: Controlled Clinical Session — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Combining openChart's policy gate with attested key release creates a bounded clinical session whose authority, processing, output, and evidence remain separately inspectable.
Topics: clinical-record-usage-control, controlled-clinical-session, policy-enforcement, confidential-processing, synthesis
Repository context: openChart end-to-end clinical record-use enforcement and evidence flow
Captured: 2026-08-29

## Possible feats

- **Medication-review controlled session** — authorize one AI workload for one
  record scope, purpose, time window, and signed-summary output.

## Members and their joints

Atomic members:
[Clinical Record-Use Policy Enforcement](clinical-record-usage-control-policy-enforcement.md),
[Confidential Processing and Cryptographic Erasure](clinical-record-usage-control-confidential-processing.md).

```text
grant + consent + role + contract state
                 |
          openChart decision
                 |
       attested KMS key release
                 |
       bounded processing session
                 |
       filtered signed output
                 |
 use event + key event + anchor receipt
```

### Authority and release

openChart first decides whether the requested clinical operation is authorized.
Only an allow decision can enter the release flow. A governed verifier and
policy service separately appraise the recipient session, and the KMS releases
key material only when that result authorizes the bound session key. None of
these components silently substitutes for another.

### Output and audit

The approved output class is part of the grant and decision. The session emits
a signed summary plus provenance, not raw PHI by default. Successful access,
refusal, expiry, revocation, abnormal termination, and failed attestation all
produce owner-local evidence with privacy-appropriate retention.

### Revocation and destruction

Revocation stops future exercises and should terminate or expire active
sessions according to a declared latency. A key event records what wrapper or
ephemeral material the provider says it destroyed. It cannot retract an output
or prove all copies vanished.

## Emergent behavior

The combined system minimizes plaintext distribution, makes the enforcement
decision attributable, binds processing to an appraised session, constrains
outputs, and gives later auditors a linked authority-to-use-to-evidence chain.

## Tensions to hold

- Patient agency and revocation must coexist with treatment duties, retention,
  emergency access, legal holds, and already completed disclosures.
- Public anchoring should strengthen evidence without becoming a care-
  availability dependency.
- A measured AI workload can still produce unsafe or excessive output.

## Recombination opportunities

The same controlled-session pattern may support document abstraction,
medication reconciliation, prior-authorization assistance, coding review, and
research extraction under different domain policies and outputs.

## Open questions

- Which first operation is narrow enough to validate the full chain without
  overclaiming TEE or deletion guarantees?
- What incident state is emitted when processing succeeds but external
  anchoring remains delayed?
