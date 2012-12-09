from mailmove import db
from mailmove.providers.base.model import BaseProvider

class GMailProvider(BaseProvider):
    exclude = db.ListField(db.StringField())
