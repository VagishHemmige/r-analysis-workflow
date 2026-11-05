# Visual teaching architecture — working plan

**Status:** Working design plan, 5 November 2026. The conceptual direction below
was agreed with the maintainer, but individual figures, navigation changes, and
implementation details remain proposals requiring separate approval. This is
not a claim that the described system has been implemented.

**Scope:** The explanatory website *about the R Analysis Workflow plugin*, in
`site/`. The plugin's instructions for figures in users' analysis repositories
are a related but separate workstream (see [Related plugin work](#related-plugin-work)).

## Purpose

The site should teach a research workflow to people with very different
experience: clinicians who do not write R, novice or experienced student leads,
statisticians, PIs, and other collaborators. It should work both as a guided
tutorial and as a reference reached directly through a link or search.

A good graphic is not merely attractive. It helps a reader understand a
relationship or process **and becomes a gateway to the relevant teaching**.
The site's diagrams and sidebar are complementary ways to navigate one body of
material. We are open to reorganizing the sidebar as the visual structure
emerges; the current hierarchy is not a fixed constraint.

## Agreed conceptual direction

The four perspectives, nested component views, and extensive cross-linking are
agreed goals. They do **not** approve a specific figure, layout, sidebar
reorganization, or technical implementation.

### Four perspectives on the same system

| Perspective | Question | Typical content |
| --- | --- | --- |
| **Information** | Where does information live, move, and remain restricted? | Data, code, documents, outputs, exchanges, access boundaries |
| **Structure** | What components exist and how are they organized and connected? | Repositories, files, packages, systems, nested components |
| **Human** | Who participates, and how does a person interact with the system? | Contributions, responsibilities, collaboration, review, authority |
| **Process** | What happens, in what order, and where does work return or branch? | Planning, coding, approval, revision, review, publication, handoff |

These are **perspectives**, not necessarily four mutually exclusive kinds of
page, four sidebar headings, or four diagrams for every topic. Choose the view
that explains a teaching problem. A component can be visited through several
perspectives, and process views can cross component boundaries.

### Nested views, with connections retained

The existing overview is predominantly information-centric: local computer,
GitHub, cloud assistant/plugin, and project website, with exchanges and the
restricted-data boundary. Selecting a component already reveals an explanation.
We want a reader to be able to continue from that explanation into a **more
detailed view** of the component, and on to still more detailed pages or views.

Zooming into GitHub should reveal its internal elements *and* more precise
links to the local computer, AI assistant, people, and site. The same applies
to the local computer and assistant. A detailed view should not become an
isolated island. It may show internal structure, internal processes, external
connections, and relevant human interactions, without cramming all of these
into the same picture simultaneously.

The overall graphic should not carry every human interaction. That would
overload the information view. Human-centric views can be organized around
the person or role; a single person may occupy several roles. Similarly,
process views should represent branching and iteration honestly, rather than
forcing a linear pipeline.

### Visuals as navigation

The agreed direction calls for extensive cross-linking; the specific links and
interaction mechanisms remain to be designed:

1. **Figure → figure:** switch perspective, zoom into a component, or follow a
   related process.
2. **Figure → page:** open the relevant Quarto guide or reference.
3. **Page → figure:** return to the applicable overview/component/step.
4. **Page → page:** follow a related explanation across sidebar sections.

The explanation must remain useful without clicking. Interaction can reveal
detail or guide a process, and links should not be the only way to obtain the
core meaning. Mobile, keyboard, static/print, and reduced-motion use matter.
Concepts and links must remain consistent across views. A stable identifier or
link registry is a **possible implementation**, not yet an agreed requirement.

## Current site and proposed relationships

The current sidebar (`site/_quarto.yml`) is grouped into Introduction, Guides,
Reference, and Evidence. Within Guides it distinguishes task-based **Using the
plugin**, chronological **Project stages**, and **People on a project**.
The Manual covers components; Evidence covers testing of the plugin, which is
different from review of an analysis.

| Current page group | Visual perspective(s) it can support | Potential development |
| --- | --- | --- |
| `start-here.qmd` | Information; entry to other views | Preserve/refine the existing interactive overview and its gateways |
| `manual/github*.qmd` | Structure, information, process | Detailed GitHub view, including external connections and iterative PR/decision processes |
| `manual/code.qmd`, data rules | Structure, information, process | Local computer/R/data/output view |
| `using/*.qmd`, agent rules | Process, structure, human | Assistant/plugin view and task pathways |
| `manual/website*.qmd` | Structure, process | Quarto rendering/publishing and links to code |
| `people/*.qmd` | Human, process | Person-centric views of interactions, not a fixed hierarchy of individuals |
| `stages/*.qmd` | Process | Lifecycle and loops, complementing task-oriented guides |
| `testing/*.qmd` | Evidence/process | Explanation of plugin tests, kept distinct from analysis review |

Existing pages should be inspected before proposing new ones. A page may
support several perspectives; a perspective need not map one-to-one to a
sidebar section. **Guides could evolve toward Processes**, but no sidebar
reorganization has been approved. Preserve useful URLs and cross-links where
practical if navigation eventually changes.

### Current overview implementation

`site/scripts/draw_workflow.py` generates the SVG and uses
`site/scripts/_workflow.html` for the interactive HTML. Quarto's pre-render
step creates `images/workflow-cloud.svg` and
`images/workflow-interactive.html`. The page links to both, with the latter
embedded in `start-here.qmd`.

Current interactive pathways: **Run the analysis**, **Revise the code**, and
**Publish results**. Current component selections explain the R session,
restricted data, results, chat app, GitHub, cloud LLM/plugin, and project
website. Their existence should be preserved while we assess their teaching
effectiveness and destinations. We have **not settled** a redesign of the
Start here graphic or decided to replace its current visual composition.

## Candidate content, not approved figure specifications

| Topic | Possible teaching contribution | Existing tracking |
| --- | --- | --- |
| Homepage/project pathway | Explain an overall route without implying rigidity | #30 |
| Repository anatomy | Clarify the role and connections of project artifacts | #79 |
| Scientific decisions | Show question, evidence, human decision, plan and change | #31 |
| R code to Quarto | Show the real labelled code and its explanatory page | #80, #32 |
| Independent/committee review | Show reviewers, verification, discussion and findings | #81, #91 |
| Contributor handoff | Show continuity through repository state | #82, #57 |
| Results and publication | Show reporting artifacts and release boundaries | #83 |
| GitHub interaction | Clarify issues, branches, PRs and merges | #84 |
| Simulation evidence | Explain the rotating-persona scenario | #85 |
| Further manual details | Restricted files, working rules, script flow, Pages | #86–#89 |
| Problems catalogue | Selective before/after teaching examples | #90, #37 |

The table is an inventory of candidate explanations, **not** an instruction
to produce every figure or give each page a graphic. Many will share a visual
model or link to one explanatory asset. The teaching objective should precede
the choice of layout, animation, or interaction.

## Visual design and implementation principles

- Components convey what exists; processes convey what happens among them.
  Both can be selectable and link into the site.
- Human agency should be clear in the relevant human/process views, while
  preserving the uncluttered information flow in the overview. Scientific
  choices have an identifiable human source. The term **named decider** is
  useful for governance but need not dominate the teaching or diagrams; no
  terminology change in plugin source has been approved.
- Avoid arrows that cross unnecessarily, connectors with ambiguous endpoints,
  unexplained symbols, visually identical categories with different meanings,
  or animation that does not reveal a meaningful sequence.
- Different perspectives can employ different graphic forms. Analytical
  figures and explanatory diagrams have overlapping principles but need not
  use the same drawing tools.
- Prefer reproducible generation. The existing figure is Python-generated
  SVG/HTML; new work should build on this convention where appropriate, with
  the generation code in the repository. Generated output and deployment
  policy should be decided for each integration, not guessed.
- Review rendered output, not just source. Check desktop and phone-sized
  views, keyboard operation, captions/alt text, reduced-motion behavior,
  static fallback, and actual navigation destinations.
- Compare approaches when more than one is reasonable. Record what the reader
  is supposed to learn, then evaluate whether the figure achieves it.

## A possible iterative development route

This is **proposed sequencing**, not approved implementation work:

1. Inventory the existing Start here components, process steps, their
   explanations, and current page destinations.
2. Prototype one detailed component view (GitHub is a candidate) outside the
   published navigation, including internal detail, external links, process
   selection, and routes back to the overview.
3. Review the prototype with the maintainer and compare its teaching value
   with the existing prose and graphics. Correct design before broadening it.
4. Extend the approach to the local computer, assistant, human-centric, and
   cross-component process views where useful.
5. Reconsider sidebar organization as the useful navigation network becomes
   clear. The design may emerge organically rather than being predetermined.
6. Test links and behavior; preserve Python/source reproducibility; make any
   changes through separately approved PRs.

## Open design questions

- Which exact destinations should each current hotspot and animated step
  open? Which deserve detailed diagrams versus existing pages?
- Where should component detail views live, and which should appear as
  selectable perspectives on the same page?
- How should navigation preserve context when moving between figures and
  pages (including deep links into a selected state)?
- Is a shared model/registry of concepts and links useful, or unnecessary
  overhead at the site's present size?
- What should be preserved, simplified, or changed in the existing overview?
- What common visual language is warranted without forcing different kinds
  of figures into one aesthetic or technology?
- Which sidebar changes genuinely improve navigation after prototypes exist?

## Related plugin work (separate scope)

The R Analysis Workflow plugin also needs guidance for **planning, developing,
and reviewing figures in other analysis repositories**. Planned table/figure
shells are proposed in #70. The addition of a sixth Visual Communication Reviewer and the two-stage
independent-then-committee review were agreed in discussion and are tracked in
#91; their precise implementation is pending. The current project instructions
still describe five reviewers and need to be reconciled when this change is
implemented. The proposed rendered-HTML/source packet is also tracked in #91. Conditional package reviewers are in #92;
other possible specialists are deferred in #93. These do not authorize
changing this website or implementing a figure-design workflow here.

## Review requested

This draft is offered for Claude and the maintainer to critique. In particular:

1. Which statements mistakenly present an unsettled idea as decided?
2. Which essential connections, perspectives, or audiences are missing?
3. Which parts are overengineered, duplicative, or inconsistent with the
   current pages and Python figure implementation?
4. What is the smallest useful prototype that would test the design?

Do not implement this plan or reorganize the sidebar solely because this
document exists. Propose individual choices first.
