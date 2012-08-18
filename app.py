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
    '/(.*)', 'index',
)

app = web.application(urls, globals())

class index:
    def GET(self, url):
        dirs, imgs = img_list(url)
        return render.index(dirs=dirs, imgs=imgs)


if __name__ == '__main__':
    web.config.debug = True
    app.run()


