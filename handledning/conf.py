import os

project = "Handledning: När? Var? Hur? - Identifikation av orsaker till hydrogeologiska störningar i undermarksbebeyggelse"
author = "Ezra Haaf (Chalmers)"
copyright = "2026, Ezra Haaf"

extensions = [
    "nbsphinx",
    "nbsphinx_link",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["config.cache"]

# --- Mermaid: JS locally, static SVG on Read the Docs ---
on_rtd = os.environ.get("READTHEDOCS") == "True"

# Pin Mermaid.js for reproducible rendering
mermaid_version = "10.9.1"

if on_rtd:
    # RTD: pre-render diagrams (no JS execution on RTD pages)
    mermaid_output_format = "svg"
else:
    # Local: render in the browser using Mermaid JS
    mermaid_output_format = "raw"
# --------------------------------------------------------

nbsphinx_execute = "never"

html_theme = "sphinxawesome_theme"
html_title = project
html_static_path = ["_static"]

html_logo = "_static/chalmers.png"

html_permalinks = False
