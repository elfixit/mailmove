import os
from flask import Blueprint, Flask, Config
from celery import Celery
from flask.ext.mongoengine import MongoEngine
from flask.ext.bcrypt import Bcrypt
from flask.ext.script import Manager
from mailmove import settings
import mailmove.pages.views as page_views
#from mailmove.views import mod as mailmove_blueprint

app = Flask(__name__)


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance

@singleton
class MailMove(object):

    def __init__(self):
        self.flask = Flask(__name__)
        self.config = Config(os.path.dirname(__file__), {})
        self.config.from_object(settings)
        if os.environ.get('MAILMOVE_SETTINGS', False):
            self.config.from_envvar('MAILMOVE_SETTINGS')
        self.flask.config.from_object(self.config)
        self.blueprint = Blueprint('mailmove', __name__)
        self.pages_blueprint = page_views.mod
        self.flask.register_blueprint(self.pages_blueprint)
        self.flask.register_blueprint(self.blueprint, url_prefix="/mailmove")
        self.celery = Celery()
        self.db = MongoEngine(self)
        self.bcrypt = Bcrypt(self)
        self.manager = Manager(self.flask)

        self.setup()

    def setup(self):
        pass

    def make_app(self):
        return self.flask

    def get_db(self):
        pass

