from sqlalchemy.dialects.postgresql import ARRAY
from .mixins import uuid_pk, user_pk, timestamps
from . import db


class ProjectComment(uuid_pk, user_pk, timestamps, db.Model):
    '''Comment class to attach comments to project car pages'''
    __tablename__ = 'project_comments'

    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.pk', ondelete="cascade"), nullable=False)
    content = db.Column(db.Text, nullable=False)


class ProjectFollower(db.Model):
    '''Following class to attach user to project car pages for the purpose of following updates'''
    __tablename__ = 'project_followers'

    user_pk = db.Column(db.Integer, db.ForeignKey(
        'users.pk', ondelete="cascade"), primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.pk', ondelete="cascade"), primary_key=True)


class Project(uuid_pk, user_pk, timestamps, db.Model):
    '''Project car class. Each project car has one owner'''
    __tablename__ = 'projects'

    model_id = db.Column(db.Integer)
    name = db.Column(db.String(30))
    description = db.Column(db.String(500))
    pictures = db.relationship('ProjectPicture', backref='project')
    mods = db.Column(ARRAY(db.String(50)))
