# Synthesis: Internationalization Accessibility And UX Platform — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects validated localization, accessible interaction, adaptive presentation, efficient navigation, resilient forms, and consented UX learning into one Frappe-native experience platform.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Internationalization Accessibility And Clinician UX Platform domain synthesis
Captured: 2026-08-24

## Possible feats

- **Release experience readiness gate** — Combine language, accessibility, theme, guidance, and resilience evidence into a human-reviewed declaration for each supported release profile.

## Focus

This synthesis relates the 30 Internationalization Accessibility And Clinician UX Platform capabilities and identifies the shared preference, translation, theme, permission, and evidence seams that make them coherent.

## Members and their joints

### Language, culture, and interpreted communication

- [Clinical Language Pack Governance](openchart-feature-catalog-iax-001-clinical-language-pack-governance.md) makes language support a release-specific evidence claim instead of a raw string count.
- [In-context Translation Editor](openchart-feature-catalog-iax-002-in-context-translation-editor.md) captures contextual proposals that return to governed packs rather than mutating live text.
- [Right-to-left Layout Support](openchart-feature-catalog-iax-003-rtl-layout-support.md) and [Locale-aware Formatting](openchart-feature-catalog-iax-004-locale-aware-formatting.md) adapt direction and representation while preserving canonical values.
- [Patient Language Preference Rendering](openchart-feature-catalog-iax-005-patient-language-preference-rendering.md), [Encounter Interpreter Workflow Flags](openchart-feature-catalog-iax-006-encounter-interpreter-workflow-flags.md), and [Translated Patient Instructions Library](openchart-feature-catalog-iax-007-translated-patient-instructions-library.md) carry language need from preference through encounter coordination to reviewed content delivery.

The joint is explicit provenance: the Frappe translation system localizes interface chrome, versioned DocTypes govern clinical content translations, and every fallback identifies the language actually shown. This is the honest differentiator over broad but uneven language counts: support is declared only when the exact release, content, layout, and clinical terminology have passed their applicable gates.

### Accessible interaction and perceivable state

- [Screen-reader Component Conformance](openchart-feature-catalog-iax-008-screen-reader-component-conformance.md) establishes semantic contracts for shared controls.
- [Keyboard-only Navigation Completeness](openchart-feature-catalog-iax-009-keyboard-only-navigation-completeness.md) verifies complete workflows, while [Visible Focus And Skip Navigation](openchart-feature-catalog-iax-010-visible-focus-and-skip-navigation.md) keeps location and bypass paths perceivable.
- [Color-independent Clinical Statuses](openchart-feature-catalog-iax-011-color-independent-clinical-statuses.md) separates meaning from color.
- [Scalable Type And High-contrast Mode](openchart-feature-catalog-iax-012-scalable-type-and-high-contrast-mode.md), [Reduced-motion Preference](openchart-feature-catalog-iax-013-reduced-motion-preference.md), and [Dyslexia-friendly Reading Mode](openchart-feature-catalog-iax-014-dyslexia-friendly-reading-mode.md) adapt presentation without rewriting source content.

The joint is component evidence against a WCAG 2.2 AA target: semantic markup, keyboard behavior, focus, text, contrast, motion, and status alternatives travel together through reusable Desk and portal components. Automated checks catch regressions, while release claims still depend on manual assistive-technology and workflow testing.

### Presentation, devices, and preference resolution

- [Shared-device Touch-target Standards](openchart-feature-catalog-iax-015-shared-device-touch-target-standards.md) protects coarse-pointer and shared-tablet interaction.
- [Clinician Density Toggle](openchart-feature-catalog-iax-016-clinician-density-toggle.md) and [Dark Mode](openchart-feature-catalog-iax-017-dark-mode.md) adapt high-volume clinical views without changing available information.
- [Synchronized User Interface Preferences](openchart-feature-catalog-iax-018-synchronized-user-interface-preferences.md) supplies the typed precedence and synchronization spine used by language, scale, contrast, motion, typography, touch, density, and appearance modes.

The joint is first-render consistency: mandatory accessibility behavior, Frappe user preferences, role or surface defaults, site policy, browser signals, and safe fallbacks resolve server-side into bootinfo. Website Theme governs portal presentation, Desk themes govern authenticated workspaces, and shared semantic tokens keep both surfaces aligned without forcing patient and clinician defaults to be identical.

### Navigation and documentation productivity

- [Context-aware Smart Defaults](openchart-feature-catalog-iax-019-context-aware-smart-defaults.md) reduces repetitive entry while keeping prefill visible and attributable.
- [Universal Search Command Palette](openchart-feature-catalog-iax-020-universal-search-command-palette.md) unifies permission-safe discovery across records, routes, reports, actions, and help.
- [Recent And Pinned Navigation](openchart-feature-catalog-iax-021-recent-and-pinned-navigation.md) provides bounded context switching without making history a disclosure channel.
- [Clinical Key-phrase Expander](openchart-feature-catalog-iax-022-clinical-key-phrase-expander.md) inserts exact clinician-reviewed text under explicit activation and placeholder checks.

The joint is assistive acceleration rather than hidden automation: defaults, search, recents, pins, and phrases reduce interaction cost, but every consequential operation returns to ordinary permission, review, confirmation, and submission paths. Personalization changes how work is reached or proposed, never who may act or what becomes clinically accepted.

### Safe action, resilience, and continuity

- [Form Autosave And Recovery](openchart-feature-catalog-iax-023-form-autosave-and-recovery.md) preserves in-progress work without confusing drafts with accepted records.
- [Tiered Confirmation And Undo](openchart-feature-catalog-iax-024-tiered-confirmation-and-undo.md) matches safeguards and compensations to consequence.
- [Actionable Error Message Standard](openchart-feature-catalog-iax-025-actionable-error-message-standard.md) turns typed failures into localized recovery guidance.
- [Loading Offline And Stale-state Signals](openchart-feature-catalog-iax-026-loading-offline-and-stale-state-signals.md) makes data freshness and connectivity explicit.
- [Secure Session Context Resume](openchart-feature-catalog-iax-027-secure-session-context-resume.md) restores only reauthorized route and draft context after timeout.

The joint is truthful state: autosave, loaders, banners, errors, confirmation, undo, and resume all distinguish proposed, pending, cached, stale, failed, compensated, and accepted outcomes. Correlation IDs and optimistic versions connect the visible state to guarded server operations without allowing a smooth interface to overstate certainty.

### Guidance and evidence-led improvement

- [Role-based Guided Tours](openchart-feature-catalog-iax-028-role-based-guided-tours.md) provides optional, versioned workflow orientation.
- [Contextual Tooltip Documentation](openchart-feature-catalog-iax-029-contextual-tooltip-documentation.md) connects concise accessible help to maintained documentation while keeping essential instructions visible.
- [Opt-in Usability Telemetry](openchart-feature-catalog-iax-030-opt-in-usability-telemetry.md) turns minimized, consented friction signals into human-reviewed backlog evidence.

The joint is a governed learning loop: maintainers teach through stable component targets, detect stale guidance when those targets change, observe only approved non-content outcomes, and prioritize repairs alongside accessibility defects and support evidence. The platform uses telemetry to improve usability, not to score clinicians or surveil clinical behavior.

## Frappe realization

- **Localization:** Frappe translation catalogs and `__()` remain authoritative for interface strings; OC-prefixed release, proposal, review, patient-content, and delivery DocTypes add clinical validation, versioning, and provenance where generic translations are insufficient.
- **Themes and components:** Website Theme governs portal tokens and shared templates; Desk themes govern authenticated workspaces; logical CSS, semantic status renderers, focus utilities, reduced-motion rules, and accessible controls form one conformance-tested component layer.
- **Preferences and bootinfo:** Frappe user preferences store approved personal settings, `OC UX Preference Policy` constrains types and precedence, and boot hooks place effective locale, direction, theme, accessibility, density, shortcut, tour, and telemetry capabilities in bootinfo before first render.
- **Workflow and roles:** Frappe Workflows govern publication and review; Localization Manager, Clinical Translation Reviewer, Accessibility Tester, UX Maintainer, UX Educator, UX Documentation Maintainer, Clinical Safety Reviewer, and Audit Reviewer roles use DocPerms, User Permissions, and permlevels 0-2.
- **API and state:** Guarded `open_chart.api.v1.ux` whitelisted methods are the supported mutation surface for preferences, translations, drafts, navigation, safeguards, resume, and telemetry; typed errors, idempotency keys, correlation IDs, and optimistic versions prevent ambiguous outcomes.
- **Surfaces and evidence:** Desk workspaces, portal pages, Web Forms, Query/Script Reports, Dashboard Charts, Print Formats, Notification Log, RQ jobs, scheduler events, and websocket events expose current state while retaining release and audit evidence.

## Boundaries

Owns: localization evidence, interface accessibility contracts, presentation preferences, navigation aids, interaction safeguards, recoverable UI state, contextual guidance, and minimized usability evidence. Consumes: patient and user identity, permissions, consent, clinical content authority, Frappe metadata, browser/device signals, and domain outcomes. Emits: validated presentations, explicit interaction states, recoverable drafts, support evidence, and human-reviewed UX backlog candidates. Does not own: clinical decisions, record authority, authentication policy, interpreter fulfillment, training competency, source documentation, device management, or autonomous clinical action.

## Emergent behavior

Together, these features create a release-evidenced experience system rather than a collection of cosmetic settings. A user's effective locale, direction, accessibility modes, theme, density, and shortcuts arrive through one preference spine; shared components then apply those choices consistently to translated, permission-safe content. When work becomes slow or interrupted, honest loading, autosave, errors, confirmations, and resume behavior preserve trust. Guided help and minimized telemetry close the loop by showing maintainers where real workflows remain difficult, making the platform capable of pursuing a usability level materially above the documented OpenEMR SUS 55 benchmark without hiding uncertainty behind language-count or conformance claims.

## Tensions to hold

- Dense clinician workflows need speed, but compactness and shortcuts cannot reduce target size, focus clarity, semantics, or confirmation for consequential actions.
- Broad language availability improves access, but only release-specific clinical validation supports an honest claim of safe coverage.
- Personalization improves comfort and efficiency, while mandatory accessibility and safety behavior must remain non-negotiable.
- Helpful recency, telemetry, draft recovery, and session context can reduce friction, but each can become a privacy risk if identifiers or content exceed minimum necessity.
- Automated accessibility checks provide scale, while manual assistive-technology and end-to-end workflow testing remain necessary.
- Offline and cached views can improve continuity, but visible freshness and restricted mutation must prevent stale data from appearing authoritative.

## Recombination opportunities

- Combine language-pack deltas, translated-instruction staleness, RTL tests, and patient fallback events into a release localization readiness board.
- Combine component conformance, keyboard workflow certification, theme matrices, and focus-path evidence into a WCAG 2.2 AA-oriented release gate.
- Combine smart-default change rates, undo events, recoverable drafts, typed errors, and opt-in telemetry to identify high-friction forms without collecting clinical content.
- Combine bootinfo-resolved preferences, dark and high-contrast themes, density, touch mode, and reduced motion into tested device-and-role experience profiles.
- Combine contextual help gaps, stale tours, support correlation IDs, and accessibility defects into a human-owned UX backlog tied to exact releases.

## Open questions

- Which language and assistive-technology combinations can openChart realistically declare supported for each release, and what evidence is mandatory?
- Which preference and recovery records may be synchronized across sites without creating privacy or policy conflicts?
- Who owns final release authority when localization, accessibility, clinical safety, and operational usability evidence disagree?
- What standardized synthetic workflows best measure progress beyond the OpenEMR SUS 55 usability bar without overfitting to one role or facility?
- Which interface events are sufficiently non-sensitive and useful to justify opt-in telemetry collection?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
