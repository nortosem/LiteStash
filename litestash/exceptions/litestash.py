"""LiteStash Exception Module

This module defines the base exception for the LiteStashPackage
"""
import datetime


class LiteStashBaseException(Exception):
    """The Base Exception for the LiteStash Project

    Provides common attributes and methods for all custom exceptions.

    Attributes:
        code (str, optional):
            The error code for a specific exception
        details (dict, optional):
            A dictionary containing more detailed error information.
        timestamp (datetime.datetime):
            The time when the exception was raised.
        user_message (str, optional):
            A user-friendly message for display.

    Methods:
        to_dict(): Returns a dictionary representation of the exception.
        __str__(): Returns a formatted string representation of the exception.
    """
    def __init__(self,
                 message=None,
                 code=None,
                 details=None,
                 user_message=None):
        super().__init__(message)
        self.code = code
        self.details = details or {}
        self.timestamp = datetime.datetime.utcnow()
        self.user_message = user_message or message

    def to_dict(self):
        """Returns a dictionary representation of the exception."""
        return {
            "message": str(self),
            "code": self.code,
            "details": self.details,
            "timestamp": self.timestamp.isoformat(),
            "user_message": self.user_message,
        }

    def __str__(self):
        """Returns a formatted string representation of the exception."""
        message = super().__str__()
        parts = []
        if self.code:
            parts.append(f"[{self.code}]")
        if message:
            parts.append(message)

        if self.details:
            detail_str = ", ".join(
                [f"{key}: {value}" for key, value in self.details.items()]
            )
            parts.append(f"({detail_str})")
        return " ".join(parts)
