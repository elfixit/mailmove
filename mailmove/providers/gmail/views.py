from flask.views import MethodView
from mailmove.topics.mail.views import blueprint

class GMailView(MethodView):
    pass

gmail_view = GMailView.as_view('gmail_view')
blueprint.add_url_rule('/gmail', view_func=gmail_view)
