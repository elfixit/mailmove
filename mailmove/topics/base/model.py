from mailmove.models import Topic

class BaseTopic(Topic):
    __allowed_providers = {}

    @classmethod
    def register_provider(cls, provider_doc):
        cls.__allowed_providers[provider_doc.__name__] = provider_doc


