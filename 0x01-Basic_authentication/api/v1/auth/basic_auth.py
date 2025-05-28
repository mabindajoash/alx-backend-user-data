#!/usr/bin/env python3
"""module for basic authentication"""

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
