# Clinician AI Change Newsletter — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes audience-targeted notices of AI model, prompt, policy, workflow, evidence, and known-issue changes before or at release.
Topics: openchart-feature-catalog, clinical-ai, frappe, change-communication
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-045 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Acknowledgment-required release brief** — Require designated users to attest understanding before first use of a material change.

## Focus

This feature isolates transparent clinician communication for AI changes and limitations.

## Behavior

- Release owners draft a notice naming affected capability, sites, roles, workflows, effective date, changes, evidence, limitations, known issues, and manual fallback.
- The system derives component diffs but requires a human owner to confirm clinical meaning.
- Audience rules deliver notices through Desk Notification Log and optional email before activation where policy requires.
- Material releases may require acknowledgment; lack of acknowledgment can deny capability use without denying manual workflow access.
- Corrections and urgent safety notices supersede prior communications visibly.
- Read and acknowledgment analytics are governance evidence, not proof of competence.

## Frappe realization

- **DocTypes:** `OC AI Release Notice` stores release Links, audience roles/sites, change summary, evidence, fallback, effective date, acknowledgment rule, and successor.
- **Workflow:** Draft → Clinical Communications Review → Approved → Scheduled → Published → Superseded.
- **Roles/permissions:** release owner drafts; `OC Clinical AI Reviewer` approves; recipients see notices scoped by role and site.
- **Hooks/surfaces:** deployment activation hook checks required publication; Notifications and Email Alerts deliver; Workspace newsletter archive and report show acknowledgment.

## Boundaries

Owns: AI release communication and acknowledgment evidence. Consumes: approved release and component diffs. Emits: scoped notices and acknowledgments. Does not own: training, competency assessment, or release approval.

## Open questions

- Which change categories warrant mandatory acknowledgment versus informational delivery?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Incident Response Workflow](openchart-feature-catalog-aic-046-ai-incident-response-workflow.md)
