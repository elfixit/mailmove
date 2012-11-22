from mailmove import db
from mailmove.providers.base.model import BaseProvider


class DummyProvider(BaseProvider):
    list = db.ListField(db.StringField())
