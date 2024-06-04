#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class to manage API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required
        """
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        # Ensure path ends with a slash
        if path[-1] != '/':
            path += '/'
        # Check if path is in excluded_paths
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user
        """
        return None
