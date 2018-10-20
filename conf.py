# -*- coding: utf-8 -*-
import json
from datetime import date
import sys, os
from datetime import date

root_dir = os.path.abspath(os.path.join('..'))

# extensions_path = os.path.join(root_dir, 'utils', 'docutils', 'directives')

# sys.path.insert(0, extensions_path)

extensions = ['sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.ifconfig',
              'sphinxcontrib.plantuml']

todo_include_todos = True
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
add_function_parentheses = True
#add_module_names = True
# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []
language = 'en'
locale_dirs = ["locale/"]

project = 'DeerNation'
copyright = '2017-%s Tobias Braeutigam' % date.today().year

with open(os.path.join(root_dir, "backend", "package.json")) as data_file:
    data = json.load(data_file)
    version = data['version']

# read versions file
versions = []

releaselevel = 'dev' if version[-4:] == '-dev' else 'release'
release = ''

# -- Options for HTML output ---------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [os.path.join(r'template', 'sphinx_rtd_theme-0.2.4')]
html_title = "DeerNation"
#html_short_title = None
# html_logo = os.path.join(root_dir, "source", "resource", "icon", "comet_webapp_icon_android_48.png")
#html_favicon = None
html_static_path = ['_static']
html_domain_indices = False
html_use_index = True
html_show_sphinx = False
htmlhelp_basename = 'DeerNation'
html_show_sourcelink = False

if len(versions):
    html_context = {
        'versions': versions,
        'current_version': version
    }

# -- Options for Code Examples output ---------------------------------------------------


code_example_dir = "code-example"
code_add_python_path = ["../py"]


################################################################################


def setup(app):
    app.add_stylesheet('theme_override.css')
    app.add_config_value('releaselevel', '', 'env')

    from sphinx.util.texescape import tex_replacements
    tex_replacements += [(u'♮', u'$\\natural$'),
                         (u'ē', u'\=e'),
                         (u'♩', u'\quarternote'),
                         (u'↑', u'$\\uparrow$'),
                         ]