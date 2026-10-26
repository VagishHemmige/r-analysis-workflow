# Filling the AGENTS.md "Data sources" table

List every source the analysis loads, one row each, found from the actual loading code (`R/setup.R`, loading scripts, `main.R`) rather than from memory. Ask the investigator about any source whose package or access terms are unclear.

- **Accessed through:** the package and its main loading function. A source with no package names its loading script instead.
- **Package documentation:** the pkgdown site, or its `llms.txt` when one is published.
- **Package maintained by:** "This team" for packages the project's investigators maintain (for example usRds, sRtr, CDCAtlas); "External" otherwise. This decides which rules in the template apply.
- **Access:** restricted under a named agreement, public, needs an API key, or paid. The restricted-data rules apply to every restricted row.
- **What AI agents may do:** "None: code, documentation and synthetic data only" for every restricted source; "No restriction (public data)" for public ones. Do not offer or suggest allowing more. Only a person changes this, through a pull request that names the agreement and section, the approved AI service, and exactly what agents may do.

## Example: HOPE-CDC-analysis-2026

Six sources, three packages maintained by the team and three external:

| Source | Accessed through | Package documentation | Package maintained by | Access | What AI agents may do |
|---|---|---|---|---|---|
| SRTR standard analysis files | sRtr (`load_srtr_file()`) | https://vagishhemmige.github.io/sRtr/ | This team | Restricted (SRTR DUA) | None: code, documentation and synthetic data only |
| HRSA transplant centers | sRtr (`get_hrsa_transplant_centers()`) | https://vagishhemmige.github.io/sRtr/ | This team | Public | No restriction (public data) |
| CDC AtlasPlus HIV surveillance | CDCAtlas (`get_atlas()`) | https://vagishhemmige.github.io/CDCAtlas/ | This team | Public, suppressed small counts | No restriction (public data) |
| ACS population estimates | tidycensus (`get_acs()`) | https://walker-data.com/tidycensus/ | External | Public, Census API key | No restriction (public data) |
| Census geography | tigris | https://github.com/walkerke/tigris | External | Public | No restriction (public data) |
| Drive-time isochrones | mapboxapi (`mb_isochrone()`) | https://walker-data.com/mapboxapi/ | External | Paid API, Mapbox token | No restriction (public data) |
