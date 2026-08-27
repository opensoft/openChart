# Broadcast Campaigns to Patient Cohorts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Sends governed multi-recipient outreach to an approved patient cohort while enforcing consent, opt-outs, and per-recipient outcomes.
Topics: openchart-feature-catalog, messaging-tasks, frappe, patient-campaigns
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-016 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Holdout measurement** — Support ethically reviewed comparison groups for outreach effectiveness.

## Focus

This feature isolates cohort broadcast execution and approval, distinct from cohort definition and channel template authorship.

## Behavior

- A campaign references a frozen, provenance-bearing cohort snapshot and approved purpose-specific template.
- Preview shows recipient count, channel eligibility, opt-outs, duplicates, missing contacts, and estimated cost.
- Required approval depends on purpose, volume, sensitivity, and whether the message is clinical or informational.
- Execution rechecks do-not-contact and channel preference immediately before each send.
- Each patient receives at most one message per deduplication key unless an authorized resend is recorded.
- Pause and cancel stop unsent jobs while preserving attempted and delivered records.
- Failures produce per-recipient outcomes and retry eligibility without rolling back successful sends.
- Replies, opt-outs, and action events link back to campaign and patient communication history.

## Frappe realization

- **DocTypes:** `OC Communication Campaign`, `OC Campaign Recipient`, and `OC Campaign Run` hold cohort snapshot, template version, purpose, approvals, dedupe key, and outcome.
- **Workflow:** Draft → Review → Approved → Scheduled/Running → Paused/Completed/Cancelled.
- **Automation:** `scheduler_events` starts due runs; RQ jobs process bounded batches with idempotency and rate limits.
- **Channels:** Frappe SMS settings and Email Accounts send approved projections; Notification Log is used for internal operator events, not patient delivery proof.
- **Reports/permissions:** Campaign Author, Communications Approver, and Campaign Operator; Script Reports show exclusions, delivery, replies, and cost.

## Boundaries

Owns: campaign approval, recipient snapshot, execution state, and outcomes. Consumes: cohort evidence, templates, consent, preferences, and channel gateways. Emits: patient communications and aggregate metrics. Does not own: cohort clinical logic or consent capture.

## Open questions

- Which campaign purposes require an explicit patient-level legal basis beyond general communication consent?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Do-not-contact Registry Enforcement](openchart-feature-catalog-msg-038-do-not-contact-registry-enforcement.md)
