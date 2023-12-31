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
        elif not isinstance(width, int):
            raise TypeError("width must be an integer")
        else:
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
        self.__width = value

    @property
    def height(self):
        """property setter and getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
