# Quarto explanatory website

Every analysis repository publishes its code and methods as a Quarto website that explains the definitive scripts. The site documents the code; it never runs the analysis. [Cryptococcus-cost-analysis](https://github.com/VagishHemmige/Cryptococcus-cost-analysis) is the reference example for formatting. The bundled [starter](../assets/starter/_quarto.yml) reproduces it with synthetic code.

## Configuration

- `_quarto.yml` and `index.qmd` at the root; explanatory pages in `quarto/`. The site renders to `docs/`, which is committed and served by GitHub Pages.
- Website defaults: `cosmo` theme, docked sidebar with search, page navigation, table of contents, `code-fold: true`, `code-tools: true`, `page-layout: full`, and `code-summary: "Click to show/hide R Code"`.
- `site-url`, `repo-url`, `repo-branch` (the repository's actual default branch) and `repo-actions: [edit, issue]` are filled in before the first render.
- Sidebar links point to source `.qmd` files and only to pages that exist.
- Global `execute: eval: false`. Chunks that must run set `eval: true` explicitly: the `read_chunk()` import, and results pages that read outputs cleared for release.

## The custom-callout extension

The pink `Rcode` callout comes from the MIT-licensed [coatless-quarto/custom-callout](https://github.com/coatless-quarto/custom-callout) extension, committed in `_extensions/`. Install it in the target project with `quarto add coatless-quarto/custom-callout` (when authorized), or copy `_extensions/coatless-quarto/` from an existing repository. Its source is not bundled in this plugin.

## Pages

- **Home** (`index.qmd`): clinical background in brief, what the analysis does, a methods summary pointing to `analysis-plan.md`, and status.
- **Background** (`quarto/background.qmd`), plus any other narrative pages the project needs (for example a methods primer).
- **Setup and helper functions**: one page each for `R/setup.R` and `R/functions.R`.
- **Data processing and analysis**: one page per definitive script, named after it (`quarto/create_cohort.qmd` for `R/create_cohort.R`), numbered in the sidebar in the order `main.R` sources them.
- **Tables and figures**: pages for `R/tables.R` and `R/figures.R` once they exist.
- **Results** (optional): only when outputs are cleared for release, by the review AGENTS.md names or because setup decided they need no review. A results page reads the committed, cleared files in `tables/` and `figures/`; it never reruns analysis or touches restricted data.
- **About** (`quarto/about.qmd`): contributors, how to contribute, and a one-line description of every page.

Exploratory scripts do not get pages. A script gets its page when it is sourced from `main.R`, in the same pull request.

## A script page

Follow [the starter's example page](../assets/starter/quarto/example.qmd):

1. A one-sentence purpose.
2. A `::: {.Rcode title="Source code"}` block linking the script on GitHub and the helper scripts it depends on.
3. A hidden import chunk (`include: false`, `eval: true`, `cache: false`) running `knitr::read_chunk("../R/<script>.R")`. The path is relative to the page, so do not set `execute-dir: project`.
4. One `##` section per labelled step, each with prose and then an empty chunk carrying the step's `label` and `eval: false`.

The prose explains purpose, inputs and where they come from, the transformation, the assumptions and plan sections it implements, the access-package functions used, and what the step produces for later scripts. Explain why, not only what. Prose must change in the same pull request as the code it describes.

A short script may instead be shown whole with `#| file: "../R/<script>.R"` and `eval: false`; label the sections once the page needs to explain them separately.

## Checks before committing `docs/`

- Every `label` used by a page exists exactly once across `R/`, and every definitive script has a page and a sidebar entry.
- No chunk evaluates analysis code; the site renders without restricted data.
- Links to scripts use the correct repository and branch.
- Render, then open the changed pages and check callouts, code folding, navigation, citations and figures.
- Report static checks, a successful render, and visual inspection separately.

References: [Quarto websites](https://quarto.org/docs/websites/), [code execution](https://quarto.org/docs/computations/execution-options.html), [knitr external code](https://bookdown.org/yihui/rmarkdown-cookbook/read-chunk.html).
