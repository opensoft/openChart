# Clinician Quick-attach From Encounter — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians capture or upload a small document directly within an encounter while enforcing classification, provenance, and deferred review rules.
Topics: openchart-feature-catalog, documents, frappe, encounter-quick-attach
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-032 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Mobile camera capture guidance** — Detect glare, blur, framing, and page edges before a clinician submits an encounter photo or scan.

## Focus

This feature isolates low-friction encounter-context attachment without weakening the typed document and review model.

## Behavior

- A Clinician selects Quick Attach from an open encounter and chooses an allowed class and source.
- Patient, encounter, author, facility, and capture time prefill from context and remain visible before submission.
- The user uploads a file or camera image, previews it, and adds service date and concise description.
- Malware, media, size, class, duplicate, and required-consent checks run before the file leaves quarantine.
- Low-risk classes may become accepted immediately under policy; others enter Document Review Required.
- Cancelling or losing connection leaves no chart-visible partial attachment and offers bounded session recovery.
- Correction after acceptance uses a successor version and never replaces the original File in place.

## Frappe realization

- **DocTypes:** Reuse `OC Patient Document` and `OC Document File Version`; `OC Quick Attach Session` tracks temporary File, encounter, expiry, and completion state.
- **Files/hooks:** Frappe file manager uploads privately; `open_chart.documents.on_file` validates session token, attachment target, checksum, and quarantine state.
- **Roles/permissions:** Clinician attaches allowed classes; Document Reviewer accepts restricted classes; encounter and patient user permissions both apply.
- **API/surfaces:** Encounter client script opens a compact dialog; guarded `open_chart.api.v1.documents.complete_quick_attach` commits atomically.
- **Automation:** Expired-session scheduler purges uncommitted temporary Files only after verifying no legal hold or accepted link exists.

## Boundaries

Owns: encounter-context capture session and handoff to typed attachment. Consumes: encounter, patient, File, class, and consent state. Emits: accepted document or review task. Does not own: encounter note content, scanner integration, or bulk import.

## Open questions

- Which classes are safe for clinician self-acceptance versus mandatory records review?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Typed Patient Document Attachment](openchart-feature-catalog-dms-001-typed-patient-document-attachment.md)
