# Synthesis: Registration Identity And Demographics — Brainstorm

Status: brainstorm
Kind: reference
Summary: Combines registration identity, demographics, relationships, coverage, privacy, consent, intake, and lifecycle controls into an auditable patient-entry foundation.
Topics: openchart-feature-catalog, registration, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; catalog entry REG synthesis (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Registration operations program** — Deliver a policy-configured, multi-channel registration service with explainable readiness and exception queues.

## Focus

Relate the REG capabilities as a Frappe-native identity and registration graph whose accepted writes remain API-guarded, provenance-rich, and human-controlled.

## Members and their joints

### Identity foundation and resolution

[Guided Patient Registration Intake](openchart-feature-catalog-reg-001-guided-patient-registration-intake.md), [Legal and Preferred Name Capture](openchart-feature-catalog-reg-002-legal-and-preferred-name-capture.md), [Alias and Prior Name History](openchart-feature-catalog-reg-003-alias-and-prior-name-history.md), [Core Demographic Profile](openchart-feature-catalog-reg-004-core-demographic-profile.md), [Patient Identity Verification Workflow](openchart-feature-catalog-reg-005-patient-identity-verification-workflow.md), [Duplicate Patient Candidate Detection](openchart-feature-catalog-reg-006-duplicate-patient-candidate-detection.md), and [Patient Record Merge Adjudication](openchart-feature-catalog-reg-007-patient-record-merge-adjudication.md) turn assertions into a reviewable patient identity. Intake composes facts, verification qualifies them, and duplicate handling blocks silent fragmentation or consolidation.

### Contact, preference, and special status

[Multiple Patient Addresses](openchart-feature-catalog-reg-008-multiple-patient-addresses.md), [Address Standardization and Validation](openchart-feature-catalog-reg-009-address-standardization-and-validation.md), [Patient Contact Point Registry](openchart-feature-catalog-reg-010-patient-contact-point-registry.md), [Communication Channel Preferences](openchart-feature-catalog-reg-011-communication-channel-preferences.md), [Emergency Contact Management](openchart-feature-catalog-reg-012-emergency-contact-management.md), [Employer Information Capture](openchart-feature-catalog-reg-013-employer-information-capture.md), [Guarantor Relationship Management](openchart-feature-catalog-reg-014-guarantor-relationship-management.md), [Preferred Pharmacy Selection](openchart-feature-catalog-reg-015-preferred-pharmacy-selection.md), and [Preferred Provider Assignment](openchart-feature-catalog-reg-016-preferred-provider-assignment.md) separate factual endpoints and relationships from permission, consent, and operational choices. [Deceased Patient Handling](openchart-feature-catalog-reg-017-deceased-patient-handling.md), [VIP Patient Privacy Flag](openchart-feature-catalog-reg-018-vip-patient-privacy-flag.md), and [Confidential Chart Flag](openchart-feature-catalog-reg-019-confidential-chart-flag.md) then alter safe use and discovery without erasing the identity.

### Evidence and coverage

[Patient Photo Capture](openchart-feature-catalog-reg-020-patient-photo-capture.md), [Government ID Image Capture](openchart-feature-catalog-reg-021-government-id-image-capture.md), and [Government ID OCR Extraction](openchart-feature-catalog-reg-022-government-id-ocr-extraction.md) keep evidence custody, extraction, and verification as separate authority steps. [Insurance Coverage Intake](openchart-feature-catalog-reg-023-insurance-coverage-intake.md), [Insurance Card Image Capture](openchart-feature-catalog-reg-024-insurance-card-image-capture.md), [Insurance Card OCR Extraction](openchart-feature-catalog-reg-025-insurance-card-ocr-extraction.md), [Subscriber and Policy Management](openchart-feature-catalog-reg-026-subscriber-and-policy-management.md), and [Coverage Review Worklist](openchart-feature-catalog-reg-027-coverage-review-worklist.md) create a reliable registration snapshot without pulling eligibility, claims, or balances into openChart.

### Relationships, authority, and assignment

[Related Person Registry](openchart-feature-catalog-reg-028-related-person-registry.md), [Guardian and Custody Authority](openchart-feature-catalog-reg-029-guardian-and-custody-authority.md), and [Minor Consent Authority](openchart-feature-catalog-reg-030-minor-consent-authority.md) progress from descriptive kinship to evidence-backed and purpose-specific authority. [Care Team Assignment](openchart-feature-catalog-reg-031-care-team-assignment.md) and [Patient Group Membership](openchart-feature-catalog-reg-032-patient-group-membership.md) add accountable operational relationships while refusing to infer consent or clinical action from membership alone.

### Inclusive demographics and identifiers

[Race and Ethnicity Capture](openchart-feature-catalog-reg-033-race-and-ethnicity-capture.md), [Preferred Language Capture](openchart-feature-catalog-reg-034-preferred-language-capture.md), [Interpreter Needs and Accommodation](openchart-feature-catalog-reg-035-interpreter-needs-and-accommodation.md), [Sex Assigned at Birth Capture](openchart-feature-catalog-reg-036-sex-assigned-at-birth-capture.md), and [Gender Identity and Pronoun Capture](openchart-feature-catalog-reg-037-gender-identity-and-pronoun-capture.md) preserve self-description, unknown states, purpose, and disclosure controls. [External Identifier Registry](openchart-feature-catalog-reg-038-external-identifier-registry.md), [Outside MRN Linkage and Validation](openchart-feature-catalog-reg-039-outside-mrn-linkage-and-validation.md), and [Global Patient Search](openchart-feature-catalog-reg-040-global-patient-search.md) make those facts discoverable through authority-qualified, privacy-aware matching rather than unrestricted lookup.

### Access channels and identity operations

[Registration Worklists](openchart-feature-catalog-reg-041-registration-worklists.md), [Self Registration Web Form](openchart-feature-catalog-reg-042-self-registration-web-form.md), and [Kiosk Registration Flow](openchart-feature-catalog-reg-043-kiosk-registration-flow.md) accept work through staff, remote, and shared-device channels but converge on review rather than direct mutation. [Patient Merge Audit Trail](openchart-feature-catalog-reg-044-patient-merge-audit-trail.md), [Chart Transfer Between Facilities](openchart-feature-catalog-reg-045-chart-transfer-between-facilities.md), and [MRN Naming Series Policy](openchart-feature-catalog-reg-046-mrn-naming-series-policy.md) preserve traceability and authority across consolidation, facility boundaries, and local number issuance.

### Transitions, acknowledgments, and readiness

[Minor to Adult Status Transition](openchart-feature-catalog-reg-047-minor-to-adult-status-transition.md) coordinates relationship changes over time, while [Social Needs Screening at Registration](openchart-feature-catalog-reg-048-social-needs-screening-at-registration.md), [Consent to Treat Capture](openchart-feature-catalog-reg-049-consent-to-treat-capture.md), [HIPAA Notice Acknowledgment](openchart-feature-catalog-reg-050-hipaa-notice-acknowledgment.md), and [Advance Beneficiary Notice Capture](openchart-feature-catalog-reg-051-advance-beneficiary-notice-capture.md) preserve distinct purposes and decisions. [Arrival Hooks into Scheduling](openchart-feature-catalog-reg-052-arrival-hooks-into-scheduling.md), [Demographic Change Request](openchart-feature-catalog-reg-053-demographic-change-request.md), [Demographic Change Approval](openchart-feature-catalog-reg-054-demographic-change-approval.md), and [Registration Completion Quality Gate](openchart-feature-catalog-reg-055-registration-completion-quality-gate.md) close the loop through idempotent handoffs, governed succession, and explainable readiness.

## Frappe realization

- **DocTypes:** `OC Patient` anchors modular OC-prefixed identity, evidence, relationship, coverage, consent, work-item, and event DocTypes; child tables carry repeatable facts without flattening authority.
- **Workflow:** channel drafts converge on review; accepted records use succession rather than in-place amendment; merge, transfer, privacy, and identity-critical changes require independent Workflow Actions.
- **Roles/permissions:** `OC Registration Clerk`, `OC Registration Supervisor`, `OC Identity Reviewer`, `OC Authority Reviewer`, `OC Coverage Reviewer`, `OC Privacy Officer`, `OC Auditor`, and narrow integration roles combine Role Permissions, User Permissions, and permlevels 0-2.
- **API/surfaces:** guarded `open_chart.api.v1.registration` methods are the supported write surface; Desk workspaces, portal and kiosk pages, worklists, Query/Script Reports, print formats, and background jobs remain permission-aware.

## Emergent behavior

Together these features make registration a durable identity-control plane: every channel produces provenance, every high-risk conclusion remains human-owned, every accepted change is traceable, and downstream systems consume purpose-qualified snapshots instead of reaching into mutable forms.

## Tensions to hold

Patient convenience competes with evidence and review latency; broad search competes with confidentiality; reusable relationships compete with purpose-specific authority; and multi-site independence competes with seamless chart transfer. The design should preserve these tensions explicitly rather than solve them through hidden defaults or unrestricted shared data.

## Recombination opportunities

The readiness gate can combine with arrival events and worklists for explainable check-in; identity evidence can combine with external identifiers for exchange matching; and language, communication, privacy, and authority records can compose a safe patient-facing access profile without becoming one undifferentiated consent flag.

## Boundaries

Owns: registration identity, demographic, relationship, evidence, consent, and readiness controls. Consumes: site policy, facility directories, approved forms, and scheduling references. Emits: permission-aware patient identity facts, events, and audit records. Does not own: clinical decisions, autonomous actions, scheduling state, billing, claims, or revenue cycle.

## Open questions

- Which policy decisions belong in shared app fixtures versus per-site configuration?
- Which accepted identity facts need cryptographic evidence sealing in the first implementation?
- What minimum cross-site contract preserves independent clinic tenancy while supporting safe transfer?

## Relationships

[Catalog anchor](openchart-feature-catalog-synthesis-reg.md)
