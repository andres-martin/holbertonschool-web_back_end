#!/usr/bin/env python3
""" auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    '''self descriptive'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''self descriptive'''
        return False

    def authorization_header(self, request=None) -> str:
        '''self descriptive'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''self descriptive'''
        return None
