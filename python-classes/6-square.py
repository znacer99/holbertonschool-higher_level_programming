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
        """Getter method for the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method of the size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter method for the position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) for num in value) or \
                not all(num >= 0 for num in value):
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
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
