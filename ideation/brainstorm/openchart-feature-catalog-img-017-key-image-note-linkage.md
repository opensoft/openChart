# Key Image and Note Linkage — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Links report or clinical-note statements to selected key images using durable external image references and provenance.
Topics: openchart-feature-catalog, imaging, frappe, key-images
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-017 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Patient-safe key-image projection** — Publish approved rendered references with disclosure controls for portal education.

## Focus

This feature isolates the semantic link between a written statement and an image selected to illustrate it.

## Behavior

- A viewer sends a key-image reference with study, series, instance, frame, annotation label, and selector identity.
- The author links the reference to a specific report finding or permitted note section.
- The UI verifies that the image belongs to the expected patient and study before acceptance.
- A thumbnail may be fetched transiently, but the durable record remains an external reference.
- Broken or remapped PACS references are flagged without deleting the textual statement.
- Signed documents snapshot link provenance; later corrections use a successor or addendum.

## Frappe realization

- **DocTypes:** `OC Key Image Reference` with source system, DICOM UIDs, frame, label, selector, target Dynamic Link, and reconciliation status.
- **Roles/permissions:** report and note authors create links within their document authority; portal exposure requires a separate approved flag.
- **API/surfaces:** signed viewer callback creates pending references; report and note editors attach them to structured rows.
- **Hooks:** target document validation enforces patient and study consistency; scheduled checks may flag unreachable references.

## Boundaries

Owns: durable image-to-document linkage and its provenance. Consumes: viewer selections and document context. Emits: contextual launch references. Does not own: image pixels, annotations stored in PACS, or portal release policy.

## Open questions

- Should key-image identifiers be normalized through DICOM Key Object Selection when available?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
