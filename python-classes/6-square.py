#!/usr/bin/python3
""" Create a new class, we'll define it with size
"""


class Square:
    """this is a square with size and error
    """

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

    @property
    def size(self):
        """provide controlled access to the private attribute __size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """provide controlled access to private attribute __position"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            x, y = value
            if isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0:
                self.__position = value
            else:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive intergers")

    def area(self):
        return self.__size ** 2


def my_print(self):
    if self.__size == 0:
        print("")
    else:
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
