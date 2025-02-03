#!/usr/bin/python3
"""
    Returns the list of available attributes and methods of an object.
    :param obj: The object to inspect
    :return: List of attributes and methods
    """


def lookup(obj):
    return dir(obj)
