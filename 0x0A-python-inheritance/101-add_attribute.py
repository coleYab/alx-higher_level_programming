#!/usr/bin/python3
"""Module to add an attribute"""


def add_attribute(a_obj, name, value):
    """Adds an attribute to an element"""

    if not hasattr(a_obj, '__dict__'):
        raise TypeError("can't add new element")
    elif '__slots__' in dir(a_obj.__class__):
        raise TypeError("can't add new element")
    elif name in dir(a_obj.__class__):
        raise TypeError("can't add new element")
    setattr(a_obj, name, value)
