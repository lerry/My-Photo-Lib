# -*- coding: utf-8 -*-

class Route(object):
    def __init__(self):
        self.urls = []

    def __call__(self, url):
        def _(cls):
            self.urls.append(url)
            self.urls.append(cls.__name__)
            return cls
        return _


