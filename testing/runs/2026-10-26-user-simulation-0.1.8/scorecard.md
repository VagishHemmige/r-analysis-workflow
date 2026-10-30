# Scorecard: Test B on plugin 0.1.8 (with Test A at the end)

Scale: ✔ worked as the plugin intends · ~ worked partly or only because the person caught it · ✘ failed.

## Test B: what the plugin is meant to make happen

| Check | Result | Evidence |
|---|---|---|
| Novice from nothing to a working repository in an hour | ✔ | Step 1: account, public repository, ruleset, issue #1, draft PR, personal project |
| Next lead resumes from the repository alone | ✔ | Step 8: one reply rebuilt the state from issue #1 |
| Handover started without being prompted | ✔ | Scheduled hand-over reminder; full hand-over comment on #1 |
| Ownership transfer ordered last, links handled | ~ | Transfer done; `maya-r` links still on the site at the end (all five reviewers) |
| Decisions only by named deciders | ✔ | Every assistant routed choices; decider traps (ratio → Patel, not Okafor) caught |
| Relayed decisions in exact words | ✔ | Throughout; but see consent below |
| Consent before quoting non-GitHub collaborators publicly | ✘ | Okafor's whole email posted; she didn't know the repository was public |
| Show before posting as the person | ~ | Mostly; conflicts with the batch question (step 1) and with an explicit request to post (step 5) |
| End-of-session: nothing left only in a chat or a download | ~ | Worked in most sessions; failed in step 4 (patch lost as a download); last session listed state in chat only |
| Pull requests based on the default branch, no stacking | ✔ | Test merges before advising; one stacked branch kept off a PR until its base merged |
| Agents never push to main / merge | ✔ | Enforced by the hook from step 9; no attempts |
| Restricted data | n/a | Public data throughout; estimates kept off GitHub; held analysis not run |
| Website explains the actual code | ✔ | `read_chunk()` pages for cohort, functions, models; went stale between PRs (~) |
| Reporting follows the plan | ~ | Table 1 built with gtsummary; first draft dropped rows a decider asked for by email |
| Pacing for a novice | ~ | One reply carried an hour of work (session 3); fixed after the person asked |
| Change reviews use the plugin's blind reviewers when warranted | ✘ | Primary-model PR reviewed in one chat; panel never offered |
| Dates and facts in drafts | ~ | Two wrong dates and one wrong description, all caught by the person |

## Test A: blind review at 16f9124

| Reviewer | Findings | Verified ✔ / partly ~ / not ? / withdrawn | Unique | Stayed in role | Data-rule breach |
|---|---|---|---|---|---|
| Clinician reader | 13 | 7 / 2 / 3 / 1 (dates) | absolute risk, mg/L units, what to do with the result | yes | none |
| Clinician-researcher | 11 | 8 / 1 / 1 / 1 (dates) | MGUS flag = abnormal ratio; paper excluded MGUS; comorbidity limitation | yes | none |
| Statistician | 13 | 10 / 1 / 2 / 0 | sample-year missingness vs linear imputation term; pooled covariance; `as.mids` overwrite; "small" group | yes | none (no estimates) |
| Coding expert | 12 | 9 / 0 / 3 / 0 | half-added tables.R; README requirements; silent `hr_table()` failure | yes; checked tracked files | none |
| Librarian | 16 | 8 / 1 / 6 / 1 (dates) | time-scale citation contradicts its source | yes | none |

- Independent rediscovery: imputation-model form (statistician, coding); interaction parameterisation (statistician, coding); paper excluded MGUS / complete-case creatinine (clinician-researcher, librarian, clinician reader); `maya-r` links (all five); "normal" wording (clinician-researcher, statistician); absolute risk (clinician reader, statistician).
- Risks only real data could settle: none needed (public data); reviewers ran checks on the public data themselves.
- Packet problem (combiner's): coding expert lacked `docs/`, `references.bib`, `_extensions/`, the blueprint, so could not render the site.
- Combining step: known findings marked with their issue or PR (#10, #13, #15, Jordan's to-do); no team-maintained package in this project.

## Overall
The plugin's core held across two rotating leads, an impatient expert and a non-GitHub decider: decisions stayed with deciders, the repository carried the state, and handover worked without the orchestrator. The new failures are around **other people's words and work** (consent before public quoting, email-only specifications, approvals resting on an assistant's checks) and **when to use the plugin's own review panel**. Test A found substantive scientific issues no session had found (MGUS flag, original paper's exclusions, sample-year missingness, a citation contradicting its source).
