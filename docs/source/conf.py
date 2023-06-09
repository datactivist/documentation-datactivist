# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Datactivist Documentation'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'recommonmark'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Add a source parser for Markdown files
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

# Set the source file suffixes to include Markdown files
source_suffix = ['.rst', '.md']
