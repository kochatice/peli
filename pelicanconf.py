#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mustafa Ray'
SITENAME = u'Mustafa Ray'
SITEURL = ''
GITHUB_URL = 'https://kochatice.github.io/peli'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

SOCIAL = (('twitter', 'http://twitter.com/ametaireau'),
          ('lastfm', 'http://lastfm.com/user/akounet'),
          ('github', 'http://github.com/ametaireau'),)

DEFAULT_PAGINATION = 10
LOAD_CONTENT_CACHE = False
RELATIVE_URLS = True
MARKUP = ('md', 'ipynb2')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb2.markup', 'ipynb2.liquid']

THEME = 'themes/pelican-clean-blog'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True