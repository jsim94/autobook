from . import db
from .mixins import uuid_pk, user_pk, timestamps


class MessageGroupUsers(db.Model):
    '''Table linking users to message groups'''
    __tablename__ = 'message_group_users'

    user_pk = db.Column(db.Integer, db.ForeignKey(
        'users.pk', ondelete="cascade"), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey(
        'message_groups.pk', ondelete="cascade"), primary_key=True)


class Message(uuid_pk, user_pk, timestamps, db.Model):
    '''Message class. Messages are tied to a user and the message group they belong to'''
    __tablename__ = 'messages'

    group_id = db.Column(db.Integer, db.ForeignKey(
        'message_groups.pk', ondelete="cascade"), nullable=False)
    content = db.Column(db.Text)


class MessageGroup(uuid_pk, timestamps, db.Model):
    '''Message groups tie users of the group the messages of the group'''
    __tablename__ = 'message_groups'

    name = db.Column(db.String(50), nullable=False)
