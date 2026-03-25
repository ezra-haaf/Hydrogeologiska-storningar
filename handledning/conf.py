project = "Handledning: När? Var? Hur? - Identifikation av orsaker till hydrogeologiska störningar i undermarksbebeyggelse"
author = "Ezra Haaf (Chalmers)"

extensions = [
    "nbsphinx",
    "nbsphinx_link",
    'sphinxcontrib.mermaid',
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["config.cache"]

nbsphinx_execute = "never"

html_theme = "sphinxawesome_theme"
html_title = project
html_static_path = ["_static"]

html_logo = "_static/chalmers.png"

html_permalinks = False