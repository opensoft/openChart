# QRDA I Submission Generation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates validated patient-level QRDA Category I submission documents from locked measure results and authorized clinical evidence.
Topics: openchart-feature-catalog, quality-reporting, frappe, qrda-i
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-010 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Submission sample viewer** — Render selected XML facts into a reviewer-friendly patient evidence summary.

## Focus

Standards-conformant, privacy-governed generation of patient-level quality-reporting artifacts with reproducible source mappings.

## Behavior

- An authorized submitter selects a locked period, destination profile, measures, and patient scope.
- Generation uses only accepted, permissioned records and the exact result and mapping releases referenced by the period.
- Each document receives identifiers, author and custodian metadata, measure references, and required clinical statements.
- Schema, schematron, vocabulary, cardinality, and destination-profile checks run before packaging.
- Validation errors block release and link to source mappings or records without modifying them.
- Patient identity conflicts, missing required identifiers, and consent restrictions route records to exceptions.
- Released artifacts are immutable, encrypted at rest, access-audited, and retained with their manifest hash.

## Frappe realization

- **DocTypes:** Add `OC QRDA I Package`, `OC QRDA Document`, and child manifest/error rows with Attach, patient Link, measure release, profile, checksum, and status.
- **Workflow:** Use draft, generating, validation-failed, review, approved, released, and superseded states with submitter/approver separation.
- **Jobs and API:** Generate and validate in rq; expose guarded package creation, validation, approval, and download methods, not writable auto-REST.
- **Surfaces:** Provide an exception Script Report, package dashboard, XML sample viewer, and permissioned download action.

## Boundaries

Owns: QRDA I document generation, validation, and packaging. Consumes: locked results, clinical evidence, identities, mappings, consent, and destination profiles. Emits: validated patient-level artifacts and errors. Does not own: transport, destination acceptance, or clinical-record correction.

## Open questions

- Which destination-specific QRDA profiles should be maintained as first-party fixtures?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
