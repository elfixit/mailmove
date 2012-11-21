from flask.views import MethodView
from flask import abort, Blueprint

mod = Blueprint('mailmove', __name__, template_folder="templates")

from mailmove.decorators import no_robot, job_required

class CreateView(MethodView):
    methods = ['GET', 'POST']
    decorators = [no_robot]

    def get(self):
        abort(501)

    def post(self):
        abort(501)

create_view = CreateView().as_view('create_view')
mod.add_url_rule('/', view_func=create_view)

class ManageView(MethodView):
    methods = ['GET', 'PUT', 'DELETE']
    decorators = [job_required,]

    def get(self, job):
        abort(501)

    def post(self):
        abort(501)

    def put(self, job):
        abort(501)

    def delete(self, job):
        abort(501)

manage_view = ManageView().as_view('manage_view')
mod.add_url_rule('/<job_uuid>', view_func=manage_view)


