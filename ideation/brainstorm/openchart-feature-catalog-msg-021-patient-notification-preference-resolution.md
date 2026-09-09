# Patient Notification Preference Resolution — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Resolves a patient's purpose-specific channel matrix into an explainable allowed, suppressed, or fallback communication decision.
Topics: openchart-feature-catalog, messaging-tasks, frappe, notification-preferences
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-021 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Preference self-service** — Let portal users review and change non-mandatory channel choices with effective-date history.

## Focus

This feature isolates precedence across patient choices, legal restrictions, purpose, urgency, verified destinations, and organizational defaults.

## Behavior

- Each communication asks for a decision using patient, purpose, candidate channels, urgency, and event time.
- Resolution evaluates explicit consent, purpose opt-ins or opt-outs, do-not-contact entries, destination verification, quiet hours, and fallback policy.
- More restrictive applicable rules win unless a documented essential-communication exception permits a narrow override.
- The result lists allowed channels in order, suppressed channels with reason codes, and the governing versioned facts.
- Missing or contradictory preferences route to a safe default or review state, never silent broad consent.
- Changes apply prospectively by effective time and do not rewrite prior delivery decisions.
- Proxy preferences require authority scope and remain distinguishable from the patient's own choices.
- Communication services store the resolution decision ID used for each attempt.

## Frappe realization

- **DocTypes:** `OC Notification Preference`, `OC Channel Consent`, and `OC Preference Resolution` hold patient, purpose, channel, effective interval, source, authority, outcome, and explanation.
- **API:** `open_chart.api.v1.messaging.resolve_preferences` is read-only and deterministic for supplied event time.
- **Permissions:** patients or proxies manage permitted choices through portal pages; Communications Privacy Manager handles restricted overrides.
- **Hooks:** patient/contact changes invalidate future cached resolutions; accepted preference history uses succession-based amendments.
- **Surfaces:** channel matrix form, effective-history view, and suppression-reason Query Report.

## Boundaries

Owns: preference and consent resolution evidence. Consumes: patient choices, proxy authority, destination status, purpose, and organizational policy. Emits: allowed channels and suppression reasons. Does not own: actual send or legal policy authorship.

## Open questions

- Which essential communications may override a channel opt-out, and who approves that policy?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Do-not-contact Registry Enforcement](openchart-feature-catalog-msg-038-do-not-contact-registry-enforcement.md)
