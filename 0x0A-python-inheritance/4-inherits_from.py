#!/usr/bin/python3
"""this is a function that will check if a class inherits form other
"""

def inherits_from(obj, a_class):
    """iherits from - checks if a class inherits from other class"""
    temp = a_class()

    return (isinstance(obj, a_class) and  type(obj) != type(temp))
