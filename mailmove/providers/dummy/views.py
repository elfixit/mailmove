from flask.views import MethodView
from mailmove.topics.dummy.views import blueprint

class DummyView(MethodView):
    pass

dummy_view = DummyView.as_view('dummy_view')
blueprint.add_url_rule('/dummy', view_func=dummy_view)
