#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-05 16:36
'''
import _env
import os
import web
import hashlib
from config import db, IMG_ROOT, CACHE_DIR, TABLE_NAME, PWD
from misc import resize_img, scan_folder

CACHE_DICT = {}

class InterCache(object):
    def __init__(self, cache_dict):
        self.cache = cache_dict

    def get(self, k):
        return self.cache.get(k)

    def set(self, k, v):
        self.cache[k] = v

cache = InterCache(CACHE_DICT)

class Dir(object):
    def __init__(self, fpath):
        self.fpath = fpath

    @property
    def link(self):
        return self.fpath[len(IMG_ROOT):]

    @property
    def name(self):
        return self.fpath.split(os.sep)[-1]


class Img(Dir):

    @property
    def thumbnail(self):
        return img_thumb(self.fpath, size=[800, 600], post_fix='_800')[len(PWD):]

    @property
    def thumbnail_small(self):
        return img_thumb(self.fpath, size=[270], post_fix='_small')[len(PWD):]

    @property
    def link(self):
        return '/static/raw' + super(Img, self).link


def img_list(url):
    fpath = os.path.join(IMG_ROOT, url)
    if os.path.isdir(fpath):
        dirs, imgs = scan_folder(fpath)
        return dirs, imgs
    else:
        return ['', '']

def img_new(fpath):
    mtime = int(os.path.getmtime(fpath))
    md5 = hashlib.md5(open(fpath, 'rb').read()).hexdigest()
    db.insert(TABLE_NAME, path=fpath, mtime=mtime, md5=md5)
    return md5

def create_thumb(fpath, thumb_path, size):
    if not os.path.isfile(thumb_path):
        try:
            resize_img(fpath, thumb_path, size) 
        except:
            print 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
            print 'something wrong with %s'%fpath

def img_thumb(fpath, size, post_fix=''):
    result = cache.get(fpath)
    if not result:
        result = db.select(TABLE_NAME, what='md5', where='path="%s"'%fpath).list()
        cache.set(fpath, result)
    if result:
        md5 = result[0]['md5']
    else:
        md5 = img_new(fpath)
    thumb_path = os.path.join(CACHE_DIR, md5+post_fix+'.jpg')
    create_thumb(fpath, thumb_path, size)
    return CACHE_DIR+ '/%s'%md5 + post_fix + '.jpg' 
        
if __name__ == '__main__':
    a = Img('/home/lerry/My-Photo-Lib/static/1.jpg')
    print a.link
    print a.thumbnail

