#!/usr/bin/python
# -*- coding: utf-8 -*-
import _env
from config import render
from models.main import img_list
from utils import route

@route('/(.*)')
class Index:
    def GET(self, url):
        dirs, imgs = img_list(url)
        return render.index(dirs=dirs, imgs=imgs)

@route('/about')
class About:
    def GET(self):
        return 'Powered by web.py, Image, Jinja2'


