#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class for handling authentication.

    This class provides methods to determine if authentication is required
    for a given path, retrieve the authorization header from a request,
    and get the current user from a request.

    Methods:
        require_auth(path: str, excluded_paths: List[str]) -> bool:
            Determines if authentication is required for a given path.

        authorization_header() -> str:
            Retrieves the authorization header from the request.

        current_user() -> None:
            Retrieves the current user from the request.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path.

        Args:
            path (str): The path to check.
            excluded_paths (List[str]): A list of paths that do not
            require authentication.

        Returns:
            bool: True if authentication is required, False otherwise.

        The method returns True if:
            - The path is None.
            - The excluded_paths list is None or empty.

        The method returns False if:
            - The path is in the excluded_paths list.

        The method is slash tolerant, meaning it treats paths with or
        without a trailing slash as equivalent.
        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        # Ensure path ends with a slash for comparison
        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            str: The authorization header if present, None otherwise.
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> None:
        """
        Retrieves the current user from the request.

        Returns:
            None: The current user if present, None otherwise.

        This method will be implemented later to extract the current
        user from the request.
        """
        return None
