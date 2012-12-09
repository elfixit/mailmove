# -*- coding: utf-8 -*-
"""
mailmove
~~~~~~~~

"""
from __future__ import absolute_import
from mailmove import mailmove
from flask.views import MethodView
from flask import request, session, abort, render_template, Blueprint

mod = Blueprint('mailmove', __name__, template_folder="templates")

from mailmove.decorators import no_robot, job_required

class CreateView(MethodView):
    """

    """
    methods = ['GET', 'POST']

    def get(self):
        topics = []
        for topic in mailmove.model_registry.keys():
            struct = dict(topic=topic, providers=[])
            for provider in mailmove.model_registry[topic].keys():
                if not provider == 'model':
                    struct['providers'].append(provider)
            topics.append(struct)
        return render_template("mailmove.html", topics=topics)

    def post(self):
        abort(501)

create_view = no_robot(CreateView().as_view('create_view'))
mod.add_url_rule('/', view_func=create_view)

class ManageView(MethodView):
    methods = ['GET', 'PUT', 'DELETE']

    def get(self, job):
        abort(501)

    def post(self):
        abort(501)

    def put(self, job):
        abort(501)

    def delete(self, job):
        abort(501)

manage_view = job_required(ManageView().as_view('manage_view'))
mod.add_url_rule('/<string:job_uuid>', view_func=manage_view)


