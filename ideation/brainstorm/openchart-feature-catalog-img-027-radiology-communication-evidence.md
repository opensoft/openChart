# Radiology Communication Evidence — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records how accepted imaging reports and recommendations were delivered to providers, patients, or external recipients with channel-specific evidence.
Topics: openchart-feature-catalog, imaging, frappe, result-delivery
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-027 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Delivery reconciliation dashboard** — Surface accepted reports with missing, failed, or ambiguous delivery outcomes.

## Focus

This feature isolates ordinary report delivery evidence distinct from critical-finding acknowledgment.

## Behavior

- Report acceptance creates delivery obligations according to recipient, consent, sensitivity, and facility policy.
- Each attempt records report version, recipient, channel, address or endpoint reference, timestamp, and outcome.
- Portal release, in-basket delivery, interface acknowledgment, fax confirmation, and direct contact remain distinct outcomes.
- Failed or ambiguous delivery retries according to policy and creates a task when automation is exhausted.
- A corrected report creates a new obligation and identifies recipients of the superseded version.
- Delivery evidence proves transmission or access, not comprehension or clinical action unless separately acknowledged.

## Frappe realization

- **DocTypes:** `OC Imaging Report Delivery` with child attempts, report version, recipient Dynamic Link, channel, consent basis, and outcome.
- **Workflow:** Pending → Sending → Delivered → Closed, with Failed, Reconciliation, and Superseded states.
- **Roles/permissions:** result-routing staff resolve failures; clinicians see delivery state; patients see only their authorized release event.
- **Hooks/API/surfaces:** report `on_submit` seeds obligations; background jobs and Notification Log capture outcomes; Script Report shows exceptions.

## Boundaries

Owns: report-delivery obligation and transmission evidence. Consumes: accepted report, recipient routing, consent, and channel outcomes. Emits: delivery status and reconciliation tasks. Does not own: clinical acknowledgment or follow-up action.

## Open questions

- Which channel outcomes are strong enough to close routine delivery without manual review?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
