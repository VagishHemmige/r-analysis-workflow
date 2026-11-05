# Site figures

`draw_workflow.py` is the source of the workflow diagram on Start here.
Quarto runs it through `project.pre-render` in `site/_quarto.yml`.
The SVG is generated locally and in the publishing workflow; generated SVG/PNG
files are ignored by Git. The earlier `site/images/workflow.svg` is retained.

From the repository root:

```sh
python3 site/scripts/draw_workflow.py
quarto render site
```

The site needs Python 3 and Quarto, with no Python packages required.
For an optional PNG export, install CairoSVG and run:

```sh
python3 -m pip install cairosvg
python3 site/scripts/draw_workflow.py --png
```

All graphics are embedded. See `SOURCES.md` for logo and icon provenance;
the Octicons MIT notice is embedded in the source and generated SVG.
