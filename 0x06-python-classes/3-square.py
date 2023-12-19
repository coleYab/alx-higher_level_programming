#!/usr/bin/python3
"""Module to define class"""


class Square:
    """Class to abstract the real square"""

    def __init__(self, size=0):
        """Constructor for the class

        Args:
            - size (int): is the posetive size of the square

        Returns:
            Nothing in the real life
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """A method to find the area of the square

        Returns:
            int: the area of the given square
        """
        return self.__size ** 2
