# Outbound Pharmacy Fax Fallback — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Sends a policy-permitted signed prescription rendition to a verified non-connected pharmacy by fax with destination and delivery evidence.
Topics: openchart-feature-catalog, eprescribing, frappe, pharmacy-fax
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-052 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Destination re-verification cadence** — Frequently used fax endpoints could require periodic staff confirmation before reuse.

## Focus

This feature isolates a controlled fallback for pharmacies without electronic connectivity. It verifies destination, policy, and duplicate-send risk before disclosure.

## Behavior

- An authorized user chooses fax fallback only when the pharmacy is non-connected or electronic routing is unavailable.
- The system verifies pharmacy identity, fax number source/freshness, prescription eligibility, consent, and jurisdiction policy.
- The user previews a minimum-necessary signed rendition and confirms destination immediately before send.
- Fax states include queued, dialing, delivered, failed, indeterminate, and manually confirmed.
- Retry warnings compare prior attempts and electronic sends to prevent accidental duplicate prescriptions.
- Delivery evidence and failures create audit events and follow-up tasks; success does not imply dispensing.

## Frappe realization

- **DocTypes:** `OC Pharmacy Fax Transmission` links prescription rendition, endpoint snapshot, purpose, attempts, provider IDs, result, and confirmation.
- **Workflow:** Prepared → Destination Verified → Sent → Delivered/Failed/Indeterminate/Manual Follow-up.
- **Roles/API:** Pharmacy operations prepare; permitted clinical roles confirm; provider callbacks enter authenticated idempotent methods.
- **Surfaces/hooks:** Fax dialog, delivery report attachment, failure queue, and Notification escalation support safe fallback.

## Boundaries

Owns: verified fax disclosure, transmission state, and evidence. Consumes: signed rendition, pharmacy endpoint, consent, and policy. Emits: fax and follow-up tasks. Does not own: telecom delivery guarantees, dispensing, or controlled-substance exceptions.

## Open questions

- Which prescription classes must never use fax fallback even during network outages?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prescription Print Report](openchart-feature-catalog-phr-051-prescription-print-report.md)
