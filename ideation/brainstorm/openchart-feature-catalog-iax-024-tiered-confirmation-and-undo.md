# Tiered Confirmation And Undo — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Matches confirmation strength and reversible undo behavior to action consequence so routine work stays fast and destructive work stays deliberate.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, safe-actions
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-024 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Action consequence registry** — Review destructive, reversible, clinical, privacy, and bulk actions for consistent safeguards.

## Focus

This feature isolates interaction safeguards around consequential actions without replacing domain-specific authorization or amendment rules.

## Behavior

- Each governed action is classified as routine, reversible, destructive, clinically consequential, privacy-sensitive, or high-volume.
- Routine actions avoid needless dialogs; reversible actions complete with a timed, accessible undo option where rollback is truthful.
- Destructive actions require a clear object-specific confirmation, while the highest tier may require typed text, reason, or second authority.
- Confirmation names the target, scope, consequence, reversibility, and affected count before acceptance.
- Undo creates a compensating server action and reports partial or expired rollback rather than pretending history was erased.
- Keyboard, screen-reader, touch, and translated presentations expose equivalent safeguards and default focus to the safe choice.
- Duplicate submissions use idempotency keys and return the original outcome.

## Frappe realization

- **DocTypes:** `OC Action Safeguard Policy` stores method/action key, consequence tier, confirmation template key, undo window, roles, and effective version.
- **API:** A shared guard wraps whitelisted mutation methods, issues short-lived confirmation tokens, enforces idempotency, and calls explicit compensating methods.
- **Surfaces:** Frappe dialogs, list bulk actions, portal controls, and Notification Log links use one accessible confirmation and undo component.
- **Evidence:** `OC Safeguarded Action Event` records actor, target Dynamic Link, policy version, reason, correlation ID, outcome, and compensation link.

## Boundaries

Owns: interaction-tier policy, confirmation tokens, undo coordination, and evidence. Consumes: action consequence, target summary, permissions, and domain compensation support. Emits: confirmed actions or explicit compensations. Does not own: domain authorization, legal deletion, or clinical amendment semantics.

## Open questions

- Which actions warrant second-person approval rather than stronger single-user confirmation?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Actionable Error Message Standard](openchart-feature-catalog-iax-025-actionable-error-message-standard.md)
