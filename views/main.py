#!/usr/bin/python
# -*- coding: utf-8 -*-
import _env
import web
from config import render
from models.main import img_list
from views._base import route, LoginView

@route('/login')
class Login:
    def GET(self):
        return render.login()

    def POST(self):
        print web.data()
        

@route('/(.*)')
class Index(LoginView):
    def GET(self, url):
        dirs, imgs = img_list(url)
        return render.index(dirs=dirs, imgs=imgs)

@route('/about')
class About:
    def GET(self):
        return 'Powered by web.py, Image, Jinja2'


