# Plugin backlog: things to address later (from Vagish, 27 Oct 2026)

## Package documentation before code (real use: ellmer, 27 Oct 2026)
An agent wrote `chat_structured()` from memory, chose a newer Claude model, tested only against a fake ellmer, and paid for calls that failed on a version difference.
Proposed (not yet decided):
1. Make "read the documentation, including known issues and NEWS" cover every package an API call depends on, not just data sources: move it from AGENTS.md "Data sources → For every package" (line 38, which says "for a source") to Coding conventions, and add a line to conventions.md "Writing R code". (Recommended)
2. Leave a trace: for code depending on a package's API, the PR or reply names the installed version and the help page or NEWS entry relied on.
3. Code tested against a fake external package also needs one check against the installed version before it is relied on.
4. Paid calls: one pilot call with the exact model and package version before a paid batch; a change of model is the person's decision (AGENTS.md line 107 only says "Ask before paid … calls").

## Reviews: every changed file, shown to the person (real use, 27 Oct 2026)
- The agent had to be told to review every file being changed; it should do so by default.
- When reviewing, it didn't put the files in the pane (the viewer beside the chat) for the person to see; it should show each reviewed file there.

## Deferred during 0.1.9 (27 Oct 2026)
- **What is public:** skipped for now. Only gap found: the template doesn't say that deleting a file doesn't remove it from history.
- **Package versions with results:** skipped for now; the PI will come back to it. Options were a template placeholder (renv.lock or saved sessionInfo()) or a conventions.md sentence.
- **Submission and publication checklist:** dropped. Manuscript and journal tasks belong to the authors, not the repository. Keep only tagging the commit the submitted results came from, folded into the package-versions item.
