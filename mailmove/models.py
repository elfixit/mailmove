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
        self.__temp_credentials = {}
        if kwargs.get('credentials', False):
            credentials = kwargs['credentials']
            for k, d in credentials.items():
                self.set_credentials(k, d)
        super(Job, self).__init__(*args, **kwargs)

    def __get_storepath(self):
        return os.path.abspath(os.path.join(mailmove.config['MAILMOVE_JOBSTORE'], str(self.id)))

    def __get_credentialstore(self, name):
        file = os.path.join(self.__get_storepath(), name)
        fp = open(file)
        return fp

    def get_credentials(self, name):
        if name in self.__temp_credentials.keys():
            return self.__temp_credentials[name]
        elif self.id:
            fp = self.__get_credentialstore(name)
            data = json.load(fp)
            fp.close()
            self.__temp_credentials[name] = data
            return data

    def set_credentials(self, name, data):
        if not name in self.credentials:
            self.credentials.append(name)
        if not self.id:
            self.__temp_credentials[name] = data

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)
        if not os.path.exists(self.__get_storepath()):
            os.mkdir(self.__get_storepath())
        for name in self.credentials:
            fp = self.__get_credentialstore(name)
            data = json.dump(data, fp)
            fp.close()
