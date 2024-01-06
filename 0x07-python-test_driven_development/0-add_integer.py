#!/usr/bin/python3
"""This is a module to do some task
    - add_integer: a function to add integer
"""


def add_integer(a, b=98):
    """# adds an integer and return the number
    checks the validity and return the number"""

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))
