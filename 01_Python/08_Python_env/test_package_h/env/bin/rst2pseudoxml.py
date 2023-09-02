#!/Users/hossamtabana/Library/Mobile Documents/com~apple~CloudDocs/Hossam_files/01_Developer/00_Vscode_2/01_Python/08_Python_env/test_package/env/bin/python3.11

# $Id: rst2pseudoxml.py 9115 2022-07-28 17:06:24Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing pseudo-XML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except Exception:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates pseudo-XML from standalone reStructuredText '
               'sources (for testing purposes).  ' + default_description)

publish_cmdline(description=description)
