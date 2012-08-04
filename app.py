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
    '/(.*)', 'index',
)

app = web.application(urls, globals())

class index:
    def GET(self, name=''):
        return 'Hello, %s'%name

if __name__ == '__main__':
    app.run()


