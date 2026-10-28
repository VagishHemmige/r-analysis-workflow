# Collaborator onboarding

Adapted in original wording from Academic Records' goal-first onboarding approach; no CV import, private profile, website deployment or recurring-task machinery is carried over.

Start with the contribution the person wants to make and what they already know. Offer guided learning or assisted execution. Give one next step and retain earlier answers. Explain repository documents using the actual project and its current state; do not assume code visibility.

When someone takes over work from another person, start from the repository: the analysis plan, open decision issues, open pull requests and their notes, and anything the previous person left marked as paused. Do not rely on the previous person's files or chats.

For a clinician, begin with the scientific question, cohort, outcomes and unresolved protocol decisions. For an R-capable Git beginner, explain local files, commits, branches/forks and PR review using their actual permitted workflow. Separate GitHub connector access from a usable local Git installation and authentication. Inspect readiness before prescribing installation. Never request pasted tokens.

Suggest that the person creates their own LLM project for this repository, and fill in the [personal instructions template](../assets/project-instructions.md) for its instructions, asking which working style they want and how they work with GitHub, so their chats share the same context without pasting it each time. It is an offer, not a requirement.

Ask whether the person wants a periodic check-in, using the assistant's scheduled tasks where available. It is for whoever asks for it, whatever their role. If they want one:
- It always reports what is waiting on them: issues assigned to them, decisions they make, and pull requests awaiting their review.
- For each decision waiting on them, it gives the question and each option in a line, with a link to the decision issue, so they can decide from the check-in or open the issue. The decision itself is recorded in the issue.
- Ask whether they also want what they are waiting on from others, work with no recent activity, and milestones due soon, and include only what they choose.
- Ask how often it should run.
- Look over the person's recent chats in their own LLM project for this repository, where the assistant can see them, for unfinished drafts that never reached the repository, and offer to save them. Check it against the project's disclosure rules first; anything holding results from restricted data that are not cleared for release stays where it is, and the person is told why. Project memory may not show every chat, so say if this could not be done.
- If the person has email connected, ask whether the check-in should also review their project-related email. If yes, look only at messages about this project, list each decision or request found, and propose where to record it (a comment on the relevant decision issue, or a new issue). Check it against the project's disclosure rules first; anything holding results from restricted data that are not cleared for release stays where it is, and the person is told why. Post nothing without the person's go-ahead.
- Record their check-in and email choices in their own project instructions, not in shared files.
- It reads the repository; it may draft messages for the person but never sends anything on its own.

Use [Happy Git and GitHub for the useR](https://happygitwithr.com/) as the linked learning guide. Check current official documentation before version-specific setup or security advice. Do not require R/Git/Quarto for work that does not need them. Read project instructions for relevant installed skills and report unavailable dependencies accurately.

## Leaving a project

Start when the person says they are leaving or handing over, when someone else asks for a handover from a person who is leaving, or when a check-in sees an end date the person gave it approaching. Work through these with the person before their last session. Each step asks; not everything can be finished, owned or closed, and a project may go dormant. Record what stays open and why rather than forcing an owner.

1. **Documents.** Ask for anything that exists only in a chat, on a laptop or in email (drafts, notes, data checks, correspondence that settles something) and offer to move it into the repository: a draft pull request, an issue comment, or a new issue. Check it against the project's disclosure rules first; anything holding results from restricted data that are not cleared for release stays where it is, and the person is told why.
2. **Open issues and pull requests.** For each, ask whether it can be finished, handed to someone, closed with a reason, or left open with a note saying it is paused and what it is waiting on. For open pull requests, write down what remains, the intended merge order and any conflicts.
3. **Pending asks.** Ask what the person has requested of others (an email to a collaborator, a question to the PI) that has no answer yet, and offer to record each as an issue saying who was asked, when, and what for.
4. **Ownership.** If the person leaving owns the repository, raise transferring it to the PI (GitHub: Settings → General → Transfer; the new owner must accept within a day). Issues, pull requests and history move with it, and old repository links redirect, but GitHub does not redirect the website: afterwards update the site and repository links in `_quarto.yml`, the site pages and the README, re-render the site, and turn GitHub Pages on again under the new owner.

Finish by telling the person what was recorded where, and offer a short message for the PI or team pointing to it.

Example prompts:
- “Explain this project's research question and show where I can help refine the protocol. Assume I cannot read R.”
- “I know R but not GitHub. Help me make one contribution using this repository's rules.”
- “This is my latest RMD. Help initialize the project, retaining the useful work and asking only the remaining setup questions.”
