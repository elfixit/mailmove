from mailmove import db
from mailmove.providers.base.model import BaseProvider

class ImapProvider(BaseProvider):
    host = db.StringField()
    port = db.IntField(required=False)
    exclude = db.ListField(db.StringField())
