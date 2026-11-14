# Arrival Hooks into Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes idempotent registration-readiness and arrival events so scheduling can update visit flow without owning patient identity data.
Topics: openchart-feature-catalog, registration, frappe, arrival-hooks
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-052 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Configurable readiness gates** — Let each visit type declare which registration checks must pass before arrival handoff.

## Focus

Define the safe event seam between registration completion and an external or future scheduling domain.

## Behavior

- Registration computes readiness for a selected appointment or arrival context using versioned clinic policy.
- Staff explicitly confirm arrival after resolving or acknowledging allowed registration exceptions.
- The hook emits patient reference, facility, appointment reference, event ID, readiness summary, actor, and time.
- Duplicate retries with the same event ID produce the original outcome and no duplicate arrival transition.
- Scheduling rejection or timeout leaves registration accepted, records integration failure, and creates a retry task.
- Cancellation or correction emits a compensating event rather than deleting the original arrival evidence.

## Frappe realization

- **DocTypes:** `OC Registration Arrival Event` with appointment reference, facility, readiness_json, idempotency_key, state, response, and compensates.
- **Workflow:** Prepared → Emitting → Acknowledged, Rejected, or Retry Required → Compensated.
- **Roles/permissions:** `OC Registration Clerk` confirms; `OC Integration User` consumes narrowly; `OC Registration Supervisor` retries or compensates.
- **API/surfaces:** `open_chart.api.v1.registration.confirm_arrival`; `doc_events` and background queue publish hooks; arrival status panel and failure worklist.

## Boundaries

Owns: registration readiness snapshot and arrival event delivery. Consumes: appointment reference and accepted registration state. Emits: idempotent scheduling hook. Does not own: appointment status, queue position, or encounter creation.

## Open questions

- What is the minimum scheduling contract when no scheduling application is installed?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
