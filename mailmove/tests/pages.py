from flask.ext.testing import TestCase
from mailmove import app

class PageTests(TestCase):

    def create_app(self):
        #app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_index(self):
        response = self.client.get('/')
        self.assert200(response)

    def test_contact(self):
        response = self.client.get('/contact')
        self.assert200(response)

    def test_about(self):
        response = self.client.get('/about')
        self.assert200(response)

    def test_inexisting(self):
        response = self.client.get('/blabla')
        self.assert404(response)