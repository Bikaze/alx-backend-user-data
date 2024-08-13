#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required.
        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not
            require authentication.
        Returns:
            bool: False for now, will be implemented later.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.
        Args:
            request: The Flask request object.
        Returns:
            str: None for now, will be implemented later.
        """
        return None

    def current_user(self, request=None) -> None:
        """
        Retrieves the current user from the request.
        Args:
            request: The Flask request object.
        Returns:
            TypeVar('User'): None for now, will be implemented later.
        """
        return None
