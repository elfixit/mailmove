# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~

"""
from __future__ import absolute_import
from werkzeug import import_string, cached_property

class LazyView(object):
    def __init__(self, import_name):
        self.__module__, self.__name__ = import_name.rsplit('.', 1)
        self.import_name = import_name

    @cached_property
    def view(self):
        return import_string(self.import_name)

    def __call__(self, *args, **kwargs):
        return self.view(*args, **kwargs)

from flask import Blueprint

class LazyBlueprint(Blueprint):
    def __init__(self, name, import_name, static_folder=None,
                 static_url_path=None, template_folder=None,
                 url_prefix=None, subdomain=None, url_defaults=None):
        self.views = '.'.join(name.split('.')[:-1] + ['views'])
        self.lazyloader = self.add_url_rule('/<path:endpoint>',
                                            'lazyloader', self.lazyloader)

    def lazyloader(self, endpoint, **kw):
        self.lazyloader.remove_url_rule() #THIS DOESN'T WORK
        self.addviews(self.views)
        self.redispatch(endpoint, **kw)
