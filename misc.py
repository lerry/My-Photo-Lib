#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Start from 2012-08-05 15:19
'''
import _env

import os
import Image
from config import img_type

def scan_folder(dir_path):
    dir_list = []
    img_list = []
    for i in os.listdir(dir_path):
        full_path = os.path.join(dir_path, i)
        if os.path.isfile(full_path) and full_path.split('.')[-1] in img_type:
            img_list.append(full_path)
        elif os.path.isdir(full_path):
            dir_list.append(full_path)
    return dir_list, img_list

def resize_img(img_path, save_path, size=[640,480], quality=90):
    img = Image.open(img_path)
    img.thumbnail(size)
    img.save(save_path, 'RGB', quality=quality)
    
            
if __name__ == '__main__':
    print scan_folder('/home/lerry/Dropbox')

