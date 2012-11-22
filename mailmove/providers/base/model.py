from mailmove.models import Provider

class BaseProvider(Provider):
    __controller = None

    @classmethod
    def set_controller(cls, controller):
        cls.__controller = controller

