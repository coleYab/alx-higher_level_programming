#!/usr/bin/python3
"""
This is the module that contains function to add integers
"""
def add_integer(a, b=98):
    """
    This is the funtion to add two integers.

    args:
        - a: first integer.
        - b: second integer.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer")

    return int(a) + int(b)
