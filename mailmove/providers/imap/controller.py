from mailmove.providers.base.controller import BaseProviderController
from mailmove.providers.imap.model import ImapProvider
from mailmove.topics.mail.views import blueprint
from mailmove.topics.mail.model import MailTopic
from mailmove.topics.mail.controller import MailController

class ImapController(BaseProviderController):
    name = 'imap'
    model = ImapProvider
    topic_name = MailController.name
    topic_blueprint = blueprint
    topic_model = MailTopic
    topic_controller = MailController
