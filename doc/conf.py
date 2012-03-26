#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -- General configuration ----------------------------------------------------

extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.todo']

master_doc = 'index'
source_suffix = '.rst'
exclude_patterns = ['_build']

# -- Poject information -------------------------------------------------------

project = 'Scala Cluster Service'
copyright = '2012, Georges Discry'
version = '0.1'
release = '0.1-SNAPSHOT'

highlight_language = 'scala'
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

html_theme = 'nature'
htmlhelp_basename = 'ScalaClusterServicedoc'

# -- Options for LaTeX output -------------------------------------------------

latex_documents = [
  ('index', 'ScalaClusterService.tex', 'Scala Cluster Service Documentation',
   'Georges Discry', 'manual'),
]

# -- Options for InterSphinx extension ----------------------------------------

intersphinx_mapping = {
    'akka20': ('http://doc.akka.io/docs/akka/2.0/', None),
    'mtp': ('http://dev.discry.be/docs/mtp/', None),
}

# -- Options for TODO extension -----------------------------------------------

todo_include_todos = True
