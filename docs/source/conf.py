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

def git_tag():
    """Return the current git tag."""
    import subprocess
    try:
        return subprocess.check_output(['git', 'describe', '--tags', '--always']).strip().decode('utf-8')
    except subprocess.CalledProcessError:
        return 'unknown'

project = 'juju-lnav'
copyright = '2025, Nicolas Bock <nicolas.bock@canonical.com>'
author = 'Nicolas Bock <nicolas.bock@canonical.com>'
release = git_tag()
version = release  # Use the same version for both release and version

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
master_doc = 'index'

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# Alabaster theme options
html_theme_options = {
    'show_powered_by': False,
    'github_user': 'nicolasbock',
    'github_repo': 'juju-lnav',
    'github_banner': True,
    'show_related': False,
    'note_bg': '#FFF59C',
    'sidebar_width': '220px',
    'page_width': '1000px',
    'show_relbars': True,
    'description': f'Version {release}',
    'logo_name': True,
    'logo_text_align': 'center',
}

# Add version information to the HTML context
html_context = {
    'display_version': True,
    'current_version': release,
}
