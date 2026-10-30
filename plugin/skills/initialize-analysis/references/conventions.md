# Shared conventions and boundaries

This plugin serves R analysis projects, not R packages. Do not introduce DESCRIPTION, NAMESPACE, roxygen, pkgdown or CRAN requirements by default.

| Location | Responsibility |
| --- | --- |
| analysis-plan.md | Scientific questions, definitions, estimands, methods and sensitivity analyses; cites references.bib for the provenance of each sourced decision. See [writing the plan](analysis-plan.md) |
| GitHub Issues | Open scientific decisions (decision issues), implementation gaps between code and plan, and known defects |
| REPOSITORY-BLUEPRINT.md | Intended organization; retain bundled text unchanged |
| ARCHITECTURE.md | Actual implemented structure and data flow, with revision scope |
| AGENTS.md | Shared contributor conventions, restrictions and project-specific implementation guidance |
| Personal project instructions | User's role, preferred assistance, authorized actions and private reference pointers |
| references/ | Supporting technical detail and evidence, not a competing analysis plan |
| references.bib | Verified citation metadata |

Read applicable guidance before substantive work. Repository rules and data restrictions are not waived by a collaborator's wider autonomy. Follow host instruction precedence; surface conflicts without silently rewriting either scientific or permission boundaries. The presence of a plugin does not grant access or permission.

R/main.R ordinarily orchestrates definitive stages in dependency order; R/setup.R centralizes paths, dependencies and shared parameters. R/functions.R or appropriate subdirectories hold reusable helpers. R/tables.R and R/figures.R generate or orchestrate outputs. Prefer explicit arguments, portable paths and labelled variables with units/time windows. Keep script role, inputs and outputs in a short header. Avoid unrelated stylistic rewrites.

## Writing R code

Write R that a clinician-analyst who learned R from online guides can read. Use pipes and dplyr/tidyr verbs for data, stringr or glue for text (not sprintf, formatC or gsub), and case_when() instead of nested if. Repeating the same steps over subgroups, years or models is fine as a for-loop over names, or a named list indexed by name (results[[group]][[year]]). Avoid the apply family, Reduce, do.call(rbind, lapply()), indexing by position ([[1]], [, 3]) and reshaping with matrix(), rep(each=) or sweep(). Prefer a plain step over a clever one. Where base R is required (matrix algebra for pooling, model internals), keep it inside a named, tested function with a comment saying why. Before calling a package's functions, read their documentation for the installed version, including NEWS; don't rely on memory. Bring existing code into line only in a style-only pull request: no change to logic, constants or model formulas, tests unchanged, and the pull request shows that every fitted model and table is identical before and after (for example all.equal(), reporting only TRUE or FALSE). Load r-tidyverse-style before writing R code, if installed. A project's established conventions win over this paragraph.

Scientific choices belong in the plan; unresolved ones are decision issues linked from the passage they affect, never settled in code. Verify unknown fields, codes and definitions against authoritative documentation rather than infer from names. Report disagreements among code, plan and narrative. Definitive analysis needs substantive Quarto explanations using actual code; exploration does not require immediate publication. Update relevant links/navigation when code changes and use Posit describe-design for material architecture updates.

Reference recommendations are project-specific: data dictionaries, release notes, operational definitions/code lists, evidence summaries, API notes and validated synthetic worked examples. Prefer .md for repeatedly consulted text, retain provenance, version/release, source URLs and page/section locations, and label conversions as derived. Preserve originals when formatting matters. Do not create empty category files. Do not publish private IRB materials, restricted data or unlicensed paper copies merely because they were supplied for review.

Changes reach the default branch through pull requests; see [GitHub workflow](github-workflow.md).

At the end of a working session, ask whether anything unfinished (a draft change, text waiting on someone's approval, a request still to send) should be saved to the repository, and offer where: a draft pull request, an issue comment marked as a draft, or a new issue. Check it against the project's disclosure rules first; anything holding results from restricted data that are not cleared for release stays where it is, and the person is told why. A new chat will not remember it.

How much to ask before acting depends on the person's working style, set in their personal instructions. If none is set, work step by step.

- **Review only:** read, review and suggest; change nothing.
- **Step by step:** before changing anything, say what will change. If several things would change at once (for example a pull request with the plan, the website and several issues), ask whether to build it all now or one piece at a time. Show each file where they can read it (the host's file pane or preview, if it has one) before the change and again after it, one file at a time. Make each change once they agree.
- **Hands-off:** build the agreed work on branches and open pull requests without asking at each step or showing each file.

In every style:

- **Walk through what was made.** Afterwards, walk the person through what was made in their name: where to see it, what each piece is, and what they should read before anyone else does, pitched at what they have said about their experience.
- **Posting as a person.** Before posting or sending anything as a person (an issue comment, a pull-request description, an email), show them the exact text and wait for their go-ahead, unless their own instructions waive this. A hands-off style covers only the pull requests it opens. When writing that a person decided, said or wrote something, link the record it comes from (an issue comment, commit, or email relayed in an issue); if there is none, ask rather than attribute it.
- **Optional alternatives.** When there is more than one reasonable way to write something (a simplification, a refactor, another method or package), or the person asks to see a change before deciding, propose it before committing it, even when the style is hands-off. Draft it outside the repository. For code, run the current and proposed versions on synthetic data and say whether every output is identical, and if not, exactly what differs. Show the change side by side (current left, proposed right, removed lines red, added green, long unchanged stretches collapsed) where the host can display it, otherwise as a unified diff, and attach the full proposed file. Give a small table of the trade (lines of code, steps or model fits, run time, outputs) and one line per change saying what it removes or adds and why. List separately anything that changes behaviour. Commit only after the person agrees. If they have not decided when the session ends, offer to save it as a draft pull request marked as a proposal.
- **Scientific choices** go to the deciders as decision issues; agents never make them.

If files uploaded to a person's LLM project differ from the repository's copies, the repository wins unless the person says theirs is newer; then compare the two and show them the differences before anything changes. Otherwise tell the person the files have drifted.

Work on the right copy. If the person's local folder is connected, use it, including uncommitted changes. Otherwise use the GitHub repository named in their instructions, at the branch, pull request or commit they name, or the default branch. Never ask them to connect a folder merely to begin. Say which copy and revision you used; when working from GitHub, say that unpushed changes are not included.

Before asking a person something, look for the answer in the repository (the analysis plan, AGENTS.md, issues and pull requests) and in earlier chats in their project where you can see them. Ask only what is still unclear, and say what you found. This does not replace the approvals their working style asks for.

When telling someone where to click in GitHub, ChatGPT or another app, use the steps in this plugin where they exist; otherwise check the app's current help pages, or say you are not sure of the exact menu and describe what to look for.
