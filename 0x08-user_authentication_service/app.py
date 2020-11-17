#!/usr/bin/env python3
""" API endpoints
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def root() -> str:
    ''' root route '''
    return jsonify({'message': 'Bienvenue'})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    ''' sefl descriptive '''
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    '''self descriptive'''
    email = request.form.get('email')
    password = request.form.get('password')
    valid_login = AUTH.valid_login(email, password)

    if valid_login:
        session_id = AUTH.create_session(email)
        message = {"email": email, "message": "logged in"}
        response = jsonify(message)
        response.set_cookie('session_id', session_id)

        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    ''' self descriptive '''
    session_id = request.cookies.get("session_id")

    if not session_id:
        abort(403)

    logged_in_user = AUTH.get_user_from_session_id(session_id)

    if not logged_in_user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile() -> str:
    """ profile route of the user
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    message = {"email": user.email}

    return jsonify(message), 200


@app.route('/reset_password', methods=['POST'])
def reset_password() -> str:
    """ reset password token function
    """
    try:
        email = request.form.get('email')
    except KeyError:
        abort(403)

    try:
        reset_user_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)

    message = {"email": email, "reset_token": reset_user_token}

    return jsonify(message), 200


@app.route('/reset_password', methods=['PUT'], strict_slashes=True)
def update_password() -> str:
    """ PUT /reset_password route """
    try:
        email = request.form.get('email')
        reset_token = request.form.get('reset_token')
        new_password = request.form.get('new_password')
    except KeyError:
        abort(400)

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)

    message = {"email": email, "message": "Password updated"}
    return jsonify(message), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
