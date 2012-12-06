import unittest2
from flask import Flask, Response
from flask.ext.testing import TestCase
from mailmove import mailmove, bcrypt
from mailmove.decorators import no_robot, job_required
from mailmove.models import Job

def job_required_test(job):
    resp = "FALSE"
    if job:
        resp = "TRUE"
    return resp


class DecoratorJobRequiredTests(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config.update(**mailmove.config)
        app.config['TESTING'] = True
        method = job_required(job_required_test)
        method.methods = ['GET', 'POST', 'OPTIONS']
        app.add_url_rule('/<string:job_uuid>', view_func=method)
        return app

    def setUp(self):
        super(DecoratorJobRequiredTests, self).setUp()
        self.job = Job()
        self.job.password = bcrypt.generate_password_hash("mailmove_test")
        self.job.status = 1
        self.job.save()

    def test_with_job(self):
        response = self.client.post('/{}'.format(self.job.id), data={'pass': 'mailmove_test'})
        self.assert200(response)

    def test_with_job_invalid_pass(self):
        response = self.client.post('/{}'.format(self.job.id), data={'pass': 'invalid_pass'})
        self.assert403(response)

    def test_with_invalid_job(self):
        response = self.client.post('/{}'.format('234fdsfesfdsjeklfakjdfsafjels'), data={'pass': 'nopass'})
        self.assert404(response)

    def tearDown(self):
        self.job.delete()
