from flask import Blueprint, render_template
from models import Project

bp = Blueprint('project', __name__)


@bp.route('/')
def project_page(project_id):
    '''Retreives the page for the project car if found and if the requesting client has access to the page.'''
