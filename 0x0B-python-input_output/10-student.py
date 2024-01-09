#!/usr/bin/python3
"""a module to abstract a class student"""


class Student:
    """A class that abstracts a student to a class"""
    def __init__(self, first_name, second_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = second_name
        self.age = age

    def to_json(self, attr=None):
        """Returns the dictionary representation of a class"""

        dic = self.__dict__
        if isinstance(attr, list):
            dictt = {}
            for i in attr:
                if i in dic.keys() and isinstance(i, str):
                    dictt[i] = self.__dict__[i]
                else:
                    break

                return dictt

        return self.__dict__
