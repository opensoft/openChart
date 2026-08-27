# Secure Staff Message Attachments — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Attaches encrypted, permission-checked files to staff messages with provenance, malware scanning, and retention controls.
Topics: openchart-feature-catalog, messaging-tasks, frappe, secure-attachments
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-026 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Attachment redaction workflow** — Create a derived, provenance-linked shareable copy without modifying the original file.

## Focus

This feature isolates secure file exchange inside staff conversations while preserving patient-context permissions and artifact lineage.

## Behavior

- A permitted participant uploads an allowed file type within configured size and sensitivity limits.
- The file remains quarantined until malware scanning and metadata validation succeed.
- Each attachment records uploader, checksum, MIME detection, patient context, classification, and source if derived.
- Recipients must pass current thread and patient permission checks on every download.
- Forwarding to another thread creates a new governed reference and revalidates all recipients.
- Rejected, infected, missing, or scan-timeout files show explicit unavailable states and notify the uploader.
- Replacing a file creates a succeeding attachment version; prior delivered evidence remains retained by policy.
- Download and preview events are audited without marking the message clinically acknowledged.

## Frappe realization

- **DocTypes:** `OC Message Attachment` wraps private Frappe File with thread Link, patient Link, checksum, detected type, scan state, classification, and supersedes Link.
- **Hooks/jobs:** `after_insert` quarantines and enqueues scanning; only a successful job exposes the attachment to recipients.
- **Permissions/API:** a whitelisted download method performs participant, source, and patient checks before issuing content; direct public file URLs are prohibited.
- **Notifications:** Notification Log reports scan rejection or availability to relevant participants.
- **Reports:** attachment inventory and retention exception Script Reports support security review.

## Boundaries

Owns: message attachment lifecycle, access, and provenance. Consumes: thread membership, patient permissions, file scanner, and retention policy. Emits: secure file availability and audit events. Does not own: source clinical documents or malware-engine operation.

## Open questions

- Which file types may be previewed in-browser versus download-only?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Patient-context Message Threads](openchart-feature-catalog-msg-003-patient-context-message-threads.md)
