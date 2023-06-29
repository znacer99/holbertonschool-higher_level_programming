#!/usr/bin/python3
"""Check type"""




class Square:
    """Define methods of Square"""

    def __init__(self, size=0):

        """Initializes attribute size"""

        self.__size = size



    @property
    def size(self):

        """setter for Square"""

        return self.__size



    @size.setter
    def size(self, value):
        """Initializes attribute size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=")
        else:
            self.__size = value



    def area(self):

        """Calculate area of Square"""

        return self.__size ** 2
