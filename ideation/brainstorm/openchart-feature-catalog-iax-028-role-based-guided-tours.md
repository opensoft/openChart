# Role-based Guided Tours — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Delivers versioned, optional onboarding tours by role and workflow without obstructing clinical work or exposing inaccessible steps.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, guided-tours
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-028 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Sandbox practice task** — Pair tours with synthetic records so users can rehearse a workflow without touching live charts.

## Focus

This feature isolates contextual onboarding sequences from mandatory competency, policy attestation, and reference documentation.

## Behavior

- UX educators publish tours for an exact role, route, workflow version, locale, and optional experience level.
- Eligible users may start, pause, skip, resume, replay, or permanently dismiss an optional tour.
- Each step identifies a stable target, explains one task concept, and offers keyboard and screen-reader controls.
- If a target is hidden by permission or feature configuration, the tour skips safely or stops with a useful explanation.
- Tours never simulate submission, trigger clinical actions, or place overlays above urgent alerts.
- Product changes mark affected tours Needs Review rather than showing stale instructions.
- Completion records support status only and are not represented as clinical competency or compliance attestation.

## Frappe realization

- **DocTypes:** `OC Guided Tour` stores role, route, release, locale, state, and ordered `OC Guided Tour Step` rows with target keys and translation keys.
- **Workflow and roles:** UX Educator drafts, UX Reviewer approves, and Localization Reviewer validates locale variants through Frappe Workflow.
- **Bootinfo and preferences:** Eligible tour summaries and user completion/dismissal preferences load through bootinfo without exposing unauthorized steps.
- **Surfaces:** A shared Desk/portal tour component uses Website Theme tokens, stable component anchors, focus control, and reduced-motion behavior.

## Boundaries

Owns: optional tour content, eligibility, progress, and version review. Consumes: role, route, locale, feature flags, and component anchors. Emits: onboarding overlays and support completion status. Does not own: training certification, competency, or clinical action.

## Open questions

- Which workflow changes should automatically invalidate an existing tour version?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Contextual Tooltip Documentation](openchart-feature-catalog-iax-029-contextual-tooltip-documentation.md)
