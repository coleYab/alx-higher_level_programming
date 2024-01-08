#!/usr/bin/python3
"""Module to add an attribute"""


def add_attribute(a_class, name, value):
    """Adds an attribute to an element"""
    if '__slots__' in dir(a_class) or name in dir(a_class):
        raise TypeError("cant add new atribute")
    else:
        a_class.name = value
