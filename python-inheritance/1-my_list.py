#!/usr/bin/python3
"""Define Mylist that inherits from List"""


class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
