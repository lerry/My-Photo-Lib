#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-04 16:00
'''
import _env
import web
from config import render

urls = (
    '/', 'index',
    '/page', 'page',
)

app = web.application(urls, globals())

class Index:
    def GET(self, name=''):
        return render.index(name=name)

class Page:
    def GET(self):
        return render.page()
        

if __name__ == '__main__':
    app.run()


