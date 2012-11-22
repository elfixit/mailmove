from mailmove.models import Provider

class BaseProvider(Provider):
    __controller = None

    @classmethod
    def set_controller(cls, controller):
        cls.__controller = controller

    def get_controller(self):
        return self.__controller(model=self)
