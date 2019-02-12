#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Arslan Ahmad'
SITENAME = "Arslan's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored. 
IGNORE_FILES = [".ipynb_checkpoints"]

#THEME = "E:\creating_data_science_blog\jupyter-blog\latest_theme\pelican-themes\\brownstone"

THEME = "E:\creating_data_science_blog\jupyter-blog\latest_theme\pelican-themes\\attila"

DISQUS_SITENAME = "arslanblog"

SITEURL = "https://arslan-san.github.io"

#PAGE_URL = '{slug}'
#PAGE_SAVE_AS = '{slug}'

DISPLAY_PAGES_ON_MENU = False
#DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('About', '/pages/about.html'),
    ('Useful Resources', '/pages/useful-resources.html'),
)

LOAD_CONTENT_CACHE = False

# if you set your home page rahther than blog page then do the following steps

# make file in a page folder called home.md and the content of the file is:

    #Title: Home
    #URL: ../
    #Save_as: ../index.html

    #This is the home page.

# content of the pelicanconfig file is:

    #SITEURL = '/blog'
    #OUTPUT_PATH = 'output/blog'
    #PAGE_URL = '../{slug}.html'
    #PAGE_SAVE_AS = '../{slug}.html'
    #DISPLAY_PAGES_ON_MENU = False
    #DISPLAY_CATEGORIES_ON_MENU = False
    #MENUITEMS = [('Home', '/'), ('Blog', '/blog/')]


