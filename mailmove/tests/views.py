from flask.ext.testing import TestCase
from mailmove import app, mailmove

mailmove.setup_from_settings()

class CreateView(TestCase):

    def create_app(self):
        return mailmove.flask

    def setUp(self):
        pass

