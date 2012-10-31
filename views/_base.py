#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
from lib.route import Route
from lib.session import session_new, id_by_session, session_rm

route = Route()

def logout(self, uid):
    s = web.cookies().get('S')
    session_rm(s)

class View(object):

    @property
    def login(self):
        s = web.cookies().get('S')
        uid = session_get(s)
        return True if uid else False

    def redirect(self, url):
        raise web.seeother(url)

class LoginView(View):
    def __init__(self):
        s = web.cookies().get('S')
        uid = session_get(s)
        if uid:
            self.uid = uid
        else:
            self.redirect('/login')

class NoLoginView(View):
    def __init__(self):
        super(NoLoginView, self).__init__()
        if self.login:
            self.redirect('/')

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
