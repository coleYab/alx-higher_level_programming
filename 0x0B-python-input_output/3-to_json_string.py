#!/usr/bin/python3
"""A module to find the string representation of the file"""


import json


def to_json_string(my_obj):
    """changes the file to json object"""

    str_representation = json.dumps(my_obj)

    return str_representation
