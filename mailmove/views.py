from flask import render_template, abort
from mailmove import bp_mailmove, bp_mailmove_pages


@bp_mailmove_pages.route('/', defaults={'page': 'index'})
@bp_mailmove_pages.route('/<page>')
def page(page):
    try:
        return render_template('pages/{}.html'.format(page), name=page)
    except:
        abort(404)
