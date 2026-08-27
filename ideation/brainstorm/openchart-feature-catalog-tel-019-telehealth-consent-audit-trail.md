# Telehealth Consent Audit Trail — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides a tamper-evident chronology of telehealth disclosure, agreement, decline, withdrawal, and override events.
Topics: openchart-feature-catalog, telehealth, frappe, consent-audit
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-019 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Consent evidence export** — Produce a minimum-necessary signed chronology for authorized legal or compliance review.

## Focus

This feature isolates durable evidence about telehealth consent lifecycle events across encounters without replacing each consent artifact.

## Behavior

- Every disclosure presentation, signature, decline, withdrawal, staff explanation, and policy invalidation appends an event.
- Events include actor, represented patient, authority basis, encounter, policy version, channel, timestamp, and correlation identifier.
- Accepted events cannot be edited; corrections append a superseding event with reason and predecessor.
- Reviewers can reconstruct what was shown, who acted, and which gate decision applied at admission time.
- Patient access presents understandable consent history while hiding internal security and reviewer notes.
- Export is permissioned, watermarked, and logged with purpose and recipient.

## Frappe realization

- **DocTypes:** immutable `OC Consent Audit Event` links `OC Telehealth Consent`, disclosure, encounter, actor, authority, predecessor, outcome, and payload checksum.
- **Hooks:** consent `after_insert`, submission, withdrawal, and succession events append through one internal service; guarded controllers reject direct mutation.
- **Reports/permissions:** a Script Report and Jinja export serve Consent Auditor; Patient receives a filtered portal projection; export actions create audit events.

## Boundaries

Owns: consent-event chronology and evidence export. Consumes: consent artifacts and gate decisions. Emits: reconstructable audit evidence. Does not own: consent policy content or legal conclusions.

## Open questions

- What cryptographic anchoring, if any, is proportionate beyond Frappe versioning and append-only controls?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
