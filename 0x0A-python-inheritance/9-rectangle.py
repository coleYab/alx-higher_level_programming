#!/usr/bin/python3
"""A module to implement the class"""


class BaseGeometry:
    """A class for a basic geometry things"""

    def area(self):
        """A module to calculate area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A module to validate the integer passeed"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))



class Rectangle(BaseGeometry):
    """Class that inherits from Base Geometery"""

    def __init__(self, width, height):
        """Costructor"""
        try:
            self.integer_validator("width", width)
        except Exception as e:
            raise e.__class__(e)

        try:
            self.integer_validator("height", height)
        except Exception as e:
            raise e.__class__(e)        

        self.__width = width
        self.__height = height

    def __str__(self):
        """a module to print the string representation
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width
