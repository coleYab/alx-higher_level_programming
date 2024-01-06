#!/usr/bin/python3
"""
# This is a module to do some task

    - add_integer: a function to add integer
    - and nothing else test is there
"""

def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    
    else:
        return (int(a) + int(b))