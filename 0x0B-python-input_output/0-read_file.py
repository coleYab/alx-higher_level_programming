#!/usr/bin/python3
"""A module to add read a file given"""


def read_file(filename=''):
    """reads a file given"""

    with open(filename, 'r') as file:
        msg = file.read()
        print(msg, end='')
