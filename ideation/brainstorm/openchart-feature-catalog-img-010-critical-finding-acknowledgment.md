# Critical Finding Acknowledgment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes critical imaging findings to an accountable recipient and records delivery, acknowledgment, escalation, and closure evidence.
Topics: openchart-feature-catalog, imaging, frappe, critical-findings
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-010 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Escalation policy simulation** — Test recipient pools and deadlines against historical synthetic scenarios before activation.

## Focus

This feature isolates closed-loop human communication for findings whose urgency cannot rely on ordinary report routing.

## Behavior

- The reporting clinician marks a finding with severity, expected action window, and concise communicated content.
- Recipient selection follows the responsible ordering or covering provider policy and remains reviewable before send.
- Each contact attempt records channel, recipient identity, timestamp, outcome, and actor or integration source.
- Acknowledgment requires an authenticated recipient and records understanding, not proof of clinical action.
- Missed deadlines escalate through configured human-owned tiers without altering care orders automatically.
- Closure requires accepted acknowledgment or a documented exception approved by an authorized role.

## Frappe realization

- **DocTypes:** `OC Critical Finding Communication` with child `OC Contact Attempt`, deadline, severity, recipient pool, acknowledgment, and exception reason.
- **Workflow:** Open → Contacting → Delivered → Acknowledged → Closed, with Escalated and Exception Review states.
- **Roles/permissions:** radiologists initiate; responsible clinicians acknowledge; communication coordinators escalate; audit reviewers read all attempts.
- **Hooks/API/surfaces:** scheduler jobs evaluate deadlines; Notification Log and whitelisted acknowledgment methods capture outcomes; dashboard shows aging obligations.

## Boundaries

Owns: critical-result communication obligation and evidence. Consumes: accepted finding, care-team routing, schedules, and channels. Emits: alerts, acknowledgments, and escalations. Does not own: diagnosis, treatment, or autonomous clinical action.

## Open questions

- Which severity classes and acknowledgment deadlines should be organization-configurable versus nationally standardized?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
