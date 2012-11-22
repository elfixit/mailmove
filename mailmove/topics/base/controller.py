from mailmove.models import Topic
from mailmove.topics.base.views import register as register_views
import importlib

class BaseController(object):
    name = 'base'
    providers = {}

    @classmethod
    def register_provider(cls, provider):
        cls.providers[provider.name] = provider

    def __init__(self, topic_uuid):
        self.model = Topic.objects.get(_id=topic_uuid)
        self.provider_controllers = []
        for provider in self.model.providers:
            if issubclass(provider.__class__, Topic):
                self.provider_controllers.append(provider.get_controller())

    def test(self):
        """
            Will be implemented in the real one
        """
        raise "you need to implemented the test method in your topic controller"

    def run(self):
        """
            Needs to be implemented in the real one
        """
        raise "you need to implemented the run method in your topic controller"

    def finish(self):
        """
            Needs to be implemented in the real one
        """
        raise "you need to implemented the finish method in your topic controller"

