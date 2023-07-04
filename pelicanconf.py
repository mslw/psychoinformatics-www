#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = 'Michael Hanke & Alex Waite'
SITETITLE = 'Psycho&shy;informatics'
SITESUBTITLE = 'at <a href="https://www.fz-juelich.de/en/inm/inm-7">Jülich</a>/<a href="https://www.uniklinik-duesseldorf.de/en/institute-of-systems-neuroscience/teamcontact">Düsseldorf</a>'
SITENAME = 'Psychoinformatics'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

#
# Configure Pelican a bit
#
PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'sitemap' ]
SITEMAP = { 'format': 'xml' }

DIRECT_TEMPLATES = ['404']  # unset all templates; add 404
THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None

#
# Configure the site
#
MENUITEMS = (('home', 'index.html'),
             ('people', 'lab-members.html'),
             ('research', 'research.html'),
             ('software', 'software.html'),
             ('teaching', 'teaching.html'),
             ('publications', 'publications.html'),
             ('contact', 'contact.html'),
)
STATIC_PATHS = ['img/', 'static/']
EXTRA_PATH_METADATA = {
    "static/apple-touch-icon.png": {'path': ''},
    "static/browserconfig.xml": {'path': ''},
    "static/favicon-16x16.png": {'path': ''},
    "static/favicon-32x32.png": {'path': ''},
    "static/favicon.ico": {'path': ''},
    "static/humans.txt": {'path': ''},
    "static/leitfaden.pdf": {'path': ''},
    "static/manifest.json": {'path': ''},
    "static/mstile-150x150.png": {'path': ''},
    "static/robots.txt": {'path': ''},
}

DEFAULT_PAGINATION = False

# We prefer document-relative URLs
RELATIVE_URLS = True
