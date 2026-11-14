# Task Completion Evidence Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Requires structured, source-linked evidence before selected task types can be marked complete.
Topics: openchart-feature-catalog, messaging-tasks, frappe, completion-evidence
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-010 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Evidence quality review** — Sample completed tasks for missing, weak, or contradictory proof without changing clinical records automatically.

## Focus

This feature isolates proof of work so a completed checkbox cannot substitute for required communication, documentation, or source-state evidence.

## Behavior

- Task type policy declares whether completion needs a response code, note, attachment, source link, timestamp, witness, or combination.
- The assignee sees required evidence fields before starting and cannot complete while mandatory elements are missing.
- Evidence may reference an accepted chart artifact without copying its protected contents into the task.
- Uploaded evidence records provenance, checksum, uploader, classification, and access restrictions.
- A completion attempt against stale or inaccessible source evidence fails with a precise remediation message.
- Supervisors may reopen completion with reason; prior evidence and completion events remain immutable.
- Evidence correction creates a succeeding evidence record rather than replacing the accepted one.
- Completing a task proves workflow closure only and does not assert a clinical outcome beyond the recorded evidence.

## Frappe realization

- **DocTypes:** `OC Task Completion Requirement`, `OC Task Evidence`, and `OC Task Completion Event` hold evidence type, source Dynamic Link, file, checksum, actor, and supersession.
- **Workflow:** the Complete action runs server validation; Completed → Reopened requires Task Supervisor authority and reason.
- **Files/permissions:** private Frappe File attachments inherit task and patient access checks; evidence metadata uses permlevels for audit-only fields.
- **API/hooks:** guarded completion method verifies requirements transactionally; `on_update` emits a completion event and Notification Log entry.
- **Reports:** Script Report identifies completed tasks by evidence type, reopen rate, and missing-source exceptions.

## Boundaries

Owns: task evidence requirements and completion proof. Consumes: task policy, chart artifacts, files, and actor identity. Emits: validated completion events. Does not own: truth of referenced clinical records or outcome adjudication.

## Open questions

- Which evidence types require dual attestation or supervisory review?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Unified Patient Communication Attempt Log](openchart-feature-catalog-msg-037-unified-patient-communication-attempt-log.md)
