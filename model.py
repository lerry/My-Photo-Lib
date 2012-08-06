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
from config import db, table_name, img_root, cache_dir, pwd
from misc import resize_img, scan_folder

class Img(object):
    def __init__(self, fpath):
        self.fpath = fpath

    @property
    def link(self):
        return self.fpath[len(pwd):]

    @property 
    def thumbnail(self):
        return img_thumb(self.fpath)[len(pwd):]

def img_list(url):
    fpath = os.path.join(img_root, url)
    if os.path.isdir(fpath):
        dirs, imgs = scan_folder(fpath)
        new_imgs = []
        for i in imgs:
            new_imgs.append(Img(i))
        return dirs, new_imgs
    else:
        return ['', '']


def img_new(fpath):
    mtime = int(os.path.getmtime(fpath))
    md5 = hashlib.md5(open(fpath, 'rb').read()).hexdigest()
    db.insert(table_name, path=fpath, mtime=mtime, md5=md5)
    create_thumb(fpath, md5)
    return md5

def create_thumb(fpath, md5):
    thumb_path = os.path.join(cache_dir, md5+'.jpg')
    if not os.path.isfile(thumb_path):
        resize_img(fpath, os.path.join(cache_dir, md5+'.jpg')) 

def img_thumb(fpath):
    result = db.select(table_name, what='md5', where='path="%s"'%fpath).list()
    if result:
        md5 = result[0]['md5']
    else:
        md5 = img_new(fpath)
    return cache_dir+ '/%s'%md5 + '.jpg' 
        
if __name__ == '__main__':
    a = Img('/home/lerry/My-Photo-Lib/static/1.jpg')
    print a.link
    print a.thumbnail

