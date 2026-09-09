# Abnormal-result Notification Composition — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Helps clinicians compose plain-language abnormal-result notifications with reviewed templates, result context, and follow-up instructions.
Topics: openchart-feature-catalog, messaging-tasks, frappe, result-notification
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-031 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Reading-level review** — Flag jargon and complex instructions before clinician approval without generating clinical interpretation.

## Focus

This feature isolates clinician-authored patient communication about an abnormal result while keeping interpretation and release authority explicit.

## Behavior

- An authorized clinician starts from a reviewed result and selects an approved purpose and language template.
- The composer inserts allowlisted result descriptors, clinician explanation, follow-up action, urgency, and contact instructions.
- Plain-language prompts distinguish what was found, what it may mean, what happens next, and when to seek help.
- The source result version and authoring clinician remain linked to the communication.
- Template text never invents interpretation; required clinical fields must be supplied or explicitly marked not applicable.
- Preview shows the exact patient-facing content for the resolved channel and language.
- High-risk classes may require second review, explicit acknowledgment, or synchronous contact instead of asynchronous delivery.
- Sending records channel decision and does not mark the result reviewed or follow-up completed unless their owning workflows say so.

## Frappe realization

- **DocTypes:** `OC Result Notification Draft`, `OC Result Communication Template`, and `OC Result Notification Approval` hold result Dynamic Link, explanation, action, urgency, language, version, and approver.
- **Workflow:** Draft → Review/Second Review → Approved → Sent/Cancelled; edits after approval create a succeeding draft.
- **API:** guarded composition and send methods validate result access and invoke preference plus PHI-aware channel policy.
- **Notifications:** portal, Frappe Email Accounts, and SMS settings deliver approved content; Notification Log records staff approval work.
- **Permissions:** Result Communicator, Ordering Clinician, and Clinical Reviewer separate drafting, approval, and audit access.

## Boundaries

Owns: patient-facing result-notification draft, approval, and send evidence. Consumes: accepted result, clinician interpretation, templates, language, and channel policy. Emits: approved communication. Does not own: result validity, release, diagnosis, or follow-up completion.

## Open questions

- Which abnormal-result classes require synchronous contact before any asynchronous message?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Recipient Read and Acknowledgment Tracking](openchart-feature-catalog-msg-006-recipient-read-and-acknowledgment-tracking.md)
