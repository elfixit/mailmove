from flask import Blueprint
from mailmove.topics.base.views import BaseTopicView
from mailmove.topics.base.views import register as base_register

blueprint = Blueprint("mail", __name__)

class MailView(BaseTopicView):
    pass

mail_view = MailView.as_view('topic_view')
blueprint.add_url_rule('/', view_func=mail_view)

