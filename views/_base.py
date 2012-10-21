#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
from lib.route import Route
from lib.session import session_set, session_get, session_rm

route = Route()

def login(self, uid):
    web.cookie.set('S', session_set(uid))

class LoginView:
    def __init__(self):
        if not web.cookies().get('S'):
             raise web.seeother('/login')

def my_loadhook():
    print "my load hook"

    def my_unloadhook():
        print "my unload hook"

        app.add_processor(web.loadhook(my_loadhook))
        app.add_processor(web.unloadhook(my_unloadhook))
    

'''
setcookie(name, value, expires="", domain=None, secure=False): 
web.cookies().get(cookieName) 
foo = web.cookies(cookieName=defaultValue)
foo.cookieName 
'''
