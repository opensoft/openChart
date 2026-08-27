# Teleradiology Package Exchange — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Sends and receives traceable teleradiology work packages containing minimum-necessary study references, context, assignments, status, and report artifacts.
Topics: openchart-feature-catalog, imaging, frappe, teleradiology
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-035 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Coverage routing console** — Match reviewed cases to contracted reader services by subspecialty and service window.

## Focus

This feature isolates accountable cross-organization interpretation exchange while images remain in standards-based archives.

## Behavior

- Staff select an eligible performed study and approved receiving organization or reading service.
- The package contains order question, protocol, performance metadata, prior references, urgency, contact route, and least necessary patient identifiers.
- Transfer state distinguishes queued, sent, received, accepted, declined, assigned, reported, and reconciled.
- Duplicate submissions use an immutable package identifier and do not create duplicate reading episodes.
- Returned preliminary and final reports retain external author, organization, signature evidence, timestamps, and source artifacts.
- Timeouts, declines, patient mismatch, and report conflicts enter human reconciliation and escalation.

## Frappe realization

- **DocTypes:** `OC Teleradiology Package` with payload manifest, destination, correlation ID, status events, report references, and reconciliation outcome.
- **Workflow:** Prepared → Approved → Sent → Accepted → Reading → Report Returned → Reconciled, with Declined and Failed states.
- **Roles/permissions:** imaging coordinators prepare; authorized radiologists approve disclosure; scoped integration users exchange packages.
- **API/jobs/surfaces:** signed whitelisted send and callback methods, RQ retries, and an operations dashboard with aging and failed packages.

## Boundaries

Owns: package manifest, exchange state, disclosure evidence, and returned-report reconciliation. Consumes: study references, clinical context, and partner responses. Emits: reading assignments and report artifacts. Does not own: external PACS or reader credentialing.

## Open questions

- Which interoperability profile should define the minimum package and signature evidence across partners?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
