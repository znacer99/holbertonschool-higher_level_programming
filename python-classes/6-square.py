#!/usr/bin/python3
"""Check type"""


class Square:
    """Define methods of Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance"""

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property for the length of a size of a square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter function for private size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Property for square position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Setter function for private position attribute"""

        if (type(value) is not tuple or
           len(value) != 2 or
           all(isinstance(num, int) for num in value) or
           any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculate the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
