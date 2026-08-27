# Community Staff Mileage And Route Log — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Builds reviewable mileage and route logs from assigned visit legs while minimizing location detail and separating reimbursement approval.
Topics: openchart-feature-catalog, mobile-devices, frappe, mileage-log
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-026 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Low-emission route summary** — Compare approved route alternatives without exposing patient destinations broadly.

## Focus

This entry isolates mobile capture of travel legs and staff correction before external reimbursement processing.

## Behavior

- Staff start a route or accept a proposed sequence of assigned visits for the work period.
- The app records visit-to-visit legs using configured manual odometer, calculated distance, or bounded location sampling.
- Personal commute, breaks, cancelled legs, detours, and nonreimbursable travel are separately classified.
- Users review, correct, and attest the log before submission; original calculations remain visible to reviewers.
- Offline logs remain encrypted and pending until server receipt.
- Supervisors approve, return, or reject with rationale under organization policy.
- Patient addresses are replaced with visit references in ordinary mileage views.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mileage Log` and child `OC Mileage Leg` with staff, visit references, method, start/end, distance, classification, correction, attestation, and state.
- **Workflow and roles:** Draft → Submitted → Approved/Returned/Rejected; `OC Community Staff` owns drafts and `OC Field Operations Supervisor` reviews.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.mileage.save` and `submit` validate assignment references; protected coordinates are excluded from auto-REST.
- **Realtime and jobs:** Websocket events return approval state; server-side RQ jobs calculate routes, apply retention, and prepare nonclinical export handoffs.
- **Files and surfaces:** Receipt or exception evidence uses private Frappe file attachment APIs; mobile review and Desk reports separate travel data from clinical charts.

## Boundaries

Owns: travel-leg evidence, staff attestation, and review state. Consumes: visit assignments, route service, and policy. Emits: approved mileage summary. Does not own: payroll, payment, tax policy, or continuous surveillance.

## Open questions

- Which distance method is authoritative when odometer, route estimate, and sampled path differ?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
