# Provider Master Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs provider identities, affiliations, specialties, and operational status independently of login accounts.
Topics: openchart-feature-catalog, platform, frappe, provider-master
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-004 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Provider directory projection** — Publish approved public fields without exposing internal affiliations or identifiers.

## Focus

This feature isolates the provider master used for attribution and routing, whether or not the provider is an active system user.

## Behavior

- Credentialing staff register legal name, display name, NPI, provider type, specialties, identifiers, and contact channels.
- Affiliations link a provider to facilities, departments, effective dates, and service roles.
- Candidate duplicate NPI or identifier matches route to review rather than silently merging records.
- Status moves through Candidate, Active, Suspended, and Retired with reasons and effective timestamps.
- Suspended providers remain visible on historical records but are excluded from new assignments and signing choices.
- Sensitive identifiers are restricted to credentialing roles while approved directory fields remain broadly readable.

## Frappe realization

- **DocTypes:** `OC Provider` stores identity and status; child `OC Provider Identifier` and `OC Provider Affiliation` rows capture scoped identifiers and effective relationships.
- **Workflow:** Credentialing Workflow controls Candidate → Active → Suspended/Retired with Credentialing Specialist and Credentialing Approver roles.
- **Permissions:** permlevel 1 protects sensitive identifiers; facility User Permissions constrain affiliation maintenance.
- **API:** guarded `open_chart.api.v1.platform.register_provider` and `change_provider_status` methods return structured duplicate conflicts.

## Boundaries

Owns: provider identity, affiliation, and operational status. Consumes: facility and department masters. Emits: provider Links and status events. Does not own: credentials, user authentication, scheduling, or clinical privileges decisions.

## Open questions

- Which non-individual practitioners require organization-level provider records?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Provider Credential Expiry Monitoring](openchart-feature-catalog-plt-005-provider-credential-expiry-monitoring.md)
