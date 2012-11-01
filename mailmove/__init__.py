from flask import Blueprint, Flask

bp_mailmove = Blueprint('mailmove', __name__, template_folder='templates', static_folder='static')
bp_mailmove_pages = Blueprint('mailmove_pages', __name__+".pages", template_folder='templates', static_folder='static')

import mailmove.views

# this flask app is just for debug and demonstration
# you can simple run it with python -m mailmove
app = Flask(__name__)
app.register_blueprint(bp_mailmove_pages)
app.register_blueprint(bp_mailmove, url_prefix="/mailmove")

def run():
    app.run(debug=True)

if __name__ == "__main__":
    run()

