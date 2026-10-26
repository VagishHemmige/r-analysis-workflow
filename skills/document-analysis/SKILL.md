---
name: document-analysis
description: Write or update the explanatory Quarto website and ARCHITECTURE.md for an R analysis project. Use when a script joins the definitive workflow and needs its page, when code changes and its page or architecture must follow, when pasted code on a page should become imports from the actual script, or when the site, README or architecture needs repair, or when the analysis plan needs updating after a decision, locking, or a new data source.
---

If the linked plugin files cannot be opened, say so and continue from the repository's own AGENTS.md and analysis plan; do not guess their contents.

Read [conventions](../../references/conventions.md), [Quarto guidance](../../references/quarto.md) and the project's AGENTS.md. Use the Posit `quarto-authoring` skill for Quarto work and `describe-design` for ARCHITECTURE.md; if either is not installed, say so and continue without claiming it was used. The starter templates are in [assets/starter](../../assets/starter/_quarto.yml).

Documentation describes what the code does now. Planned behavior belongs in the plan; open work belongs in GitHub Issues.

## When a script joins the definitive workflow

A script joins when `R/main.R` sources it. In the same pull request:

1. **Label the script.** Divide it into `## ---- step-name` sections: kebab-case, describing the step, unique across all scripts. Labels never change what the code does. Give it the header comment AGENTS.md requires.
2. **Write its page** in `quarto/`, named after the script, following [the example page](../../assets/starter/quarto/example.qmd): one-sentence purpose, the Source code callout linking the script and its helpers on GitHub, the hidden `knitr::read_chunk("../R/<script>.R")` import, then one section per label with prose followed by an empty `eval: false` chunk.
3. **Add it to the sidebar** in `_quarto.yml`, numbered in the order `main.R` sources it, and to the list on the About page.
4. **Link neighbours.** Link the scripts it depends on and the ones that use its output.
5. **Render, check and commit `docs/`** (see "Before committing").

## Writing the prose

- For each section: what it does and why, its inputs and where they come from, the transformation, the assumptions and the plan sections it implements, the data-access package functions it uses, and what it produces for later scripts. Explain why, not only what.
- Write for a clinician who is not a statistician: define abbreviations and technical terms on first use, and give statistics their plain meaning.
- Describe associations as associations; do not use causal language the design does not support.
- Cite sources with `[@key]` from `references.bib`, not bare links. Never invent a citation; when a statement needs one that is not in `references.bib`, flag it for the librarian review rather than guessing.
- Describe the code as it is. If code and plan disagree, report the difference; do not write prose that papers over it.

## When code changes

Update the prose of every section whose behavior changed, in the same pull request. After renaming or removing a label, search the `.qmd` files and fix every import. Re-render.

## Converting pasted code to imports

Where a page holds a copy of code instead of importing it: add labels to the script at the boundaries the page uses, replace each pasted block with an empty chunk carrying the label and `eval: false`, add the import chunk, and confirm the rendered code matches the script. Report any pasted code that no longer exists in the script; it means the page described something the code no longer does.

## ARCHITECTURE.md

Refresh it with `describe-design` after a material structural change (a script added, removed or reordered; data flow between scripts changed). It names the commit it describes and whether uncommitted changes were included, describes only what is implemented, and keeps implementation status out (that belongs in GitHub Issues).

## README

If the project has `README.Rmd`, it is the source: edit it and knit `README.md`. Otherwise edit `README.md`. Keep the status badges accurate.

## Established sites

When an existing site departs from these conventions (pasted code, `.html` sidebar links, a missing page, a different layout), list the differences and ask before changing them. Do not restyle a site silently. Install the custom-callout extension only when authorized.

## Before committing `docs/`

- Every label used by a page exists exactly once across `R/`, and every definitive script has a page and a sidebar entry.
- No chunk runs analysis code; the site renders without restricted data. Results pages read only outputs cleared for public release.
- Script links use the right repository and branch; citations resolve; figures have alt text.
- Render, then look at the changed pages.
- Report static checks, a successful render and visual inspection separately.

For an independent check afterwards, offer the "Site ↔ code" review in the review skill.
