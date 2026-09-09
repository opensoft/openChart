# Result Escalation Ladder — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Escalates unacknowledged results through timed, role-aware tiers while preserving ownership and response evidence.
Topics: openchart-feature-catalog, cpoe, frappe, result-escalation
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-038 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Escalation simulation** — Preview recipients and timing against synthetic schedules before a policy is activated.

## Focus

This feature isolates deterministic escalation when accountable review is late.

## Behavior

- Policies define tiers by priority, elapsed time, care setting, owner type, and recipient pool.
- Each escalation records trigger time, recipient resolution, notification channel, and delivery outcome.
- Escalation adds accountable visibility but does not silently transfer ownership unless policy explicitly says so.
- Acknowledgment stops future tiers idempotently while retaining sent events.
- Missing recipients or notification failures route to an operational exception pool.
- Rules notify humans and never acknowledge, order, or contact patients autonomously.

## Frappe realization

- **DocTypes:** `OC Result Escalation Policy` with versioned tiers and provenance; submitted `OC Result Escalation Event` records execution.
- **Workflow:** policy Draft → Tested → Approved → Active → Retired; events Pending → Sent → Delivered/Failed/Cancelled.
- **Roles/permissions:** `OC Result Governance` authors; separate `OC Clinical Safety Reviewer` approves; oversight staff handle failures.
- **Scheduler/API/surface:** minute/hourly scheduler scans due accountability records, queues notifications, and exposes REST filters for failed or current-tier items.

## Boundaries

Owns: escalation timing, recipients, and evidence. Consumes: accountability state, schedules, and policy. Emits: notifications and exceptions. Does not own: acknowledgment or patient outreach.

## Open questions

- Which critical-result tiers require synchronous human-to-human communication evidence?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Result Follow-Up Deadline](openchart-feature-catalog-ord-039-result-follow-up-deadline.md)
