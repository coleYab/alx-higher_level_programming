#!/usr/bin/python3
"""A module that convert a class to a string"""


def class_to_json(a_obj):
    """Converts a class to an object"""

    dic = a_obj.__dict__

    string = []
    for key, value in dic.items():
        p_h = '"'
        if not isinstance(value, str):
            p_h = ''
        string.append(f'"{key}": {p_h}{value}{p_h}')

    msg = '{'
    for i in range(len(string) - 1):
        msg += string[i]
        msg += ', '

    msg += string[-1]
    msg += '}'

    return msg
