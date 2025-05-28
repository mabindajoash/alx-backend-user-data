#!/usr/bin/env python3
"""module for basic authentication"""
import base64
from api.v1.auth.auth import Auth


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
            decoded = base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None
        return decoded

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
