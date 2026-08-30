# Confidential Processing and Cryptographic Erasure — Brainstorm

Status: brainstorm
Kind: architecture
Summary: openChart could stream encrypted record scopes into an attested processing session and retain scoped key-lifecycle evidence while avoiding claims that a TEE or destruction receipt proves all plaintext copies disappeared.
Topics: clinical-record-usage-control, confidential-processing, openchart, cryptographic-erasure, remote-attestation
Repository context: openChart protected record delivery, AI processing, output, and key-lifecycle integration
Captured: 2026-08-29

## Possible feats

- **Confidential medication-review session** — stream a purpose-limited FHIR
  scope into an accepted enclave and permit only a signed summary output.
- **Scoped destruction event** — link a provider-signed key or wrapper
  destruction statement to the grant and clinical-use event.

## Focus

This document isolates the proposed protected processing path and its honest
security boundary. The goal is not to prevent copying of ciphertext. It is to
avoid distributing durable decryption material and to minimize where plaintext
can exist.

## Proposed model

```text
encrypted record store
  -> openChart selects authorized FHIR scope
  -> KMS receives grant + session + attestation evidence
  -> KMS releases or unwraps key only for accepted session key
  -> plaintext exists inside measured processing boundary
  -> output filter emits signed, purpose-limited result
  -> session terminates and ephemeral material is destroyed
  -> scoped provider destruction event is recorded
```

Envelope encryption can keep stable record encryption keys while creating
independently revocable wrapping paths per grant or session. Destroying one
wrapper revokes that path only if no equivalent wrapper, exported key, or
plaintext copy remains accessible.

Remote attestation is evidence of an appraised measured configuration. It does
not prove the software is correct, continuously resident, non-exfiltrating, or
free from side channels. The processing design also needs constrained egress,
structured outputs, rate limits, endpoint binding, log redaction, memory and
swap controls, model/prompt review, and side-channel analysis.

A signed destruction receipt proves that the named KMS or HSM made a scoped
statement about a named key or wrapper. It does not prove universal deletion of
plaintext, derived outputs, caches, replicas, backups, snapshots, or unknown key
copies. The term "verifiable deletion" should therefore remain a research goal,
not an unqualified product guarantee.

## Interfaces and boundaries

openChart owns record selection, session authorization, protected streaming,
output acceptance, and clinical-use evidence. A confidential-computing provider
issues attestation evidence; a governed verifier and policy service appraise it;
a KMS/HSM owns key operations and enforces the release decision. openXwallet
owns holder and grant evidence. Medx policy owns permitted purposes and output
classes.

For a human viewer, controls can reduce accidental export, but no design can
prevent an authorized person from photographing, remembering, or retyping
visible information. Human viewing must be treated as controlled disclosure,
not cryptographically confined computation.

## Alternatives and tensions

- TEEs reduce selected host threats but add hardware, firmware, verifier,
  side-channel, portability, and availability risks.
- Per-session wrapping improves revocation precision but increases key-event
  volume and recovery complexity.
- Homomorphic or ciphertext-to-ciphertext processing could reduce plaintext
  exposure for narrow operations, but general clinical AI remains far more
  practical inside a confidential-computing boundary.
- Legal hold and clinical retention may forbid key destruction even after
  patient authorization expires; access revocation and source-record retention
  are separate state machines.

## Open questions

- What exact output schema is safe enough for the medication-review pilot?
- Which cloud and attestation verifier establish the first measured boundary?
- How are model weights, prompts, retrieval tools, and egress endpoints included
  in appraisal policy?
- Which key copies, wrappers, backups, and derived outputs must a destruction
  event inventory?

## Relationships

The application authorization seam is defined in
[Clinical Record-Use Policy Enforcement](clinical-record-usage-control-policy-enforcement.md).
Their combined flow is explored in
[Synthesis: Controlled Clinical Session](clinical-record-usage-control-synthesis-controlled-session.md).
