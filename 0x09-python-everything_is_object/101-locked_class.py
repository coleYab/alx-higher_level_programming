#!/usr/bin/python3
"""
A module to abstract a locked class

### Tools
    - LockedClass: class: the main class
    - __slots__: list: The list to store allowed attributes
    - __init__: constructor
"""


class LockedClass:
    """Uses slots to store the set of allowed attribute"""
    __slots__ = ['first_name']

    def __init__(self):
        pass
