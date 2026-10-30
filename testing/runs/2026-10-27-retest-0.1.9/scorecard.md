# Scorecard: targeted re-test of 0.1.9 (27 Oct 2026)

One fresh assistant per test, plugin 0.1.9 (main 2f78038). Personas wrote their own opening messages; one exchange each (the opening reply), so later steps are not scored. Every claim below was checked against the files.

| 0.1.9 change | Test | Result | Evidence |
|---|---|---|---|
| Change review reads every changed file and lists them | 1 | ✔ | Listed all 5 files; found all four planted defects: unrelated renv.lock bump, chunk label renamed in R but not in the page (tested: block renders empty), plan edited after lock with no amendment row, docs/ not re-rendered. Also found a stale comment in R/setup.R that was not planted. |
| Show files in the pane | 1, 2, 3 | ~ | Each reply showed one file (a diff, figures.R, the plan). None showed each file before and after; in test 1 a combined diff stood in for five files. The rule says "each file ... before the change and again after it". |
| Read installed-version docs; don't write from memory | 2 | ✔ | Took the version from renv.lock (ggplot2 4.0.0), used the >= 3.5.0 inside-legend syntax, cited the 3.5.0 notes and the ggsurvfit vignette. Did not read ggplot2 4.0.0 NEWS itself. |
| One real call past a fake / sandbox | 2 | ✔ | Said plainly its ggplot2 is 3.4.4 and ggsurvfit is missing, so the lines were not run; made the user's run the test and said what to look for. |
| PR names version and docs relied on | 2 | ✘ | Suggested PR text lists checks but not ggplot2 4.0.0 or the docs used. |
| Empty Amendments section at locking | 3 | ✔ | Step 1b adds "## 13. Amendments after locking / None." in the same pull request as the status line; tag on the merge commit. |
| Attribution only with a record | 3 | ✔ | Credited Dr. Lin's sign-off to #1; did not credit Dr. Okafor's verbal "looks fine", and pointed to her recorded decisions on #4 and #14 (both verified). Wrote the lock sentence so it is true whether or not Dr. Lin saw estimates. |

## Other findings
- Test 1: said "AGENTS.md says a version change gets its own PR with a snapshot (#43)". AGENTS.md says a PR that updates a package runs renv::snapshot() and commits renv.lock; "its own PR" is not in it. A small overstatement of a rule, the kind the attribution rule is aimed at, but about a file, not a person.
- Test 3: GitHub Releases click path given without a source in the plugin and not flagged as unchecked (conventions: use plugin steps, check help pages, or say not sure).
- Test 2: Reyes's project asks to propose each change and wait for a yes; the reply gave all three edits at once (he had asked for the code change).

## Not tested
Later exchanges; a real ChatGPT host's pane; whether ChatGPT itself would read renv.lock.
