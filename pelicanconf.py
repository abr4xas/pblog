#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
AUTHOR = u'abr4xas'
SITENAME = u'El blog de abr4xas'
SITEURL = 'https://blog.abr4xas.org'
# Development
#SITEURL = 'http://localhost:8001'
TIMEZONE = 'America/Caracas'
DEFAULT_LANG = u'es'
SITE_LANG = 'es_ES'
SITE_LANG_ALTERNATE = 'en_GB'
DEFAULT_PAGINATION = 6
STATIC_PATHS = ['files', 'images']
GITHUB_URL = 'https://github.com/abr4xas/'
THEME = 'Casper2Pelican'
FEED_RSS = 'feed'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISQUS_SITENAME = 'elblogdeabr4xas'
TWITTER_USERNAME = 'abr4xas'
USE_OPEN_GRAPH = 'True'
OPEN_GRAPH_FB_APP_ID = '742637482460716'
PUBLISHER = 'https://plus.google.com/+Abr4xasOrg'
RELATED_POSTS_MAX = 10
GOOGLE_ANALYTICS = 'UA-18333188-1'
GOOGLE_SV = '858AWu06X8qc7TbbcoxGVUySmw5YVEvau_yPyr3_QKI'
ALEXA = '1zzoXK9co8WU3QqIDIWkiNC1Li0'
MY_WOT = '5b964f1b4f47785f7e24'
MSVALIDATE = 'F42B6441E13617A9043193F830381A74'
SITE_DESCRIPTION = 'El blog de abr4xas, blog sobre noticias, tecnología, música, gnu/linux, anime, actualidad, intercambio y directorio de informacion de servicios profesionales en tecnología. Eventos, Asesorias Software Libre'
TAG_LINE = '# nano /var/log/life.log'
AUTHOR_PIC_URL = 'https://secure.gravatar.com/avatar/b5a93f6390e4bdb85a484d15b549d467'
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', '404')
# [Casper2Pelican] Header images
DEFAULT_HEADER_IMAGE = u'theme/images/main-header.jpg'
ARCHIVE_HEADER_IMAGE = u'theme/images/banner-bg.jpg'
SITE_LOGO = None #u'theme/images/logo.png'
AUTHOR_LOCATION = u'Venezuela'
AUTHOR_BIO = u'Front/Back end Web Developer, algunas veces linux otras OSX...'

# Blogroll
LINKS =  (
    ('abr4xas @ linkedin', 'https://ve.linkedin.com/in/ancrz'),
    ('abr4xas @ behance', 'https://behance.net/abr4xas'),
    ('abr4xas @ twitter', 'https://twitter.com/abr4xas'),
    ('abr4xas @ github', 'http://github.com/abr4xas'),
    ('abr4xas @ fiverr', 'https://www.fiverr.com/abr4xas'),
    )
PLUGIN_PATHS = ["plugins",]
PLUGINS = ['neighbors','minification','sitemap',]
SITEMAP = {
    'format': 'xml',
        'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
STATIC_PATHS = [
    'images',
    'static/browserconfig.xml',
    'static/large.png',
    'static/square.png',
    'static/tiny.png',
    'static/wide.png',
    'static/socialmedia.txt',
]
EXTRA_PATH_METADATA = {
    'static/browserconfig.xml': {
        'path': 'browserconfig.xml'
    },
    'static/large.png': {
        'path': 'large.png'
    },
    'static/square.png': {
        'path': 'square.png'
    },
    'static/tiny.png': {
        'path': 'tiny.png'
    },
    'static/wide.png': {
        'path':'wide.png'
    },
    'static/socialmedia.txt': {
        'path':'socialmedia.txt'
    },
}
