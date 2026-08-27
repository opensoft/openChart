# Communication Retention and Purge Schedules — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies policy-versioned retention, legal hold, archival, and purge actions to messages, tasks, attachments, and delivery evidence.
Topics: openchart-feature-catalog, messaging-tasks, frappe, communication-retention
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-039 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Retention impact preview** — Enumerate records and blocked dependencies before a policy version is activated or a purge run begins.

## Focus

This feature isolates lifecycle governance for communication artifacts while preserving records incorporated into the clinical chart or subject to hold.

## Behavior

- Records receive a retention class from type, purpose, patient context, jurisdiction, and incorporation status.
- Active policies define retain-until basis, archive action, purge eligibility, and required evidence.
- Legal, audit, complaint, safety, or investigation holds suspend purge for named records and related evidence.
- A preview reports counts, date ranges, holds, broken-link risks, and storage estimates without mutation.
- Approved purge runs process bounded batches and record success, skip, failure, checksum evidence, and actor or job identity.
- Purging content may retain a minimal tombstone where policy requires provenance or referential integrity.
- Source clinical records and accepted evidence are never purged merely because a message copy expires.
- Policy changes apply prospectively to evaluation and never falsify prior retention decisions.

## Frappe realization

- **DocTypes:** `OC Communication Retention Policy`, `OC Record Hold`, `OC Retention Evaluation`, and `OC Purge Run` store classes, rules, scope, approvals, records, and outcomes.
- **Workflow:** policy Draft → Review → Active → Retired; purge Proposed → Approved → Running → Completed/Failed.
- **Automation:** `scheduler_events` evaluates due records; RQ jobs purge bounded batches with resumable checkpoints.
- **Permissions:** Records Manager, Privacy Officer, and Audit Reviewer separate policy, approval, execution, and evidence access.
- **Surfaces:** retention inventory, hold registry, purge preview, and storage/reconciliation Script Reports.

## Boundaries

Owns: communication retention classification, holds, and purge evidence. Consumes: artifact metadata, clinical-incorporation links, and policy authority. Emits: archive, purge, skip, and tombstone events. Does not own: enterprise records policy or source clinical-record retention.

## Open questions

- Which message and task artifacts become part of the designated clinical record, and by what explicit action?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Secure Staff Message Attachments](openchart-feature-catalog-msg-026-secure-staff-message-attachments.md)
