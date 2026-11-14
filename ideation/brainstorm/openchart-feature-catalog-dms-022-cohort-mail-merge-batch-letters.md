# Cohort Mail-merge Batch Letters — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates individually reviewable letters from a frozen patient cohort and approved template with exclusions, manifests, and delivery-ready outputs.
Topics: openchart-feature-catalog, documents, frappe, mail-merge
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-022 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Returned-mail reconciliation** — Link undeliverable outcomes to the exact batch item and address snapshot for human follow-up.

## Focus

This feature isolates safe high-volume personalization without turning a cohort query into autonomous outreach.

## Behavior

- An Outreach Coordinator selects an approved letter template and a permissioned cohort definition.
- Starting the batch freezes recipient membership, address snapshot, language, merge values, and exclusion reasons.
- Consent, deceased status, communication preference, invalid address, duplicate household, and sensitive-program rules flag or exclude recipients.
- The coordinator previews samples and low-confidence items before approving generation.
- Each letter renders separately with recipient-specific checksum and template-version provenance.
- Failed items can retry without regenerating successful letters or changing the frozen cohort.
- Release to print or external mail service requires explicit approval and produces a batch manifest.

## Frappe realization

- **DocTypes:** `OC Letter Batch` (template_version, cohort_reference, frozen_at, state, counts) with child `OC Letter Batch Recipient` (patient, address_snapshot JSON, exclusions, output_file, checksum).
- **Jobs/files:** RQ renders approved Jinja Print Formats to private Frappe Files in bounded batches; `open_chart.documents.on_file` validates output ownership.
- **Workflow:** Preparing → Review → Approved → Generating → Ready, with Partial Failure, Cancelled, and Released states.
- **Roles/permissions:** Outreach Coordinator prepares; Privacy Reviewer approves sensitive cohorts; Print Operator accesses only released outputs.
- **Surfaces:** Desk batch wizard, exception list, progress dashboard, and batch manifest Print Format.

## Boundaries

Owns: frozen batch membership, merge snapshot, per-recipient output, exceptions, and manifest. Consumes: approved template, cohort, preferences, and addresses. Emits: delivery-ready letters. Does not own: cohort clinical logic, postal delivery, or autonomous outreach approval.

## Open questions

- When may one household letter replace individual letters without obscuring patient-specific content or consent?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Template Letter Library](openchart-feature-catalog-dms-021-template-letter-library.md)
