# -*- coding=utf-8 -*-

from flask import current_app as app
from flask import g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from mongoengine import (BooleanField, DateTimeField, Document, ListField,
                         ReferenceField, StringField)
from werkzeug.security import check_password_hash, generate_password_hash

from app import http_auth


class Role(Document):
    name = StringField(max_length=32)
    description = StringField(max_length=256)


class User(Document):
    username = StringField(max_length=32)
    email = StringField()
    password_hash = StringField()
    active = BooleanField(default=False)
    active_date = DateTimeField()
    last_active = DateTimeField()
    role = ListField(ReferenceField(Role), default=[])

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def generate_auth_token(self, expiration=600):
        expiration = app.config['TOKEN_EXPIRATION'] or expiration
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id':self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.objects.get(id=data['id'])
        return user

@http_auth.verify_password
def verify_password(username_or_token, password):
    user = User.verify_auth_token(username_or_token)
    if not user:
        try:
            user = User.objects.get(username=username_or_token)
            if check_password_hash(user.password_hash, password) is True:
                user['id'] = str(user['id'])
                g.user = user
                return g.user
            else:
                return False
        except User.DoesNotExist:
            return False
    g.user = user
    return g.user
