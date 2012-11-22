# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~

"""
from __future__ import absolute_import
from mailmove import db

class Provider(db.Document):
    topic = db.ReferenceField('Topic')
    credential = db.StringField()
    delete_after = db.BooleanField()

    meta = {
        'allow_inheritance': True
    }

class Topic(db.Document):
    job = db.ReferenceField('Job')
    providers = db.ListField(db.ReferenceField(Provider))

    meta = {
        'allow_inheritance': True
    }

class Job(db.Document):
    tasks = db.ListField(db.ReferenceField(Topic))
    password = db.StringField()
    state = db.IntField()
    credentials = db.ListField(db.StringField())

    def get_credentials(self, name):
        pass

#from mailmove.controller import MailMove
"""
class FileCollection(object):

    def __init__(self, collection):
        MailMove.config.get("")

class FileModel(object):

    def __init__(self, *args, **kwargs):
        pass
"""

