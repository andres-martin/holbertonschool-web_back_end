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
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''self descriptive'''
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''self descriptive'''
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None
