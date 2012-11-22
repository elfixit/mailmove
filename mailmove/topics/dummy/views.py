from mailmove.topics.base.views import BaseTopicView
from mailmove.topics.base.views import register as base_register
from flask import Blueprint

blueprint = Blueprint("topic.dummy", __name__)

class DummyView(BaseTopicView):
    pass

