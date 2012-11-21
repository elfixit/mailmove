from flask import Blueprint
from mailmove.topics.base.views import BaseTopicView
from mailmove.topics.base.views import register as base_register

blueprint = Blueprint(__name__)

class MailView(BaseTopicView):
    pass


