#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jepio'
SITENAME = 'Jepio\'s blog'
SITEURL = '//jepio.github.com'
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', '//getpelican.com/'),
         ('Python.org', '//python.org/'),
         ('Jinja2', '//jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', '//github.com/jepio'),
          ('twitter', '//twitter.com/jeremip'),)

DEFAULT_PAGINATION = False

THEME = "notmyidea"
CSS_FILE = 'my_main.css'
GITHUB_URL = "//www.github.com/jepio/jepio.github.io"

PLUGINS = [ "pelican_gist" ]
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
