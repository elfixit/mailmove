from mailmove.providers.base.controller import BaseProviderController
from mailmove.providers.dummy.model import DummyProvider
from mailmove.topics.dummy.views import blueprint
from mailmove.topics.dummy.model import DummyTopic
from mailmove.topics.dummy.controller import DummyController

class DummyController(BaseProviderController):
    name = 'dummy'
    model = DummyProvider
    topic_name = DummyController.name
    topic_blueprint = blueprint
    topic_model = DummyTopic
    topic_controller = DummyController
