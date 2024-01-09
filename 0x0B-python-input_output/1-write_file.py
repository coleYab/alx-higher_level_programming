#!/usr/bin/python3
"""A module to write to a file"""


def write_file(filename='', text=''):
    """Erases the file and add the text to it"""

    with open(filename, 'w') as file:
        file.write(text)
        return (len(text))
