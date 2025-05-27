#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth:
    """Class to be used for authentication"""


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method returns false"""
        return False


    def authorization_header(self, request=None) -> str:
        """authoriztion header"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
