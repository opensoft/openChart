# Screen-reader Component Conformance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs a shared component library against WCAG 2.2 AA-oriented screen-reader contracts and repeatable assistive-technology tests.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, screen-reader-conformance
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-008 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Component accessibility scorecard** — Publish supported browser and assistive-technology combinations with known limitations.

## Focus

This feature isolates reusable semantic and announcement behavior for shared clinical interface components.

## Behavior

- Component maintainers define accessible name, role, value, state, error, and live-region behavior for each reusable control.
- Clinicians and patients receive equivalent labels, instructions, validation, status changes, and table relationships nonvisually.
- Modal dialogs trap focus only while open, announce their purpose, and return focus to the invoking control on close.
- Dynamic clinical alerts announce once at the appropriate urgency and remain available for later review.
- Automated checks run on every component change, while manual screen-reader scripts gate declared support releases.
- Components with unresolved critical failures cannot be promoted to the supported library.
- Conformance records identify browser, operating system, assistive technology, version, tester, and synthetic scenario.

## Frappe realization

- **DocTypes:** `OC Accessibility Conformance Case` stores component, criterion, test steps, environment, result, evidence, and release; `OC Accessibility Defect` tracks remediation.
- **Surfaces:** Shared Desk controls, Web Forms, portal components, dialogs, grids, and Website Theme patterns consume semantic templates rather than page-specific ARIA patches.
- **Hooks and tests:** Build hooks run static accessibility checks; synthetic browser suites exercise Frappe routes and store release evidence through a guarded import method.
- **Roles and reports:** Accessibility Tester and UX Maintainer roles manage cases; a Script Report blocks support declarations when critical cases fail.

## Boundaries

Owns: component-level semantic contracts and conformance evidence. Consumes: supported environment matrix and synthetic workflows. Emits: approved components and defects. Does not own: individual assistive technologies or guarantee conformance of untested custom pages.

## Open questions

- Which screen-reader and browser combinations form the minimum release gate for Desk and portal separately?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Keyboard-only Navigation Completeness](openchart-feature-catalog-iax-009-keyboard-only-navigation-completeness.md)
