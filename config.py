#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-04 16:03
'''
import _env
import os
from os.path import join
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
pwd = _env.PWD
img_root = '/home/lerry/imgs'
cache_dir = join(pwd, 'cache')

db_file = join(pwd, 'img.db')
table_name = join(pwd, 'img_list')
