#!/usr/bin/env python3
""" basic auth module
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar


class BasicAuth(Auth):
    '''self descriptive'''

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''self descriptive'''
        if authorization_header and isinstance(
                authorization_header,
                str) and authorization_header.startswith("Basic "):
            return authorization_header[6:]
