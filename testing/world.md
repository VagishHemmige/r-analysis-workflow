# Simulation world (read by every agent)

This is a simulated research team. Nothing here is real patient data.

## The project
Dr. Patel (PI, transplant/ID clinician-investigator, maintainer) wants a new observational
analysis: "Is serum free light chain (FLC) elevation associated with all-cause mortality,
independent of age, sex and kidney function?" using the public `flchain` dataset in the R
`survival` package (Olmsted County cohort; no data use agreement needed). It should become
a GitHub repository with an analysis plan, AGENTS.md, a Quarto explainer site and R code,
in the PI's usual style. Dr. Patel gives input but does not do the work; rotating students lead.

## People
- Dr. Patel: PI and maintainer. Decides scientific questions. Merges pull requests.
- Dr. Okafor: clinician-scientist (nephrology), no R, comments on the protocol.
- Dr. Lin: biostatistician, fluent R and Git, comments on methods.
- Student leads rotate (about 4 weeks each).

## Simulated GitHub (stands in for github.com)
- Remote repositories live in sim/github/<owner>/<repo>.git (bare git repos).
- Issues: sim/github/<owner>/<repo>.issues/NNN.md (title, body, comments appended).
- Pull requests: sim/github/<owner>/<repo>.pulls/NNN.md (branch, description, review notes).
- The default branch is protected: nothing is pushed to it directly; it changes only when the
  maintainer merges a pull request (the orchestrator performs merges Dr. Patel approves).
- Personal LLM projects: sim/projects/<person>/ (instructions.md, files/, chats/, and checkin.md if
  a check-in was set up). A person has one only if they created it when a chat suggested it.
- Email: sim/inbox/<person>/NNN.md, one message per file (from, to, date, subject, body).
- Website actions a person must do themselves (creating an account, creating a repository,
  changing settings, connecting GitHub to ChatGPT, creating a ChatGPT project and pasting its instructions,
  turning on a scheduled task) happen when the user says
  they did them; the orchestrator then makes them true in the simulated GitHub.
