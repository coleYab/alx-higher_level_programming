#!/usr/bin/python3
"""A function to add a file"""


class Student:
    """A class that abstracts a student to a class"""
    def __init__(self, first_name, second_name, age):
        """Constructor"""
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of a class"""
        return self.__dict__
