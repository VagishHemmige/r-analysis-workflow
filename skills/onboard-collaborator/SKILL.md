---
name: onboard-collaborator
description: Help someone join an R analysis project, or leave one, at the level of help they choose. Use for anyone joining (including people new to R, Quarto or GitHub) and for anyone leaving or handing over work.
---

If the linked plugin files cannot be opened, say so and continue from the repository's own AGENTS.md and analysis plan; do not guess their contents.

Read [onboarding](../../references/onboarding.md), the project's AGENTS.md and README, and the person's own instructions. Start from what they want to contribute and what they already know. Give one next step at a time and keep their earlier answers.

## Explain the project through its own documents

Use the project as it is now; do not assume the person can read code or knows the folders.

- **The website** is the way in for anyone who does not code: it explains each step of the analysis in plain language. Start a clinician there.
- **`analysis-plan.md`** says what the analysis must do. Its "Open:" markers point to the scientific questions still undecided.
- **GitHub Issues** hold those open decisions, plus known gaps between code and plan.
- **`AGENTS.md`** says how work is done here, including the data rules and who the deciders are.
- **`ARCHITECTURE.md`** says how the code fits together, for people who will work on it.

## Ways to contribute

- **Clinical input without code:** comment on a decision issue with options, evidence and clinical reasoning; review the plan or the site for clinical accuracy and clarity; suggest literature. Only the named deciders settle a decision, but anyone may inform one.
- **Code:** a change made on a branch and offered as a pull request, following AGENTS.md. Explain only the Git steps their chosen tool needs; do not prescribe a tool. Use [Happy Git and GitHub for the useR](https://happygitwithr.com/) for deeper learning.
- **Review:** anyone may ask for a review through the review skill.

## Leaving

When someone is leaving or handing over, follow "Leaving a project" in [onboarding](../../references/onboarding.md).

## Boundaries

- Do not require R, Git or Quarto for work that does not need them.
- Check what is already installed and authorized before suggesting installation. Keep GitHub connector access separate from a working local Git setup. Never ask for pasted tokens.
- Do not change account settings, install software or publish work without the person's say-so.
- Restricted data stay with authorized people in approved environments, whatever the collaborator's role.
- Use the setup skill only to set up a project, not for every onboarding conversation.
