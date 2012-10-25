#!/usr/bin/python
# -*- coding: utf-8 -*-
import _env
import web
from config import render
from views._base import route, LoginView, View, NoLoginView
from lib.base import login as _login
from models.main import img_list

@route('/login')
class Login(NoLoginView):
    def GET(self):
        return render.login()

    def POST(self):
        u =  web.input().u
        p = web.input().p
        if u and p:
            _login(123)
            raise web.redirect('/comment/222')
        
@route('/about')
class About:
    def GET(self):
        return 'Powered by web.py, Image, Jinja2'

@route('/uploads')
@route('/avatar')
@route('/')
#class Index(LoginView):
class Index:
    def GET(self, url=''):
        dirs, imgs = img_list(url)
        return render.index(dirs=dirs, imgs=imgs)

