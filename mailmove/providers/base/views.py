# needs to be implemented on the real provider
from flask import render_template
from flask.views import MethodView

class BaseProviderView(MethodView):

    def get(self):
        return render_template(self.template_name, **self.context)
