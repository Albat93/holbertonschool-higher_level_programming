#!/usr/bin/python3
"""Module containing the BaseGeometry class."""


class BaseGeometry:
    """A class with basic geometric operations."""

    def area(self):
        """
        Raises an Exception with the message
        'area() is not implemented' since it is meant to be overridden.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer and greater than 0.

        :param name: The name of the variable (as a string)
        :param value: The value to be validated
        :raises TypeError: If value is not an integer
        :raises ValueError: If value is not greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
