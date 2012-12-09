from mailmove.topics.base.views import BaseTopicView
from mailmove.topics.base.views import register as base_register
from flask import Blueprint

blueprint = Blueprint("dummy", __name__)

class DummyView(BaseTopicView):
    pass

dummy_view = DummyView.as_view('topic_view')
blueprint.add_url_rule('/', view_func=dummy_view)
