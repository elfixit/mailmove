from mailmove.providers.base.controller import BaseProviderController
from mailmove.providers.dummy.model import DummyProvider
from mailmove.topics.dummy.views import blueprint
from mailmove.topics.dummy.model import DummyTopic

class DummyController(BaseProviderController):
    model = DummyProvider
    topic_blueprint = blueprint
    topic_model =
