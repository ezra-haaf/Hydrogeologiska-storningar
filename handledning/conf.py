project = "Handledning: När? Var? Hur? - Identifikation av orsaker till hydrogeologiska störningar i undermarksbebeyggelse"
author = "Ezra Haaf (Chalmers)"
copyright = "2026, Ezra Haaf"

extensions = [
    "nbsphinx",
    "nbsphinx_link",
    "sphinx.ext.graphviz",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["config.cache"]

graphviz_output_format = "svg"

nbsphinx_execute = "never"

html_theme = "sphinxawesome_theme"
html_title = project
html_static_path = ["_static"]

html_logo = "_static/chalmers.png"

html_permalinks = False
