#!/usr/bin/python3
"""
This is the module that aims to abstract rectangle class
"""


class Rectangle:
    """This is the class to abstract the Rectangle entity"""

    def __init__(self, width=0, height=0):
        """Constructor"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        self.height = height
        self.width = width

    @property
    def width(self):
        """property setter and getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property setter and getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self) -> int:
        """Calculates area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculates the perimeter of a rectangle"""
        if self.__height * self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])
