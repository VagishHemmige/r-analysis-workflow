# Writing analysis-plan.md

`analysis-plan.md` is the scientific source of truth: what the analysis must do, independent of how the code is organized. It sits at the repository root. Code implements it; code never redefines it.

## Rules that apply to every plan

**Open decisions live in GitHub Issues, not in the plan.**

- Each unresolved design choice is one **decision issue**: a GitHub issue that states the choice, the options, and the evidence for each. Mark decision issues however the project marks issues (a label, a title prefix); the plugin does not prescribe one.
- The plan marks the open point where it occurs, linking the issue: `**Open:** [#14](../../issues/14)`. It does not keep a separate table of decisions.
- **Anyone may open or contribute to a decision issue**: any collaborator, and any agent working for one. Contributions are options, evidence and arguments.
- **Only a named decider settles it.** `AGENTS.md` lists who makes scientific decisions for the project, and their areas. The decider states the choice in the issue. A decider who does not use GitHub can decide by email or in a meeting: whoever received the decision posts the decider's exact words in the decision issue, with their name, the date and how it was given (for example "by email to <name>"), and that settles it as the decider's decision. A decision that is only summarized or remembered does not settle it.
- **A decision takes effect when the plan changes.** A pull request that closes the issue (`Closes #14`) rewrites the passage to state the decision and its reason, cites the evidence, and removes the **Open:** marker. Anyone may write that pull request once the decider has stated the choice; it counts when merged into the protected default branch.
- **Agents implement decisions; they do not make them.** An agent may draft options, and may write the plan change and code for a choice a decider has stated. It never chooses among options on its own, in the issue, the plan or the code. A person may give their own agents stricter rules in their personal instructions.

**Cite the provenance of decisions.**

- Every definition, threshold, code list, parameter value, or method taken from an outside source cites it with a `[@key]` from the root `references.bib`.
- Verified entries for the reporting guidelines named here are in [the plugin's guideline file](../assets/guidelines.bib); copy into the project's `references.bib` only those its plan cites.
- Every key must resolve to a verified entry (DOI, PMID, or official URL plus the release or version used). Never invent a citation, and never cite from memory without checking the entry.
- For data documentation (for example the USRDS Researcher's Guide or an SRTR data dictionary), cite the specific release and give the appendix, section, or page.

**Record changes in git.**

- While the plan is a draft, git history is the change record. Commit each design change on its own. The commit message gives the reason and says whether any results that depend on it had already been seen.
- When the plan is locked (before outcome data are analyzed, or at registration), tag the commit (`sap-v1.0`) and, if registering, cite the OSF or other registration and the tag in the plan header. From then on, every change also gets a dated entry under **Amendments after locking**, saying what changed, why, and whether it was made before or after seeing outcome data, plus a new tag (`sap-v1.1`).

**Keep it a plan.** No results, no implementation status (that belongs in Issues), no code structure (that belongs in `ARCHITECTURE.md`), no working conventions (that belong in `AGENTS.md`).

## Choosing the variant

| Study type | Reporting guideline | Template |
|---|---|---|
| Observational study using routinely collected data (USRDS, SRTR, claims, registries, EHR) | STROBE + RECORD [@vonelm2007strobe; @benchimol2015record] | A |
| Observational study with a causal question | Consider target-trial emulation; if used, add TARGET [@cashin2025target] | A, plus Appendix A if used |
| Economic evaluation or decision model | CHEERS 2022 [@husereau2022] | B |
| Descriptive, geographic or access analysis | STROBE + RECORD, with the analysis framed as descriptive | C |

Other designs (trials, diagnostic accuracy, prediction models) use their own guideline (CONSORT, STARD, TRIPOD+AI [@collins2024tripodai]) with the same shared head and tail. Ask before inventing a section structure for them.

The guideline sets what must be *reported*; the plan still has to state every *decision*, including ones the checklist does not ask about.

## Shared head

```markdown
# <Analysis plan | Health economic analysis plan>: <title>

<Status: draft | locked as sap-vX.Y on YYYY-MM-DD | registered: <DOI>>

## Scope and reporting framework

This document is the authoritative specification of the study's scientific objectives,
population, definitions, estimands and statistical methods. `ARCHITECTURE.md` documents
the implementation, `AGENTS.md` the working conventions, and GitHub Issues the open
decisions and implementation status. Neither file supersedes this plan.

Reporting will follow <guideline> [@key]. The reporting map below links each checklist
item to a section of this plan.
```

## Template A: observational, routinely collected data

1. **Objective** — question, hypotheses stated in advance, primary vs secondary vs exploratory.
2. **Design** — design type, and for causal questions the estimand, with a pointer to Appendix A if target-trial emulation is used.
3. **Data source** — database, release, files and components used, linkage, observation window, data currency; whether the investigators have already used this release (secondary-data declaration).
4. **Study population** — source population, eligibility, exclusions in order (each becomes one flowchart step), index event.
5. **Exposure and time zero** — definition with code lists and matching rules (exact or prefix, ICD-9 and ICD-10 by date), diagnosis date rule, time zero; covariates and when they are measured (at or before time zero, or time-varying if the plan uses them).
6. **Comparator or matching** — when used: comparator definition, matching variables, ratio, method, balance criteria.
7. **Outcomes** — definition, measurement window, follow-up and censoring events.
8. **Statistical analysis** — descriptive analysis (Table 1, missingness), estimand, primary model, secondary analyses, effect modification and subgroups, multiplicity, missing data, software.
9. **Sensitivity analyses** — each with the assumption it tests.

## Template B: economic evaluation

1. **Decision problem and objective**
2. **Comparators**
3. **Population and setting**
4. **Perspective, time horizon, discounting and currency** — price year and index.
5. **Model** — type, structure, required structural features.
6. **Inputs** — definitions, sources (each cited), distributions, correlated inputs.
7. **Health outcomes** — endpoint, utilities.
8. **Costs** — costs vs payments vs charges, price year.
9. **Analysis** — reference case and decision rule, scenario, one-way, threshold, probabilistic, value of information, heterogeneity, software.
10. **Validation**
11. **Engagement and distributional effects**

## Template C: descriptive, geographic or access

1. **Background and rationale**
2. **Objectives** — primary descriptive, secondary, exploratory.
3. **Study design and setting**
4. **Data sources and measurement periods**
5. **Study populations and unit definitions** — exclusions in order (each becomes one flowchart step)
6. **Estimation** — allocation, suppressed or imputed counts.
7. **Linkage and geography**
8. **Measures and outcomes** — catchments, inclusion rules, denominators.
9. **Analysis and interpretation** — including what may and may not be inferred.
10. **Missing data and validity requirements**
11. **Sensitivity analyses**

## Shared tail

Number these after the variant's last section.

- **Disclosure control** — the governing DUA or policy, the small-cell rule, complementary-cell suppression, figures that may not be published.
- **Limitations to address in reporting**
- **Reporting map** — one row per checklist item:

  ```markdown
  | Checklist item | Topic | Plan section |
  |---|---|---|
  | STROBE 6 / RECORD 6.1–6.3 | Eligibility, selection codes and algorithms, validation, linkage | 4, 5 |
  ```

- **Amendments after locking** — only once the plan has a `sap-v` tag.
- **References** — rendered from `references.bib`; no hand-typed reference list.
- **Appendix A: Target-trial protocol** — only when target-trial emulation is used: eligibility, treatment strategies, assignment, time zero, follow-up, outcome, causal contrast, analysis plan, each mapped to how the emulation achieves it.

## When drafting a plan

- Start from the investigator's materials (protocol, IRB, prior RMD, papers). Extract the choices the materials already make and present them together, as one list, for the deciders to confirm or change. A choice a decider confirms goes into the plan as decided; anything else gets a decision issue. Choices settled in a signed protocol or IRB approval count as decided, and are cited as such.
- Verify every code, variable and definition against the authoritative release-specific documentation. Never infer a variable's meaning from its name.
- Check that each section a checklist item needs exists, using the reporting map, before calling the plan complete.
