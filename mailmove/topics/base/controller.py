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
    def provider_register(cls, provider):
        cls.providers.add(provider.name, provider)

    def __init__(self, topic_uuid):
        self.model = BaseTopic.objects.get(_id=topic_uuid)

