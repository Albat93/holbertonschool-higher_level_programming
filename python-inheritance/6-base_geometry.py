#!/usr/bin/python3
"""
"""


class BaseGeometry():
    def area(self):
        if not isinstance(self, int):
            raise Exception("area() is not implemented")
