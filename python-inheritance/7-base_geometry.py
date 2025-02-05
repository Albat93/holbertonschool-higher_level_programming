#!/usr/bin/python3
"""Module defining the BaseGeometry class with basic geometric operations."""


class BaseGeometry:
    """A base class for geometric operations."""

    def area(self):
        """
        Raises an Exception to indicate that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.
        raise error if needed.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater 0")
