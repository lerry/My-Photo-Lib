#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-05 16:36
'''
import _env
import web
from config import db, img_root

class Img(object):
    def __init__(self, fpath):
        self.fpath = fpath

    @property
    def link(self):
        return self.fpath[len(img_root):]

    @property 
    def thumbnail(self):
        return get_

def img_list(url):
    fpath = os.path.join(img_root, url)
    if os.path.isdir(fpath):
        return scan_folder(fpath)
    else:
        return ['', '']


def save_img(path, mtime, md5):
    db.insert(table_name, path, mtime, md5)

def get_thumb(fpath):
    result = db.where(table_name, path=fpath)
    print result


if __name__ == '__main__':
    a = Img('/home/lerry/imgs/static/1.jpg')
    print a.link

