# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~

"""
from __future__ import absolute_import
import os, json
from mailmove import db, mailmove

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

    def __init__(self, *args, **kwargs):
        if kwargs.get('credentials', False):
            credentials = kwargs['credentials']
            for k, d in credentials.items():
                self.set_credentials(k, d)
        super(Job, self).__init__(*args, **kwargs)

    def __get_storepath(self):
        return os.path.abspath(os.path.join(mailmove.config['MAILMOVE_JOBSTORE'], self._id))

    def __get_credentialstore(self, name):
        file = os.path.join(self.__get_storepath(), name)
        fp = open(file)
        return fp

    def get_credentials(self, name):
        fp = self.__get_credentialstore(name)
        data = json.load(fp)
        fp.close()
        return data

    def set_credentials(self, name, data):
        fp = self.__get_credentialstore(name)
        data = json.dump(data, fp)
        fp.close()
