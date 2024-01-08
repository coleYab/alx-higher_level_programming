#!/usr/bin/python3
"""Lookup - the module to print all the available attribures and modules
def lookup(obj): prints the content of a class.
"""


def lookup(obj):
    """lookup - returns the all the list of the objects in a class
    """

    return dir(obj)
