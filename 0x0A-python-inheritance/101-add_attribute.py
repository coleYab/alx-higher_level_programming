#!/usr/bin/python3
"""Module to add an attribute"""


def add_attribute(a_class, name, value):
    """Adds an attribute to an element"""
    if hasattr(a_class, '__dict__'):
        raise TypeError("can't add new element")
    setattr(a_class, name, value)
