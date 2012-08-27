#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-04 16:00
'''
import _env
import web
from os.path import join
from config import render
from model import img_list

urls = (
    '/about', 'About',
    '/(.*)', 'Index',
)

app = web.application(urls, globals(), autoreload=True)

class Index:
    def GET(self, url):
        dirs, imgs = img_list(url)
        return render.index(dirs=dirs, imgs=imgs)

class About:
    def GET(self):
        return 'Powered by web.py, Image, Jinja2'

if __name__ == '__main__':
    web.config.debug = True
    app.run()

