# Do-not-contact Registry Enforcement — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces patient contact restrictions consistently across every outbound channel with purpose-aware exceptions and audit evidence.
Topics: openchart-feature-catalog, messaging-tasks, frappe, do-not-contact
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-038 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Restriction conflict review** — Surface contradictory patient, proxy, legal, and operational restrictions before the next planned contact.

## Focus

This feature isolates the cross-channel hard gate for full, destination-specific, channel-specific, and purpose-specific contact restrictions.

## Behavior

- A restriction records patient, scope, purpose, channel or destination, effective period, source, authority, and reason category.
- Every outbound SMS, email, call, portal push, campaign, reminder, and generated letter checks the registry immediately before release.
- Matching restrictions return blocked, allowed by documented exception, or requires review with an explanation.
- Essential clinical and legal exceptions must be explicitly versioned; urgency alone does not imply permission.
- Patient or authorized proxy requests create effective-dated records and preserve who supplied the instruction.
- Wrong-number, complaint, and opt-out events may propose or create restrictions according to governed rules.
- Removing a restriction creates a successor record and never erases prior enforcement evidence.
- Bypass requires authorized role, purpose, reason, and immutable link to the specific communication attempt.

## Frappe realization

- **DocTypes:** `OC Contact Restriction`, `OC Contact Exception Policy`, and `OC Contact Enforcement Decision` store scope, authority, effective dates, decision, reason, and attempt Link.
- **API:** `open_chart.api.v1.messaging.enforce_contact_policy` is mandatory for all outbound channel services.
- **Hooks:** guarded send paths reject missing enforcement decision IDs; preference changes and inbound opt-outs append registry events.
- **Permissions:** Patient Communications Privacy Manager handles exceptions; patients/proxies can submit permitted restrictions through portal pages.
- **Reports:** blocked attempts, overrides, conflicts, and channels missing checks appear in compliance reports.

## Boundaries

Owns: contact restrictions and enforcement decisions. Consumes: patient/proxy authority, purpose, channel, destination, and exception policy. Emits: allow, block, or review outcomes. Does not own: consent policy interpretation or communication transport.

## Open questions

- Which legally required notices remain permissible when a patient requests no contact by every channel?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Patient Notification Preference Resolution](openchart-feature-catalog-msg-021-patient-notification-preference-resolution.md)
