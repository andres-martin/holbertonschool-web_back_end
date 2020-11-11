#!/usr/bin/env python3
""" sesion auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.app import auth
import os
from flask import session


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """ GET /api/v1/users
    Return:
      - list of all User objects JSON represented
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 401
    if not user[0].is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    sesion_id = auth.create_session(user[0].id)
    sesion_name = os.getenv("SESSION_NAME")
    user_dict = jsonify(user[0].to_json())
    user_dict.set_cookie(sesion_name, sesion_id)
    return user_dict
