from flask import Blueprint, render_template, g
from models import User

bp = Blueprint('profile', __name__)


@bp.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = User.query.filter_by(url_slug=values.pop('user_url_slug'))
    g.profile_owner = query.first_or_404()


@bp.route('/')
def user_page(username):
    '''Retrieves the profile page for the user by username if the requesting client has access to the page, otherwise displays a private page.'''
