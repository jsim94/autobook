from datetime import datetime
from sqlalchemy.dialects.postgresql import ARRAY, UUID, ENUM
from flask_bcrypt import Bcrypt


from . import db
from .mixins import uuid_pk, timestamps
from .enums import FriendStatus

bcrypt = Bcrypt()


class User(uuid_pk, timestamps, db.Model):
    '''User model'''
    __tablename__ = 'users'

    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    last_login = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow())
    private = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='user')
    projects = db.relationship('Project', backref='user')
    profile_pictures = db.relationship('ProfilePicture', backref='user')
    messages = db.relationship('Message', backref='user')
    friends = db.relationship(
        'User', secondary="friends", backref='friended_by')
    block_list = db.relationship(
        'User', secondary="blocked", backref='blocked_by')

    def __repr__(self):
        return '<User %r>' % self.username


class Friend(db.Model):
    '''Connects users together to represent a friend connection, pending or accepted'''
    __tablename__ = 'friends'

    user1_id = db.Column(db.Integer, db.ForeignKey(
        'users.pk', ondelete="cascade"), primary_key=True)
    user2_id = db.Column(db.Integer, db.ForeignKey(
        'users.pk', ondelete="cascade"), primary_key=True)
    status = db.Column(ENUM(FriendStatus),
                       nullable=False, server_default="PENDING")
    request_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    response_date = db.Column(
        db.DateTime)


class Blocked(timestamps, db.Model):
    '''Connects users together to represent a blocked user'''
    __tablename__ = 'blocked'

    blocking_user = db.Column(db.Integer, db.ForeignKey(
        'users.pk', ondelete="cascade"), primary_key=True)
    blocked_user = db.Column(db.Integer, db.ForeignKey(
        'users.pk', ondelete="cascade"), primary_key=True)
