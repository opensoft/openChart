# Interoperability And Exchange — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should make production exchange turnkey — complete FHIR R4/USCDI surface, national network participation, and outside-record normalization with selective write-back — so clinics get Oracle QHIN-class data flow without OpenEMR's assemble-it-yourself exchange reality.
Topics: openchart-feature-list, interoperability, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **FHIR-first completeness** — every user-visible capability exposed through documented FHIR/REST APIs with US Core profiles, granular scopes, bulk export; API parity as release gate.
- **National network membership** — TEFCA/QHIN or network-aggregator participation shipped as configuration, not a consulting project.
- **Outside-record normalization** — incoming records matched, deduplicated, cleansed, shown side-by-side against local data with clinician-approved selective write-back (Oracle Seamless Exchange pattern).
- **Public developer ecosystem** — sandbox, app registration, playbooks, validated-integration registry (open.epic/Millennium-program analog, but open-source native).
- **Direct/HISP bundled** — clinical mail operated as product with address-directory discovery.
- **Public-health pipelines** — immunization registry, syndromic surveillance, electronic case reporting as managed connections.

## Focus

What does it take for openChart to promise — and operationally deliver — that patient data arrives complete, clean, and usable wherever it needs to go?

## Current state: OpenEMR baseline

OpenEMR core includes FHIR R4 API with SMART on FHIR, OAuth2/OIDC/PKCE, granular scopes, bulk export, broad resource coverage (patient, encounter, condition, medication, allergy, observation, procedure, diagnostic-report, document-reference, coverage, care-team, goal, questionnaire), CCDA generation/import, Direct Messaging, EHI export, QRDA. The qualification: API coverage is expanding but uneven versus the UI; production Direct/HISP may need external services; no national network membership of its own; HIE connectivity is implementer work. Reviewers report integration failures from identifier mismatch, incomplete mappings, transport unreliability, and missing operational monitoring.

Sources: github.com/openemr/openemr API_README; Features wiki; CapMinds interoperability guide.

## Enterprise gap candidates

- Epic Care Everywhere at TEFCA scale (2000+ hospitals claim); open.epic publishes 750+ no-cost APIs/interfaces plus workflow playbooks; HL7v2 interface breadth.
- Oracle operates its own TEFCA-designated QHIN (Oracle Health Information Network), CommonWell connect, vendor-agnostic HIE, Connection Hub console, Seamless Exchange normalization with dedupe/cleanse/side-by-side/selective auto-write.
- MEDITECH Traverse Exchange FHIR-based targeted retrieval presenting consolidated, deduplicated, filterable external summaries inside native workflows; Google Cloud/partner ecosystem positioning.
- Common thread: exchange is a governed operational service with reconciliation UX, not an interface spec.

## Proposed feature set for openChart

Parity floor: match OpenEMR's certified FHIR/SMART/CCDA/Direct/EHI-export surface and exceed its coverage uniformity. Adopted gaps: API-parity release gate enforced in validation; network participation via established aggregator with roadmap to direct QHIN status; outside-record ingestion pipeline producing reconciled side-by-side views with approved field-level write-back carrying provenance; public sandbox + validated-app directory; managed public-health connection catalog (per-state registry formats absorbed by product). Twist: because openChart is open-source, its developer ecosystem can publish reference implementations competitors legally cannot — openness as interop strategy.

## Interfaces and boundaries

Consumes: canonical clinical model across all domains, consent state from patient-engagement, terminology services, identity matching inputs. Emits: FHIR/REST surfaces, C-CDA/Direct payloads, public-health submissions, normalized outside records into domain workflows. Owns exchange operations and mapping governance; does not own counterpart systems' behavior.

## Alternatives and tensions

Aggregator-first vs own-QHIN changes cost/timeline dramatically. Selective auto-write-back (Oracle pattern) trades clinician review time against record completeness — default-to-review is safer and slower. API-parity gates slow feature velocity; shipping UI-first recreates OpenEMR's unevenness complaint.

## Open questions

- Which network aggregator partnership anchors launch?
- Is write-back always clinician-approved v1, with automation only as measured opt-in?
- What is the honest certification sequencing (ONC) given OpenEMR's Feb 2026 retirement precedent?

## Relationships

Clustered in [Synthesis: Business And Exchange](openchart-feature-list-synthesis-business-and-exchange.md). Adjacent: [Analytics And Population Health](openchart-feature-list-analytics-and-population-health.md), [Platform Security And Deployment](openchart-feature-list-platform-and-security.md).
