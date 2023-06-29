#!/usr/bin/python3
"""Check type"""


class Square:
    """Define methods of Square"""

    def __init__(self, size=0):
        """Initializes attribute size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
