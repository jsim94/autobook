from . import db
from .mixins import uuid_pk, user_pk, timestamps


class ProfilePicture(uuid_pk, user_pk, timestamps, db.Model):
    '''Model for users' profile pictures'''
    __tablename__ = 'profile_pictures'

    image_name = db.Column(db.Text, nullable=False)


class PostPicture(uuid_pk, user_pk, timestamps, db.Model):
    '''Model for pictures that are attached to posts'''
    __tablename__ = 'post_pictures'

    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.pk', ondelete="cascade"), nullable=False)
    image_name = db.Column(db.Text, nullable=False)


class ProjectPicture(uuid_pk, user_pk, timestamps, db.Model):
    '''Model for pictures that are attached to projects'''
    __tablename__ = 'project_pictures'

    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.pk', ondelete="cascade"), nullable=False)
    image_name = db.Column(db.Text, nullable=False)
