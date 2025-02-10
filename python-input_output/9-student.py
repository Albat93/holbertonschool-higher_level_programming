#!/usr/bin/python3
"""create a class student with instanciation"""


class Student:
    """define a class student"""

    def __init__(self, first_name, last_name, age):
        """instanciation of class attribute"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return the json dict"""
        return self.__dict__
