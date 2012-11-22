from mailmove.providers.base.model import BaseProvider
#from mailmove.topics.base.views import blueprint
from mailmove.topics.base.model import BaseTopic


class BaseProviderController(object):
    name = 'base'
    model = BaseProvider
    #topic_blueprint = blueprint
    topic_name = 'base'
    topic_model = BaseTopic

    @classmethod
    def register(cls, factory):
        factory.register_topic(cls.topic_name, cls.topic_blueprint, cls.topic_model)
        factory.register_provider(cls.topic_name, cls.name, cls.model)

    def __init__(self, data):
        pass
