#!/usr/bin/python3
"""A function that checks if a specified obj is
a member of a specific class
"""


def is_same_class(obj, a_class):
    """Checks if the object 'obj' is in class 'a_class'
    """
    
    temp = a_class()
    
    return (type(obj) == type(temp))
