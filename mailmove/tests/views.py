from flask.ext.testing import TestCase
from mailmove import app, mailmove

mailmove.setup_from_settings()

class ViewTests(TestCase):
    pass
