# Scorecard: continuation to publication (Test B, plugin 0.1.8, then 0.1.8 + readable-R changes)

Simulated time: 4 Jan 2027 (Dr. Patel leads) → 26 Apr 2027 (submission) → 4 Oct 2027 (major revision; Dr. Reyes, cardiology fellow learning R, leads) → 15 Mar 2028 (publication).
Plugin: 0.1.8 until simulated 11 Feb 2027; from then 0.1.8 plus the approved "Writing R code" changes (branch `tidyverse-readability`).
Scale: ✔ worked as the plugin intends · ~ partly, or only because a person caught it · ✘ failed.
Compressed weeks (marked in run-notes.md) are not scored: 15–26 Mar 2027, 5–26 Apr 2027, May–Sep 2027, 28 Oct 2027 – Mar 2028.

## What the plugin is meant to make happen

| Check | Result | Evidence |
|---|---|---|
| Decisions only by named deciders | ✔ | Every reviewer point became a decision issue (D10–D13) with whether/how split between Patel and Lin; switching the primary analysis after results was refused by the plan's own rule (#37, #39) |
| Decisions attributed to the right person | ~ | Assistant wrote "Dr. Patel: no per-doubling model" into code and pages when he had routed it to Lin (caught by Patel); "Lin co-wrote" an outputs line that was Maya's (caught by Lin) |
| Plan locked before results; amendments recorded | ~ | sap-v1.0 → v1.3 each with a section 13 row saying whether results had been seen. But the plugin's amendment rule never reached the repository (Lin invented section 13), and three "before any results were seen" claims proved false (#21, #26, plan section 8) |
| Claims about who saw what, when | ✘ | Three false timing claims (status line, read-off values, plan note) written by a person and by the assistant; each caught by Lin |
| Provenance of cited claims | ~ | When asked, quotes were verified (Dispenzieri, ?flchain, ICMJE, PLOS, survival docs, mice NEWS: all checked by the orchestrator and correct). Unprompted, a plan sentence overclaiming two papers was carried into the Methods; one BMJ "quote" was a paraphrase |
| Numbers in text from code | ✔ | Manuscript reads results.rds by inline R; provenance stamp (commit, tag, clean) on the draft; failure path fixed after Lin's review |
| Results kept off GitHub until intended | ~ | The assistant said "keep estimates off GitHub" while the project's .gitignore tracked tables/ (would have committed real HRs on a real laptop); its disclosure audit missed the real HR it had itself pushed. Policy then set by the PI (#29) and the cover letter declared exposure |
| Reproducibility across package versions | ~ | Drift caught and routed correctly (#42, renv #43), but nothing in the plugin records package versions with results; submission versions were lost |
| Handover between leads | ✔ / ~ | Patel → Reyes worked from #1's latest note and the plan; access route was one line on #1; the private manuscript repo has no AGENTS.md; the plugin's leaving steps worked at the end (R6) |
| Pacing for a learner | ~ | Heaviest replies ~650 lines (Patel, Feb); improved when asked; Reyes sessions fitted 45 minutes once the project instructions said so |
| Readable R (after the change) | ✔ (early) | New code used loops over names and named lists, no apply/Reduce/do.call; existing tested statistical code left alone with Lin's conditions for any clean-up. Not yet tested on a large new analysis (compressed) |
| Show before posting as the person | ✔ | Held throughout; it let Reyes correct provenance in his own #42 text |
| Release and publication | ~ | Assistant built submission and publication checklists from general knowledge; the plugin has none (ethics, authorship of departed contributors, AI disclosure, code licence, release tag, citation, access after publication) |

## Persona and orchestrator errors (not plugin findings)
Logged in run-notes.md: relay paraphrases and invented content (Lin's wording, "short acknowledgement"), wrong "facts" given to Patel (read-off values), a simulated Mac's outputs and package versions, a persona wiping Lin's local clone through a symlink, "David" wrongly logged as invented (my own brief named him), nudges on pacing and verification. Credit for catches that followed a nudge is reduced.

## Overall
The decision machinery held from analysis through peer review: two leads, a statistician who caught real errors, a non-GitHub decider by email, a learner who never decided science. The failures cluster in four places the plugin doesn't cover: (1) statements about timing and provenance (who saw what when; where a claim came from); (2) what is public and when (tracked outputs, branch history, manuscript text, reviewer reports); (3) environment and version records for results; (4) the end of a project (submission, publication, licence, leaving).
