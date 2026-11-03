# Quarto explanatory website

Every analysis repository publishes its code and methods as a Quarto website that explains the definitive scripts. The site documents the code; it never runs the analysis. [Cryptococcus-cost-analysis](https://github.com/VagishHemmige/Cryptococcus-cost-analysis) is the reference example for formatting. The bundled [starter](../assets/starter/_quarto.yml) follows its layout with synthetic code; where the two differ, this guidance and the starter take precedence.

## Configuration

- [`_quarto.yml`](../assets/starter/_quarto.yml), `index.qmd`, [`404.qmd`](../assets/starter/404.qmd) and [`styles.css`](../assets/starter/styles.css) at the root; explanatory pages in `quarto/`. A `render:` list (`index.qmd`, `404.qmd`, `quarto/**`) keeps Quarto from also rendering the root Markdown files as pages of their own. The site renders to `docs/`, which is either committed and served by GitHub Pages or left untracked and rendered and published by a GitHub Actions workflow; the project's AGENTS.md says which.
- Website defaults: `cosmo` theme with `css: styles.css`, docked sidebar with search and `collapse-level: 3` (every section starts open), page navigation, table of contents, `code-fold: true`, `code-tools: true`, `page-layout: full`, and `code-summary: "Click to show/hide R Code"`.
- `site-url`, `repo-url`, `repo-branch` (the repository's actual default branch) and `repo-actions: [edit, issue]` are filled in before the first render.
- Sidebar links point to source `.qmd` files and only to pages that exist.
- Global `execute: eval: false`. Chunks that must run set `eval: true` explicitly, and only these may: the `read_chunk()` import; the Architecture page's chunk that reads `ARCHITECTURE.md` as text; site-only helpers that read code or text and never data; and results pages that read outputs cleared for release. The project's AGENTS.md lists any others it allows.

## The custom-callout extension

The site's callouts, pink `Rcode` (💻, `#d63384`, the laptop icon's colour), green `Results` (📊) and yellow `Pending` (⏳), come from the MIT-licensed [coatless-quarto/custom-callout](https://github.com/coatless-quarto/custom-callout) extension, committed in `_extensions/`. Install it in the target project with `quarto add coatless-quarto/custom-callout` (when authorized), or copy `_extensions/coatless-quarto/` from an existing repository. Its source is not bundled in this plugin. The three callout definitions are in the starter's `_quarto.yml` under `custom-callout:`; copy all three into a project's `_quarto.yml`.

## Visual cues

Each kind of page has one icon and one colour. The icon is the sidebar entry's `icon:` in `_quarto.yml`; `styles.css` colours it, keyed to the icon rather than to a position, so pages can be added or moved without editing the CSS. Pages mark the same kind of content with the callout of that colour. A project that already has a `styles.css` keeps its own rules and adds the starter's.

| Kind | Sidebar icon | Colour | Callout |
|---|---|---|---|
| Background | `book` | blue | — |
| Study design and methods | `diagram-3` | orange | — |
| R code | `laptop` | pink | `Rcode` (💻) |
| Results | `clipboard-data` | green | `Results` (📊) |
| Project documents | `file-earmark-ruled` | grey | — |

A page that fits none of these takes the kind of its main content. For example, a page of original or historical code is R code; a log of corrections to the methods is Study design and methods; a log of maintenance changes is Project documents. Pages that reproduce results already published elsewhere take the Results kind and keep any notice about where they come from. The kind is only a label for the page: it does not make anything publishable, and it does not change the release review AGENTS.md names. Home has `house` and About `info-circle`. Section headings are bold, with a thin rule between sections, and sections inside another section (those under Code) are lighter. Give every new page the icon of its kind.

## Provisional content

Text that depends on an open decision is highlighted in yellow. The filter [`quarto/_pending.lua`](../assets/starter/quarto/_pending.lua), registered before `custom-callout` in `filters:`, marks every paragraph that starts with **Decision pending:**, and, on the plan's page only, every paragraph that contains the plan's own **Open:** marker, wherever it stands in the paragraph (the colon inside or just after the bold), and any phrase written as `[text]{.pending}`, and adds a ⏳ `Pending` callout at the top of each page that has a mark. When the reader-comments extension is set up, the callout also says how to comment, using the extension's button label. Mark only what an open decision could change, and remove the mark when the decision is settled. Yellow is used for nothing else. The filter marks paragraphs only: a **Decision pending:** note in a bullet or a table cell is not marked, so write such notes as their own paragraph, or wrap the text as `[text]{.pending}`, which works anywhere, table cells included. Decision pending notes link the decision issue (see [analysis plan](analysis-plan.md)). Open choices labelled another way (for example "Open decision" rows in a table) get no yellow mark until they are rewritten as **Decision pending** notes or wrapped as `[text]{.pending}`; bringing an existing site up to date does that (below).

## Pages

- **Home** (`index.qmd`): clinical background in brief, what the analysis does, a short methods summary pointing to Study design and methods and to the plan's page on the site (`quarto/analysis-plan.qmd`), and status.
- **Background**: **Clinical background** (`quarto/background.qmd`) and **Methodological background** (`quarto/methodological_background.qmd`), the general knowledge the methods rest on (data sources, how records become the outcome, how comparison groups are chosen, why the models fit), with nothing specific to this study.
- **Study design and methods** ([`quarto/study_methods.qmd`](../assets/starter/quarto/study_methods.qmd)): what this study chose and why, in plain language, with **Specified in**, **Current code** and **Decision pending** notes. Start with one page; when it grows, split it into a section of pages chosen for the study, each opening with a line pointing back to the key to the notes. Keep `study_methods.qmd` as the first page of the split, so links to it keep working.
- **Code**, one section with every subsection open:
  - **Setup and helper functions**: one page each for `R/setup.R` and `R/functions.R`.
  - **Data processing and analysis**: one page per definitive script, named after it (`quarto/create_cohort.qmd` for `R/create_cohort.R`), numbered in the sidebar in the order `main.R` sources them.
  - **Tables and figures**: pages for `R/tables.R` and `R/figures.R` once they exist.
- **Results** (optional): only when outputs are cleared for release, by the review AGENTS.md names or because setup decided they need no review. A results page reads the committed, cleared files in `tables/` and `figures/`; it never reruns analysis or touches restricted data.
- **Project documents**: the analysis plan, Architecture, AGENTS.md and the repository blueprint (see below). The plan sits here, not under Background, because it is written for the people and agents working on the code; Study design and methods explains it in plain language and links its sections.
- **About** ([`quarto/about.qmd`](../assets/starter/quarto/about.qmd)): the study and who decides, the repository, how the site was made, the four project documents, and a one-line description of every page in the sidebar.
- **404** (`404.qmd`): the page GitHub Pages shows for a missing address. Quarto does not create one. Rendered from the root, its links work from any address once `site-url` is set.

Apart from About, pages do not end with a list of the other pages; the sidebar already lists them. Links to the scripts a page depends on, or the ones that use its output, are not such a list.

Exploratory scripts do not get pages. A script gets its page when it is sourced from `main.R`, in the same pull request.

## Project-document pages

`analysis-plan.md`, `ARCHITECTURE.md`, `AGENTS.md` and `REPOSITORY-BLUEPRINT.md` stay at the repository root and are the only copies anyone edits. Each has a thin page in `quarto/` that shows it at render time:

- [`quarto/analysis-plan.qmd`](../assets/starter/quarto/analysis-plan.qmd), [`agents.qmd`](../assets/starter/quarto/agents.qmd) and [`repository-blueprint.qmd`](../assets/starter/quarto/repository-blueprint.qmd) include the root file with `{{< include ../<file>.md >}}`. The plan's page sets `from: markdown+gfm_auto_identifiers`, so its GitHub-style links (`#2-design`) work on both GitHub and the site.
- [`quarto/architecture.qmd`](../assets/starter/quarto/architecture.qmd) reads `ARCHITECTURE.md` as text in one `eval: true` chunk and turns its ```` ```mermaid ```` fences into Quarto diagrams, which Quarto would otherwise show as code. It reads only that file.

The starter has all four pages. The includes stop the render if a root file is missing, so a new project creates `analysis-plan.md`, `AGENTS.md` and `REPOSITORY-BLUEPRINT.md` (the bundled blueprint, unchanged) before the first render; the Architecture page shows a note until `ARCHITECTURE.md` exists. When adding these pages to an existing site, the `from:` setting matters only if the plan links its own sections, and the Architecture reader only if `ARCHITECTURE.md` has mermaid diagrams.

## Reader comments (optional)

The [issue-comments](https://github.com/VagishHemmige/quarto-commenting-extension) extension lets readers highlight text and leave a comment, which a relay files as a GitHub issue in the repository. It needs the relay and its GitHub App set up once, as its [installation guide](https://vagishhemmige.github.io/quarto-commenting-extension/quarto/installation.html) describes; each further site then needs the extension in `_extensions/`, the GitHub App's access to its repository, and, in `_quarto.yml`, both the commented-out `issue-comments` filter line and the `issue-comments:` block, with the same `endpoint`. Turn on all three together: without the extension the render fails, and without the filter line the Pending callout points readers to a Comment button that is not there.

## Bringing an existing site up to date

A site built before these conventions is updated only after the maintainer agrees to the list of differences (see the document-analysis skill). Then, in one pull request:

1. Add `404.qmd`, and add it to the `render:` list, keeping every target the list already has (pages outside `quarto/` included). If there is no `render:` list, add one that names every page the site renders now.
2. Copy `quarto/_pending.lua`, register it in `filters:` before `custom-callout`, and add the `Results` and `Pending` callout definitions next to the existing ones.
3. Create `styles.css` from the starter's, or, if the project has one, add the starter's rules to it and keep its own. Register it under `format: html: css:`, adding it to any stylesheets already listed rather than replacing them.
4. Add icons, `collapse-level: 3` and the Code group to the sidebar.
5. Add any missing project-document pages, and check that each root document they include exists.
6. Rewrite the site's existing open-decision labels ("Open decision" rows, "to be decided" notes and the like) as **Decision pending** notes linked to their decision issues, or wrap them as `[text]{.pending}` in tables, without changing what they say is open. This is the one content change the procedure makes; list each one in the pull request.
7. Update the project AGENTS.md "Quarto website" section to match, including the publishing route.

Render, then check that every page that was on the site before is still in the sidebar and still renders, and that the icons are coloured (if not, the stylesheet is not registered). Pages the site lacks, such as Methodological background or Study design and methods, are proposed to the maintainer with an outline, never added as placeholder pages, because their content is the study team's. Apart from step 6, existing callouts, labels and wording stay as they are unless the maintainer asks.

## A script page

Follow [the starter's example page](../assets/starter/quarto/example.qmd):

1. A one-sentence purpose.
2. A `::: {.Rcode title="Source code"}` block linking the script on GitHub and the helper scripts it depends on.
3. A hidden import chunk (`include: false`, `eval: true`, `cache: false`) running `knitr::read_chunk("../R/<script>.R")`. The path is relative to the page, so do not set `execute-dir: project`.
4. One `##` section per labelled step, each with prose and then an empty chunk carrying the step's `label` and `eval: false`.

The prose explains purpose, inputs and where they come from, the transformation, the assumptions and plan sections it implements, the access-package functions used, and what the step produces for later scripts. Explain why, not only what. Prose must change in the same pull request as the code it describes.

A short script may instead be shown whole with `#| file: "../R/<script>.R"` and `eval: false`; label the sections once the page needs to explain them separately.

## Checks before committing

- Every `label` used by a page exists exactly once across `R/`, and every definitive script has a page and a sidebar entry with its kind's icon.
- Each root project document has its page, and every **Decision pending** note is still an open decision.
- No `<placeholder>` text from the starter remains, and no example **Decision pending** line is left in a page that has no open decision (search the `.qmd` files for `<` at the start of a placeholder).
- No chunk evaluates analysis code; the site renders without restricted data.
- Links to scripts use the correct repository and branch.
- Render, then open the changed pages and check callouts, code folding, navigation, citations and figures.
- Report static checks, a successful render, and visual inspection separately.

References: [Quarto websites](https://quarto.org/docs/websites/), [code execution](https://quarto.org/docs/computations/execution-options.html), [knitr external code](https://bookdown.org/yihui/rmarkdown-cookbook/read-chunk.html).
