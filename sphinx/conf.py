project = "Notebook Gallery Boilerplate"
author = "Chalmers"

extensions = [
    "nbsphinx",
    "nbsphinx_link",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
suppress_warnings = ["config.cache"]

nbsphinx_execute = "never"

html_theme = "alabaster"
html_title = project
html_static_path = ["_static"]
