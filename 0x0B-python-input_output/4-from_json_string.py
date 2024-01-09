#!/usr/bin/python3
"""A module to decode a python code"""


import json


def from_json_string(my_str):
    """Coverts the file from str -> json"""

    real_obj = json.loads(my_str)

    return real_obj
