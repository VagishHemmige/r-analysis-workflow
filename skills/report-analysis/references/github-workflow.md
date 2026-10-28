# GitHub workflow

Applies to any analysis repository, whatever its default branch is called and whoever owns it. Use the repository's actual default branch; do not rename it unless the maintainer asks.

## Protect the default branch

Every change reaches the default branch through a pull request. This makes each change visible before it lands, including changes made by agents working through a person's GitHub account, which GitHub treats as that person.

The maintainer sets this up once per repository, in GitHub: **Settings → Rules → Rulesets → New ruleset → New branch ruleset**.

1. Name it (for example "Protect default branch") and set **Enforcement status** to **Active**.
2. **Target branches → Add target → Include default branch.**
3. Tick **Restrict deletions**, **Block force pushes**, and **Require a pull request before merging**.
4. Set **Required approvals** to the number the team wants. A solo maintainer uses 0, because GitHub never lets the author of a pull request approve it.
5. Leave the **Bypass list** empty unless the team decides otherwise. An account on the bypass list can push directly, and so can any agent acting through that account.

Rulesets on private repositories need a paid GitHub plan (Pro, Team or Enterprise Cloud). Agents do not change repository settings; they describe these steps for the maintainer.

## Pull requests

Any tool that creates a branch and opens a pull request will do; each person uses what they prefer. When someone new to Git needs help, explain the approach they already use (see [onboarding](onboarding.md)) rather than prescribing one.

Good practice for everyone, and required of agents:

- One branch per piece of work, not per commit.
- Base each pull request on the default branch. If a change needs one that has not been merged, wait for it to merge, or fold both into one pull request. Never leave someone to work out a merge order.
- Re-render `docs/` on the same branch as the change it reflects.
- A pull request says which plan section or issue it addresses and what was checked (see `AGENTS.md`).
- A pull request that settles a decision issue includes `Closes #<n>` and the plan change.

## Publishing the website

The site goes live only after someone with admin or maintainer permission on the repository turns on GitHub Pages, once a pull request containing `docs/` has been merged:

1. On the repository page, click **Settings**, then **Pages** in the sidebar.
2. Under "Build and deployment", set **Source** to **Deploy from a branch**.
3. Choose the default branch and the **/docs** folder, then click **Save**.

Agents cannot change settings; they tell the person who can.

## Issues

GitHub Issues hold open decisions, gaps between code and plan, and known defects. Each project chooses its own labels, templates and conventions; the plugin prescribes none.

## Milestones (optional)

Milestones group issues and pull requests under a phase of the project with a target date, so anyone can see what a phase is waiting on. Each project chooses its own phases and dates, for example: plan locked, cohort built, models fitted, manuscript drafted.

To create one on the GitHub website:
1. Open the repository, then click **Issues**.
2. Next to the search field, click **Milestones**, then **New milestone**.
3. Enter a title, an optional due date and a short description, then click **Create milestone**.

To put issues or pull requests in a milestone: on the **Issues** (or **Pull requests**) list, tick the items, open the **Milestone** menu above the list, and choose the milestone. A decision issue placed in a milestone shows which phase it holds up. The **Milestones** page shows each milestone's due date and how many of its items are closed.

If the assistant's GitHub connection can create milestones and assign items, it may do this for the person once they have given the phases and dates; otherwise it walks them through the steps above.

## Tags

When the analysis plan is locked, tag the commit (for example `sap-v1.0`); see [writing the plan](analysis-plan.md). Tags and releases are created by the maintainer or with their explicit authorization.

## What stays personal

How each person uses AI tools with the repository (which tool reviews, which edits, what each may do) belongs in that person's own instructions, not in shared files.
