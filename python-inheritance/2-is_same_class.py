#!usr/bin/python3
"""Define a function that checks if the object is exactly
an instance of the specified class
"""


def is_same_class(obj, a_class):
    return type(obj) is a_class
