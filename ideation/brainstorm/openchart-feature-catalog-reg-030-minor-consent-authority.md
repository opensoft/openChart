# Minor Consent Authority — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Resolves who may consent for a minor for a specific purpose, service context, and time using verified authority records and policy.
Topics: openchart-feature-catalog, registration, frappe, minor-consent
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-030 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Contextual assent prompts** — Pair authority resolution with age-appropriate patient assent capture where policy requires it.

## Focus

Provide a registration-time authority determination for minor consent without encoding legal conclusions as simple age rules.

## Behavior

- Staff select the requested consent purpose and service context before resolving authority.
- The system presents active guardian, custody, self-consent, and exception records applicable to the date.
- Conflicting or missing authority returns Needs Review rather than choosing a person automatically.
- Authorized reviewers record determination, policy reference, evidence, and expiry.
- The result distinguishes consent authority from records access and financial responsibility.
- Every consumer receives the purpose-scoped decision and must not reuse it for another purpose.

## Frappe realization

- **DocTypes:** `OC Minor Consent Determination` with patient, purpose, service_context, authority link, policy_reference, outcome, and validity.
- **Workflow:** Requested → Review → Authorized, Not Authorized, Exception, or More Information Needed.
- **Roles/permissions:** `OC Registration Clerk` requests; `OC Authority Reviewer` decides; `OC Privacy Officer` handles restricted contexts.
- **API/surfaces:** `open_chart.api.v1.registration.resolve_minor_consent_authority`; registration decision dialog and unresolved-authority worklist.

## Boundaries

Owns: purpose-specific minor consent-authority determination. Consumes: authority records, age, context, and policy. Emits: dated decision. Does not own: consent document content or legal advice.

## Open questions

- How should site policy encode jurisdiction-specific minor self-consent without becoming an unreviewed rules engine?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
