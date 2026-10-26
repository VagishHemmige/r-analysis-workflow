---
name: report-analysis
description: Build and check the reporting of an R biomedical analysis with flowchart, gtsummary, ggplot2 and ggsurvfit - the participant flow diagram, figures and survival curves with risk tables, descriptions and missingness, Table 1, two-variable, longitudinal and time-to-event summaries, fitted-model tables, and numbers quoted in prose. Does not choose models, covariates or estimands. For an independent check, use the Reporting review in the review skill.
---

If the linked plugin files cannot be opened, say so and continue from the repository's own AGENTS.md and analysis plan; do not guess their contents.

Read [reporting guidance](../../references/reporting.md), [conventions](../../references/conventions.md), the analysis plan and the project's AGENTS.md first.

## Boundaries

- **The plan decides; reporting follows.** Model, covariates, functional forms, estimand, missing-data handling and the target journal's style come from the plan. Where the plan leaves one open, open or point to a decision issue instead of choosing through a reporting helper.
- **Data.** Write and test reporting code on synthetic data. Agents do not read restricted data; real results are produced by an authorized person in the approved environment, and every table, figure and flowchart box passes the project's disclosure rules (see [data handling](../../references/data-handling.md)) before it leaves.
- **Code.** Write calls as `package::function()`. Check the installed package versions and their official documentation before giving recipes that depend on version. Link to the references; do not copy them.

## Order of work

Follow the sections of the [reporting guidance](../../references/reporting.md) in order, using those that apply to the design:

1. **Participant flow:** the cohort built with the flowchart package, so the diagram and the analytic data come from the same code.
2. **Descriptions and missingness:** every analysis variable, with missing counts shown, and missingness patterns.
3. **Table 1:** by the plan's grouping, with the journal theme when one is chosen.
4. **Two-variable and stratified summaries**, as the plan calls for.
5. **Longitudinal structure**, when observations repeat over time.
6. **Time to event:** follow-up, events and censoring before any model.
7. **Figures:** principles first, KMunicate-style survival curves with risk tables, and small-count rules for every count shown.
8. **Fitted models:** tables that report the model actually fitted.

## Checks before finishing

- Every n in tables, figures and prose reconciles with the flow diagram.
- Estimates, confidence intervals, model N and events, reference categories and scales (odds, hazard or rate ratios; dollars or geometric means) match the fitted model and are labelled correctly.
- Every number in prose comes from a computed object (`gtsummary::inline_text()` or another object), never retyped.
- Figures have captions and alt text.
- Say which checks ran on synthetic data and which were only read; code inspection is not reproduction.

Then offer the Reporting review in the review skill for an independent check.
