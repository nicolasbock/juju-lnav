# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Requirements ------------------------------------------------------------
# Required packages for building this documentation:
# - sphinx
# - myst-parser

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'juju-lnav'
copyright = '2025, Nicolas Bock <nicolas.bock@canonical.com>'
author = 'Nicolas Bock <nicolas.bock@canonical.com>'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

# MyST parser configuration
myst_enable_extensions = [
    "deflist",
    "tasklist",
    "html_admonition",
    "html_image",
]

# Allow MyST to parse files with .md extension
source_suffix = {
    '.rst': None,
    '.md': 'markdown',
}

# Set the master document to readme.md instead of index.rst
# master_doc = 'index.md'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
