#!/usr/bin/python3
"""a module to check if an object belongs to a class
or a super class
"""


def is_kind_of_class(obj, a_class):
    """Is a module to check if an object is parent of a_class"""

    return isinstance(obj, a_class)
