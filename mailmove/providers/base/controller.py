from mailmove.providers.base.model import BaseProvider
#from mailmove.topics.base.views import blueprint
from mailmove.topics.base.model import BaseTopic
from mailmove.topics.base.controller import BaseController


class BaseProviderController(object):
    name = 'base'
    model = BaseProvider
    #topic_blueprint = blueprint
    topic_name = 'base'
    topic_model = BaseTopic
    topic_controller = BaseController

    @classmethod
    def register(cls, factory):
        cls.model.set_controller(cls)
        factory.register_topic(cls.topic_name, cls.topic_blueprint, cls.topic_model)
        factory.register_provider(cls.topic_name, cls.name, cls.model)
        cls.topic_controller.register_provider(cls)

    def __init__(self, authentication, data=None, model=None):
        self.authentication = authentication
        if data:
            self.model(**data)
        else:
            self.model = model

    def validate(self):
        """
            Shut be implemented on the real controller
        """
        raise "you need to implement the method validate in your controller"

    def get_real_provider(self):
        """
            Shut be implemented on the real controller
        """
        raise "you need to implement the method get_real_provider in your controller"
