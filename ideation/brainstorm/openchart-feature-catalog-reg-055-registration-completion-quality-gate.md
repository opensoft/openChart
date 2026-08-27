# Registration Completion Quality Gate — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates a patient registration against versioned clinic requirements and returns Ready, Ready with Exceptions, or Blocked with explainable findings.
Topics: openchart-feature-catalog, registration, frappe, completion-gate
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-055 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Visit-type policy profiles** — Compose minimum registration requirements by facility, service, age, and arrival channel.

## Focus

Provide one explainable readiness decision without hiding incomplete registration behind a generic complete checkbox.

## Behavior

- Staff evaluate readiness for a patient, facility, visit context, and point in time.
- Versioned rules inspect identity assurance, required demographics, contacts, authority, coverage capture, notices, and open exceptions.
- Each finding states requirement, evidence checked, severity, owner, and allowed override role.
- Ready with Exceptions requires explicit acknowledgment and creates follow-up work for every deferred item.
- Blocked cannot be bypassed except through a configured supervisor override with reason and expiry.
- Re-evaluation creates a new snapshot so later users can reconstruct the decision used at arrival.

## Frappe realization

- **DocTypes:** `OC Registration Readiness Check` and child `OC Readiness Finding` with policy_version, context, outcome, evidence refs, override, and checked_on.
- **Workflow:** Evaluating → Ready, Ready with Exceptions, Blocked, or Failed → Superseded.
- **Roles/permissions:** `OC Registration Clerk` evaluates; `OC Registration Supervisor` applies allowed overrides; source permissions remain enforced.
- **API/surfaces:** `open_chart.api.v1.registration.evaluate_readiness`; intake summary, patient readiness badge, arrival dialog, and exception Script Report.

## Boundaries

Owns: contextual registration-readiness decision. Consumes: versioned requirements and registration evidence. Emits: explainable snapshot and follow-up tasks. Does not own: source facts, appointment status, or clinical clearance.

## Open questions

- Which requirements must remain hard blocks during emergency registration?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
