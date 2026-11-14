# Advance Beneficiary Notice Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures an advance beneficiary notice presentation and patient option selection with version, estimate inputs, signature, and delivery evidence.
Topics: openchart-feature-catalog, registration, frappe, beneficiary-notice
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-051 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **External estimate handoff** — Accept a signed, purpose-limited estimate snapshot from an authorized revenue-cycle system.

## Focus

Record the notice artifact during registration while keeping coverage prediction and billing logic outside openChart.

## Behavior

- Staff start from a reviewed notice template and an externally supplied service-and-estimate snapshot.
- The patient sees reason, estimated amount, available options, and assistance in an accessible format.
- The selected option, signer, authority, date, signature, witness, and copy-delivery method are captured.
- Missing estimate provenance or required fields blocks finalization and routes back to the originating system or supervisor.
- Refusal or inability to sign is documented as an outcome rather than converted to acceptance.
- Amendments create a successor notice and preserve the exact prior version and estimate relied upon.

## Frappe realization

- **DocTypes:** submittable `OC Advance Beneficiary Notice` with template_version, external_estimate_ref, snapshot_json, option, signer, authority, and evidence.
- **Workflow:** Prepared → Presented → Option Selected, Refused, or Unable → Submitted or Superseded.
- **Roles/permissions:** `OC Registration Clerk` presents; `OC Registration Supervisor` resolves defects; financial snapshot at permlevel 1.
- **API/surfaces:** `open_chart.api.v1.registration.record_beneficiary_notice`; guided form, Jinja print format, patient receipt, and exception report.

## Boundaries

Owns: notice presentation and selection evidence. Consumes: approved template and external estimate snapshot. Emits: signed notice artifact. Does not own: medical-necessity prediction, payer rules, claims, or balances.

## Open questions

- Which external system is authoritative for estimate content and correction?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
