#!/usr/bin/python3
"""Module to add an attribute"""


def add_attribute(a_class, name, value):
    """Adds an attribute to an element"""
    if '__slots__' in dir(a_class):
        if name not in a_class.__slots__:
            setattr(a_class, name, value)
        else:
            raise TypeError("can't add new element")
    elif name not in dir(a_class):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new element")
