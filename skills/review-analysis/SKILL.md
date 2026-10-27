---
name: review-analysis
description: Review an R analysis project, or a change to one, against its analysis plan, website, architecture and repository rules, using blind clinical, statistical, coding and librarian reviewers and the relevant Posit review skills. Use for code or pull-request review, plan review, citation and literature checks, site and code sync, architecture currency, repository conformance, reporting review and pre-release checks.
---

If the linked plugin files cannot be opened, say so and continue from the repository's own AGENTS.md and analysis plan; do not guess their contents.

Read [conventions](../../references/conventions.md), the project's AGENTS.md and the directing person's instructions. Reviews are read-only; acting on findings comes afterwards, as the reader chooses.

## 1. Fix what is being reviewed

Choose and state the copy and revision as the [conventions](../../references/conventions.md) describe. A pull request or branch is reviewed against its merge base; a single commit against its parent; a whole-project review covers the current state. A change review reads every file the change touches (code, tests, plan, pages, docs/, AGENTS.md, lockfiles), not a sample, and lists them in the report; a file not read is named as not reviewed, with the reason.

## 2. Choose the review

| Review | What it checks | Reviewers |
|---|---|---|
| **Change** | A pull request, branch or uncommitted work against the plan and AGENTS.md "Checks for any change" | Coding expert; statistician if the change affects the analysis |
| **Plan ↔ code** | Every plan section has code and every analysis has a plan section; each open point links an open decision issue; no open decision is settled in code | Coding expert, statistician |
| **Plan** | Completeness against the reporting map and named guideline; methods fit the question; definitions are valid; claims are cited and citations support them | Clinician-researcher, statistician, librarian; clinician reader for clinical relevance and clarity |
| **Site ↔ code** | Against the [Quarto guidance](../../references/quarto.md): labels exist once and are used; every definitive script has a page and sidebar entry; prose matches the code; no site chunk runs analysis code; citations on the site | Coding expert, librarian; clinician reader for understandability |
| **Architecture** | ARCHITECTURE.md names a current commit and matches the scripts | Coding expert (with `describe-design`) |
| **Repository conformance** | The repository against the [blueprint](../../references/REPOSITORY-BLUEPRINT.md) and templates: required files, the AGENTS.md data-sources table against the packages actually loaded, `.gitignore`, branch protection | No reviewer; a direct check |
| **Reporting** | The flow diagram, tables, models and numbers in prose against the cohort and what was fitted ([reporting guidance](../../references/reporting.md)) | Statistician, clinician reader |
| **Release** | Against [data handling](../../references/data-handling.md), before the site or outputs go public: nothing from restricted data unless cleared for release by the review AGENTS.md names, alt text, no credentials | A direct check, then a person signs off |

Pick the review that fits the request. A request for "a full review" runs Plan, Plan ↔ code, Site ↔ code and Reporting together.

## 3. Run the reviewers

Follow [blind reviewers](../../references/reviewers.md): each reviewer gets its packet and the public material its role needs, loads its Posit skills, and runs as an independent agent where the host allows. Reviewers never receive restricted data. Report any Posit skill that is not installed and continue.

For a direct check (repository conformance, release), inspect the files yourself and report in the same finding format.

## 4. Combine and report

Combine the reports as described in [blind reviewers](../../references/reviewers.md#combining-the-reports): verify claimed errors against the source, merge duplicates, mark findings already known from issues or earlier chats with their current status, keep disagreements visible, turn scientific choices into proposed decision issues, and number every finding. State what was reviewed, what ran and what was only read, and what could not be assessed.

## 5. Act only as the reader chooses

Offer the actions in [acting on the results](../../references/reviewers.md#acting-on-the-results) and carry out only what the reader picks, within their authorized actions. Do not repost resolved findings.

When running anything (synthetic checks, renders), do it in an isolated copy, check for paths, startup files or configuration that read or write back into the original or restricted locations, and avoid full or expensive reruns beyond what was authorized.
