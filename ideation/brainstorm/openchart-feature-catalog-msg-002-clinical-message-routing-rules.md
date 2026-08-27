# Clinical Message Routing Rules — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes incoming messages by result type, patient panel, schedule, facility, and urgency into the correct accountable destination.
Topics: openchart-feature-catalog, messaging-tasks, frappe, message-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-002 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Routing simulation** — Preview destinations and conflicts against synthetic events before activating a policy version.

## Focus

This feature isolates clinically meaningful routing criteria and precedence, distinct from the generic engine that evaluates and applies assignments.

## Behavior

- Messaging administrators define ordered rules using message type, result category, patient panel, facility, service, schedule, and urgency.
- Each rule resolves to a user, role-backed pool, coverage schedule, or explicit review queue.
- Effective dates and version states prevent retroactive changes to already routed items.
- A preview explains which clauses matched, which rule won, and which fallback would apply.
- Ambiguous equal-priority matches route to a configured exception pool rather than selecting silently.
- Missing panel or schedule data follows an explicit fallback and records the absent input.
- Clinical supervisors activate or retire rules; authors cannot self-approve when separation of duties is configured.
- Every routed item stores the policy version, evaluated facts, selected destination, and correlation ID.

## Frappe realization

- **DocTypes:** `OC Message Routing Policy`, `OC Message Routing Rule`, and `OC Routing Decision` store criteria JSON, precedence, effective period, target, and explanation.
- **Workflow:** Draft → Review → Active → Retired uses Frappe Workflow; only one compatible active version is allowed per scope.
- **Roles/permissions:** Messaging Rule Author, Clinical Supervisor, and Audit Reviewer use permlevels to separate criteria editing from activation.
- **Engine:** Frappe Assignment Rules provide the assignment action while a validated server-side predicate adapter supplies clinical criteria and deterministic precedence.
- **API/report:** `open_chart.api.v1.messaging.simulate_route` is read-only; a Query Report exposes unmatched and exception-routed items.

## Boundaries

Owns: clinical routing policy and decision evidence. Consumes: message metadata, panels, schedules, and coverage. Emits: explained destinations and exceptions. Does not own: source-result interpretation or staff scheduling.

## Open questions

- Which criteria may be authored locally by a facility versus governed globally?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Assignment Rule Engine](openchart-feature-catalog-msg-011-assignment-rule-engine.md)
