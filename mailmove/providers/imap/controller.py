from mailmove.providers.base.controller import BaseProviderController
from mailmove.providers.imap.model import ImapProvider
from mailmove.topics.mail.views import blueprint
from mailmove.topics.mail.model import MailTopic

class ImapController(BaseProviderController):
    name = 'imap'
    model = ImapProvider
    topic_name = 'mail'
    topic_blueprint = blueprint
    topic_model = MailTopic
