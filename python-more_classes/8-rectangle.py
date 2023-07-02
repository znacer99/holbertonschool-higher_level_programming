#!/usr/bin/python3
"""Check type"""


class Rectangle:
    """A class representation of a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a rectangle object"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """When an instance of Rectangle is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter method for retrieving the width of rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for setting the width of rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height of rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for setting the height of rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + '\n'
        return rectangle_str.rstrip()

    def __repr__(self):
        """Returns a string representation of a rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
