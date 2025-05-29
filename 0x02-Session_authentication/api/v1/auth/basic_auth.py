#!/usr/bin/env python3
"""module for basic authentication"""


import base64
from api.v1.auth.auth import Auth
from typing import Tuple, TypeVar
from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """class BasicAuth inheriting from Auth"""
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Returns the base 64 part of the authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """returns the decoded value of Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
        except Exception:
            return None
        return decoded.decode('utf-8')

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """return user email and password from decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        email, password = decoded_base64_authorization_header.split(":", 1)
        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Returns the user instance based on email an password"""
        if not isinstance(user_pwd, str) or user_pwd is None:
            return None
        if not isinstance(user_email, str) or user_email is None:
            return None
        try:
            user = User.search({'email': user_email})
        except Exception:
            return None
        if not user:
            return None
        if user[0].is_valid_password(user_pwd):
            return user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request."""
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
