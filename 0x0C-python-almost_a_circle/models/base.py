#!/usr/bin/python3
"""Module Name - base.py
A module that contains the base class
"""


class Base:
    """A base class for all the classes that comes after it
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor Method
        args:
            - self - the class instance its self.
            - id - unique identifier for the instances
        return: none
        """
        Base.__nb_objects += 1
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects
