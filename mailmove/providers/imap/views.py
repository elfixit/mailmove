from flask.views import MethodView
from mailmove.topics.mail.views import blueprint

class ImapView(MethodView):
    pass

imap_view = ImapView.as_view('imap_view')
blueprint.add_url_rule('/', view_func=imap_view)
