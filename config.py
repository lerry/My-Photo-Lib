#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-04 16:03
'''
import _env
import os
from web.contrib.template import render_jinja

render = render_jinja(
    'template', 
    encoding = 'utf-8',
)

img_type = (
        'jpg',
        'bmp',
        'png',
        'gif',
)

img_root = '/home/lerry/Dropbox'

cache_dir = os.path.join(_env.PWD, 'cache')
