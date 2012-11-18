from flask.views import MethodView

class BaseTopicView(MethodView):
    __topic__ = 'base'

    def get(self, target):
        abort(501)

    def post(self, target):
        abort(501)

def register(blueprint, view=BaseTopicView):
    view_func = view().as_view(view.__topic__)
    blueprint.add_url_rule('/{}/<target>', view_func=view_func)
