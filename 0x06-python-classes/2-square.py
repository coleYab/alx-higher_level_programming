#!/usr/bin/python3
"""Module for class square"""


class Square:
    """Square class to encapsulate square"""

    def __init__(self, size=0) -> None:
        """Constructor to the square class

        Args:
            - size (int): is the size of the square posetive always.

        Returns:
            None if succided otherwise it will raise errors.
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
