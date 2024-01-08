#!/usr/bin/python3
"""A module to implement a base geometry class"""


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
