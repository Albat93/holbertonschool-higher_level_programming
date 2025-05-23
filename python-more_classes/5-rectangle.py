#!/usr/bin/python3
""" Create a new class, we'll define it with size
"""


class Rectangle:
    """this is a rectangle with width and height parameters
    """

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width and of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return ()
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Retourne une représentation du rectangle avec '#'."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Retourne une chaîne permettant de recréer l'objet."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Affiche un message lorsqu'un objet Rectangle est supprimé."""
        print("Bye rectangle...")
