from mailmove.topics.base.controller import BaseController

class DummyController(BaseController):
    name = 'dummy'

    def test(self):
        result = False
        real_providers = []
        for controller in self.provider_controllers:
            real_providers.append(controller.get_real_provider())
        for provider in real_providers:
            if len(provider) > 0:
                result = True
        return result

    def run(self):
        pass

    def finish(self):
        pass
