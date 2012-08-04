#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
by Lerry  http://lerry.org
Last edit at 2012-08-04 16:18
'''
import sys
from os.path import dirname, abspath

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

PWD = dirname(abspath(__file__))
if PWD and PWD not in sys.path:
    sys.path.insert(0, PWD)
