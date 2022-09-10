from flask import Blueprint, render_template

bp = Blueprint('home', __name__)


@bp.route('/')
def homepage():
    '''If not logged in, returns a homepage with a signup form and a link to a login form.'''
    return 'Hello!'
