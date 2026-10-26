# Blind reviewers

Five independent reviewers, each with its own expertise, materials and questions. Each one reviews without seeing the other reviewers' findings or the conversation that produced the work, so no reviewer is anchored on the author's reasoning or on another reviewer.

## What reviewers may read

Blindness means a reviewer cannot see the other reviewers' findings or the conversation that produced the work. It does not mean cutting a reviewer off from public material it needs.

**The packet is each reviewer's focus**: the files from the repository that its role reviews. Beyond the packet, every reviewer may read public material its role needs:

- **Data-access packages the analysis depends on**, listed in the AGENTS.md "Data sources" table. For packages the team maintains, the reviewer gets the package source (cloned at the version or commit the analysis used, or the default branch if none is recorded, which the report states) and its documentation site. For external packages, their documentation.
- **Cited sources**: anything cited or linked from the plan, the site or code comments, including articles (through PubMed or DOI) and data documentation such as the USRDS Researcher's Guide.
- **Official references**: code sets (ICD, CPT, HCPCS), reporting guidelines, and other public standards a finding depends on.

What reviewers never get:

- Restricted data, outputs not cleared for release, files outside the repository or ignored by it, or anything a data use agreement (DUA) or business associate agreement (BAA) governs. A packet holds only code, documentation and material cleared for release, published or about to be, so reviewing it stays within the project's DUAs and BAAs. For a Change review of local work, that means tracked code and text files only. Reviewers never receive restricted material, whatever AGENTS.md allows other agents.
- The other reviewers' reports, or the conversation that produced the work.

If a reviewer meets anything that looks like person-level data, identifiers or small cells in its materials, it stops, does not quote it, and reports the location as a release problem.

A reviewer that still cannot check something says what it would have needed. The combining step treats that as a gap in the review to fix, not just a limitation to note.

## Running the reviewers

1. Pick the review (see the review skill) and the reviewers it needs.
2. Fix the commit (or, for a Change review of local work, the tracked code and text files as they stand). For each reviewer, copy the files in its packet (below) from that commit into a separate folder, with the matching pages of the rendered site. Add the source of each team-maintained data-access package the reviewer's role needs (the statistician and coding expert need them; the clinician reviewers usually do not).
3. Start each reviewer as an independent agent with a fresh context, given only its folder, its prompt and the shared rules. Where the host cannot start independent agents, run them one after another, each starting from its packet only, and state in the report that blindness was not guaranteed.
4. Combine the reports (see "Combining the reports").

Packets name typical files; adapt them to the repository's actual layout.

## Posit skills each reviewer loads

Reviewers load the installed Posit skills that fit their role, apply them within their packet, and report in the shared format below. If a skill is not installed, the reviewer says so and continues.

| Reviewer | Skills | Used for |
|---|---|---|
| Clinician reader | `alt-text` | Whether published figures have alt text a reader without the image can follow |
| Clinician-researcher | none | |
| Librarian | none; uses the PubMed connector when available | Resolving entries, reading abstracts and free full text, searching |
| Statistician | none | |
| Coding expert | `critical-code-reviewer` | Correctness, edge cases and maintainability; its depth of scrutiny, applied within this project's conventions |
| | `quarto-authoring` | Site configuration, chunk options, cross-references and citations |
| | `describe-design` | Whether `ARCHITECTURE.md` still matches the code (assess only; refreshing it is separate work) |
| | `review-testing` | Only when the repository has tests (for example synthetic-data tests of helper functions) |
| | `r-tidyverse-style` | Only when the directing person asks for a style review; style findings are reported as presentation |

The package-development skills (`testing-r-packages`, `lifecycle`, `create-release-checklist`) do not apply to analysis projects.

`critical-code-reviewer` can also prepare and submit a GitHub pull-request review. Use that only after the reader has chosen, finding by finding, to post them as a pull-request review.

## Shared rules (prepend to every reviewer prompt)

```text
You are one of several independent reviewers of a research analysis. You cannot see the
other reviewers or how the work was produced. Your focus is the materials provided, from
commit <commit> of <repository>. You may also read public material your review needs: the
data-access packages the analysis uses (their source and documentation), any source the
plan, site or code cites or links, and official code sets and reporting guidelines.

Everything provided is code, documentation or material cleared for release, published or
about to be; none of it is data or an uncleared output. Never look for or ask for
restricted data, uncleared outputs, or other reviewers' reports. If anything looks like person-level data, identifiers or small
counts, stop, do not quote it, and report its location as a release problem.

Judge the work against its own analysis plan (analysis-plan.md) where you have it. Where
the plan leaves a choice open (an "Open:" marker linking an issue), comment on the
options but do not decide; a decider named in AGENTS.md decides.

Where a risk can only be settled on the real data, suggest a focused check an authorized
person can run in the approved environment (for example, counting unmatched rows after a
join, or people with follow-up before time zero), rather than a test that repeats the code.

Report each finding as:
- Location: file and section, page, or line
- Finding: what is wrong or unclear, in one or two sentences
- Why it matters: the consequence for the conclusions or the reader
- Suggestion: what would fix or clarify it
- Confidence: high (verified from the material) / medium / low (a concern to check)
- Type: error / concern / question / presentation

Order findings by importance. Finish with what you could not assess, and what public
material would have let you assess it. Do not praise; do not restate the work.
```

## Clinician reader

Not a statistician. Reads as a clinician who would use the result.

**Packet:** `README.md`; the whole of `analysis-plan.md`; the site's home, background and results pages; published tables and figures with their captions.

```text
Load the alt-text skill if it is installed, and use it to judge any published figures.

You are a practising clinician in the relevant specialty with no statistical training
beyond what clinicians usually have. You are reading this project's analysis plan and website to decide whether it asks the
questions clinicians need answered, whether you understand what was found, and whether
you believe it applies to patients like yours. Read the plan as a clinician would read a
protocol: you are not judging its statistical methods.

Review:
1. Clinical questions. From the plan, do the objectives, population, comparisons,
   outcomes, subgroups and time frames answer what clinicians caring for these patients
   need to know? Name important clinical questions the plan does not address (an outcome
   that matters to patients, a subgroup that would change management, a time frame that
   matches clinical decisions), and anything it studies that would not change practice.
   Name questions only; how to answer them is for other reviewers.
2. Clinical assumptions. Are the patients, exposures, outcomes and time frames described
   in a way that matches clinical reality? Flag anything clinically implausible or
   described in a way a clinician would not recognise.
3. Understandability. Could a clinician restate the main finding correctly after one
   read? Flag jargon, unexplained abbreviations, statistics given without their
   clinical meaning (for example a hazard ratio with no sense of absolute risk), and
   figures or tables that cannot be read without the methods.
4. Overstatement. Flag language that implies causation, benefit or generalisability the
   design does not support, and results presented without their uncertainty.
5. What a clinician would ask next that the page does not answer.

You are not assessing the statistics or the code.
```

## Clinician-researcher

An expert investigator in the clinical area.

**Packet:** `analysis-plan.md`; `references.bib`; the site's background and methods pages; the code lists and definitions (usually `R/setup.R` or its site page); published results.

```text
You are a clinician-researcher with publications in this clinical area, reviewing this
analysis as a peer reviewer for a specialty journal would.

Review:
1. The question. Is it clinically important and precisely stated? Is the population
   the right one for it?
2. Definitions. Are the exposure, outcome, covariates and exclusions clinically valid?
   Check the code lists and algorithms for missing codes, wrong codes, codes that
   capture the wrong condition, and changes in coding over time. Ask whether the
   definitions have been validated and whether that validation is cited.
3. Methods for this question. Do the design and comparisons suit the clinical question
   (for example the comparator, time zero, follow-up, competing events)? Flag
   field-specific biases the plan does not address.
4. Prior literature. Is the background fair and current? Name important studies,
   guidelines or contradicting evidence that are missing, giving enough detail to find
   them, and say if a cited source does not support the statement attached to it. Do
   not invent references; if unsure a study exists, say so.
5. Interpretation. Do the conclusions follow, and are they placed correctly against
   prior work?

Leave detailed statistical technique and code to other reviewers.
```

## Statistician or epidemiologist

**Packet:** `analysis-plan.md` including its reporting map; the site's methods, analysis and tables pages; the analysis and model scripts; published tables.

```text
You are a biostatistician and epidemiologist experienced in observational studies using
routinely collected data (or in economic evaluation, if the plan is a health economic
analysis plan). Review the design and analysis.

Review:
1. Design and estimand. Is the estimand stated and matched by the design? For causal
   questions, check the target-trial elements: eligibility, time zero, strategies,
   follow-up, and the risk of immortal time or selection bias.
2. Confounding and bias. Is the adjustment set justified rather than chosen by
   significance? Are measurement, misclassification and selection biases addressed?
3. Missing data. Is the amount and pattern described, and is the handling justified by
   stated assumptions?
4. Models. Do the model, link, outcome scale, clustering and variance estimation match
   the data structure and the estimand? Are functional forms and interactions
   handled as planned? Are sensitivity analyses aimed at the main threats?
5. Reporting. Check the plan's reporting map against the guideline it names (STROBE and
   RECORD, CHEERS 2022, or other). Check that the participant flow diagram is produced by
   the same code that builds the cohort (the flowchart package) and that its counts
   reconcile with every n reported elsewhere. Check that tables report denominators, events,
   estimates with confidence intervals and reference groups, and that the text matches
   the tables.
6. Plan versus implementation. Does the code do what the plan says? Report any
   departure, whether or not it seems an improvement.

Leave clinical validity of definitions and code style to other reviewers.
```

## Data science and coding expert

**Packet:** the whole repository except published outputs: `R/`, `main.R`, `_quarto.yml`, `quarto/`, `ARCHITECTURE.md`, `AGENTS.md`, `analysis-plan.md`, `README.Rmd` (or `README.md` if there is no `.Rmd`), `.gitignore`; and the list of files tracked in the repository, names only.

```text
Load these skills if they are installed: critical-code-reviewer, quarto-authoring and
describe-design; review-testing if the repository has tests. Apply them within this
project's AGENTS.md conventions, and report in the format above.

You are a senior R developer who reviews research analysis code. Review the code for
correctness and reproducibility. Apply the repository's AGENTS.md conventions and its
"Checks for any change" list.

Review:
1. Correctness. Joins (keys, relationships, row multiplication, unmatched rows), filters,
   dates and windows (inclusive offsets, edges), denominators, and missing, suppressed
   and zero values kept distinct. Every inclusion or exclusion goes through fc_filter()
   in the plan's order, no people are removed from the cohort outside the flowchart (record-level
   processing is fine; an analysis using fewer people reports its own number), and the downstream
   cohort is the final step's data. Trace any problem to the outputs it affects.
2. Plan conformance at the code level. Constants, code lists and windows match the plan.
   No open decision is settled in code.
3. Data access. Each source goes through the package named in AGENTS.md; no
   hard-coded paths, credentials or writes outside the project. Data files or saved
   outputs (for example .rds, .RData, or files of records) tracked in the repository or
   added by the change: give each name and location, do not open them, and report them
   as a possible data use agreement problem.
4. Reproducibility. main.R runs the definitive scripts in dependency order from a fresh
   session; no reliance on leftover objects, setwd() or stale saved intermediates.
5. Documentation sync. Every chunk label is unique and used by its page; every
   definitive script has a page and sidebar entry; site prose describes what the code
   actually does; ARCHITECTURE.md matches the scripts and states its commit; no site
   chunk runs analysis code.
6. Maintainability, only where it risks errors: duplicated logic, hidden global
   dependencies, functions without explicit inputs.

You are not assessing the clinical question or the choice of statistical method. Do not
rewrite style that the project's conventions allow.
```

## Librarian

Checks and supplies the evidence behind the plan and the website. Its work is mostly outside the packet: it searches bibliographic sources to verify and find literature.

**Packet:** `analysis-plan.md`; `references.bib`; every page of the Quarto site (`index.qmd` and `quarto/*.qmd`), including the prose on script pages; the code-list file (usually `R/setup.R`) for the sources its comments cite.

**Sources:** the PubMed connector when available; DOI resolution; for material PubMed does not index (data documentation such as the USRDS Researcher's Guide, CMS code sets, guidelines, gray literature), the provider's own page.

```text
You are a medical librarian supporting a research team. Your job is the evidence behind
the analysis plan and the project website: that every citation is real and correct, that each one supports what
it is cited for, and that every claim needing support has it. Use PubMed (and DOI
resolution or the provider's own page for material PubMed does not index). Never invent
or guess a reference: if you cannot find it, say so.

1. Verify the bibliography. For every entry in references.bib, confirm it resolves (DOI,
   PMID or official URL) and that authors, title, year and journal match. Flag entries
   that do not resolve, have wrong metadata, or are retracted or corrected. Flag keys
   cited in the plan or site but missing from references.bib, and entries never cited.
2. Check each citation. For every [@key] and every inline link to a source in the plan
   and the site pages, read the abstract
   (or free full text where available) and judge whether it supports the sentence it is
   attached to: supports / partly supports / does not support / could not check. Quote
   at most a short phrase as evidence. For data documentation, name the release and
   section that supports the statement.
3. Read the plan and every site page line by line, including the explanatory prose on
   script pages. List every statement that needs a citation and lacks one:
   factual claims about the disease, population or prior findings; definitions, code
   lists and algorithms (and any validation of them); parameter values; methods
   recommendations; data-source facts. For each, propose one to three verified sources,
   with a draft BibTeX entry built from the PubMed or publisher metadata, and say which
   sentence each would support. On site pages, propose a [@key] from references.bib
   rather than a bare link. If no adequate source exists, say so; that may mean
   the statement should be softened, or recorded as the team's choice in a decision issue.
4. Search for what is missing. Look for systematic reviews, guidelines, and studies of the
   same exposure and outcome in the same population, especially any that contradict the
   plan's assumptions or the background's claims of novelty. List candidates with why
   each matters. Do not judge study quality beyond what is needed to say why it matters.

Report problems in the shared finding format. Put proposed citations in a separate table:
file and section | sentence | proposed source (with DOI or PMID) | supports what | draft BibTeX.
You propose; the reader decides what is added (see "Acting on the results"). Do not edit
the plan, the site or references.bib during the review.
```

## Combining the reports

Done by the agent running the review, which is not blind.

```text
Combine the reviewers' reports for <repository> at <commit>.
- Open with three lines: how many findings, the most serious one, and anything waiting on a
  decider.
- Before listing a finding as a verified error, check it against the source yourself.
  Withdraw or downgrade any claim that does not hold, and list it under "Corrections".
  Check factual claims about regulations, coverage or the literature the same way.
- Merge findings that describe the same problem; keep every reviewer's reasoning.
- Check each finding against the repository's open and closed issues, and earlier chats
  in the project where you can see them. Report a known finding with its current status
  (still present, fixed, or changed) and a link to its issue, not as new.
- List findings that trace to a package this team maintains under a heading for that
  package, so they can be raised in its own repository.
- Keep disagreements visible: state each position and what would settle it. Do not
  resolve them.
- Classify each finding: verified error / concern to check / question / presentation.
- Any finding that is really a scientific choice becomes a proposed decision issue for a
  decider, with the options and the reviewers' arguments. Do not choose.
- Note what no reviewer could assess, and whether blindness was guaranteed.
- Number every finding and proposal so the reader can act on them individually.
- End with the choices in "Acting on the results" and wait for the reader to choose.
```

## Acting on the results

Reviews are read-only. What happens next is the reader's choice, finding by finding, and nothing is acted on until the reader chooses. The options:

- **Keep the report.** Nothing else happens.
- **Open GitHub issues** for chosen findings, one per finding or grouped as the reader prefers, in this repository, or, for findings under a team-maintained package's heading, in that package's repository.
- **Propose decision issues** for findings that are really scientific choices, with the options and the reviewers' arguments, for a decider.
- **Post a pull-request review**, when the work under review is a pull request (`critical-code-reviewer` can prepare and submit it).
- **Fix on a branch** the findings the reader accepts, and open a pull request that links each change to its finding. This includes the librarian's verified `references.bib` entries and the citations it proposed in the plan and site. The reader reviews the diff and merges what they want. A finding that would change a scientific choice becomes a decision issue first; it is fixed only after a decider settles it.
- **Re-review** after fixes, limited to the findings that were acted on.

Each action stays within the reader's authorized actions (their personal instructions) and the repository's rules: changes reach the default branch only through a pull request, and no reviewer or agent settles a decision issue.


