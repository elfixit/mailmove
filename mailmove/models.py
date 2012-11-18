from mailmove.app import MailMove

mm = MailMove()
db = mm.db

class Provider(db.EmbeddedDocument):
    delete_after = db.BooleanField()

    meta = {
        'allow_inheritance': True
    }

class Topic(db.Document):
    job = db.ReferenceField('Job')
    providers = db.ListField(db.EmbeddedDocumentField(Provider))

    meta = {
        'allow_inheritance': True
    }

class Job(db.Document):
    tasks = db.ListField(db.ReferenceField(Topic))
    password = db.StringField()
    state = db.IntField()
    credentials = db.StringField()

    def get_crediential(self, name):
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

