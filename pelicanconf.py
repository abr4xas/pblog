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
DEFAULT_PAGINATION = 3
STATIC_PATHS = ['files', 'images']
GITHUB_URL = 'https://github.com/abr4xas/'
THEME = 'abr4xas'
FEED_RSS = 'feed'
DISQUS_SITENAME = 'elblogdeabr4xas'
TWITTER_USERNAME = 'abr4xas'
USE_PAGER = 'True'
CC_LICENSE = "CC-BY-NC-SA"
OPEN_GRAPH_FB_APP_ID = '742637482460716'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap','related_posts']

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

RELATED_POSTS_MAX = 10
GOOGLE_ANALYTICS = 'UA-56619331-1'
