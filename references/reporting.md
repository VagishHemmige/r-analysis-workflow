# Biomedical EDA, Table 1 and fitted-model reporting

Links provide implementation details; do not reproduce source chapters or documentation. Model decisions belong in analysis-plan.md. Always write calls as package::function(), including ggplot2::aes() and helpers; operators and locally defined functions are exceptions. After rendering any table, check that every variable row shows its readable label, not the raw variable name.

## Participant flow (STROBE diagram)

Build the cohort with the [flowchart](https://bruigtp.github.io/flowchart/) package so that the diagram and the analytic cohort come from the same code and cannot disagree. Start with flowchart::as_fc() on the source population, apply every inclusion and exclusion with flowchart::fc_filter() in the order the plan lists them, and split into groups with flowchart::fc_split(). Never remove people from the cohort outside the flowchart. Record-level processing (cleaning claims, choosing among a person's records) is fine. An analysis that uses fewer people than the cohort (complete cases, a subgroup) reports its own number with that analysis. The cohort used downstream is the data from the final step, taken with flowchart::fc_view(what = "data"). Draw with flowchart::fc_draw() and save with flowchart::fc_export(). Build box labels from the constants in `R/setup.R` so they cannot go stale. This is the flow diagram for STROBE item 13 and RECORD 13.1. Apply the governing small-cell rule to every box, including counts recoverable by subtraction, before the diagram leaves the approved environment.

## Descriptions and missingness

Describe every analysis variable with gtsummary::tbl_summary(), excluding identifier fields from meaningless distribution summaries. Check types, labels, units, impossible values and documented missing sentinels; do not automatically recode valid zero/999 values. Use median/IQR for skewed continuous variables or mean/SD when appropriate, set explicitly with statistic; categorical n (%). Inspect continuous histograms using ggplot2::geom_histogram() with several sensible bin widths and categorical counts with ggplot2::geom_bar(). Respect disclosure limits.

Show missing counts for each descriptive variable, including zero when requested by this workflow. Default tbl_summary behavior is only-if-any. In the checked 2.6.1 documentation use `missing = tidyselect::everything() ~ "always"`, `missing_stat = "{N_miss}"`; check compatibility with installed versions. Check jointly missing variables and missingness associations with finalfit::missing_pattern(), finalfit::missing_pairs() and finalfit::missing_compare(). These descriptions do not establish a missing-data mechanism or choose imputation.

## Table 1 and paired/stratified descriptions

Use gtsummary::tbl_summary(by = exposure), with the actual design-appropriate grouping. No baseline significance tests in RCTs. Set gtsummary::theme_gtsummary_journal() before tables when a journal theme is selected; ask/retain the intended journal rather than choose one silently. Use readable labelled metadata or explicit labels. A missing grouping category can be displayed with forcats::fct_na_value_to_level() on a factor; do not silently change analytic missingness handling.

Use gtsummary::tbl_cross() for two categorical variables and choose row, column or cell percentages explicitly. Use gtsummary::tbl_continuous() for a continuous variable across two categorical variables, gtsummary::tbl_strata() for strata, and gtsummary::add_difference() for appropriate differences and CIs. For paired tests use gtsummary::add_p() with the chosen paired test and group = id; verify pairing and missing pairs. Test choices remain consistent with the plan.

## Longitudinal data only

Describe participants observed at each visit, dropout, intermittent missingness and death distinctly, visit-timing irregularity and individual trajectories on an appropriate subset using ggplot2::geom_line(ggplot2::aes(group = id)). Keep participant and observation denominators separate. Follow Lusa et al. and the linked R report for further implementation.

## Time to event

Describe follow-up (median follow-up, number of events, censoring) before any model. Use the estimators the plan specifies (usually Kaplan-Meier curves and Cox hazard ratios), and check proportional hazards whenever a Cox model is fitted. When the plan calls for them, use landmark analysis or time-dependent covariates (avoiding immortal time) and competing-risks methods (cumulative incidence, Fine-Gray or cause-specific hazards) instead of treating competing events as censoring. Follow [Zabor, Survival analysis in R](https://www.emilyzabor.com/survival-analysis-in-r.html) for implementation with survival, ggsurvfit, gtsummary and tidycmprsk.

## Figures

Start from the question the figure answers and who will read it, then choose the display. Follow the PSI/EFSPI Visualisation SIG's [graphics principles cheat sheet](https://graphicsprinciples.github.io) and its paper, [Vandemeulebroecke et al., "Effective visual communication for the quantitative scientist"](https://doi.org/10.1002/psp4.12455); use [Wilke](https://clauswilke.com/dataviz/) for which display suits which data. Build figures with ggplot2 (write `ggplot2::` calls), give every figure a caption and alt text, and pass the plot object to `ggplot2::ggsave()` explicitly.

**Survival curves.** Follow the [KMunicate recommendations (Morris et al., BMJ Open 2019)](https://doi.org/10.1136/bmjopen-2019-030215): show confidence intervals, and put a table under the plot with the numbers at risk, censored and with events. With ggsurvfit: `ggsurvfit::ggsurvfit()`, then `ggsurvfit::add_confidence_interval()` and `ggsurvfit::add_risktable(risktable_stats = c("n.risk", "cum.censor", "cum.event"))`. Label the time axis with its units and the y axis with what is estimated.

**Small counts in figures.** Risk tables, flowchart boxes, and annotations carry counts. Numbers at risk fall late in follow-up, so under a small-cell rule end the plotted follow-up, or suppress the cells, before any count drops below the threshold, including counts recoverable by subtraction. Figures that plot individual people (scatter, beeswarm, spaghetti plots of real records) are not published from restricted data.

**House style.** Figures start from the house style below. A person may ask for any change to a figure; follow their request. <House style to be written: theme, fonts, palette, export format, size and resolution, reusable plot types.>

## Model reporting

- Use gtsummary::tbl_regression() for the fitted model. Exponentiate log-odds/log-rate/log-hazard coefficients when appropriate; check family/link and label OR, rate ratio, risk ratio or HR correctly. Poisson exponentiation is not universally a risk ratio. Do not exponentiate identity-link or other incompatible coefficients.
- Show actual model N and events where meaningful using gtsummary::add_n() and gtsummary::add_nevent() when supported, or verified model-derived counts otherwise. Distinguish rows, participants/clusters and events. Report excluded/missing observations; pooled-imputation counts need special review.
- Lead with estimates and 95% CIs, keep reference rows, use readable variable labels, and avoid gtsummary::bold_p() as a significance highlighter. Use gtsummary::add_global_p() for appropriate multi-level terms only when its test and variance estimator match the approved analysis.
- When requested, put gtsummary::tbl_uvregression() crude estimates beside gtsummary::tbl_regression() adjusted estimates using gtsummary::tbl_merge(). Label them clearly and verify cohorts; univariable estimates are not a variable-selection rule.
- Explain splines/interactions with effect plots or clinically meaningful contrasts, consistent with the plan, rather than interpreting raw basis coefficients in isolation.
- For multiple imputation, pass the unpooled `mice` model object (the result of `with()` on the imputed data) to gtsummary::tbl_regression(); gtsummary's gtsummary::pool_and_tidy_mice() tidier pools it. Never pass an already pooled object. State the number of imputations, and check the pooled estimates and CIs.
- Mixed-model tidying commonly needs broom.mixed; confirm the actual class and whether fixed/random components are shown. Verify geepack::geeglm() extraction and variance convention for GEE; do not replace its intended covariance silently.
- Robust/clustered inference: gtsummary::tidy_robust() accepts vcov/vcov_args through parameters::model_parameters(). A wrapper can supply a chosen sandwich::vcovCL covariance; cluster identifiers must align with the fitted model's retained rows. Verify current documentation and compare estimates, SEs and CIs to the intended model calculation. Do not assume a global test automatically uses the same covariance.
- Use gtsummary::inline_text() for supported table-derived numerical prose rather than retyping; use other computed objects when that API cannot express the needed result.

## Implementation references

- [flowchart](https://bruigtp.github.io/flowchart/)
- [gtsummary](https://www.danieldsjoberg.com/gtsummary/)
- [Summary API](https://www.danieldsjoberg.com/gtsummary/reference/tbl_summary.html)
- [FAQ and Gallery](https://www.danieldsjoberg.com/gtsummary/articles/gallery.html)
- [Regression tutorial and supported models](https://www.danieldsjoberg.com/gtsummary/articles/tbl_regression.html)
- [Custom tidiers](https://www.danieldsjoberg.com/gtsummary/reference/custom_tidiers.html)
- [Higgins Table One](https://bookdown.org/pdr_higgins/rmrwr/building-your-table-one-with-the-gtsummary-package.html)
- [Wilke visualization, chapters 7–9](https://clauswilke.com/dataviz/)
- [PSI/EFSPI graphics principles cheat sheet](https://graphicsprinciples.github.io) and [Vandemeulebroecke et al. 2019](https://doi.org/10.1002/psp4.12455)
- [KMunicate, Morris et al. 2019](https://doi.org/10.1136/bmjopen-2019-030215) and [ggsurvfit](https://www.danieldsjoberg.com/ggsurvfit/)
- [R for Data Science EDA](https://r4ds.hadley.nz/eda)
- [finalfit missing-data vignette](https://cran.r-project.org/web/packages/finalfit/vignettes/missing.html)
- [Zabor, Survival analysis in R](https://www.emilyzabor.com/survival-analysis-in-r.html)
- [Lusa et al., 2024](https://doi.org/10.1371/journal.pone.0295726) and [longitudinal R report](https://stratosida.github.io/longitudinal/)

API documentation checked 2026-10-26 for summary missingness, regression tidying, pooling and robust-covariance interfaces. This is documentation verification, not execution validation of all package/model combinations. Check installed versions at use time.
