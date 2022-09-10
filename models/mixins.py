import uuid
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declared_attr
from . import db


class timestamps(object):
    '''Mixin for creation date column'''
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
    last_edit = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)


class uuid_pk(object):
    '''Mixin for an auto increment int primary key and a unique UUID'''
    pk = db.Column(db.Integer, primary_key=True)
    id = db.Column(UUID(as_uuid=True), unique=True,
                   nullable=False, default=uuid.uuid4)


class user_pk(object):
    '''Mixin to tie table to a user'''
    @declared_attr
    def user_pk(cls):
        return db.Column(db.Integer, db.ForeignKey(
            'users.pk', ondelete="cascade"))
