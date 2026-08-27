# Post-Visit Summary Delivery — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Releases the authorized after-visit summary to the patient after a virtual encounter ends and documentation is ready.
Topics: openchart-feature-catalog, telehealth, frappe, virtual-visit-summary
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-024 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Follow-up acknowledgment** — Let patients confirm receipt and flag inability to follow instructions for staff review.

## Focus

This feature isolates release timing, channel delivery, and receipt state for a virtual encounter summary.

## Behavior

- Ending media marks the visit disconnected but does not release an incomplete or unsigned summary.
- The clinician reviews medications, instructions, orders, follow-up, warning signs, and contact guidance in the linked encounter.
- Release checks signature, amendment state, patient-access restrictions, proxy scope, and preferred language.
- The portal receives the canonical summary; external channels send only a privacy-safe availability notice unless policy permits more.
- Delivery failure creates a staff task and retry state without changing the signed clinical artifact.
- A corrected summary supersedes the prior version and produces a new release notice with visible lineage.

## Frappe realization

- **DocTypes:** `OC Visit Summary Release` links encounter, summary version, audience, restriction, channel, delivery attempts, acknowledgment, and superseded release.
- **Hooks/jobs:** encounter signature or amendment queues an idempotent release job; Notifications and Notification Log track portal, email, or SMS availability notices.
- **Permissions/surfaces:** Patient and authorized Proxy access a portal page; Clinician controls readiness; Release Reviewer resolves restrictions and failures.

## Boundaries

Owns: summary-release orchestration and delivery evidence. Consumes: signed encounter summary and access policy. Emits: patient-visible release and notifications. Does not own: clinical summary authorship or external messaging transport.

## Open questions

- Which virtual services require immediate release, clinician-controlled delay, or additional safety review?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
