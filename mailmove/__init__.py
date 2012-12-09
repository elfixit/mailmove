# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~


"""

from __future__ import absolute_import
import os
from flask import Flask, Config
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from celery import Celery
from mailmove import settings
from mailmove.factory import MailMoveFactory
from mailmove.utils import LazyBlueprint

config = Config(os.path.dirname(__file__), {})
config.from_object(settings)
config.from_envvar('MAILMOVE_SETTINGS', silent=True)

app = Flask(__name__)

mailmove = MailMoveFactory(app, config)

db = MongoEngine(app)

bcrypt = Bcrypt(app)

celery = Celery('mailmove.celery', include=['mailmove.tasks'])
celery.conf.update(**config)
