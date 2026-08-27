# Reduced-motion Preference — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Honors operating-system and user requests to reduce nonessential animation while preserving clear state transitions and progress.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, reduced-motion
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-013 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Motion inventory** — Catalog every transition, animation, and auto-updating region with its essentiality rationale.

## Focus

This feature isolates motion preference resolution and reduced alternatives for Desk and portal interactions.

## Behavior

- The interface honors `prefers-reduced-motion` before first render and allows an explicit per-user override.
- Decorative animation, parallax, smooth scrolling, pulsing, and large spatial transitions stop or become instantaneous.
- Essential progress remains perceivable through stable text, percentage, or step indicators rather than motion alone.
- Live boards avoid repeated attention-capturing movement and announce meaningful changes through controlled status regions.
- No reduced-motion substitution flashes, rapidly fades, or introduces another vestibular trigger.
- A preference change applies immediately and persists across devices for authenticated users.
- Unsupported custom animations are detectable by conformance tests and block component promotion when critical.

## Frappe realization

- **Preferences:** Frappe user preferences store `motion_mode`; bootinfo resolves System, Reduced, or Full before Desk initialization.
- **Themes and scripts:** Website Theme and Desk theme CSS use reduced-motion media queries and root attributes; shared JS utilities bypass animated transitions.
- **Configuration:** `OC Motion Pattern Register` records component, purpose, essentiality, reduced substitute, and release status.
- **Quality:** Synthetic browser checks inspect computed durations and route transitions across Desk and portal surfaces.

## Boundaries

Owns: nonessential interface motion and user preference resolution. Consumes: operating-system setting, user override, and component motion metadata. Emits: reduced alternatives and defects. Does not own: diagnostic media playback or clinically necessary time-series visualization.

## Open questions

- Which real-time clinical changes merit a non-motion attention cue when motion is reduced?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Synchronized User Interface Preferences](openchart-feature-catalog-iax-018-synchronized-user-interface-preferences.md)
