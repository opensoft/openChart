# Secure Session Context Resume — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Restores safe navigation and recoverable draft context after timeout only after reauthentication and fresh authorization checks.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, session-resume
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-027 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Private timeout handoff screen** — Show a neutral reauthentication surface that conceals patient identity and task details on shared displays.

## Focus

This feature isolates post-timeout context restoration from authentication, draft storage, and clinical record acceptance.

## Behavior

- Before timeout, the client stores a minimal resumable context token containing route and eligible draft references, not rendered patient data.
- The timeout screen immediately conceals protected content and requires normal reauthentication.
- After successful authentication, the server rechecks user identity, role, patient access, route permission, and draft ownership.
- Valid context offers Resume, Start Fresh, or Review Draft choices and explains any elements that cannot be restored.
- Revoked access, changed records, expired drafts, or a different authenticated user prevent restoration without disclosing prior context.
- Resuming a form invokes version-aware draft comparison and never auto-submits or replays consequential actions.
- Resume tokens are short-lived, single-use, device-bound where supported, and audited without storing PHI in browser history.

## Frappe realization

- **DocTypes:** `OC Session Resume Token` stores hashed token, user, session/device reference, encrypted route context, draft links, expiry, state, and correlation ID.
- **Hooks:** Login and session-expiry hooks issue, consume, and revoke tokens; Frappe session authentication remains authoritative.
- **API:** `open_chart.api.v1.ux.session_resume` validates single use and reauthorizes every target before returning minimum-necessary restore options.
- **Surfaces:** A Website Theme-compatible neutral timeout page and Desk resume dialog restore focus and link to `OC Form Recovery Draft` comparisons.

## Boundaries

Owns: minimal resume tokens, post-auth context checks, and restoration choices. Consumes: Frappe session outcome, current permissions, route, and draft references. Emits: safe navigation or recovery handoff. Does not own: authentication policy, session duration, or draft contents.

## Open questions

- Which routes are too sensitive to retain even as encrypted resume context?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Form Autosave And Recovery](openchart-feature-catalog-iax-023-form-autosave-and-recovery.md)
