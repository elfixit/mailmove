# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~

"""

from __future__ import absolute_import
import importlib
from werkzeug import import_string

class MailMoveFactory(object):
    """
        The Registry for all sync components
    """


    def __init__(self, flask, config=False):
        self.flask = flask
        self.config = config
        if not config:
            self.config = flask.config
        else:
            self.flask.config.update(**config)
        self.topic_blueprints = {}
        self.model_registry = {}
        self.main_blueprint = None
        self.pages_blueprint = None

    def setup_from_settings(self):
        self.register_providers()
        for k, b in self.topic_blueprints.items():
            self.flask.register_blueprint(b, url_prefix='/topic/{}'.format(k))
        self.main_blueprint = import_string('mailmove.views.mod')
        self.flask.register_blueprint(self.main_blueprint, url_prefix='/mailmove')
        if self.config.get('ADD_BLUEPRINTS', False):
            for prefix, bp_name in self.config['ADD_BLUEPRINTS'].items():
                blueprint = import_string(bp_name)
                self.flask.register_blueprint(blueprint, url_prefix=prefix)

    def register_topic(self, name, blueprint, model):
        self.topic_blueprints[name] = blueprint
        self.model_registry[name] = dict(model=model)

    def register_providers(self):
        for provider in self.config.get('PROVIDERS', []):
            provider_mod = importlib.import_module(provider)
            provider_mod.register(self)

    def register_provider(self, topic, name, model):
        self.model_registry[topic][name] = model

