#!/usr/bin/python3
"""Module to define the class name sqare"""


class Square:
    """Class that abstracts the sqare"""

    def __init__(self, size=0) -> None:
        """Constructor

        Args:
            size (int): an attribute of size
        """
        self.size = size

    def area(self):
        """Calculates the area of the given square

        Returns:
            int: the square of the integer
        """
        return self.__size ** 2

    @property
    def size(self):
        """Either sets or gets a specific member from a class"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
