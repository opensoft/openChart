# Email Templates and Delivery Events — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs patient email templates and records provider delivery events without treating tracking signals as clinical acknowledgment.
Topics: openchart-feature-catalog, messaging-tasks, frappe, email-delivery
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-017 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Branded locale packs** — Apply facility-approved visual and language variants without forking template logic.

## Focus

This feature isolates versioned email composition and transport evidence, including the uncertainty of opens and link clicks.

## Behavior

- Authors create subject, plain-text, HTML, language, purpose, sensitivity, and allowlisted variable definitions.
- Preview uses synthetic data and checks missing variables, unsafe links, absent plain-text, and accessibility basics.
- Approved versions are immutable and rendered server-side against minimum-necessary context.
- Sending selects an authorized outbound account by facility, purpose, and verified sender identity.
- Provider or SMTP events record queued, accepted, delivered, bounced, complained, opened, and clicked where available.
- Opens and clicks are labeled probabilistic and never satisfy clinical acknowledgment by themselves.
- Bounce and complaint outcomes can suppress future nonessential email through preference resolution.
- Historical messages retain template version, rendered-content digest, account, and provider correlation ID.

## Frappe realization

- **DocTypes:** `OC Email Template Version` and `OC Email Delivery Event` extend governed use of Frappe Email Template and Communication records.
- **Workflow:** Draft → Review → Active → Retired separates template author and Communications Approver.
- **Transport:** Frappe Email Accounts select inbound/outbound identity; `frappe.email` sends, and signed webhook methods append delivery events.
- **Security:** PHI-aware policy validation can replace sensitive body content with a portal link before enqueueing.
- **Reports:** Query Reports expose bounce, complaint, and uncertain engagement rates by template version.

## Boundaries

Owns: email template governance and delivery-event evidence. Consumes: approved context, preferences, and Email Accounts. Emits: rendered email and transport events. Does not own: recipient consent, portal content, or proof that a human read the email.

## Open questions

- Should privacy-sensitive deployments disable open and click tracking entirely?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [PHI-aware External Email Gateway](openchart-feature-catalog-msg-027-phi-aware-external-email-gateway.md)
