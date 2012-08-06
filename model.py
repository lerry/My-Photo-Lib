#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-05 16:36
'''
import _env
import web
from config import db_file, table_name

db = web.database(dbn='sqlite', db=db_file)

def save_img(path, mtime, md5):
    db.insert(table_name, path, mtime, md5)

def thumbnail_list(path_list):
    result = []
    for i in path_list:
        result.append(db.where(table_name, path=i))

