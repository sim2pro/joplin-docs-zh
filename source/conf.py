# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Joplin Tutorial Zh_CN'
copyright = '2025, Joplin'
author = 'Joplin'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'zh_CN'

gettext_compact = False
locale_dirs = ['locale/']  # 翻译文件存放目录

extensions = [
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
    'myst_parser',
#    'sphinx_multiversion',
    'sphinx_tabs.tabs',
    'sphinx_rtd_theme',
    #'sphinx_sitemap_ros',
    'sphinxcontrib.mermaid',
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
