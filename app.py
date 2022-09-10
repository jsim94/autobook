CURR_USER_KEY = "curr_user"
UPLOAD_FOLDER = '/assets/user_pictures'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

import os

from flask import Flask
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config.update(
    TESTING=True,
    SECRET_KEY=os.environ.get(
        'SECRET_KEY', "b387efc4-b5c0-435b-b05f-c81a3408ac8e"),
    SQLALCHEMY_DATABASE_URI=(
        os.environ.get('DATABASE_URL', 'postgresql:///autobook')),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_ECHO=True,
    DEBUG_TB_INTERCEPT_REDIRECTS=False,
    UPLOAD_FOLDER=UPLOAD_FOLDER
)

toolbar = DebugToolbarExtension(app)


from models import connect_db
from views import home, profile, project

connect_db(app)

app.register_blueprint(home.bp)
app.register_blueprint(profile.bp, url_prefix='/u/<username>')
app.register_blueprint(project.bp, url_prefix='/p/<project_name>')
