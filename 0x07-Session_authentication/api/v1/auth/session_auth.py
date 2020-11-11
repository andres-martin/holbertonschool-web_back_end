#!/usr/bin/env python3
'''Session Auth class'''

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
import uuid
from models.user import User


class SessionAuth(Auth):
    '''self descriptive'''
    pass
