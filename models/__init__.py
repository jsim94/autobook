from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .users import *
from .posts import *
from .projects import *
from .messages import *
from .images import *


def connect_db(app):

    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()
