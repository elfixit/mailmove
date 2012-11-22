from __future__ import absolute_import
import os
import importlib
from flask import Flask, Config
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from celery import Celery
from werkzeug import import_string
from mailmove import settings
from mailmove.utils import LazyBlueprint

class MailMoveFactory(object):

    def __init__(self, flask, config=False):
        self.flask = flask
        self.config = config
        if not config:
            self.config = flask.config
        else:
            for k, v in config.items():
                self.flask.config[k] = v
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
        if k, b in self.config.get('ADD_BLUEPRINTS', (())):
            self.flask.register_blueprint(b, url_prefix=k)

    def register_topic(self, name, blueprint, model):
        self.topic_blueprints[name] = blueprint
        self.model_registry[name] = dict(model=model)

    def register_providers(self):
        for provider in self.config.get('PROVIDERS', []):
            provider_mod = importlib.import_module(provider)
            provider_mod.register(self)

    def register_provider(self, topic, name, model):
        self.model_registry[topic][name] = model



config = Config(os.path.dirname(__file__), {})
config.from_object(settings)
config.from_envvar('MAILMOVE_SETTINGS', silent=True)

app = Flask(__name__)

mailmove = MailMoveFactory(app, config)

db = MongoEngine(app)

bcrypt = Bcrypt(app)

celery = Celery('mailmove.celery', include=['mailmove.tasks'])
celery.conf.update(**config)
