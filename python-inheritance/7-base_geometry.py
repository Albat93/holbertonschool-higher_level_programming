#!/usr/bin/python3
"""Module defining the BaseGeometry class with basic geometric operations."""


class BaseGeometry:
    """A base class for geometric operations."""

    def area(self):
        """
        Raises an Exception to indicate that the method is not implemented.

        This method should be overridden in a subclass to provide
        a specific implementation for calculating the area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        :param name: The name of the variable (as a string).
        :param value: The value to be validated.
        :raises TypeError: If 'value' is not an integer.
        :raises ValueError: If 'value' is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
