# Patient-context Message Threads — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Anchors internal message threads to a patient and optional chart artifact while preserving permissions and conversational history.
Topics: openchart-feature-catalog, messaging-tasks, frappe, patient-context
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-003 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Context timeline projection** — Show thread milestones alongside the linked chart artifact without copying message bodies into the chart.

## Focus

This feature isolates durable colleague conversation attached to patient context, including the authority boundary between a message and the clinical record.

## Behavior

- A permitted user starts a thread from a patient, encounter, result, order, medication, or other supported chart record.
- The header identifies the patient and immutable source snapshot metadata while opening the live source only after a fresh permission check.
- Participants post replies, add recipients, and mark the thread resolved or reopened with a reason.
- Replies are append-only; corrections create linked superseding entries rather than editing accepted text.
- Removing a participant stops future access unless policy requires retained access to previously delivered content.
- Patient merges or source amendments update links through governed identity mapping without rewriting message history.
- A deleted or restricted source leaves a tombstone description and blocks unauthorized navigation.
- Resolution does not imply that the linked result, order, or encounter is clinically complete.

## Frappe realization

- **DocTypes:** `OC Message Thread`, `OC Message Entry`, and `OC Thread Participant` use patient Link, source Dynamic Link, snapshot label, recipients, state, and supersedes Link.
- **Workflow:** Open → Resolved → Reopened is reason-gated; entries use succession rather than in-place amendment.
- **Roles/permissions:** Clinical Messaging User and Message Auditor rely on patient/facility user permissions plus participant checks in `has_permission`.
- **Hooks/API:** guarded reply and participant methods under `open_chart.api.v1.messaging`; `validate` rejects inaccessible context and `on_update` emits realtime events.
- **Surfaces:** chart timeline widget, Desk thread page, activity feed references, and Notification Log alerts expose context without duplicating the clinical artifact.

## Boundaries

Owns: thread membership, entries, and source linkage. Consumes: patient identity, chart permissions, and source metadata. Emits: conversation events and resolution state. Does not own: clinical truth or source-record completion.

## Open questions

- When should prior recipients retain access after their chart authorization is revoked?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Secure Staff Message Attachments](openchart-feature-catalog-msg-026-secure-staff-message-attachments.md)
