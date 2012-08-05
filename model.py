#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-05 16:36
'''
import _env
import web
from config import db_file, db_table

db = web.database(dbn='sqlite', db=db_file)

def save_img(path, mtime, md5):
    db.insert(db_table, path, mtime, md5)

def get_list
