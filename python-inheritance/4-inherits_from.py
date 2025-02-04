#!/usr/bin/python3
"""Function that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class. Otherwise, returns False.

    :param obj: The object to check
    :param a_class: The class to compare with
    :return: True if obj is an instance of a subclass of a_class, else False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
