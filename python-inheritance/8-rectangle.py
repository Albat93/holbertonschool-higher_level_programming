#!/usr/bin/python3
"""Module containing the Rectangle class, which inherits from BaseGeometry."""


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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))


class Rectangle(BaseGeometry):
    """A class that represents a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height, ensuring validation.

        :param width: The width of the rectangle (must be a positive integer)
        :param height: The height of the rectangle (must be a positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
