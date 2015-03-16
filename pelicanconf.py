#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
AUTHOR = u'abr4xas'
SITENAME = u'El blog de abr4xas'
SITEURL = 'http://blog.abr4xas.org'
TIMEZONE = 'America/Caracas'
DEFAULT_LANG = u'es'
SITE_LANG = 'es_ES'
SITE_LANG_ALTERNATE = 'en_GB'
DEFAULT_PAGINATION = 6
STATIC_PATHS = ['files', 'images']
GITHUB_URL = 'https://github.com/abr4xas/'
#THEME = 'pelican-vapor-theme'

THEME = 'Casper2Pelican'
FEED_RSS = 'feed'
DISQUS_SITENAME = 'elblogdeabr4xas'
TWITTER_USERNAME = 'abr4xas'
USE_OPEN_GRAPH = 'True'
OPEN_GRAPH_FB_APP_ID = '742637482460716'
PUBLISHER = 'https://plus.google.com/+Abr4xasOrg'
RELATED_POSTS_MAX = 10
GOOGLE_ANALYTICS = 'UA-56619331-1'
GOOGLE_SV = '858AWu06X8qc7TbbcoxGVUySmw5YVEvau_yPyr3_QKI'
SITE_DESCRIPTION = 'El blog de abr4xas, blog sobre noticias, tecnología, música, gnu/linux, anime, actualidad, intercambio y directorio de informacion de servicios profesionales en tecnología. Eventos, Asesorias Software Libre'
TAG_LINE = '# nano /var/log/life.log'
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
PLUGIN_PATHS = ["plugins",]
PLUGINS = ['minification','sitemap',]
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
		'static/wide.png',
        'static/socialmedia.txt',
        'static/.htaccess',]
EXTRA_PATH_METADATA = {
    'static/browserconfig.xml': {'path': 'browserconfig.xml'},
    'static/large.png': {'path': 'large.png'},
    'static/square.png': {'path': 'square.png'},
    'static/tiny.png': {'path': 'tiny.png'}, 
    'static/wide.png': {'path':'wide.png'},
    'static/socialmedia.txt': {'path':'socialmedia.txt'}, 
    'static/.htaccess': {'path':'.htaccess'},     
}
