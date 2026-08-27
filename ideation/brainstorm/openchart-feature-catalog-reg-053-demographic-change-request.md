# Demographic Change Request — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets patients, representatives, integrations, or staff propose demographic corrections with evidence and provenance without direct accepted-record mutation.
Topics: openchart-feature-catalog, registration, frappe, demographic-change
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-053 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Field-sensitive evidence guidance** — Explain required support based on the fact being changed and requester authority.

## Focus

Create a standard proposal envelope for demographic changes before policy-specific approval.

## Behavior

- A requester selects one or more demographic facts and supplies proposed values, reason, source, and evidence.
- The form displays current values only when the requester is authorized to see them.
- Requests from representatives include relationship and authority references valid for the affected fact.
- Exact duplicate requests return the existing request rather than creating parallel review work.
- The submission validates syntax but does not apply accepted patient changes.
- Withdrawal, cancellation, and additional-information responses preserve the original proposal and activity history.

## Frappe realization

- **DocTypes:** `OC Demographic Change Request` and child `OC Proposed Demographic Change` with field_path, old hash, proposed value, reason, evidence, and requester.
- **Workflow:** Draft → Submitted → More Information Needed, Withdrawn, Canceled, or Pending Approval.
- **Roles/permissions:** `OC Patient Portal User` proposes own changes; `OC Registration Clerk` assists; evidence and protected old values use permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.submit_demographic_change`; portal form, patient activity timeline, and request-status page.

## Boundaries

Owns: demographic change proposal and requester interaction. Consumes: current fact hashes and requester authority. Emits: approval-ready request. Does not own: approval decision or accepted-value mutation.

## Open questions

- Which low-risk changes may use expedited review while still preserving succession history?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
