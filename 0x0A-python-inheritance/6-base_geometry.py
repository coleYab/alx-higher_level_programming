#!/usr/bin/python3
"""A module to abstract a base geometry"""


class BaseGeometry:
    """Base Geometry a class to abstract the thing"""

    def area(self):
        """area -> returns an area of the Geometry"""
        raise Exception("area() is not implemented")
