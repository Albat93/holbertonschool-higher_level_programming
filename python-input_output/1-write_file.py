#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8)"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return(file.write(text))
