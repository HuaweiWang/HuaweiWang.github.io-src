#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Huawei Wang'
SITENAME = u'Huawei Wang'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = u'en'

THEME = "pelican-blueidea"

PLUGINS = ["render_math",
	   "pdf_img"]

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']

#USE_FOLDER_AS_CATEGORY = False


# Display pages list on the top menu
#DISPLAY_PAGES_ON_MENU = True

# Display categories list on the top menu
#DISPLAY_CATEGORIES_ON_MENU = True

# Display categories list as a submenu of the top menu
#DISPLAY_CATEGORIES_ON_SUBMENU =True

# Display the category in the article's info
#DISPLAY_CATEGORIES_ON_POSTINFO (False)

# Display the author in the article's info
#DISPLAY_AUTHOR_ON_POSTINFO (False)

# Display the search form
DISPLAY_SEARCH_FORM  = True

# Sort pages list by a given attribute
PAGES_SORT_ATTRIBUTE = 'tags'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Linkedin', 'www.linkedin.com/in/huawei-wang-biomech'),
         ('CHMS', 'http://chms.csuohio.edu/'),
         ('HMC', 'http://hmc.csuohio.edu/'),)

# Social widget
SOCIAL = (('Tiwtter', 'https://twitter.com/Peter_W_Wang'),)
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
