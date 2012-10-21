#!/usr/bin/python
# -*- coding: utf-8 -*-
import _env
import os
import web
from os.path import join
from redis import Redis, StrictRedis
from web.contrib.template import render_jinja


render = render_jinja(
    'template',
    encoding='utf-8',
)
img_type = (
        'jpg',
        'bmp',
        'png',
        'gif',
)
PWD = _env.PWD

redis = StrictRedis(host='localhost', port=6379, db=0)


HOST = 'img.lerry.tk'
IMG_ROOT = '/home/lerry/imgs'
CACHE_DIR = join(PWD, 'static/.cache')
DB_NAME = join(PWD, 'img.db')
TABLE_NAME = 'img_list'
db = web.database(dbn='sqlite', db=DB_NAME)

if not os.path.exists(CACHE_DIR):
    os.mkdir(CACHE_DIR)

