#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
from lib.session import session_new, session_rm
def login(uid):
    web.setcookie('S', session_new(uid))
