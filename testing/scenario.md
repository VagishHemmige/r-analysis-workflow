# Scenario: a new project from start to finish with rotating leads

Project: free light chains and all-cause mortality in the public `flchain` dataset (see `world.md`). The orchestrator injects the events below between sessions. Persona prompts are in `personas/`.

| Step | Who | Session goal | Orchestrator events before or during |
|---|---|---|---|
| 1 | Student lead 1 (`student-novice.md`) | Get the project started in an hour, with no GitHub account and no R installed | Answers any email to the PI by running the PI persona |
| 2 | Student lead 1, new chat next day | First pull request | Follow what step 1 led to. If the student was told to ask the PI for a repository, the PI created `dr-patel/flchain-mortality` (default branch protected, README only) and invited the student, who accepted and connected ChatGPT to GitHub. If the student was told to create it, the run becomes the student-owned variant below. Stage whatever the student downloaded in step 1, and their LLM project if they made one |
| 3 | PI (`pi.md`) | Review the first pull request; answer the student's questions | Merge if the PI merges; enable Pages if asked |
| 4 | Clinician-scientist (`clinician-scientist.md`), biostatistician (`biostatistician.md`) | Give input on the decision issues | Clinician replies by email (no GitHub); biostatistician comments on the issues |
| 5 | Student lead 1, new chat a week later | Record the clinician's input; decide what can start before decisions | Stage the clinician's email as pasted text |
| 6 | PI | Decide some of the open questions | Merge any pull requests the PI approves |
| 7 | Student lead 1, new chat, last session before the rotation ends | As much as possible before leaving | Do not prompt the student about handoff; see whether anything does |
| 8 | Student lead 2 (`student-r-no-github.md`), new chat, two weeks later | Pick up the project with no handover from student 1 | Stage only what student 2 would realistically have: the repository link and an email from the PI. Not student 1's files |
| 9 | Biostatistician | Review methods and push to change the model directly | |
| 10 | PI and student 2 | Settle remaining decisions; models, reporting, site | |
| 11 | Orchestrator | Run Test A (blind review) on the finished repository; release check | |
| 12 | PI as lead (`pi-as-lead.md`) | Finish the analysis and write the manuscript | Compress weeks with no sessions; mark them |
| 13 | Revision lead (`student-revision.md`), six months later | Handle reviewer comments with no handover beyond the repository, manuscript and decision letter | Stage the decision letter and the PI's email only |
| 14 | Revision lead, last session | Resubmit, then leave | Do not prompt about publication or leaving; see whether anything does |

**Variant: student-owned repository.** In step 1, the PI replies "set it up yourself and add me" instead of creating the repository (or a chat has already told the student to create it). The student creates it under their own account. Probe at step 7 (the student's last session) and step 8 (the next student): does anything raise transferring ownership to the PI before the handover, and does a transfer leave the website or its links broken (GitHub does not redirect Pages)?

Between steps, run each check-in that has been set up and is due (see README, "Check-ins"), and deliver Dr. Okafor's emails to the inbox of whoever she wrote to.

Stop early when a step shows the same gap as an earlier one; the point is to find gaps, not to finish the study.
