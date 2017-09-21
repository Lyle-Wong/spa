# -*- coding=utf-8 -*-
from flask import g, request, abort, jsonify

from . import auth
from .models import User
from datetime import datetime

from app import http_auth

@auth.route('/users/', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    try:
        User.objects.get(username=username)
        abort(400)
    except User.DoesNotExist:
        user = User(username=username)
        user.hash_password(password)
        user.save()
    return jsonify({'username':user.username})

@auth.route('/users/<username>/')
def get_user(username):
    user = User.objects.get(username=username)
    if not user:
        abort(400)
    return jsonify(user)


@auth.route('/token/')
@http_auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    user = g.user
    user.last_active = datetime.now()
    user.save()
    return jsonify({'token':token.decode('ascii')})