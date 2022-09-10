CURR_USER_KEY = "curr_user"
UPLOAD_FOLDER = '/assets/user_pictures'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

import os

from functools import wraps
from flask import Flask, render_template, request, flash, redirect, session, g, url_for
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.utils import secure_filename

from views import home, profile, project
# from forms import SignupForm, LoginForm
from models import db, connect_db
from validators import allowed_file


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

login_manager = LoginManager()
login_manager.init_app(app)

connect_db(app)

app.register_blueprint(home.bp)
app.register_blueprint(profile.bp, url_prefix='/u/<username>')
app.register_blueprint(project.bp, url_prefix='/p/<project_name>')
