# Unified Patient Communication Attempt Log — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents one provenance-rich patient timeline of SMS, email, phone, portal, letter, and in-person communication attempts.
Topics: openchart-feature-catalog, messaging-tasks, frappe, communication-log
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-037 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Contact episode reconstruction** — Group related attempts, replies, tasks, and outcomes into one reviewable narrative.

## Focus

This feature isolates the normalized communication evidence layer so staff can understand contact history without searching each channel subsystem.

## Behavior

- Every supported channel emits a normalized attempt with patient, purpose, direction, time, actor or system, destination reference, and outcome.
- The timeline displays minimum-necessary summaries and opens source records only after current permission checks.
- Related attempts may share campaign, reminder, incident, or contact-episode correlation identifiers.
- Delivery, read, acknowledgment, response, and staff disposition remain separate event types.
- Corrections append superseding events and never rewrite provider webhook or staff-entered evidence.
- Duplicate provider events collapse by source key while retaining raw-event audit references.
- Users filter by purpose, direction, channel, outcome, date, and unresolved follow-up.
- Restricted communications can appear as sealed placeholders to users lacking content authority.

## Frappe realization

- **DocTypes:** `OC Communication Attempt` and `OC Communication Event` store normalized fields, source Dynamic Link, patient, purpose, channel, timestamps, outcome, correlation ID, and supersession.
- **Hooks:** channel adapters append normalized records after accepted source events; direct edits are blocked.
- **Permissions:** patient/facility user permissions plus sensitivity permlevels govern summary and source access.
- **Surfaces:** patient chart timeline, Query Report, channel filters, and export with provenance metadata.
- **API:** `open_chart.api.v1.messaging.patient_communication_timeline` returns scoped, paginated projections rather than raw payloads.

## Boundaries

Owns: normalized attempt and event projection. Consumes: source-channel records and identity links. Emits: unified timeline and aggregate inputs. Does not own: channel workflows, message bodies, or delivery truth beyond source evidence.

## Open questions

- Which minimum summary remains useful when the source content is sealed by sensitivity policy?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Communication Retention and Purge Schedules](openchart-feature-catalog-msg-039-communication-retention-and-purge-schedules.md)
