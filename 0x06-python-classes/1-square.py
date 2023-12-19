#!/usr/bin/python3
"""Defines a class sqare"""


class Square:
    """This is the class to abstract a square"""
    def __init__(self, size) -> None:
        """Constructor for square class

        Args:
            - size (int): is the length of the integer.

        Returns:
            None
        """
        self.size = size
