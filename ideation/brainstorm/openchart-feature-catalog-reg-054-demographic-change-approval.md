# Demographic Change Approval — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies field-sensitive review, conflict checks, and succession-based updates to submitted demographic change requests.
Topics: openchart-feature-catalog, registration, frappe, change-approval
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-054 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Risk-based dual approval** — Require independent review for identity-critical or legally sensitive field combinations.

## Focus

Decide and safely apply requested demographic changes through the guarded API surface.

## Behavior

- Reviewer sees requester authority, evidence, current value, proposal, prior changes, and duplicate risk signals.
- Each proposed field can be approved, rejected, or returned for more information with a reason.
- A stale current-value hash forces re-review instead of overwriting a newer accepted change.
- Identity-critical approvals rerun duplicate detection before application.
- Accepted values create successor records and never mutate the prior accepted fact in place.
- The requester receives a permission-safe outcome that omits restricted reviewer notes and other patient facts.

## Frappe realization

- **DocTypes:** `OC Demographic Change Decision` linked to request, with per-field disposition, reviewer, policy, conflict check, and applied successor.
- **Workflow:** Pending Review → In Review → Partially Approved, Approved, Rejected, or More Information Needed → Applied or Apply Failed.
- **Roles/permissions:** `OC Registration Supervisor` reviews routine fields; `OC Identity Reviewer` handles identity-critical fields; dual approval uses Workflow Actions.
- **API/surfaces:** `open_chart.api.v1.registration.decide_demographic_change` and `.apply_demographic_change`; comparison desk page and approval queue.

## Boundaries

Owns: review decision and guarded application. Consumes: submitted request, policy, evidence, and current facts. Emits: successor records and outcome notice. Does not own: request capture or duplicate merge.

## Open questions

- Which exact field combinations require dual control in the first policy profile?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
