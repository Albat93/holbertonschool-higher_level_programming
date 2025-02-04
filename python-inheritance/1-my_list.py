#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
