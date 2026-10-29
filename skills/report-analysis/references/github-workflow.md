# GitHub workflow

Applies to any analysis repository, whatever its default branch is called and whoever owns it. Use the repository's actual default branch; do not rename it unless the maintainer asks.

## Setting up from R

For a maintainer who has R and wants to set up or check the repository from the console. Anyone without R uses the website steps in the sections below. The person runs every command; agents suggest them and never run them.

Find out where things stand first: the person runs `usethis::git_sitrep()` in the project folder and shares the result. Suggest only the next step whose indication applies, one at a time, and check again after each.

| Indication | Command | What it changes |
|---|---|---|
| No project folder yet | `usethis::create_project("<path>")` | Creates the folder as an RStudio project. |
| `git_sitrep()` shows no Git name or email | `usethis::use_git_config(user.name = "<name>", user.email = "<email>")` | Sets the Git identity on this computer. The email appears in every public commit; GitHub offers a private no-reply address. |
| `git_sitrep()` shows no GitHub token | `usethis::create_github_token()`, then `gitcreds::gitcreds_set()` | Creates a token on GitHub and stores it on this computer. Never paste a token into a chat. |
| Not a Git repository, and `file.exists(".gitignore")` is `FALSE` | Save the adapted starter `.gitignore` under exactly that name, and review it (see `data-handling.md`) | Nothing in Git yet. No Git step comes before this one. |
| Not a Git repository; `.gitignore` in place and reviewed | `usethis::use_git()` and answer **no** when it offers to commit; run `gert::git_status()` and read the whole list; when it is right, run `usethis::use_git()` again and answer yes | Starts Git, then makes the first commit. The prompt shows only the first ten files, so the full list is read with `git_status()`. If it shows any data file, an output that should be ignored, or a file nobody recognises, stop, fix `.gitignore` and check again. |
| Git repository with no GitHub remote | `usethis::use_github()` (public unless told otherwise) | Creates the repository on GitHub and pushes the first commit. From here the files are public. |
| The check below shows the default branch unprotected | The ruleset call below | Protects the default branch, as in "Protect the default branch" below. |
| The check below shows `docs/` on the default branch and Pages off | `usethis::use_github_pages(branch = "<default branch>", path = "/docs")` | Publishes the site, as in "Publishing the website" below. |

The check reads the settings rather than assuming them, so it can be rerun at any time, for example after the repository is transferred:

```r
remote <- gh::gh_tree_remote()
api <- function(endpoint, ...) {
  tryCatch(
    gh::gh(endpoint, owner = remote$username, repo = remote$repo, ...),
    http_error_404 = function(e) NULL
  )
}
branch <- api("GET /repos/{owner}/{repo}")$default_branch

# Protected by a ruleset, or by classic branch protection
rules <- api("GET /repos/{owner}/{repo}/rules/branches/{branch}", branch = branch)
rule_types <- vapply(rules, function(rule) rule$type, character(1))
protected <-
  all(c("pull_request", "deletion", "non_fast_forward") %in% rule_types) ||
  !is.null(api("GET /repos/{owner}/{repo}/branches/{branch}/protection", branch = branch))

docs_merged <- !is.null(api("GET /repos/{owner}/{repo}/contents/docs", ref = branch))
pages_on <- !is.null(api("GET /repos/{owner}/{repo}/pages"))

cat("Default branch:", branch, "\nProtected:", protected,
    "\ndocs/ merged:", docs_merged, "\nPages on:", pages_on, "\n")
```

The ruleset call, matching the website steps below (0 approvals, empty bypass list):

```r
gh::gh(
  "POST /repos/{owner}/{repo}/rulesets",
  owner = remote$username, repo = remote$repo,
  name = "Protect default branch",
  target = "branch",
  enforcement = "active",
  conditions = list(ref_name = list(include = list("~DEFAULT_BRANCH"), exclude = list())),
  bypass_actors = list(),
  rules = list(
    list(type = "deletion"),
    list(type = "non_fast_forward"),
    list(type = "pull_request", parameters = list(
      required_approving_review_count = 0,
      dismiss_stale_reviews_on_push = FALSE,
      require_code_owner_review = FALSE,
      require_last_push_approval = FALSE,
      required_review_thread_resolution = FALSE
    ))
  )
)
```

The same limits apply as on the website: a token with admin rights on the repository, and on GitHub Free a private repository has neither rulesets nor Pages.

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
