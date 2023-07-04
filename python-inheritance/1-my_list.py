#!/usr/bin/python3
"""Define Mylist that inherits from List"""


class MyList(list):
    """Define methods of class"""

    def print_sorted(self):
        """Print sorted list"""

        sorted_list = sorted(self)
        print(sorted_list)
