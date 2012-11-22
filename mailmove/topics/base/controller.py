from mailmove.topics.base.model import BaseTopic
from mailmove.topics.base.views import register as register_views
import importlib

class BaseController(object):
    name = 'base'
    providers = {}

    @classmethod
    def register(cls, main):
        main.register_topic(cls.name, cls)
        settings_name = "{}_PROVIDERS".format(cls.name.upper())
        for provider in main.config.get(settings_name):
            provider_mod = importlib.import_module(provider)
            provider_mod.register(cls)
        register_views(main.provider_blueprint)

    @classmethod
    def register_provider(cls, provider):
        cls.providers[provider.name] = provider

    def __init__(self, topic_uuid):
        self.model = BaseTopic.objects.get(_id=topic_uuid)

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

