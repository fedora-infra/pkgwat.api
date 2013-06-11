# -*- coding: utf-8 -*-

import sys
import os
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'pkgwat'
copyright = u'2012-2013, Red Hat, Inc.  Ralph Bean <rbean@redhat.com>'
version = '0.9'
release = '0.9'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pkgwatdoc'
latex_elements = {
}
latex_documents = [
    ('index', 'pkgwat.tex', u'pkgwat Documentation',
     u'Red Hat, Inc.  Ralph Bean \\textless{}rbean@redhat.com\\textgreater{}',
     'manual'),
]
man_pages = [
    ('index', 'pkgwat', u'pkgwat Documentation',
     [u'Red Hat, Inc.  Ralph Bean <rbean@redhat.com>'], 1)
]
texinfo_documents = [
    ('index', 'pkgwat', u'pkgwat Documentation',
     u'Red Hat, Inc.  Ralph Bean <rbean@redhat.com>', 'pkgwat',
     'One line description of project.',
     'Miscellaneous'),
]
epub_title = u'pkgwat'
epub_author = u'Red Hat, Inc.  Ralph Bean <rbean@redhat.com>'
epub_publisher = u'Red Hat, Inc.  Ralph Bean <rbean@redhat.com>'
epub_copyright = u'2012, Red Hat, Inc.  Ralph Bean <rbean@redhat.com>'
