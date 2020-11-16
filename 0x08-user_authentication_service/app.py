#!/usr/bin/env python3
""" API endpoints
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def root() -> str:
    ''' root route '''
    return jsonify({'message': 'Bienvenue'})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
