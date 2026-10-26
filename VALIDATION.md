# Validation — 0.1.8, 2026-10-26

What was checked, and what was not.

## Checked

- **Layout:** follows OpenAI's curated plugins (github.com/openai/plugins, checked 2026-10-26), whose skills ship non-Markdown files and link to shared plugin-level `references/` with `../../`. Every relative link resolves (`check_links.py`). Version 0.1.4 installed in ChatGPT with this manifest format.
- **Quarto starter:** rendered with Quarto 1.7.32 and the custom-callout extension; all pages build, source sections import through `knitr::read_chunk()`, and the Rcode callout, code folding and sidebar display correctly (inspected visually). `R/main.R` runs in a fresh session.
- **README template:** knits to `README.md` with `rmarkdown`.
- **`.gitignore`:** tested in a scratch repository with `git check-ignore`: `docs/`, scripts and settings files are tracked; data formats, credentials, `figures/` and `tables/` are ignored; a narrow exception (`!output/*.csv`) works.
- **Templates against practice:** the blueprint, analysis-plan structure, AGENTS.md, Quarto site and README were compared with five of the author's maintained analysis repositories.
- **APIs checked against current documentation:** gtsummary 2.6.1 (`tbl_summary()` missing arguments, `pool_and_tidy_mice()`, `tidy_robust()`), ggsurvfit 1.2.1 (`add_risktable()` statistics), flowchart 1.0.x (function names).
- **Blind reviewers:** the clinician reader, clinician-researcher, statistician and coding-expert prompts were run as independent agents on a public repository (Cryptococcus-cost-analysis at 015aa6b). Each stayed in its role; findings were verified against the code in the combining step, which withdrew one incorrect claim and corrected one imprecise one. The coding expert was rerun with Posit skills loaded. Prompts were revised afterwards (combining step verifies claims; reviewers may read public dependencies and cited sources; clinician reader reads the whole plan).
- **0.1.7 changes** (from the 2026-10-26 user simulation: personal LLM project and working styles, check-ins, offboarding, drafts kept in the repository, show text before posting as someone, look before asking, which copy to work on, GitHub Pages and milestones, no stacked pull requests, menu paths, no results in code, review combining and coding-expert checks): every link resolves (`check_links.py`). GitHub steps for Pages, milestones and repository transfer were checked against GitHub's documentation on 2026-10-26. OpenAI's GitHub plugin (openai/plugins, version 0.1.12 at commit 0722921) was read: it packages the GitHub connection only and has no skills, so it neither overlaps nor conflicts with this plugin. GitHub's stacked pull requests are in public preview (announced around 31 July 2026); this plugin avoids stacks.
- **Claude:** `claude plugin validate` (Claude Code 2.1.310) passes the plugin with and without `.claude-plugin/plugin.json`; its only warning is a missing icon, which matters only for Anthropic's directory. Loaded in Claude Code with `--plugin-dir`, all five skills appear, and a skill followed its `../../` link into the shared `references/` folder and quoted it correctly.
- **Blind review of the plugin (0.1.7), 2026-10-26:** five independent reviewers (structure, novice student lead, PI, statistician, data governance) read only the shipped plugin and its stated principles; ChatGPT's own reading was added as a sixth. Every claimed error was checked against the files or documentation before it was listed (46 findings; record in the source's `testing/runs/2026-10-26-plugin-review/`). 0.1.8 makes the fixes the maintainer chose, including: agents read restricted data only where AGENTS.md's Data sources table explicitly allows it (nothing by default); decisions relayed by email; deciders asked at setup; review packets defined by content; cleared outputs on the site; results kept out of every repository text; `fc_view(what = "data")`; verified guideline entries in `assets/guidelines.bib` (STROBE, RECORD, CHEERS 2022, TARGET, TRIPOD+AI, from PubMed).
- **`check_links.py`** now also checks `#anchors`, the links in `assets/` (except the starter templates) and manifest keywords; it caught three planted errors in a scratch copy.
- **`.gitignore` template:** `/data-raw/` ignores files of any format there (tested with `git check-ignore`).

## Not yet checked

- Whether a ChatGPT scheduled task inside a person's project can see that project's earlier chats (needed for the check-in's draft search). OpenAI's documentation does not say; test in ChatGPT.
- The librarian reviewer has not been run.
- Reviewers have not been rerun since their access rules and prompts were revised, including the 0.1.7 combining step (known findings, team-package headings), the coding expert's tracked-file check and the real-data check suggestions.
- The 0.1.7 and 0.1.8 changes have not been tested by rerunning the user simulation (steps 7 and 8, and the student-owned variant). The test procedure in the source's `testing/` folder was updated for them.
- The model-reporting recipes (GEE, mixed models, `add_global_p()`, multiple imputation) have not been executed on synthetic data.
- Upload to claude.ai and use in chat and Cowork: Anthropic's documentation describes supporting files inside each skill's folder and does not say whether skills there can read the shared root folders through `../../`. Check on first upload.
- Use in ChatGPT: whether its skills follow `../../` links to the shared root folders as Codex plugins do, and read the non-Markdown starter files. Check this on first use.
- Real-user testing of the setup questionnaire.
- No scientific results were reproduced.
