#!/usr/bin/python3
"""Class Student that defines a student"""


class Student:
    """Define a class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of class attributes"""
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

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
