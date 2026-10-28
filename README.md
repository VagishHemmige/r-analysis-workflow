# R Analysis Workflow

Version 0.1.10. A skills-only plugin for R biomedical analysis projects whose code and methods are published on GitHub with a Quarto website. It is not for R packages.

**Who it's for.** Anyone working on such a project: clinicians who will never write R, students who know R but not GitHub, statisticians and maintainers.

**Where to start.**
- Starting a project, or tidying an existing one: `initialize-analysis`.
- Joining or leaving a project: `onboard-collaborator`.
- Adding or changing a script: `document-analysis`, then `report-analysis` for tables and figures.
- Checking work before it is merged or published: `review-analysis`.

## Install

- **Claude** (chat, Desktop and Cowork; paid plans): open **Customize** → **Plugins** → **Add** → **Add marketplace** → **Add from a repository**, enter `VagishHemmige/r-analysis-workflow`, then install **R Analysis Workflow**. It also syncs to Claude Code on the same account.
- **Claude Code:** `claude plugin install r-analysis-workflow --marketplace VagishHemmige/r-analysis-workflow`
- **ChatGPT:** Install Plugin Creator, then ask it to create a plugin from this repository: `https://github.com/VagishHemmige/r-analysis-workflow`. For subsequent updates, ask Plugin Creator to update the existing R Analysis Workflow plugin from the repository, preserving its identity. This is an explicitly requested update, not automatic GitHub synchronization. Workspace administrators also have a separate GitHub marketplace import and daily-sync option; see [OpenAI's plugin documentation](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt).

Installing grants no data access or GitHub permissions; see Dependencies.

## Updating

- **Claude Code:** auto-update is off for this marketplace by default. Turn it on in `/plugin` → **Marketplaces** → `r-analysis-workflow` → **Enable auto-update**, or update by hand:
  `claude plugin update r-analysis-workflow@r-analysis-workflow`
- **ChatGPT** (not yet tested): mention `@plugin-creator` and your existing R Analysis Workflow plugin, and ask it to update from the repository.

## Using it

Ask in plain words; you don't need to name a skill. For example:

- "Set up my R analysis project from my latest RMD and protocol."
- "I'm joining this project and I'm new to GitHub. Where do I start?"
- "Write the Quarto page for the script I just added to main.R."
- "Run a full blind review of this repository."

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

Shared material has one source at the plugin root: `references/` for guidance and `assets/` for templates (the Quarto starter, AGENTS.md, personal instructions). Edit it there only. ChatGPT's cloud skills package only each skill's own folder, so each skill also carries generated copies of the shared files it uses, at the same paths (`skills/<skill>/references/`, `skills/<skill>/assets/`), and its `SKILL.md` links to those copies. After changing a `SKILL.md` or anything in `references/` or `assets/`, run `python3 build_skills.py` and commit the regenerated copies with the change. The ChatGPT manifest follows the Agent Plugins standard (a root `plugin.json`), which ChatGPT accepts; OpenAI's own plugins use `.codex-plugin/plugin.json`. The manifest is `plugin.json` for ChatGPT, with a matching `.claude-plugin/plugin.json` for Claude (claude.ai, Cowork and Claude Code); keep the two in step. Run `python3 check_links.py` before releasing; it checks the links, that the manifests agree, and that every skill's copies match the shared files.

See VALIDATION.md for what has been checked and SOURCES.md for provenance. Original text and code are MIT licensed; linked external content keeps its own license.

## Before you rely on it

The plugin guides an assistant; it does not check your science. Review what it produces, as you would a new collaborator's work, before it goes into a plan, a paper or a decision. VALIDATION.md lists what has and has not been tested.

New to skills? See [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills) (Claude) or [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).
