#!/usr/bin/python3
"""A module to implement a base geometry class"""


class BaseGeometry:
    """A class for a basic geometry things"""
    
    def area(self):
        """A module to calculate area"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """A module to validate the integer passeed"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be greater than 0")
