from mailmove.providers.base.controller import BaseProviderController
from mailmove.providers.gmail.model import GMailProvider
from mailmove.topics.mail.views import blueprint
from mailmove.topics.mail.model import MailTopic
from mailmove.topics.mail.controller import MailController

class GMailController(BaseProviderController):
    name = 'gmail'
    model = GMailProvider
    topic_name = MailController.name
    topic_blueprint = blueprint
    topic_model = MailTopic
    topic_controller = MailController
