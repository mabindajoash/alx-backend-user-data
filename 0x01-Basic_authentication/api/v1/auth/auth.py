#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth:
    """Class to be used for authentication"""


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:


    def authorization_header(self, request=None) -> str:


    def current_user(self, request=None) -> TypeVar('User'):
