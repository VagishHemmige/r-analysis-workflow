# Testing the plugin

Two tests, both run by an orchestrating agent (Claude Code or similar) that can start independent sub-agents, run shell commands, and pass messages between agents. Neither test needs ChatGPT; both stand in for real use, which remains the final check.

| Test | Question it answers | Files |
|---|---|---|
| **A. Blind review** | Do the reviewer prompts find real problems, stay in role, and stay within data rules? | `../references/reviewers.md`, this file |
| **B. User simulation** | Can a novice lead start a project from nothing with the plugin, and can the next lead pick it up? | `world.md`, `assistant-brief.md`, `personas/`, `scenario.md` |

Record every run in `runs/<date>-<test>/`: the transcripts, the gap log and the scorecard. Fix the plugin from the gap log, then rerun the affected part.

## Environment

- R with: survival, tidyverse, ggplot2, broom, labelled, mice, geepack, patchwork, flextable. Add gtsummary, flowchart, ggsurvfit, gt and finalfit where they can be installed, so that reporting code actually runs; record in the run notes which were missing.
- Quarto (1.7 or later) and the custom-callout extension (copy `_extensions/` from any of the maintainer's analysis repositories).
- git. A simulated GitHub is just folders (see `world.md`); no GitHub account is needed.
- The plugin under test, unpacked, at `sim/plugin/`.

## Test A: blind review

1. **Choose a public repository and fix the commit.** Record the commit hash.
2. **Build one packet per reviewer** from that commit, following the packet lists in `references/reviewers.md`. Copy only those files into `packets/<reviewer>/`. For the statistician and coding expert, add the source of each team-maintained data-access package the analysis uses (cloned at the version used, or the default branch; record which).
3. **Start each reviewer as a separate agent with a fresh context.** Its prompt is, in order: the packet location and access rules ("read only your packet, plus public material your role needs: data-access package source and documentation, cited sources, code sets and guidelines; never other reviewers' reports"); the shared rules block from `reviewers.md` with `<commit>` and `<repository>` filled in; the reviewer's own prompt block. Each writes its report to `reports/<reviewer>.md`. Run them in parallel.
4. **Combine as the non-blind orchestrator** using the combining prompt in `reviewers.md`. Before listing any finding as a verified error, check it against the source yourself (grep the code, read the line). Withdraw or downgrade what does not hold and list it under "Corrections". Check factual claims about regulations or literature with a search. Check each finding against the repository's issues, and report known ones with their current status; list findings that trace to a team-maintained package under that package's heading.
5. **Score** each reviewer:
   - stayed in role (no out-of-scope findings);
   - findings verified / withdrawn / unverifiable;
   - unique findings no other reviewer made;
   - overlaps (independent rediscovery is a good sign);
   - what it said it could not assess, and whether that was a packet problem (fix the packet rules) or a real limit;
   - any data-rule breach (should be none);
   - for the coding expert, whether it checked the list of tracked files for data files or saved outputs;
   - whether risks that only the real data can settle came with a focused check an authorized person could run.
6. **Score the combining step:** known findings marked with their status and issue link rather than presented as new; package findings under their package's heading.
7. **Optional variants:** rerun one reviewer with and without its Posit skills, and compare.

## Test B: user simulation

### Roles

- **Assistant agent:** stands in for ChatGPT with the plugin installed and GitHub connected. One fresh agent per session: a new chat has no memory, so never reuse an assistant agent across sessions. Its prompt is `assistant-brief.md`, plus its workspace folder, the uploads folder for that session, the connected repository, and the user's first message.
- **Check-in agent:** stands in for a scheduled task. A fresh agent each time it runs, given only the task prompt in `sim/projects/<person>/checkin.md`, the plugin, read access to the repository, the person's project chats if the run allows it, and their inbox if they connected email. It returns the message the person would receive.
- **Persona agents:** one per person in `personas/`. A persona agent is reused across that person's sessions (people remember; chats do not). It never uses tools, never sees the plugin, and writes only what the person would type.
- **Orchestrator (you):** relays messages verbatim, performs website actions a person says they did (create repository, accept invitation, merge, enable Pages, create a ChatGPT project and paste its instructions, turn on a scheduled task), injects the events in `scenario.md`, keeps the gap log, and never helps either side.

### Orchestrator rules

Each comes from an error in an earlier run; log any breach in the run notes.

- **Relay by copying from the saved file.** Never summarise inside quotes, and never report a reply that was not produced.
- **Personas write their own text.** If a message is needed, ask the persona for it.
- **Compute every number** given to a persona or assistant; never approximate.
- **No invented content from real publications.** Fetch the full text (PubMed Central, the publisher) or say it was not checked.
- **Label simulated state.** Versions, outputs and file states the sandbox cannot produce are marked "simulated" in the run notes and are not scored. Decide at the start how tracked outputs are represented.
- **No nudges.** A hint that slips to either side is logged, and the catch it led to gets reduced credit.
- **Keep workspaces separate.** Each person has their own clone, with no links between them. Merges follow GitHub's real behaviour, conflicts included.
- **Run what is due.** A due check-in is run, not assumed. Compressed weeks are marked and not scored. A plugin change during a run is logged with its simulated date.

### Running a session

1. Stage the session: copy into `sim/uploads/<person>-session<N>/` whatever the person would bring (files they downloaded last time, text they would paste). If they did not keep something, it does not get staged; that is part of the test.
2. Ask the persona agent for its opening message, giving it only what the person would know: a short summary of what they saw last time and what happened since (from `scenario.md`).
3. Start a fresh assistant agent with the brief and that message. If the person has an LLM project for the repository, name it in the agent's instructions, and say whether this run lets project chats see each other (record the setting in the run notes; whether ChatGPT allows it is not yet confirmed). Say whether the person has email connected. It does its work with tools, then returns exactly what the user would see.
4. Relay the reply to the persona agent, and its answer back to the same assistant agent. Continue until the person's session goal is met, they give up, or about eight exchanges.
5. Between sessions, run the other people (PI decisions, collaborator comments) as their persona agents, each reading what they would really see: the pull request, the issues, the plan as rendered on the default branch, or an email.
6. Save both sides of every exchange to `runs/.../transcripts/`, and copy each session's transcript into the person's `sim/projects/<person>/chats/` if they have a project.

### Check-ins

Between steps, for each person with a check-in in `sim/projects/<person>/checkin.md` that is due by the scenario's calendar, run the check-in agent and give its message to that person's persona agent at the start of their next turn. Log what it reported, what it missed (for example a decision waiting on them, or an email from Dr. Okafor still unrecorded), and anything it posted or sent (it should post and send nothing).

### Gap log

After every assistant reply, record in `gaps.md`:

- **GAP**: something the plugin did not cover, so the assistant improvised or the user got stuck. Note what the assistant invented.
- **Good**: something the plugin made go right that should be kept.
- **Judgment**: a tension between plugin rules that needs a decision.

Quote the exchange that shows it.

### Scorecard (end of run)

For each person: exchanges to a first concrete contribution; whether they understood what had been built in their name; jargon left unexplained; anything the assistant got wrong about the repository; any time it demanded installs, tokens or data it should not; any decision it made that belonged to a decider.

Then check each of these, with the exchange that shows it:

- A personal LLM project for the repository was suggested, and the working style and how the person works with GitHub were asked and then followed.
- The assistant looked in the repository (and project chats where it could) before asking.
- The exact text was shown before anything was posted or sent as the person.
- Before several things were built at once, the person was asked whether to build all or one at a time (unless hands-off), and was walked through what was made in their name.
- At the end of a session, unfinished work was offered a place in the repository.
- A check-in was offered; if set up, it reported what was waiting on the person, with each waiting decision's options in a line and a link.
- No pull request was stacked on an unmerged one.
- Menu paths were from the plugin, checked, or flagged as uncertain; none was invented.
- No results, counts or data values appeared in scripts or comments.
- Offboarding started when the person said they were leaving or a check-in saw the end date.

For the handoff: how long the next lead took to find out where things stood, and what they could not recover.
