#!/usr/bin/python
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
