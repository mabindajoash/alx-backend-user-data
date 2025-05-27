#!/usr/bin/env python3

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
        normalized_path = path if path.endswith('/') else path + '/'

        if normalized_path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """authoriztion header"""
        return None

    def current_user(self, request=None) -> User:
        """current user"""
        return None
