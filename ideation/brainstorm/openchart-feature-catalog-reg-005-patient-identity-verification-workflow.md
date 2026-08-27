# Patient Identity Verification Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records evidence-based identity assurance decisions so registration can distinguish asserted, provisionally matched, and verified patients.
Topics: openchart-feature-catalog, registration, frappe, identity-verification
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-005 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Configurable assurance profiles** — Apply different evidence requirements to telehealth, portal, and in-person registration.

## Focus

Provide a human-controlled verification workflow with explicit evidence and assurance outcomes.

## Behavior

- Registration Clerk starts verification against a selected patient or intake.
- The checklist records evidence type, issuing authority, inspection method, and result without storing unnecessary secrets.
- Verification may resolve as Unverified, Provisional, Verified, or Unable to Verify.
- Mismatched evidence blocks automatic acceptance and creates an identity-review assignment.
- Supervisors can override a failed check only with reason, policy basis, and expiry when applicable.
- Downstream surfaces display the assurance state and last verified date without exposing evidence images broadly.

## Frappe realization

- **DocTypes:** `OC Identity Verification` with assurance_level, evidence rows, result, reason, verifier, and expires_on.
- **Workflow:** Draft → In Review → Verified, Provisional, or Failed; Failed may transition to Supervisor Override.
- **Roles/permissions:** `OC Registration Clerk` submits; `OC Identity Reviewer` decides; evidence metadata and files use permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.submit_identity_verification`; verification dialog, review queue, and patient identity badge.

## Boundaries

Owns: identity assurance decision and evidence metadata. Consumes: patient facts and presented evidence. Emits: assurance state and review events. Does not own: authentication credentials or payer eligibility.

## Open questions

- How long should each evidence type remain valid before reverification?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
