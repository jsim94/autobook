from sqlalchemy.dialects.postgresql import ENUM


from . import db
from .mixins import uuid_pk, user_pk, timestamps
from .enums import Reactions


class PostReaction(db.Model):
    '''Reaction class to attach reactions to posts'''
    __tablename__ = 'post_reactions'

    user_pk = db.Column(db.Integer, db.ForeignKey(
        'users.pk', ondelete="cascade"), primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.pk', ondelete="cascade"), primary_key=True)
    reaction = db.Column(ENUM(Reactions),
                         nullable=False, server_default="LIKE")


class PostComment(uuid_pk, user_pk, timestamps, db.Model):
    '''Comment class to attach comments to posts.'''
    __tablename__ = 'post_comments'

    post_id = db.Column(db.Integer, db.ForeignKey(
        'posts.pk', ondelete="cascade"), nullable=False)
    content = db.Column(db.Text)


class Post(uuid_pk, user_pk, timestamps, db.Model):
    '''User post class. Posts can have one user and one user can have many posts'''
    __tablename__ = 'posts'

    content = db.Column(db.String(300), nullable=False)
    pictures = db.relationship('PostPicture', backref='post')
