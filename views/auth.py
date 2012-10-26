#!/usr/bin/python
# -*- coding: utf-8 -*-
import _env
import web
from config import render
from models.main import img_list
from views._base import route, LoginView, NoLoginView

@route('/register')
class Register(NoLoginView):
    def GET(self, id=0):
        return render.register()

    def POST(self):
        print web.data()
        
