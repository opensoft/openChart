# Session Timeout and Reauthentication — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Ends or reauthenticates idle and absolute-time-limit sessions according to role, risk, device, and care setting.
Topics: openchart-feature-catalog, security, frappe, session-timeout
Repository context: openChart — Frappe v15 native EMR; catalog entry SEC-011 (Security Privacy Audit And Access Control)
Captured: 2026-08-24

## Possible feats

- **Context-aware timeout warnings** — Extend this capability with governed evidence, simulation, or automation while retaining human review.

## Focus

This entry isolates session timeout and reauthentication as one hardened-by-default capability. It favors explicit authorization and reviewable evidence over permissive fallback behavior.

## Behavior

- **Actor:** Security Administrators and End Users initiate or review the workflow according to assigned authority.
- **Inputs:** The decision consumes role, idle timeout, absolute lifetime, warning period, context, and reauthentication method.
- **Decision:** The service evaluates the request server-side before disclosing data or committing a protected change.
- **States:** The governed lifecycle is Draft → Active → Superseded; each transition records actor, timestamp, purpose, and rationale.
- **Success:** The workflow produces predictable session expiry with safe preservation of unsaved work metadata and returns a stable reference plus decision reason.
- **Permission:** Absence of an explicit role, user permission, purpose, or current scope denies the action; UI hiding is never treated as enforcement.
- **Edge case:** offline, shared-workstation, and active emergency workflows receive bounded grace without indefinite access.
- **Error path:** Stale versions, malformed scope, unavailable dependencies, or conflicting policy reject atomically and create no partial authorization.
- **Audit:** Allowed, denied, failed, overridden, exported, and administrative events emit minimum-necessary audit evidence without copying secrets or clinical payloads.

## Frappe realization

- **DocTypes:** Create `OC Session Policy` with naming series `OC-SEC-.YYYY.-.#####`, policy/version links, scope fields, effective dates, state, decision rationale, evidence references, and immutable provenance fields.
- **Workflow:** Use a Frappe Workflow for `Draft → Active → Superseded` with explicit reviewer actions; accepted clinical or privacy records use succession-based amendments instead of in-place rewriting.
- **Roles and permissions:** Configure `OC Security Administrator`, `OC Privacy Officer`, `OC Security Auditor`, and feature operators through Role Permission Manager; enforce patient, provider, facility, and site user permissions; reserve sensitive rationale and evidence at permlevels 1–2.
- **Hooks and audit:** Register `hooks.py` `doc_events` handlers for `validate`, `before_save`, `on_update`, `on_submit`, and `after_insert` as applicable; they fail closed on bypass and append `OC Audit Event` records for the audit trail. Read and export wrappers also record view outcomes because Frappe `doc_events` do not observe reads.
- **API:** Expose guarded whitelisted methods under `open_chart.api.v1.security` for evaluation and transitions; allow `/api/resource/OC%20Session%20Policy` reads only where server-side permission queries apply, and reject unsupported direct writes.
- **Surfaces:** Add a Security and Privacy Desk workspace list plus a permission-aware Query or Script Report, assignments and Notifications for due review, and dashboard counts that never reveal restricted patient identity.

## Boundaries

Owns: the policy record, decision state, and feature-specific evidence. Consumes: authenticated identity, roles, user permissions, patient and facility context, consent, and trusted time. Emits: decision reason, assignments or alerts, and append-only audit events. Does not own: the underlying clinical record, external identity provider, cryptographic key material, legal interpretation, or autonomous clinical action.

## Open questions

- Which clinical workflows justify a grace period after the idle threshold?

## Relationships

[Synthesis: Security Privacy Audit And Access Control](openchart-feature-catalog-synthesis-sec.md)
