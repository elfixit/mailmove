from flask import Blueprint, render_template, abort

mod = Blueprint('mailmove.pages', __name__, template_folder="templates")

@mod.route('/', defaults={'page': 'index'})
@mod.route('/<page>')
def page(page):
    try:
        return render_template('pages/{}.html'.format(page), name=page)
    except:
        abort(404)
