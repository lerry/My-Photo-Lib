#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-04 16:03
'''
import _env
from web.contrib.template import render_jinja

render = render_jinja(
    'temlates', 
    encoding = 'utf-8',
)
