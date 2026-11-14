# PHI-aware External Email Gateway — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Inspects outbound patient email purpose and sensitivity, replacing unsafe PHI content with a secure portal-link notification.
Topics: openchart-feature-catalog, messaging-tasks, frappe, phi-email-policy
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-027 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Policy explanation preview** — Show composers which content class triggered redirect, block, or approval before sending.

## Focus

This feature isolates the last-mile policy gate between approved composition and external email transport.

## Behavior

- Every external patient email submits purpose, template version, recipient, sensitivity labels, and referenced chart artifacts to the gateway.
- Policy returns send-as-composed, replace-body-with-portal-link, require approval, or block with structured reasons.
- Portal-link replacement stores sensitive content in an authorized portal object and sends only approved minimal text.
- Links are recipient-bound, expiring, revocable, and require portal authentication before content access.
- Free text and attachments receive stricter handling than approved low-sensitivity variables.
- Overrides require authorized role, reason, policy basis, and immutable audit evidence.
- Transport begins only after destination verification, preference, and do-not-contact checks pass.
- Delivery events reference the gateway decision without exposing sensitive content in logs.

## Frappe realization

- **DocTypes:** `OC External Email Policy`, `OC Email Gateway Decision`, and `OC Secure Message Link` store purpose, sensitivity, action, reason, approver, expiry, and revocation.
- **Transport:** all patient outbound mail uses a guarded service before `frappe.email`; approved Frappe Email Accounts remain the transport identity.
- **Hooks/API:** override direct patient-email whitelisted methods where necessary; `open_chart.api.v1.messaging.prepare_external_email` returns a signed decision.
- **Portal:** a `www/` page authenticates the recipient and fetches content under current patient/proxy authority.
- **Reports:** blocked, redirected, overridden, expired-unread, and account-selection events support privacy review.

## Boundaries

Owns: outbound email policy decisions and secure-link projection. Consumes: composed email, sensitivity, portal identity, preferences, and Email Accounts. Emits: approved mail payload or block. Does not own: source content or email transport delivery.

## Open questions

- Which content classifications may ever be sent directly when a patient explicitly requests email?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Email Templates and Delivery Events](openchart-feature-catalog-msg-017-email-templates-and-delivery-events.md)
