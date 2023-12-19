#!/usr/bin/python3
"""A module to abstract the class."""


class Square:
    """A class that will be used to abstract the square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor

        Args:
            - size (int): the size of the square
            - position (tuple): the position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Simple function to set and get values"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """sets or gets the position of the square"""
        return (self.__postion)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = (value[0], value[1])

    def my_print(self):
        """my_print prints a wierd square in the class"""
        if (self.__size == 0):
            print()
            return
        for j in range(self.__position[1]):
            print()
        for k in range(self.__size):
            for u in range(self.__position[0]):
                print(" ", end='')
            for m in range(self.__size):
                print("#", end='')
            print()
