#!usr/bin/python3
"""Define a function that checks if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    otherwise False"""
    return type(obj) is a_class
