#!/usr/bin/python3
"""Module defining the Rectangle class, which inherits from BaseGeometry."""


class BaseGeometry:
    """A base class for geometric operations."""

    def area(self):
        """
        Raises an Exception indicating that the method is not implemented.

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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")


class Rectangle(BaseGeometry):
    """A class that represents a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height, ensuring validation.

        :param width: The width of the rectangle (must be a positive integer).
        :param height: The height of the rectangle (must be positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
