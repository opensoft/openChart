# openChart

openChart is a Frappe-native, open-source clinical charting and electronic
medical records platform.

## Status

The repository currently contains project-governance and specification tooling.
The Frappe application and clinical data model have not yet been implemented.

The planned Frappe application/package name is `open_chart`.

## Product boundary

openChart will own general clinical records and workflows, including patients,
encounters, conditions, allergies, medications, supplements, observations,
results, orders, care plans, documents, provenance, and clinical
interoperability surfaces.

It will not own billing, claims, revenue cycle, or general practice operations;
those belong to [openPractice](https://github.com/opensoft/openPractice).
Medx-specific scenario, evidence, authority, and decision workflows belong to
[MedxEHR](https://github.com/opensoft/MedxEHR), which will extend openChart.

## Original implementation

openChart is an original Frappe application. OpenEMR, Marley/Frappe Healthcare,
other EHR products, and healthcare standards may guide requirements and
interoperability behavior, but their code is not an implementation base for
this project. openChart is not an OpenEMR or Marley fork.

## Spec-driven development

Product and architecture changes use OpenSpec for governance and Spec Kit for
feature specification, planning, implementation, and verification. Specs and
code live together in this repository so each implementation commit remains
traceable to its requirements and tests.

See [AGENTS.md](AGENTS.md) for the shared workflow and repository constraints.

## License

Licensed under the [Apache License 2.0](LICENSE).

Never commit real patient information, credentials, decrypted clinical
records, wallet secrets, or encryption keys to this repository.
