# Provider Credential Expiry Monitoring — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks provider licenses, NPI evidence, DEA registrations, and other credentials with review and expiry escalation.
Topics: openchart-feature-catalog, platform, frappe, credential-expiry
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-005 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Primary-source verification adapters** — Attach authoritative verification outcomes to credential reviews.

## Focus

This feature isolates a credential registry that makes expiration and verification state visible before authority is affected.

## Behavior

- Credentialing staff record credential type, jurisdiction, identifier, issued date, expiry date, evidence attachment, and verification source.
- Records move through Draft, Pending Verification, Verified, Expiring, Expired, Rejected, and Superseded states.
- Configurable warning windows create assignments before expiration and escalate unacknowledged items.
- A replacement credential supersedes prior evidence without deleting its history.
- Expired or rejected credentials emit an authority-change event but never autonomously cancel clinical work.
- Users without credentialing permission see only a safe eligibility result, not protected identifiers or attachments.

## Frappe realization

- **DocTypes:** `OC Provider Credential` links provider and holds type, jurisdiction, identifier, dates, evidence File, verification source, and state.
- **Workflow:** Frappe Workflow governs verification and rejection; Credentialing Specialist and Credentialing Approver have distinct actions.
- **Automation:** daily `scheduler_events` marks warning states, creates Assignments, and sends Frappe Notifications with idempotency keys.
- **Surface:** a Query Report groups credentials by days to expiry; role-safe API returns authority eligibility and reasons.

## Boundaries

Owns: credential evidence, verification state, and expiry alerts. Consumes: provider identity and credential policy. Emits: eligibility events and review tasks. Does not own: prescribing, ordering, signing, or employment decisions.

## Open questions

- Which credential types require dual verification before becoming effective?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Provider Master Registry](openchart-feature-catalog-plt-004-provider-master-registry.md) · [E-signature Authority Registry](openchart-feature-catalog-plt-043-e-signature-authority-registry.md)
