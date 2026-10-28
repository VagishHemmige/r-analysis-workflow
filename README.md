# R Analysis Workflow

Version 0.1.9. A skills-only plugin for R biomedical analysis projects whose code and methods are published on GitHub with a Quarto website. It is not for R packages.

## Install

- **Claude** (chat, Desktop and Cowork; paid plans): open **Customize** → **Plugins** → **Add** → **Add marketplace** → **Add from a repository**, enter `VagishHemmige/r-analysis-workflow`, then install **R Analysis Workflow**. It also syncs to Claude Code on the same account.
- **Claude Code:** `claude plugin install r-analysis-workflow --marketplace VagishHemmige/r-analysis-workflow`
- **ChatGPT:** <your steps>

Installing grants no data access or GitHub permissions; see Dependencies.

## Skills

| Skill | Use it to |
|---|---|
| `initialize-analysis` | Set up or reorganize a project: questionnaire, blueprint, analysis plan, AGENTS.md (with a row per data source and its access package), Quarto site, README, `.gitignore`, branch protection |
| `document-analysis` | Write the Quarto page when a script joins `main.R`, keep pages and ARCHITECTURE.md in step with the code, convert pasted code to imports |
| `report-analysis` | Build the reporting: flowchart participant flow, descriptions and missingness, Table 1, longitudinal and time-to-event summaries, figures and survival curves with risk tables, model tables |
| `review-analysis` | Review a change or a whole project: blind clinician, clinician-researcher, statistician, coding-expert and librarian reviewers, plus direct checks for repository conformance and release |
| `onboard-collaborator` | Bring a clinician, student or new collaborator into a project at the level of help they want, suggest a personal LLM project and check-in, and help someone leave or hand over |

## Principles

- `analysis-plan.md` decides the science. Open scientific choices are decision issues on GitHub, settled only by named deciders; agents implement decisions and never make them.
- Every sourced decision cites `references.bib`.
- Code that touches a data source goes through that source's package.
- The website explains the actual scripts and never runs the analysis.
- Changes reach the default branch through pull requests.
- Reviewers read only code, documentation and material cleared for release, so reviews stay within data use agreements; acting on a review is the reader's choice.
- Agents never read restricted data unless a project's AGENTS.md explicitly allows it for a source; by default nothing is allowed.

## Dependencies

Uses installed Posit skills where relevant (`quarto-authoring`, `describe-design`, `critical-code-reviewer`, `review-testing`, `r-tidyverse-style`, `alt-text`); each skill says what it does when one is missing. The Quarto starter needs the [custom-callout](https://github.com/coatless-quarto/custom-callout) extension. No MCP server, data access, GitHub write permission or installation permission is granted by this plugin.

## Layout

Shared material lives once at the plugin root, as OpenAI's own plugins do with shared references: `references/` for guidance and `assets/` for templates (the Quarto starter, AGENTS.md, personal instructions). Each skill is a single `SKILL.md` that links to them with `../../`. Edit a reference once and every skill sees the change. The ChatGPT manifest follows the Agent Plugins standard (a root `plugin.json`), which ChatGPT accepts; OpenAI's own plugins use `.codex-plugin/plugin.json`. The manifest is `plugin.json` for ChatGPT, with a matching `.claude-plugin/plugin.json` for Claude (claude.ai, Cowork and Claude Code); keep the two in step. Run `python3 check_links.py` before releasing; it checks the links and that the manifests agree.

See VALIDATION.md for what has been checked and SOURCES.md for provenance. Original text and code are MIT licensed; linked external content keeps its own license.
