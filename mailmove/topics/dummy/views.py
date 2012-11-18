from mailmove.topics.base.views import BaseTopicView
from mailmove.topics.base.views import register as base_register

class DummyView(BaseTopicView):
    pass

def register(blueprint):
    base_register(blueprint, view=DummyView)
