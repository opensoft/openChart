# Restricted Order Privileges — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces provider credentialing limits for restricted orderables such as chemotherapy, controlled substances, and high-risk procedures.
Topics: openchart-feature-catalog, cpoe, frappe, restricted-ordering
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-031 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Privilege impact preview** — Show credential prerequisites before a provider invests in composing a restricted order.

## Focus

This feature isolates authorization checks tied to provider credentials and order risk.

## Behavior

- Restricted orderables declare required privilege codes, care settings, facilities, and optional patient-age constraints.
- Search results show restricted status without exposing confidential credential details.
- The server rechecks current privileges at draft creation and signature.
- Missing, suspended, out-of-scope, or expired privileges block submission and identify a remediation route.
- Emergency override is unavailable unless explicitly governed as a separate permissioned action.
- Every allow or deny decision records policy and credential references for audit.

## Frappe realization

- **DocTypes:** `OC Ordering Privilege` with provider, code, scope, facility, effective dates, status, issuer, and provenance; `OC Orderable Restriction` maps requirements.
- **Workflow:** privilege Proposed → Verified → Active → Suspended/Expired/Revoked.
- **Roles/permissions:** `OC Credentialing Officer` governs privileges; providers read their own effective summary; clinical users cannot edit credential data.
- **Hooks/API/surface:** server permission service runs in `validate` and `on_submit`; guarded search and submit APIs return stable denial codes without bypass paths.

## Boundaries

Owns: order-specific privilege enforcement. Consumes: credential records and order restrictions. Emits: allow or deny evidence. Does not own: credentialing source processes.

## Open questions

- How should external credentialing systems attest changes into openChart?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Credential Expiry Ordering Guard](openchart-feature-catalog-ord-032-credential-expiry-ordering-guard.md)
