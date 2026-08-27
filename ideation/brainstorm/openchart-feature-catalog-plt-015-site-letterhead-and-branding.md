# Site Letterhead And Branding — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs site-specific logos, colors, contact details, and letterheads for consistent digital and printed output.
Topics: openchart-feature-catalog, platform, frappe, site-branding
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-015 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Brand accessibility audit** — Check color contrast, image alternatives, and print legibility before publication.

## Focus

This feature isolates approved visual identity by site without allowing branding to alter clinical content or record authority.

## Behavior

- Site administrators upload approved logos and define organization name, contacts, colors, footer text, and effective dates.
- Preview covers Desk accents, portal shell, email header, standard page sizes, and monochrome printing.
- File type, dimensions, contrast, and unsafe embedded content are validated before review.
- Branding moves through Draft, Review, Published, Retired, and Superseded states.
- Outputs pin the effective branding version so historical PDFs remain explainable after a rebrand.
- Missing or invalid assets fall back to an accessible openChart baseline and create an administrator warning.

## Frappe realization

- **DocTypes:** `OC Site Brand Profile` stores site, organization details, logo Files, colors, footer, effective dates, and state.
- **Surface:** integrate native Letter Head and Website Theme configuration through a governed preview and approval page.
- **Permissions:** Site Brand Administrator writes only permitted sites; Print Administrator and Communications Designer consume published profiles.
- **Hooks:** publication generates or updates controlled Letter Head records and clears website and print caches.

## Boundaries

Owns: approved site visual identity and letterhead version. Consumes: site master and brand assets. Emits: branding tokens and native Letter Head configuration. Does not own: document wording, signatures, or marketing campaigns.

## Open questions

- Must every legal entity have a separate brand profile even when visual assets are shared?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Print Format Designer](openchart-feature-catalog-plt-016-print-format-designer.md)
