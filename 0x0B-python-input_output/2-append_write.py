#!/usr/bin/python3
"""The module to append a file"""


def append_write(filename='', text=''):
    """Append file is the module to append file"""
    with open(filename, 'a') as file:
        file.write(text)
        return len(text)
