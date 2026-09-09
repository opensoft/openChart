# Pharmacogenomic Drug-Gene Alerts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates candidate medications against verified genotype and phenotype results using versioned drug-gene guidance and explainable uncertainty.
Topics: openchart-feature-catalog, eprescribing, frappe, pharmacogenomics
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-034 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Phenotype reinterpretation queue** — New guidance releases could flag affected prior interpretations for human review without altering signed prescriptions.

## Focus

This feature isolates pharmacogenomic prescribing alerts. It uses only verified results and makes guideline version, phenotype derivation, applicability, and uncertainty visible.

## Behavior

- The engine checks candidate medication and indication against accepted genotype, phenotype, and relevant laboratory reports.
- Findings show gene, allele or phenotype used, result source, test date, guideline release, recommendation category, and limitations.
- Unverified patient-reported results, uncertain phenotypes, and unsupported alleles are labeled and not treated as definitive.
- Conflicting laboratory interpretations enter a review path rather than selecting one silently.
- The prescriber may modify the draft or document a reasoned disposition; no recommendation is applied automatically.
- Signed evidence retains exact result versions and guidance release evaluated.

## Frappe realization

- **DocTypes:** `OC Pharmacogenomic Result` references source documents; `OC Drug Gene Guidance` is versioned; findings link both immutable versions.
- **Workflow:** Results may pass Imported → Verification → Accepted/Rejected before becoming eligible for evaluation.
- **Permissions:** Genomic data uses restricted roles, User Permissions, and purpose-of-use checks across API and Desk.
- **Surfaces/hooks:** Composer warning card, result provenance drawer, and guidance-update background review queue support governed use.

## Boundaries

Owns: drug-gene evaluation and prescribing disposition. Consumes: verified genomic results and guidance releases. Emits: explainable alerts and reinterpretation tasks. Does not own: laboratory interpretation, diagnosis, or autonomous drug selection.

## Open questions

- Which genomic result types and guideline bodies meet the threshold for prescribing use?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Clinical Alert Override Documentation](openchart-feature-catalog-phr-035-clinical-alert-override-documentation.md)
