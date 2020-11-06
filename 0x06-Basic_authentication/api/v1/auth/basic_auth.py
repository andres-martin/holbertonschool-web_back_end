#!/usr/bin/env python3
""" basic auth module
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar
import base64
import binascii


class BasicAuth(Auth):
    '''self descriptive'''

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''self descriptive'''
        if authorization_header and isinstance(
                authorization_header,
                str) and authorization_header.startswith("Basic "):
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_auth_header: str) -> str:
        '''self descriptive'''
        if base64_auth_header and isinstance(
                base64_auth_header, str):
            try:
                encoded = base64_auth_header.encode('utf-8')
                base = base64.b64decode(encoded)
                return base.decode('utf-8')
            except binascii.Error:
                return None
