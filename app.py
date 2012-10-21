#!/usr/bin/python
# -*- coding: utf-8 -*-
import _env
import web
from app_list import *
from views._base import route

urls = route.urls
app = web.application(urls, globals(), autoreload=True)

if __name__ == '__main__':
    web.config.debug = True
    app.run()

