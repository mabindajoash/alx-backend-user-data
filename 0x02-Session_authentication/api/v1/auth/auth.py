#!/usr/bin/env python3
"""Module for the authentication system"""

from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """Class to be used for authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method returns false"""
        if path is None:
            return True
        if not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'

        for excluded in excluded_paths:
            if excluded.endswith('*'):
                if path.startswith(excluded[:-1]):
                    return False
            else:
                if not excluded.endswith('/'):
                    excluded += '/'
                if path == excluded:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """authoriztion header"""
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None

        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """current user"""
        return None
