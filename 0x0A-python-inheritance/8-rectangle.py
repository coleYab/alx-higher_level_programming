#!/usr/bin/python3
"""A module to implement the class"""


BaseGeometry = __import__('7-base_geometry')


class Rectangle(BaseGeometry):
    """Class that inherits from Base Geometery"""

    def __init__(self, width, height):
        """Costructor"""
        if (self.integer_validator(width)):
            self.__width = width
        if (self.integer_validator(height)):
            self.__height = height

    def __str__(self):
        """a module to print the string representation
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width
