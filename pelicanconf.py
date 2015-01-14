#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
AUTHOR = u'abr4xas'
SITENAME = u'El blog de abr4xas'
SITEURL = 'http://blog.abr4xas.org'
TIMEZONE = 'America/Caracas'
DEFAULT_LANG = u'es'
# Blogroll
LINKS =  (
		('xombra', 'http://xombra.com/'),
          	('sinfallas', 'http://sinfallas.wordpress.com/'),
          	('echevemaster', 'http://echevemaster.org/'),
          	('Blog Bitix', 'http://picodotdev.github.io/blog-bitix/'),    
)
# Social widget
SOCIAL = (
          ('twitter', 'http://twitter.com/abr4xas'),
          ('github', 'http://github.com/abr4xas'),
)
DEFAULT_PAGINATION = 10
STATIC_PATHS = ['files', 'images']
GITHUB_URL = 'https://github.com/abr4xas/'
THEME = 'pelican-vapor-theme'
FEED_RSS = 'feed'
DISQUS_SITENAME = 'elblogdeabr4xas'
TWITTER_USERNAME = 'abr4xas'
USE_PAGER = 'True'
CC_LICENSE = "CC-BY-NC-SA"
OPEN_GRAPH_FB_APP_ID = '742637482460716'
PUBLISHER = 'https://plus.google.com/+Abr4xasOrg'
STARTUP_IMAGE = 'http://blog.abr4xas.org/theme/images/logo.png'
PLUGIN_PATHS = ['plugins/',]
PLUGINS = ['sitemap',]
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
STATIC_PATHS = ['static/browserconfig.xml',
		'static/large.png',
		'static/square.png',
		'static/tiny.png',
		'static/wide.png',]

EXTRA_PATH_METADATA = {
    'static/browserconfig.xml': {'path': 'browserconfig.xml'},
    'static/large.png': {'path': 'large.png'},
    'static/square.png': {'path': 'square.png'},
    'static/tiny.png': {'path': 'tiny.png'}, 
    'static/wide.png': {'path':'wide.png'},
}
RELATED_POSTS_MAX = 10
GOOGLE_ANALYTICS = 'UA-56619331-1'
GOOGLE_SV = '858AWu06X8qc7TbbcoxGVUySmw5YVEvau_yPyr3_QKI'
