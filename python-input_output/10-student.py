#!/usr/bin/python3
"""lass Student that defines a student"""


class Student:
    """define a class student"""

    def __init__(self, first_name, last_name, age):
        """instanciation of class attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of Student instance"""
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__
