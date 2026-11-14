# Specimen Collection Label Scanning — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Verifies patient, order, container, label, and collector at collection time and records a traceable specimen handoff.
Topics: openchart-feature-catalog, mobile-devices, frappe, specimen-scanning
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-015 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Mobile label-printer handoff** — Send an authorized print job to a nearby managed printer after bedside identity confirmation.

## Focus

This capability isolates positive identification and collection evidence at the specimen source.

## Behavior

- The collector opens an active order, verifies the patient wristband, and scans or prints each expected label.
- The server checks order status, patient, accession, specimen type, container, collection window, and duplicate state.
- The collector records actual collection time, site, method, exceptions, and each container produced.
- Wrong-patient, wrong-container, duplicate-label, cancelled-order, and expired-label outcomes block normal completion.
- Recollection and unused-label destruction remain explicit, auditable paths.
- Offline collection requires a signed work manifest and reserves no new accession unless policy supports safe allocation.
- Handoff to transport or laboratory records actor, time, and container count.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Specimen Collection` and child `OC Collected Container` with order, accession, label hash, patient check, type, time, collector, state, and handoff.
- **Workflow and roles:** Planned → Identity Verified → Collected → Handed Off/Rejected/Recollect; `OC Phlebotomist` and `OC Nurse` act within facility permissions.
- **API and auth:** Use token-authenticated `open_chart.api.v1.mobile.specimen.verify` and `collect`; guarded methods enforce accession and idempotency rules.
- **Realtime and jobs:** Websocket events invalidate cancelled orders and consumed labels; server-side RQ jobs reconcile offline collections and route exceptions.
- **Files and surfaces:** No routine camera frame is stored; exception images use private Frappe file attachment APIs with restricted roles and retention, plus collection worklists.

## Boundaries

Owns: mobile collection and label verification evidence. Consumes: lab order, accession, patient verification, and container policy. Emits: collected-container and handoff events. Does not own: test performance or result interpretation.

## Open questions

- Can any site safely allocate accessions offline, and what collision-proof range policy would apply?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
